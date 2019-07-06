from .Object import Object
from .database import DatabaseOp as db

class Games(Object):
  def __init__(self):
    # informa o nome da tabela no banco de dados
    Object.__init__(self, "games")

  # def create(self, name,score_critics,genres_id,series_id,art):
  #   new_obj = "INSERT INTO %s (name, score_critics, genres_id, series_id, art) VALUES ('%s','%s','%s','%s',%s)" % ('games', name,score_critics,genres_id,series_id,art)
  #   print(new_obj)
  #   datab = db()
  #   datab.manip(new_obj, None)
  #   datab.close()