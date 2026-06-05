from flask import Flask, render_template, request, jsonify
from config import Config
from models import db, SearchQuery, SearchArticle
from services.mistral_service import MistralService
from services.openalex_service import OpenAlexService
from datetime import datetime
import json

app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных
db.init_app(app)

# Инициализация сервисов
mistral_service = MistralService()
openalex_service = OpenAlexService()

# Создание таблиц
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.form.get('query', '')
    
    if not user_query.strip():
        return render_template('index.html', error="Пожалуйста, введите поисковый запрос")
    
    #Обработка запроса через Mistral
    processed_query = mistral_service.process_query(user_query)
    
    #Поиск через OpenAlex
    results = openalex_service.search_articles(processed_query)
    
    # Сохраняем запрос в базу данных
    search_record = SearchQuery(
        original_query=user_query,
        processed_query=json.dumps(processed_query),
        keywords=json.dumps(processed_query.get('keywords', [])),
        results_count=len(results),
        search_date=datetime.utcnow(),
        ip_address=request.remote_addr
    )
    db.session.add(search_record)
    db.session.flush()  
    
    # Сохраняем статьи в базе данных
    for article in results:
        article_record = SearchArticle(
            query_id=search_record.id,
            title=article.get('title', 'Без названия'),
            authors=json.dumps(article.get('authors', []), ensure_ascii=False),
            publication_year=int(article.get('year')) if article.get('year', '').isdigit() else None,
            doi=article.get('doi', ''),
            doi_url=article.get('doi_url', ''),
            cited_by_count=article.get('cited_by_count', 0),
            publication_type=article.get('type', 'unknown'),
            abstract=article.get('abstract', ''),
            is_open_access=article.get('open_access', False),
            openalex_id=article.get('id', '')
        )
        db.session.add(article_record)
    
    db.session.commit()
    
    return render_template(
        'results.html',
        query=user_query,
        processed_query=processed_query,
        results=results
    )

@app.route('/history')
def history():
    # Получаем историю запросов
    page = request.args.get('page', 1, type=int)
    per_page = 20
    
    searches = SearchQuery.query.order_by(
        SearchQuery.search_date.desc()
    ).paginate(page=page, per_page=per_page, error_out=False)
    
    return render_template('history.html', searches=searches)

@app.route('/history/<int:query_id>')
def view_search(query_id):
    search = SearchQuery.query.get_or_404(query_id)
    articles = SearchArticle.query.filter_by(query_id=query_id).all()
    
    # Преобразуем JSON строки обратно в объекты
    for article in articles:
        try:
            article.authors_list = json.loads(article.authors) if article.authors else []
        except:
            article.authors_list = []
    
    return render_template('search_detail.html', search=search, articles=articles)

@app.route('/api/search', methods=['POST'])
def api_search():

    data = request.get_json()
    user_query = data.get('query', '')
    
    if not user_query.strip():
        return jsonify({'error': 'Query is required'}), 400
    
    # Обработка запроса через Mistral
    processed_query = mistral_service.process_query(user_query)
    
    # Поиск через OpenAlex
    results = openalex_service.search_articles(processed_query)
    
    # Сохраняем в базу данных
    search_record = SearchQuery(
        original_query=user_query,
        processed_query=json.dumps(processed_query),
        keywords=json.dumps(processed_query.get('keywords', [])),
        results_count=len(results),
        ip_address=request.remote_addr
    )
    db.session.add(search_record)
    db.session.flush()
    
    for article in results:
        article_record = SearchArticle(
            query_id=search_record.id,
            title=article.get('title', 'Без названия'),
            authors=json.dumps(article.get('authors', []), ensure_ascii=False),
            publication_year=int(article.get('year')) if article.get('year', '').isdigit() else None,
            doi=article.get('doi', ''),
            doi_url=article.get('doi_url', ''),
            cited_by_count=article.get('cited_by_count', 0),
            publication_type=article.get('type', 'unknown'),
            abstract=article.get('abstract', ''),
            is_open_access=article.get('open_access', False),
            openalex_id=article.get('id', '')
        )
        db.session.add(article_record)
    
    db.session.commit()
    
    return jsonify({
        'query': user_query,
        'processed_query': processed_query,
        'results': results,
        'count': len(results)
    })

if __name__ == '__main__':
    app.run()
