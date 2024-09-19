# Meu projeto da Pós Graduação em Desenvolvimento Fullstack - **MPV Sprint Desenvolvimento Fullstack básico**

Esse projeto inicial é um cadastro spa de locatários de um projeto maior de imobiliaria com foco em controle de aluguéis.


## Pré-requisitos para rodar o projeto:

> Obs: Para rodar o projeto é indicado o uso de ambiente virtual, abaixo os passo a passo para criar um ambiente virtual (https://virtualenv.pypa.io/en/latest/installation.html):

1º - Rodar o código para criar a ambiente virtual:

```
python -m venv env
```

2º - Entrar no ambiente virtual:

```
.\env\Script\activate
```

3º - Após a criação do ambiente virtual, instalar as dependências/bibliotecas, onde encontram-se no arquivo `requirements.txt` na pasta app:

```
(env)$ pip install -r requirements
```


## Como executar o projeto

Após efetuar os passos anteriores, após os requirements instalados, dentro da pasta app, no ambiente virtual, rodar o código abaixo:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para acessar a API.

Para rodar o projeto no navegador pelo html, abrir o arquivo index.html(na pasta front) no navegador.