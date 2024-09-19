from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Locatario
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API MVP", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger")
locatario_tag = Tag(name="Locatario", description="Adição, visualização e remoção de locatarios à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/locatario', tags=[locatario_tag],
          responses={"200": LocatarioViewSchema})
def add_locatario(form: LocatarioSchema):
    """Adiciona um novo Locatario à base de dados

    Retorna uma representação dos locatarios.
    """
    locatario = Locatario(
        nomeLocatario=form.nomeLocatario,
        sobrenomeLocatario=form.sobrenomeLocatario,
        emailLocatario=form.emailLocatario,
        cpfLocatario=form.cpfLocatario,
        telLocatario=form.telLocatario,
        celLocatario=form.celLocatario
        )
    try:
        # criando conexão com a base
        session = Session()
        # adicionando locatario
        session.add(locatario)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado locatario de nome: '{locatario.nomeLocatario}'")
        return apresenta_locatario(locatario), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Locatario com o mesmo nome já está cadastrado na base"
        logger.warning(f"Erro ao adicionar locatario '{locatario.nomeLocatario}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar locatario '{locatario.nomeLocatario}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/locatarios', tags=[locatario_tag],
         responses={"200": ListagemLocatariosSchema})
def get_locatarios():
    """Faz a busca por todos os Locatarios cadastrados

    Retorna uma representação da listagem de locatarios.
    """
    logger.debug(f"Coletando locatarios ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    locatarios = session.query(Locatario).all()

    if not locatarios:
        # se não há locatarios cadastrados
        return {"locatarios": []}, 200
    else:
        logger.debug(f"%d locatarios encontrados" % len(locatarios))
        # retorna a representação de locatario
        return apresenta_locatarios(locatarios), 200


@app.get('/locatario', tags=[locatario_tag],
         responses={"200": LocatarioViewSchema})
def get_locatario(query: LocatarioBuscaSchema):
    """Faz a busca por um Locatario a partir do nome do locatario

    Retorna uma representação dos locatarios e comentários associados.
    """
    locatario_nome = query.nomeLocatario
    logger.debug(f"Coletando dados sobre locatario #{locatario_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    locatario = session.query(Locatario).filter(Locatario.nomeLocatario == locatario_nome).first()

    if not locatario:
        # se o locatario não foi encontrado
        error_msg = "Locatario não encontrado na base :/"
        logger.warning(f"Erro ao buscar locatario '{locatario_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Locatario encontrado: '{locatario.nomeLocatario}'")
        # retorna a representação de locatario
        return apresenta_locatario(locatario), 200


@app.delete('/locatario', tags=[locatario_tag],
            responses={"200": LocatarioDelSchema})
def del_locatario(query: LocatarioBuscaSchema):
    """Deleta um Locatario a partir do nome do locatario informado

    Retorna uma mensagem de confirmação da remoção.
    """
    locatario_nome = unquote(unquote(query.nomeLocatario))
    print(locatario_nome)
    logger.debug(f"Deletando dados sobre locatario #{locatario_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Locatario).filter(Locatario.nomeLocatario == locatario_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado locatario #{locatario_nome}")
        return {"mesage": "Locatario removido", "nome": locatario_nome}
    else:
        # se o locatario não foi encontrado
        error_msg = "Locatario não encontrado na base :/"
        logger.warning(f"Erro ao deletar locatario #'{locatario_nome}', {error_msg}")
        return {"mesage": error_msg}, 404