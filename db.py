"""
Python module for persisting sensor data to Postgres database.
"""
import os

import psycopg2

# ----- Global config variables -----
DB_USER = os.environ.get('DB_USER')
DB_PWD = os.environ.get('DB_PWD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')


def connection():
    """
    Connect to database and return connection object.
    """
    try:
        conn = psycopg2.connect(dbname=DB_NAME, 
                                user=DB_USER, 
                                password=DB_PWD, 
                                host=DB_HOST, 
                                port=DB_PORT)

        conn.autocommit = True
    except:
        print('Error connecting to database')
    else:
        return conn

def write_record(msg):
    """
    Write a single record of data to the database.
    """
    # Retrieve database connection
    conn = connection()    
    cursor = conn.cursor()
    
    # Insert row
    try:
        stmt = """INSERT INTO sensor_data (data) VALUES ('{}')""".format(msg)
        cursor.execute(stmt)
    except:
        print('Error in write_record')
        
def get_records():
    """
    Return all records from the database
    """
    conn = connection()
    cursor = conn.cursor()
    
    try:
        stmt = """SELECT * FROM sensor_data"""
        cursor.execute(stmt)
        rows = cursor.fetchall()
    except:
        print('select failed')
    else:
        return rows
