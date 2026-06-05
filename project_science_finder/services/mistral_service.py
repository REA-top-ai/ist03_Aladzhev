from mistralai.client import Mistral
import json
from config import Config

class MistralService:
    def __init__(self):
        self.client = Mistral(api_key=Config.MISTRAL_API_KEY)
    
    def process_query(self, user_query):
        try:
            prompt = f"""
            Ты помощник для поиска научных статей. Преобразуй следующий пользовательский запрос 
            в оптимизированный поисковый запрос для API OpenAlex, который ищет научные публикации.
            Пользовательский запрос: "{user_query}"
            Верни ТОЛЬКО JSON объект с полями:
            - search_query: оптимизированная поисковая строка на английском, не доолжна превышать максимум способностей OpenAlex
            - keywords: массив из 3-5 ключевых слов, не больше
            - language: предпочитаемый язык (если указан в запросе), если нет None   
            Ответ должен быть ТОЛЬКО JSON без дополнительного текста:
            """
            
            chat_response = self.client.chat.complete(
                model="mistral-small-latest",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            result_text = chat_response.choices[0].message.content

            result_text = result_text.strip().replace('```json', '').replace('```', '')
            
            return json.loads(result_text)
            
        except Exception as e:
            print(f"Error processing query with Mistral: {e}")

            return {
                "search_query": user_query,
                "keywords": user_query.split()[:5],
                "language": None
            }
