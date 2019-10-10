from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


Base = declarative_base()
engine = create_engine('mysql+pymysql://'+os.environ.get('DB_CONECTION')+'@localhost/inmobiliaria')
# Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
