#include <iostream>
#include <fstream>

// Функция переводит 4 байта в обычное целое
// В BMP байты записаны задом наперед поэтому умножаем на 256 в степенях
int bytes_to_int4(unsigned char* bytes) {
    int result = 0;
    result = result + bytes[0];
    result = result + bytes[1] * 256;
    result = result + bytes[2] * 256 * 256;
    result = result + bytes[3] * 256 * 256 * 256;
    return result;
}

// Функция переводит 2 байта в целое
int bytes_to_int2(unsigned char* bytes) {
    int result = 0;
    result = result + bytes[0];
    result = result + bytes[1] * 256;
    return result;
}
//Функция для цветов
void print_pixel(unsigned char* bytes) {
    // Собираем байты в одно чилсо
    int pixel = bytes_to_int2(bytes);

    int blue = pixel % 32;
    int green = (pixel / 32) % 64;
    int red = pixel / (32 * 64); 
    // Переводим значения в диапазон 0 255.

    red   = red   * 255 / 31;
    green = green * 255 / 63;
    blue  = blue  * 255 / 31;
    std::cout << "R: " << red << " G: " << green << " B: " << blue << std::endl;
}

int main(const int argc, char** argv) {
    //Путь к файлу если не указан в баше
    const char* path = argc > 1 ? argv[1] : "images/image.bmp";

    // Открываем файл
    std::ifstream file(path, std::ios::binary);
    if (!file) {
        std::cerr << "Не удалось открыть файл" << path << std::endl;
        return 1;
    }

    // Читаем первые 54 байта
    unsigned char headers[54];
    file.read(reinterpret_cast<char*>(headers), 54);

    // Проверяем на BM
    if (headers[0] != 'B' || headers[1] != 'M') {
        std::cerr << "Ошибка: файл не является BMP." << std::endl;
        return 1;
    }

    // Достаём нужные поля из заголовка
    int file_size      = bytes_to_int4(headers + 2);
    int data_offset    = bytes_to_int4(headers + 10);
    int header_size    = bytes_to_int4(headers + 14);
    int width          = bytes_to_int4(headers + 18);
    int height         = bytes_to_int4(headers + 22);
    int planes         = bytes_to_int2(headers + 26);
    int bits_per_pixel = bytes_to_int2(headers + 28);
    int compression    = bytes_to_int4(headers + 30);
    int image_size     = bytes_to_int4(headers + 34);
    int x_pixels_m     = bytes_to_int4(headers + 38);
    int y_pixels_m     = bytes_to_int4(headers + 42);
    int colors_used    = bytes_to_int4(headers + 46);
    int colors_imp     = bytes_to_int4(headers + 50);

    // Печатаем заголовок.
    std::cout << "2b headers.bitmap_signature : " << headers[0] << headers[1] << std::endl;
    std::cout << "4b headers.bitmap_file_size : " << file_size << std::endl;
    std::cout << "4b headers.bitmap_data_offset : " << data_offset << std::endl;
    std::cout << "4b headers.bitmap_info_header_size : " << header_size << std::endl;
    std::cout << "4b headers.bitmap_width : " << width << std::endl;
    std::cout << "4b headers.bitmap_height : " << height << std::endl;
    std::cout << "2b headers.bitmap_planes : " << planes << std::endl;
    std::cout << "2b headers.bitmap_bits_per_pixel : " << bits_per_pixel << std::endl;
    std::cout << "4b headers.bitmap_compression : " << compression << std::endl;
    std::cout << "4b headers.bitmap_image_size : " << image_size << std::endl;
    std::cout << "4b headers.bitmap_XpixelsPerM : " << x_pixels_m << std::endl;
    std::cout << "4b headers.bitmap_YpixelsPerM : " << y_pixels_m << std::endl;
    std::cout << "4b headers.bitmap_ColorsUsed : " << colors_used << std::endl;
    std::cout << "4b headers.bitmap_ColorsImportant : " << colors_imp << std::endl;

    //Считаем сколько занимает строка с выравниванием
    int row_bytes = width * 2;  
    int padding = (4 - (row_bytes % 4)) % 4;  
    int stride = row_bytes + padding;         
    unsigned char pixel[2];

    // Левый нижний пиксель
    file.seekg(data_offset, std::ios::beg);
    file.read(reinterpret_cast<char*>(pixel), 2);
    std::cout << "Левый нижний пиксель: ";
    print_pixel(pixel);

    // Правый нижний
    file.seekg(data_offset + (width - 1) * 2, std::ios::beg);
    file.read(reinterpret_cast<char*>(pixel), 2);
    std::cout << "Правый нижний пиксель: ";
    print_pixel(pixel);

    // Левый верхний пиксель
    file.seekg(data_offset + (height - 1) * stride, std::ios::beg);
    file.read(reinterpret_cast<char*>(pixel), 2);
    std::cout << "Левый верхний пиксель: ";
    print_pixel(pixel);

    // Правый верхний
    file.seekg(data_offset + (height - 1) * stride + (width - 1) * 2, std::ios::beg);
    file.read(reinterpret_cast<char*>(pixel), 2);
    std::cout << "Правый верхний пиксель: ";
    print_pixel(pixel);

    file.close();
    return 0;
}
