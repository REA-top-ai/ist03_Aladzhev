import requests
from config import Config

class OpenAlexService:
    def __init__(self):
        self.base_url = Config.OPENALEX_BASE_URL
    
    def search_articles(self, query_params):

        search_query = query_params.get('search_query', '')
        keywords = query_params.get('keywords', [])
        language = query_params.get('language')
        

        params = {
            'search': search_query,
            'per_page': Config.MAX_RESULTS,
            'sort': 'relevance_score:desc'
        }

        if language and language != None:
            params['filter'] = f'language:{language}'
        
        try:
            response = requests.get(
                f"{self.base_url}/works",
                params=params,
                timeout=25
            )
            response.raise_for_status()
            
            data = response.json()
            return self._format_results(data.get('results', []))
            
        except requests.RequestException as e:
            print(f"Error searching OpenAlex: {e}")
            return []
    
    def _format_results(self, results):
        """
        Форматирует результаты для отображения
        """
        formatted = []
        for work in results:
            # Извлекаем основную информацию
            title = work.get('title', 'Без названия')
            
            # Авторы
            authors = []
            for authorship in work.get('authorships', []):
                author = authorship.get('author', {})
                if author:
                    authors.append(author.get('display_name', 'Неизвестный автор'))
            
            # Год публикации
            publication_date = work.get('publication_date', 'Дата неизвестна')
            year = publication_date[:4] if publication_date else 'N/A'
            
            # DOI
            doi = work.get('doi', '')
            doi_url = f"https://doi.org/{doi}" if doi else None
            
            # Цитирования
            cited_by_count = work.get('cited_by_count', 0)
            
            # Тип публикации
            pub_type = work.get('type', 'unknown')
            
            # Абстракт (может быть инвертированным индексом)
            abstract = self._extract_abstract(work.get('abstract_inverted_index'))
            
            # Open Access
            open_access = work.get('open_access', {}).get('is_oa', False)
            
            formatted.append({
                'title': title,
                'authors': authors[:5], 
                'year': year,
                'doi': doi,
                'doi_url': doi_url,
                'cited_by_count': cited_by_count,
                'type': pub_type,
                'abstract': abstract[:500] if abstract else 'Аннотация отсутствует',
                'open_access': open_access,
                'id': work.get('id', '')
            })
        
        return formatted
    
    def _extract_abstract(self, inverted_index):
        """
        Восстанавливает текст аннотации из инвертированного индекса OpenAlex
        """
        if not inverted_index:
            return None
        

        word_positions = {}
        for word, positions in inverted_index.items():
            for pos in positions:
                word_positions[pos] = word
        

        sorted_positions = sorted(word_positions.keys())
        abstract = ' '.join([word_positions[pos] for pos in sorted_positions])
        
        return abstract
