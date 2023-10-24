print('__init__: Starting')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy




print('__init__: Creating db variables')

DB_NAME = "liteDB_cita450.db"
DataBase = f'sqlite:///{DB_NAME}'
print(f'__init__: Check/Create db = {DataBase}')

global db
db = SQLAlchemy()



def create_app():
    from .authManager import auth
    from .views import views
     
    app = Flask(__name__)
    

    app.config['SECRET_KEY'] = 'passmypasstopass'
    app.config['SQLALCHEMY_DATABASE_URI'] = DataBase 
    
    db.init_app(app)
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
   # app.register_blueprint(test, url_prefix='/test/')
    createdatabase()
    return app
def createdatabase():
    from os import path
    if not path.exists(DB_NAME):
        from sqlalchemy import create_engine, text
        print('__init__: Importing Classes')
        engine = create_engine(DataBase,echo=True)
        from website.models import Base
        from sqlalchemy import create_engine
        print("Creating tables")
        Base.metadata.create_all(bind=engine)
"""        db.create_Database(app)
        print('__init__: Created Table')"""