import os

class Config:
    SECRET_KEY = '7b083c0fa0ac180c6b8244e6923ba179'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'soorn4657@hotmail.com'
    MAIL_PASSWORD = 'zjmxujxotsfwdgec'