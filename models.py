from database import Base
from sqlalchemy import String,Integer,Column


# Define Produto class from Base
class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)
    valor = Column(Integer)