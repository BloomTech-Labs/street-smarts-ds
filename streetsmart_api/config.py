# configure the app
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    """ Base configuration reading from .env file"""
    DEBUG = os.getenv("DEBUG")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_ADDRESS")
    SQLALCHEMY_TRACK_MODIFICATIONS = False