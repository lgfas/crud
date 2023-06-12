from database import Base,engine
from models import Produto

print("Creating database ....")

Base.metadata.create_all(engine)