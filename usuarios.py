
from models import User

usuarios = [
    User(id=1, username="arincon", password="12345", is_admin=False),
    User(id=2, username="fjimenez", password="5678", is_admin=False),
    User(id=3, username="admin", password="0000", is_admin=True),
]
