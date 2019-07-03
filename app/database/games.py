from .Object import Object

class Games(Object):
  def __init__(self):
    # informa o nome da tabela no banco de dados
    Object.__init__(self, "games")