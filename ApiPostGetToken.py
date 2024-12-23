import requests
import json

# URL da API
url = "https://apis.com.br/access-token"

# Token de autorização decodificado
token = "<token_aqui>"

# Cabeçalhos da requisição
headers = {
    "Authorization": f"Basic {token}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Dados da requisição (exemplo)
data = {
    "grant_type": "<valor_aqui>"
}

# Fazendo a requisição POST
response = requests.post(url, headers=headers, data=data)

# Verificando a resposta e formatando o JSON
if response.status_code == 200:
    # Retorna o access_token
    response_json = response.json()
    access_token = response_json.get("access_token")
    print("Access Token:", access_token)

    formatted_json = json.dumps(response_json, indent=4)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body:\n{formatted_json}")
else:
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")