from flask import Flask

# para executar a classe deve passar o parametro __main__, neste caso usaremos só este arquivo então o parâmetro deve ser __name__ indicando o próprio arquivo
app = Flask(__name__)

# criando a rota
@app.route("/")
def ola_mundo():
    return "Hello World!"

@app.route("/about")
def exibir_sobre():
    return "Página sobre"

# modo debug ativo para ambiente local
if __name__ == "__main__":
    app.run(debug=True)