# Создать задачу,
# Проставить отметку о выполнении
# и проверить что completed ==True
import requests


def test_add():
    body = {"title": "new", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    body = {"completed": True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200
    response = response.json()
    assert response['completed'] == True