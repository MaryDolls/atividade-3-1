from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/imc', methods=['GET'])
def calcular_imc():
    # Recebe os parâmetros do formulário
    nome = request.args.get('nome')
    peso = float(request.args.get('peso'))
    altura = float(request.args.get('altura'))

    # Calcula o IMC
    imc = peso / (altura ** 2)

    # Retorna o template com as informações
    return render_template('imc.html', nome=nome, imc=round(imc, 2))

if __name__ == '__main__':
    app.run(debug=True)
