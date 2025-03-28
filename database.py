from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Подключение к SQLite
engine = create_engine('sqlite:///database.db')

Base = declarative_base()

class Announcement(Base):
    __tablename__ = 'announcements'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Integer)
    author = Column(String(50))
    date_create = Column(DateTime, default=datetime.utcnow)

# Создаем таблицы
Base.metadata.create_all(engine)

# Создаем фабрику сессий
Session = sessionmaker(bind=engine)
