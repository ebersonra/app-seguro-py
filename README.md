## Projeto de Consulta de Apólice e Aviso de Sinistro

Este projeto é uma aplicação web que permite consultar informações de apólices e avisos de sinistro da Tokio Marine. A aplicação foi desenvolvida utilizando Flask para o backend e HTML, CSS e JavaScript para o frontend. A aplicação faz requisições a APIs externas para obter os dados necessários.

## Estrutura do Projeto

- `index.html`: Página inicial do projeto.
- `aviso.html`: Página para consultar avisos de sinistro.
- `apolice.html`: Página para consultar apólices.
- `style.css`: Arquivo de estilos CSS.
- `server.py`: Servidor Flask que serve as páginas e executa os scripts Python.
- `ApiGetAviso.py`: Script Python que faz a requisição à API de avisos de sinistro.
- `ApiGetApolice.py`: Script Python que faz a requisição à API de apólices.
- `ApiPostGetToken.py`: Script Python que obtém o token de acesso necessário para autenticação nas APIs.

## Requisitos

- Python 3.x
- Flask
- Requests

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/ebersonra/app-seguro-py.git
   cd app-seguro-py
   ```
2. Instale as dependências:
    ```sh
    pip install flask requests
    ```