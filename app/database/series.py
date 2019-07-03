from .Object import Object

class Series(Object):
  def __init__(self):
    # informa o nome da tabela no banco de dados
    Object.__init__(self, "series")
