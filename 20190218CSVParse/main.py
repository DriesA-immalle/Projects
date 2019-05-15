import csv
import sqlite3

conn = sqlite3.connect('apps')
cursor = conn.cursor()

with open('apps.csv') as csvfile:
    text = csv.reader(csvfile, delimiter=',')
    for row in text:
        appid = row[0]
        name = row[1]
        category = row[2]
        downloads = row[3]
        price = row[4]
        cursor.execute(f'INSERT INTO apps(ID,Name,Category,Downloads,Price) VALUES ("{appid}","{name}","{category}","{downloads}","{price}");')
        conn.commit()