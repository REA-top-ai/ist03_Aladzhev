from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class SearchQuery(db.Model):
    __tablename__ = 'search_queries'
    
    id = db.Column(db.Integer, primary_key=True)
    original_query = db.Column(db.Text, nullable=False)
    processed_query = db.Column(db.Text)
    keywords = db.Column(db.Text) 
    results_count = db.Column(db.Integer, default=0)
    search_date = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(45))
    
    articles = db.relationship('SearchArticle', backref='search_query', lazy='dynamic', 
                              cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<SearchQuery {self.original_query[:50]}>'


class SearchArticle(db.Model):
    __tablename__ = 'search_articles'
    
    id = db.Column(db.Integer, primary_key=True)
    query_id = db.Column(db.Integer, db.ForeignKey('search_queries.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.Text)
    authors = db.Column(db.Text)  
    publication_year = db.Column(db.Integer)
    doi = db.Column(db.String(100))
    doi_url = db.Column(db.Text)
    cited_by_count = db.Column(db.Integer, default=0)
    publication_type = db.Column(db.String(50))
    abstract = db.Column(db.Text)
    is_open_access = db.Column(db.Boolean, default=False)
    openalex_id = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<SearchArticle {self.title[:50]}>'
