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
## Executando o Servidor

1. Navegue até o diretório do projeto:
    ```sh
    cd /<seu_diretorio_desenvolvimento_aqui>/
    ```
2. Execute o servidor Flask:
    ```sh
    python server.py
    ```
3. Abra o navegador e acesse `http://127.0.0.1:5000`.

## Testando as Telas

### Página Inicial
1. Acesse `http://127.0.0.1:5000`.
2. A página inicial deve ser exibida com links para as páginas de Aviso e Apólice.

### Página de Aviso
1. Acesse `http://127.0.0.1:5000/aviso`.
2. Preencha os campos `Sinistro` e `CNPJ`.
3. Clique no botão `Exibir Aviso`.
4. A aplicação fará uma requisição à API de avisos e exibirá os resultados com paginação.
5. Se ocorrer um erro, a mensagem de erro será exibida.

### Página de Apólice
1. Acesse `http://127.0.0.1:5000/apolice`.
2. Preencha os campos `Placa ou Chassi`, `Data da Ocorrência` e `Número do Documento do Segurado`.
3. Clique no botão `Consultar Apólice`.
4. A aplicação fará uma requisição à API de apólices e exibirá os resultados com paginação.
5. Se ocorrer um erro, a mensagem de erro será exibida.

## Scripts Python
### ApiGetAviso.py
1. Este script faz uma requisição à API de avisos de sinistro.
2. Para executar o script manualmente:
    ```sh
    python ApiGetAviso.py <sinistro> <cnpj>
    ```
3. O script imprimirá o resultado no console.

### ApiGetApolice.py
1. Este script faz uma requisição à API de apólices.
2. Para executar o script manualmente:
    ```sh
    python ApiGetApolice.py <placaOuChassi> <dataOcorrencia> <numeroDocumentoSegurado>
    ```
3. O script imprimirá o resultado no console.
### ApiPostGetToken.py
1. Este script obtém o token de acesso necessário para autenticação nas APIs.
2. Para executar o script manualmente:
    ```sh
    python ApiPostGetToken.py
    ```
3. O script imprimirá o token de acesso no console.

## Estrutura de Pastas
## Estrutura de Pastas

```plaintext
/<seu_diretorio_desenvolvimento_aqui>/app-seguro-py/
│
├── ApiGetApolice.py
├── ApiGetAviso.py
├── ApiPostGetToken.py
├── apolice.html
├── aviso.html
├── index.html
├── server.py
└── style.css
```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


### Explicação:
1. **Markdown**:
   - O README foi escrito em Markdown para fornecer uma visão geral do projeto, incluindo a estrutura do projeto, requisitos, instalação, execução do servidor, teste das telas, scripts Python, estrutura de pastas, contribuição e licença.
   - Instruções detalhadas são fornecidas para testar cada tela e script.

### Executando o Servidor

1. **Navegue até o Diretório do Arquivo**:
   ```sh
   cd /<seu_diretorio_desenvolvimento_aqui>/app-seguro-py/
   ```
2. Execute o Servidor:
    ```sh
    python server.py
    ```
3. Acesse a Página:
    - Abra o navegador e vá para `http://127.0.0.1:5000`.

Isso deve garantir que a página `index.html` funcione corretamente, permitindo que o usuário insira os dados necessários para consultar o aviso ou apólice. Após a consulta, o resultado será exibido com os dados em seus respectivos campos. Caso falhe a chamada para api, uma mensagem de erro deve ser exibida conforme o retorno.