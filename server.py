from flask import Flask, jsonify, send_from_directory, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/execute-script')
def execute_script():
    result = subprocess.run(['python', 'ApiPostGetToken.py'], capture_output=True, text=True)
    return jsonify(stdout=result.stdout, stderr=result.stderr)

@app.route('/aviso')
def aviso():
    return send_from_directory('.', 'aviso.html')

@app.route('/execute-aviso')
def execute_aviso():
    sinistro = request.args.get('sinistro')
    cnpj = request.args.get('cnpj')
    result = subprocess.run(['python', 'ApiGetAviso.py', sinistro, cnpj], capture_output=True, text=True)
    return jsonify(stdout=result.stdout, stderr=result.stderr)

@app.route('/apolice')
def apolice():
    return send_from_directory('.', 'apolice.html')

@app.route('/execute-apolice')
def execute_apolice():
    placaOuChassi = request.args.get('placaOuChassi')
    dataOcorrencia = request.args.get('dataOcorrencia')
    numeroDocumentoSegurado = request.args.get('numeroDocumentoSegurado')
    result = subprocess.run(['python', 'ApiGetApolice.py', placaOuChassi, dataOcorrencia, numeroDocumentoSegurado], capture_output=True, text=True)
    return jsonify(stdout=result.stdout, stderr=result.stderr)

if __name__ == '__main__':
    app.run(debug=True)