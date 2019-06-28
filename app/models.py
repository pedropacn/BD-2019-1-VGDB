from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.database.Object import Object

class User(UserMixin, Object):
    """
    Create an Employee table
    """

    id = None
    email = None
    username = None
    first_name =None
    last_name =None
    password_hash = None

    def __init__(self):
      Object.__init__(self, 'Users')

    def password_hash(self, password):
        """
        password to a hashed password
        """
        return generate_password_hash(password)

    def verify_password(self, password_hash, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(password_hash, password)

    def filter_by(self, **kwargs):
      user = super().filter_by(**kwargs)
      self.id = user['id']
      self.email = user['email']
      self.username = user['username']
      return user
    


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.filter_by(id=int(user_id))
    return user
