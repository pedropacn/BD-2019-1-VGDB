import mysql.connector
from mysql.connector import errorcode


class DatabaseOp:

  __connection = None
  __cursor = None

  def __init__(self):    
    try:
      self.__connection = mysql.connector.connect(user='root', password='root', database='vgbd_db')
      self.__cursor = self.__connection.cursor(dictionary=True)

      # Insert new employee
      # cursor.execute("select * from Dogs")

      # print(cursor.fetchone())

      # cursor.close()
      # cnx.close()
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)

  def query(self, query, params=None):
       self.__cursor.execute(query, params)
       return self.__cursor

  def manip(self, query, params=None):
      self.__cursor.execute(query, params)
      self.__connection.commit()
      # try:
      # except:
      #   self.__connection.rollback()
      #   print("Rollback!")

  def close(self):
      self.__cursor.close()
      self.__connection.close()
