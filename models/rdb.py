from dotenv import load_dotenv
load_dotenv()

import os
from mysql.connector.pooling import MySQLConnectionPool
dbconfig = {
  "user": os.getenv("DB_USER"),
  "password": os.getenv("DB_PASSWORD"),
  "host": os.getenv("DB_HOST"),
  "port": "3306",
  "database": "aws",
  "pool_name": "mypool"
}
cnxpool = MySQLConnectionPool(pool_size=5, **dbconfig)

class CRUD:
  def create_article(text, image_url):
    with cnxpool.get_connection() as cnx:
      cursor = cnx.cursor()
      insert = "INSERT INTO article(text, image) VALUE(%s, %s)"
      cursor.execute(insert, (text, image_url))
      cnx.commit()
  def read_article():
    with cnxpool.get_connection() as cnx:
      cursor = cnx.cursor()
      select = "SELECT * from article"
      cursor.execute(select)
      rows = cursor.fetchall()
      return rows
  def delete_article():
    with cnxpool.get_connection() as cnx:
      cursor = cnx.cursor()
      delete = "DELETE FROM article"
      cursor.execute(delete)
      cnx.commit()