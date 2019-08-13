import os

class Config:
   # simple mde  configurations
   QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
   SIMPLEMDE_JS_IIFE = True
   SIMPLEMDE_USE_CDN = True
   SECRET_KEY = os.environ.get('SECRET_KEY')
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/blog'
   UPLOADED_PHOTOS_DEST = 'app/static/photos'
   MAIL_SERVER = 'smtp.googlemail.com'
# email configuration
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    
   @staticmethod
   def init_app(app):
       pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class TestConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:12345@localhost/blog'
    pass

class DevConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
