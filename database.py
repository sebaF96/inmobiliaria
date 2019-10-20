from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv(override=True)

Base = declarative_base()
engine = create_engine('mysql+pymysql://'+os.getenv('DB_CONECTION')+'@'+os.getenv('DB_HOST')+'/'+os.getenv('DB_SCHEMA'))
Session = sessionmaker(bind=engine)
