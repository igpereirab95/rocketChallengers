from flask import Flask, request, jsonify
from models.task import Task
# para executar a classe deve passar o parametro __main__, neste caso usaremos só este arquivo então o parâmetro deve ser __name__ indicando o próprio arquivo
app = Flask(__name__)

# criando a rota
# CRUD inicial

# instanciando lista vazia
tasks = []

# contador de ID
task_id_control = 1

# não auto completa, é uma variavel que pode ser setada mas deve ser escrita por completa qual verbo http usar
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control # usar quando faz interacao com variaveis fora da funcao, forca olha pra fora do escopo
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", "")) # pode ter um segundo parametro com string vazia para setar sem alguma informacao
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id}) # id vai servir pra rastrear

# recuperar a listagem e/ou um uníco registro
@app.route('/tasks', methods=['GET']) 
def get_tasks():
    task_list = [task.to_dict() for task in tasks] # for numa linha, criando lista com dicionario no formato da funcao to_dict

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }

    return jsonify(output) # retorno em json

# recuperar uma informacao, informacao convertida pelo flash dentro do <>
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict()) # retorna o dict correspondente ao id solicitado    
        
    return jsonify({"message":"Não foi possível encontrar a atividade"}), 404 # virgula status de retorno

# parametros de usuario -> https://flask.palletsprojects.com/en/stable/quickstart/#routing

# update
@app.route('/tasks/<int:id_task>', methods=['PUT'])
def update_task(id_task):
    task = None # se não achar, retorna vazio e status 404
    
    for t in tasks:
        if t.id == id_task:
            task = t
            break

    if task == None:
        return jsonify({"message":"Não foi possível encontrar a atividade"}), 404

    data = request.get_json() # recupera as informacoes da requisicao
    
    # inicio update
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    # fim update

    return jsonify({"message": "Tarefa atualizada com sucesso"}) # padrao sempre 200, caso queira mudar alterar o status aqui

# delete
@app.route('/tasks/<int:id_task>', methods=['DELETE'])
def delete_task(id_task):
    task = None # se não achar, retorna vazio e status 404
    
    for t in tasks:
        if t.id == id_task:
            task = t
            break # se atender a condicao, para assim parar quando encontrar e nao percorrer toda a lista

    if task == None:
        return jsonify({"message":"Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message":"Tarefa deletada com sucesso"})

# modo debug ativo para ambiente local
if __name__ == "__main__":
    app.run(debug=True)