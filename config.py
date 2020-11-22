import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    START_NGROK=os.environ.get('START_NGROK') is not None

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=1
    MAIL_USERNAME='norulesanymore@gmail.com'
    MAIL_PASSWORD=b"\xe2z\x91\xaf\x00(\x90\xad\xb2'A\xeeM\x92cy"
    ADMINS=['tastebolder@gmail.com']