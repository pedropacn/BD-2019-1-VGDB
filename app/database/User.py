from .Object import Object

class User(Object):
  def __init__(self, table_name):
    Object.__init__(table_name)