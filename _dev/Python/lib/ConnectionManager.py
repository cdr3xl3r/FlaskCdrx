#The magic engine that will make all your DB dreams come true



print('ConnectionManager: Starting')
from sqlalchemy import create_engine, text
print('ConnectionManager: Importing Classes')
engine = create_engine(website.DataBase,echo=True)
print('ConnectionManager: Creating Tables')


#def of simple sessions functions
def createSessionMaker(commit):
        from ConnectionManager import engine
        from sqlalchemy.orm import  sessionmaker

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(commit)
        session.commit()
def createDatabase():
        from models import Base
        from sqlalchemy import create_engine
        print("Creating tables")
        Base.metadata.create_all(bind=engine)

"""with engine.connect() as connection:
    result = connection.execute()
    
    print(result.all())"""

