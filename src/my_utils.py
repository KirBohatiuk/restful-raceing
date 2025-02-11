from dotenv import dotenv_values
import random
from string import ascii_letters, digits

def get_engine_info():
    credentials = dotenv_values()
    db = credentials["DB"]
    user = credentials["USER"]
    password = credentials["PASSWORD"]
    host = credentials["HOST"]
    port = credentials["PORT"]
    db_name = credentials["DB_NAME"]
    return db, user, password, host, port, db_name
