import sqlite3
conn = sqlite3.connect('automa_job.db')

mydb = conn.cursor()
mydb.execute(''' CREATE TABLE jobs
				(title text, company text, link text, term text)''')
mydb.execute("INSERT INTO jobs VALUES ('semi-professional waffle cosplayer','Office of Carol Christ','pornhub.com','20XX-20YY')")
conn.commit()
conn.close()