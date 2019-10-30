
import os

class Config:
    
    SECRET_KEY = os.getenv('SECRET_KEY')  
    # SECRET_KEY = 'dc1e593547d2fe6360915b6ce5bc091a'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    # SQLALCHEMY_DATABASE_URI ='sqlite:///site.db'
    # Mail config
    MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_SERVER = 'smtp.mailtrap.io'
    # MAIL_PORT = 587
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = '6aa1b105d5f87a'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    # MAIL_PASSWORD = 'c2eded0939c1de'
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')




# class Config:
    
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
#     # Mail config
#     MAIL_SERVER = 'smtp.mailtrap.io'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     # MAIL_USERNAME = '6aa1b105d5f87a'
#     MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
#     # MAIL_PASSWORD = 'c2eded0939c1de'
#     MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')