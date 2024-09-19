from pydantic import BaseModel
from typing import List
from typing import Union
from model.locatario import Locatario


class LocatarioSchema(BaseModel):
    """ Define como um novo locatario a ser inserido deve ser representado
    """
    # id_locatario: int = 1
    nomeLocatario: str = 'Teste'
    sobrenomeLocatario: str = 'sobrenome Teste'
    emailLocatario: str = 'teste@teste.com.br'
    cpfLocatario: str = '00000000000'
    telLocatario: str = 'xxxxxxxx'
    celLocatario: str = 'xxxxxxxxx'

class LocatarioBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do locatario.
    """
    nomeLocatario: str = "Teste"
    
class ListagemLocatariosSchema(BaseModel):
    """ Define como uma listagem de locatarios será retornada.
    """
    locatario:List[LocatarioSchema]


def apresenta_locatarios(locatarios: Union[Locatario, List[Locatario]]):
    """ Retorna uma representação de um ou mais locatarios seguindo o schema definido em LocatarioViewSchema.
    """
    if isinstance(locatarios, Locatario):
        # Se for um único locatario, transforma em lista
        locatarios = [locatarios]
    
    result = []
    for locatario in locatarios:
        result.append({
            "nomeLocatario": locatario.nomeLocatario,
            "sobrenomeLocatario": locatario.sobrenomeLocatario,
            "emailLocatario": locatario.emailLocatario,
            "cpfLocatario": locatario.cpfLocatario,
            "telLocatario": locatario.telLocatario,
            "celLocatario": locatario.celLocatario
        })

    return {"locatarios": result}

class LocatarioViewSchema(BaseModel):
    """ Define como um locatario será retornado: locatario.
    """
    # id_locatario: int = 1
    nomeLocatario: str = 'Teste'
    sobrenomeLocatario: str = 'sobrenome Teste'
    emailLocatario: str = 'teste@teste.com.br'
    cpfLocatario: str = '00000000000'
    telLocatario: str = 'xxxxxxxx'
    celLocatario: str = 'x xxxxxxxx'


class LocatarioDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nomeLocatario: str

def apresenta_locatario(locatario):
    # Verifica se é uma lista
    if isinstance(locatario, list):
        return [{
            "id_locatario": locatario.id_locatario,
            "nomeLocatario": locatario.nomeLocatario,
            "sobrenomeLocatario": locatario.sobrenomeLocatario,
            "emailLocatario": locatario.emailLocatario,
            "cpfLocatario": locatario.cpfLocatario,
            "telLocatario": locatario.telLocatario,
            "celLocatario": locatario.celLocatario}
            for locatario in locatario]
    else:
        # Caso seja um único objeto Locatario
        return {
            "id_locatario": locatario.id_locatario,
            "nomeLocatario": locatario.nomeLocatario,
            "sobrenomeLocatario": locatario.sobrenomeLocatario,
            "emailLocatario": locatario.emailLocatario,
            "cpfLocatario": locatario.cpfLocatario,
            "telLocatario": locatario.telLocatario,
            "celLocatario": locatario.celLocatario
        }