import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY', 'key')
    OPENALEX_BASE_URL = 'https://api.openalex.org'
    MAX_RESULTS = 20
    

    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '123456789')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'research_search')
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
