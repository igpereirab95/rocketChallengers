import pytest
import requests

# testar CRUD

BASE_URL = 'http://127.0.0.1:5000'

tasks = []

# testando o CREATE da API
def test_create_task():
    # nova tarefa que sera criada
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Testando nova tarefa"
    }
    # lib requests que vai chamar a api com os dados, lembrando de setar uma string como parametro
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    # testa o status 200 da resposta da requisicao
    assert response.status_code == 200

    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

# test READ
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

# get ID unico
def test_get_task():
    if tasks:
        task_id = tasks[0] # esse id e criado nesse script, mas vai ter coorelacao com o a api por conta deste teste que cria uma tarefa no inicio tambem
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]

# testando UPDATE
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "APIs com Flask",
            "title": "Estudar API do LOL"
        }

        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        # validar se foi alterado mesmo
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]


# testando DELETE
def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404