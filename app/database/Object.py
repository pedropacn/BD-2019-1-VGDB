from .database import DatabaseOp as db

class Object:
  def __init__(self, table_name):
      self.__db = db()
      self.table_name = table_name

  def __del__(self):
    self.__db.close()

  def all(self):
      query = "SELECT * FROM %s" % (self.table_name)
      cursor = self.__db.query(query)
      # print(cursor.fetchall())
      return cursor.fetchall()

  def create(self, **kwargs):
    labels = ", ".join([k for k in kwargs.keys()])
    values = ", ".join(["'{}'".format(v) for v in kwargs.values()])
    new_obj = "INSERT INTO %s (%s) VALUES (%s)" % (self.table_name, labels, values)
    # print(new_obj)
    self.__db.manip(new_obj, None)
    # print("Object created successfully!")

  def update(self, id, **kwargs):
    obj = self.select(id)
    attr = ", ".join(["{}='{}'".format(k,v) for k,v in kwargs.items()])
    update_obj = "UPDATE %s SET %s WHERE id = %s" % (self.table_name, attr, id)
    # print(update_dog)
    self.__db.manip(update_obj, None)
    # print("{} updated successfully!".format(obj))


  def delete(self, id):
    obj = self.select(id)
    delete_obj = "DELETE FROM %s WHERE id = %d" % (self.table_name, id)
    self.__db.manip(delete_obj, None)
    # print("{} deleted successfully!".format(obj))

  def select(self, id):
    select_obj = "SELECT * FROM %s WHERE id = %d" % (self.table_name, id)
    obj = self.__db.query(select_obj).fetchone()
    return obj

  def filter_by(self, **kwargs):
    if len(kwargs) == 1:
      query = "".join(["{}='{}'".format(k,v) for k,v in kwargs.items()])
      select_obj = "SELECT * FROM %s WHERE %s" % (self.table_name, query)
      # print(select_obj)
      obj = self.__db.query(select_obj).fetchone()
      # print(obj)
      return obj
    else:
      print("Filter falhou.")
      return False


# dogo = Dogs()
# dogo.all()
# # dogo.create('carlinhos', 32)
# dogo.select(2)
# dogo.delete(3)
# dogo.all()
# dogo.update(4, name='joao', age=14)
# dogo.all()
