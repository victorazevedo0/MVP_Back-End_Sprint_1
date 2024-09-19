from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from model.base import Base
from model.locatario import Locatario

db_path = "database/" #diretorio do banco de dados

#verifica se existe o diretorio
if not os.path.exists(db_path):
#caso o diretorio do banco não existe, o comando abaixo cria o diretorio
    os.makedirs(db_path)

#url de acesso ao banco (nesse caso é local)
db_url = 'sqlite:///%s/db_imobiliaria.sqlite3' % db_path

#cria o motor de conexao com o banco
engine = create_engine(db_url, echo=False)

#instacia um criador de sessão com o banco
Session = sessionmaker(bind=engine)

#caso o banco não exista, no codigo abaixo ele cria
if not database_exists(engine.url):
    create_database(engine.url)

#cria as tabelas do banco de dados, caso não existam
Base.metadata.create_all(engine)