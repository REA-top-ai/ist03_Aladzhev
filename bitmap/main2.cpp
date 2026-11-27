#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

struct Pixel {
    int R = 0;
    int G = 0;
    int B = 0;
    int Y = 0; // Luminance
};


int bytes_to_int4(unsigned char* bytes) {
    int result = 0;
    result += bytes[0];
    result += bytes[1] * 256;
    result += bytes[2] * 256 * 256;
    result += bytes[3] * 256 * 256 * 256;
    return result;
}

int bytes_to_int2(unsigned char* bytes) {
    return bytes[0] + bytes[1] * 256;
}
class Bitmap {
private:
    int width = 0;
    int height = 0;
    std::vector<Pixel> pixels;

    Pixel decode_pixel(unsigned char* bytes) {
        int pixel_data = bytes_to_int2(bytes);

        int blue = pixel_data % 32;
        int green = (pixel_data / 32) % 64;
        int red = pixel_data / (32 * 64);

        red = red * 255 / 31;
        green = green * 255 / 63;
        blue = blue * 255 / 31;

        Pixel p;
        p.R = red;
        p.G = green;
        p.B = blue;
        // Luminance по формуле из задания 0.2126*R + 0.7152*G + 0.0722*B
        p.Y = (int)std::round(0.2126 * p.R + 0.7152 * p.G + 0.0722 * p.B);
        return p;
    }
    void PrintPeaks(const char* name, int* hist) {
        int max_count = 0;
        int peak_value = 0;

        for (int i = 0; i < 256; i++) {
            if (hist[i] > max_count) {
                max_count = hist[i];
                peak_value = i;
            }
        }
        std::cout << "Канал " << name << ": Пик на значении " << peak_value
                  << " (встречается " << max_count << " раз)" << std::endl;
    }

public:
  void PrintHeaders(const char* path) {
        std::ifstream file(path, std::ios::binary);
        if (!file) {
            std::cerr << "Не удалось открыть файл: " << path << std::endl;
            return;
        }

        unsigned char headers[54];
        file.read(reinterpret_cast<char*>(headers), 54);

        if (headers[0] != 'B' || headers[1] != 'M') {
            std::cerr << "Файл не является BMP" << std::endl;
            return;
        }
        int file_size      = bytes_to_int4(headers + 2);
        int data_offset    = bytes_to_int4(headers + 10);
        int header_size    = bytes_to_int4(headers + 14);
        int w              = bytes_to_int4(headers + 18);
        int h              = bytes_to_int4(headers + 22);
        int planes         = bytes_to_int2(headers + 26);
        int bits_per_pixel = bytes_to_int2(headers + 28);
        int compression    = bytes_to_int4(headers + 30);
        int image_size     = bytes_to_int4(headers + 34);
        int x_pixels_m     = bytes_to_int4(headers + 38);
        int y_pixels_m     = bytes_to_int4(headers + 42);
        int colors_used    = bytes_to_int4(headers + 46);
        int colors_imp     = bytes_to_int4(headers + 50);

        std::cout << "2b headers.bitmap_signature : BM" << std::endl;
        std::cout << "4b headers.bitmap_file_size : " << file_size << std::endl;
        std::cout << "4b headers.bitmap_data_offset : " << data_offset << std::endl;
        std::cout << "4b headers.bitmap_info_header_size : " << header_size << std::endl;
        std::cout << "4b headers.bitmap_width : " << w << std::endl;
        std::cout << "4b headers.bitmap_height : " << h << std::endl;
        std::cout << "2b headers.bitmap_planes : " << planes << std::endl;
        std::cout << "2b headers.bitmap_bits_per_pixel : " << bits_per_pixel << std::endl;
        std::cout << "4b headers.bitmap_compression : " << compression << std::endl;
        std::cout << "4b headers.bitmap_image_size : " << image_size << std::endl;
        std::cout << "4b headers.bitmap_XpixelsPerM : " << x_pixels_m << std::endl;
        std::cout << "4b headers.bitmap_YpixelsPerM : " << y_pixels_m << std::endl;
        std::cout << "4b headers.bitmap_ColorsUsed : " << colors_used << std::endl;
        std::cout << "4b headers.bitmap_ColorsImportant : " << colors_imp << std::endl;
    }

