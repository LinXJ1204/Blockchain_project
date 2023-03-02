TESTING = True
SECRET_KEY = "project_name in flask"
DEBUG_TB_INTERCEPT_REDIRECTS = False
TEMPLATES_AUTO_RELOAD = True  # html debug mode

# flask-mysql setting
MYSQL_DATABASE_HOST = 'localhost'  # default
MYSQL_DATABASE_PORT = 8889  # default
MYSQL_DATABASE_CHARSET = 'utf8'  # default
MYSQL_DATABASE_USER = 'zhengmacbook16'
MYSQL_DATABASE_PASSWORD = 'wayne1204'
MYSQL_DATABASE_DB = 'blockchain_project'

SQLALCHEMY_DATABASE_URI = 'mysql://zhengmacbook16:wayne1204@127.0.0.1:8889/blockchain_project'
SQLALCHEMY_BINDS = {
    'backend': 'mysql://zhengmacbook16:wayne1204@127.0.0.1:8889/blockchain_project'
}
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
