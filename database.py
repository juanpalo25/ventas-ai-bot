# database.py
from sqlalchemy import create_engine

engine = create_engine("sqlite:///ventas.db")  