import os
from pathlib import Path

basedir = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'