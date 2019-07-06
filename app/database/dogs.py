from .Object import Object

class Dogs(Object):
  def __init__(self):
    # informa o nome da tabela no banco de dados
    Object.__init__(self, "Dogs")

# from .database import DatabaseOp as db

# class Dogs:
#   def __init__(self):
#        self.__db = db()

#   def all(self):
#       cursor = self.__db.query("SELECT * FROM Dogs")
#       # print(cursor.fetchall())
#       # [{"id": i, "name": n, "age": a} for (i,n,a) in cursor.fetchall()]
#       return cursor.fetchall()

#   def create(self, name, age): # **kwargs
#     new_dog = ("INSERT INTO Dogs "
#                "(name, age) "
#                "VALUES (%s, %s)")
    
#     self.__db.manip(new_dog, (name, age))
#     print("Dogo created successfully!")

#   def update(self, id, **kwargs):
#     dog = self.select(id)
#     attr = ", ".join(["{}='{}'".format(k,v) for k,v in kwargs.items()])
#     update_dog = "UPDATE Dogs SET %s WHERE id = %s" % (attr, id)
#     # print(update_dog)
#     self.__db.manip(update_dog, None)
#     print("{} updated successfully!".format(dog))


#   def delete(self, id):
#     dog = self.select(id)
#     # print(dog)
#     delete_dog = "DELETE FROM Dogs WHERE id = %d" % (id)
#     self.__db.manip(delete_dog, None)
#     print("{} deleted successfully!".format(dog))

#   def select(self, id, name=None, age=None):
#     # porque funciona ?
#     select_dog = "SELECT * FROM Dogs WHERE id = %d" % id
#     dog = self.__db.query(select_dog)
#     # print(dog.fetchone())
#     return dog.fetchone()


# # dogo = Dogs()
# # dogo.all()
# # # dogo.create('carlinhos', 32)
# # dogo.select(2)
# # dogo.delete(3)
# # dogo.all()
# # dogo.update(4, name='joao', age=14)
# # dogo.all()
