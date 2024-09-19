#aqui é o banco de dados do cadastro
from sqlalchemy import Column, String, Integer
from model import Base

#classe que cria a tabela locatario
class Locatario(Base):
    __tablename__ = 'locatario'

    id_locatario = Column("id", Integer, primary_key=True, autoincrement=True)
    nomeLocatario = Column("nomeLocatario", String(20))
    sobrenomeLocatario = Column("sobrenomeLocatario", String(50))
    emailLocatario = Column("emailLocatario", String(100))
    cpfLocatario = Column("cpfLocatario", String(11))
    telLocatario = Column("telLocatario", String(8))
    celLocatario = Column("celLocatario", String(9))

    def __init__(self, nomeLocatario, sobrenomeLocatario, emailLocatario,cpfLocatario,telLocatario, celLocatario):
        self.nomeLocatario = nomeLocatario
        self.sobrenomeLocatario = sobrenomeLocatario
        self.emailLocatario = emailLocatario
        self.cpfLocatario = cpfLocatario
        self.telLocatario = telLocatario
        self.celLocatario = celLocatario