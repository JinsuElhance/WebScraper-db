import sqlite3
import pandas as pd
from weekone import get_webpage

conn = sqlite3.connect('automa_job.db')

conn = sqlite3.connect("WebScraper-db\web.db")

mydb = conn.cursor()
mydb.execute(''' CREATE TABLE jobs
    (title text, company text, link text, term text)''')
mydb.execute("INSERT INTO jobs VALUES ('semi-professional waffle cosplayer','Office of Carol Christ','pornhub.com','20XX-20YY')")

job_info = get_webpage('https://www.ziprecruiter.com/candidate/search?location=Berkeley%2C%20California&search=Software')

for job in job_info:
    job_title = job[0]
    job_company = job[1]
    job_link = job[2]
    mydb.execute("INSERT INTO jobs VALUES (" + job_title + ',' + job_company + ',' + job_link + ',' + 'N/A' + ")")

conn.commit()

def show_table(table):
	sql_statement = "SELECT * FROM ?", table
	pd.read_sql(sql_statement, conn)
conn.commit()

conn.close()
