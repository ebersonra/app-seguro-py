import requests
import json
import sys
import subprocess

# Função para obter o access_token do ApiPostGetToken.py
def get_access_token():
    result = subprocess.run(['python', 'ApiPostGetToken.py'], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if "Access Token:" in line:
            return line.split("Access Token:")[1].strip()
    return None

# Obter o access_token
access_token = get_access_token()

if access_token:
    # Obter os parâmetros sinistro e cnpj da linha de comando
    sinistro = sys.argv[1]
    cnpj = sys.argv[2]

    # URL da API
    url = f"https://apis.com.br/v1/avisos/{sinistro}/{cnpj}"

    # Cabeçalhos da requisição
    headers = {
        "Origin": "https://apis.com.br",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    # Executa a requisição GET
    response = requests.get(url, headers=headers)

    # Verifica o status da resposta
    if response.status_code == 200:
        # Imprime o corpo da resposta em formato JSON
        response_json = response.json()
        formatted_json = json.dumps(response_json, indent=4)
        print(f"Status Code: {response.status_code}")
        print(f"Response Body:\n{formatted_json}")
    else:
        # Imprime o código de status e a mensagem de erro no stderr
        response_json = response.json()
        formatted_json = json.dumps(response_json, indent=4)
        print(f"Status Code: {response.status_code}", file=sys.stderr)
        print(f"Response Body:\n{formatted_json}", file=sys.stderr)
else:
    print("Failed to retrieve access token", file=sys.stderr)