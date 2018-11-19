import sqlite3
import pandas as pd

conn = sqlite3.connect('automa_job.db')

conn = sqlite3.connect("WebScraper-db\web.db")

mydb = conn.cursor()
mydb.execute(''' CREATE TABLE jobs
    (title text, company text, link text, term text)''')
mydb.execute("INSERT INTO jobs VALUES ('semi-professional waffle cosplayer','Office of Carol Christ','pornhub.com','20XX-20YY')")
conn.commit()

def show_table(table):
	sql_statement = "SELECT * FROM ?", table
	pd.read_sql(sql_statement, conn)
conn.commit()

conn.close()
