import os


class Config:
    '''
    general configuration parent class
    '''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
    '''
    production configuration child class
    
        Arg:
            Config: th parent configuration class with general configuration settings
    '''
    # 'SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://iano:ianoteno2@localhost/pitch'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    #if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
       # SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
   # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql  File "/home/moringa/pitches-app/virtual/lib/python3.8/site-packages/sqlalchemy/util/compat.py", line 207, in raise_://", 1)
       

class TestConfig(Config):
    '''
    Test configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:moringa@localhost/pitching'

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:moringa@localhost/pitching'

    DEBUG = True

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