    bool Load(const char* path) {
        std::ifstream file(path, std::ios::binary);
        if (!file) return false;

        unsigned char headers[54];
        file.read(reinterpret_cast<char*>(headers), 54);

        if (headers[0] != 'B' || headers[1] != 'M') {
            return false;
        }

        int data_offset = bytes_to_int4(headers + 10);
        width = bytes_to_int4(headers + 18);
        height = bytes_to_int4(headers + 22);
        int bits_per_pixel = bytes_to_int2(headers + 28);

        pixels.clear();
        pixels.resize(width * height);

        int row_bytes = width * 2;
        int padding = (4 - (row_bytes % 4)) % 4;
        int stride = row_bytes + padding;

        unsigned char pixel_bytes[2];

        // BMP хранит данные снизу вверх, переворачиваем при загрузке,
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int file_y = height - 1 - y;
                file.seekg(data_offset + file_y * stride + x * 2, std::ios::beg);
                file.read(reinterpret_cast<char*>(pixel_bytes), 2);

                pixels[y * width + x] = decode_pixel(pixel_bytes);
            }
        }

        return true;
    }

    Pixel GetPixel(int x, int y) const {
        if (x < 0 || x >= width || y < 0 || y >= height) {
            return Pixel();
        }
        return pixels[y * width + x];
    }

    int GetWidth() const { return width; }
    int GetHeight() const { return height; }

    // Оценка экспозиции
    void EvaluateExposure() {
        int histogram[256] = {0};
        double sum_Y = 0;
        int total_pixels = width * height;

        for (int i = 0; i < total_pixels; i++) {
            int y_val = pixels[i].Y;
            if (y_val < 0) y_val = 0;
            if (y_val > 255) y_val = 255;

            histogram[y_val]++;
            sum_Y += y_val;
        }

        double mean = sum_Y / total_pixels;

        int median = 0;
        int accumulated = 0;
        int half_pixels = total_pixels / 2;

        for (int i = 0; i < 256; i++) {
            accumulated += histogram[i];
            if (accumulated >= half_pixels) {
                median = i;
                break;
            }
        }

        std::cout << "\nОценка экспозиции" << std::endl;
        std::cout << "Среднее значение: " << std::fixed << std::setprecision(2) << mean << std::endl;
        std::cout << "Медиана: " << median << std::endl;

    }

    //Баланс белого
    void EvaluateWhiteBalance() {
        double sum_R = 0, sum_G = 0, sum_B = 0;
        int total = width * height;

        for (int i = 0; i < total; i++) {
            sum_R += pixels[i].R;
            sum_G += pixels[i].G;
            sum_B += pixels[i].B;
        }

        double avg_R = sum_R / total;
        double avg_G = sum_G / total;
        double avg_B = sum_B / total;

        std::cout << "\nОценка баланса белого" << std::endl;
        std::cout << "Средний R: " << std::fixed << std::setprecision(2) << avg_R << std::endl;
        std::cout << "Средний G: " << avg_G << std::endl;
        std::cout << "Средний B: " << avg_B << std::endl;

        double max_avg = std::max({avg_R, avg_G, avg_B});
        double min_avg = std::min({avg_R, avg_G, avg_B});
    }

    // Расчет гистограмм
    void PrintHistograms() {
        int hist_R[256] = {0};
        int hist_G[256] = {0};
        int hist_B[256] = {0};
        int hist_Y[256] = {0};

        for (int i = 0; i < width * height; i++) {
            hist_R[pixels[i].R]++;
            hist_G[pixels[i].G]++;
            hist_B[pixels[i].B]++;
            hist_Y[pixels[i].Y]++;
        }

        std::cout << "\nГистограммы" << std::endl;
        PrintPeaks("Red", hist_R);
        PrintPeaks("Green", hist_G);
        PrintPeaks("Blue", hist_B);
        PrintPeaks("Luminance (Y)", hist_Y);
    }
};

int main(int argc, char** argv) {
    const char* path = argc > 1 ? argv[1] : "image.bmp";

    Bitmap bitmap;

    // Вывод заголовка
    bitmap.PrintHeaders(path);
    std::cout << std::endl;

    // Загрузка изображения
    if (!bitmap.Load(path)) {
        std::cerr << "Не удалось загрузить файл" << std::endl;
        return 1;
    }

    std::cout << "Проверка углов" << std::endl;
    int w = bitmap.GetWidth();
    int h = bitmap.GetHeight();

    Pixel p1 = bitmap.GetPixel(0, 0); // Верхний левый
    std::cout << "Левый верхний (0,0):   R: " << p1.R << " G: " << p1.G << " B: " << p1.B << " Y: " << p1.Y << std::endl;

    Pixel p2 = bitmap.GetPixel(w - 1, 0); // Верхний правый
    std::cout << "Правый верхний (" << w-1 << ",0): R: " << p2.R << " G: " << p2.G << " B: " << p2.B << " Y: " << p2.Y << std::endl;

    Pixel p3 = bitmap.GetPixel(0, h - 1); // Нижний левый
    std::cout << "Левый нижний (0," << h-1 << "):  R: " << p3.R << " G: " << p3.G << " B: " << p3.B << " Y: " << p3.Y << std::endl;

    Pixel p4 = bitmap.GetPixel(w - 1, h - 1); // Нижний правый
    std::cout << "Правый нижний (" << w-1 << "," << h-1 << "): R: " << p4.R << " G: " << p4.G << " B: " << p4.B << " Y: " << p4.Y << std::endl;

    bitmap.EvaluateExposure();
    bitmap.EvaluateWhiteBalance();
    bitmap.PrintHistograms();

    return 0;
}
