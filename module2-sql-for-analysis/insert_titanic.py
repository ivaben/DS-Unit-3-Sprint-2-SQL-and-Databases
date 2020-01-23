import sqlite3
import psycopg2
import pandas


titanic_df = pandas.read_csv('titanic.csv')

dbname = 'wuufwvap'
user = 'wuufwvap'
password = 'GUVqMp5Hij-fYFgCOCDd_xgnDs6khydb'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# enumerated type of declaration
CREATE TYPE survived_e AS ENUM ('0','1');
CREATE TYPE gender_e AS ENUM ('male', 'female');

pg_curs.execute(survived_e)
pg_conn.commit()

pg_curs.execute(gender_e)
pg_conn.commit()


create_table_statement = """
CREATE TABLE titanic ( Survived survived_e, 
                       Pclass INT,
                       Name VARCHAR(150), 
                       Sex gender_e,
                       Age NUMERIC(6),
                       Siblings Spouses VARCHAR(40),
                       Aboard INT,
                       Parents Children INT, 
                       Aboard INT,
                       Fare FLOAT
  
);
"""
pg_curs.execute(create_table_statement)
pg_conn.commit()


insert_statement = """
INSERT INTO titanic_table (Survived, 
                       Pclass,
                       Name, 
                       Sex,
                       Age,
                       Siblings/Spouses,
                       Aboard,
                       Parents/Children, 
                       Aboard,
                       Fare ) VALUES ();

  
"""

pg_curs.execute(insert_statement)
pg_conn.commit()

query = "SELECT * FROM titanic_table;"
pg_curs.execute(query)
pg_curs.fetchall()




