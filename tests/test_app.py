from http import HTTPStatus

"""
Os testes estão interdependentes um do outro e isso precisa ser corrigido.
"""


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (acao do teste)
    assert response.status_code == HTTPStatus.OK  # Assert (verifica o teste)
    assert response.json() == {'message': 'Olá Mundo'}  # Assert


def test_create_user(client):
    response = client.post(  # Act
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {  # Assert
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'users': [
            {  # Assert
                'id': 1,
                'username': 'alice',
                'email': 'alice@example.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'alice_updated',
            'email': 'aliceupdt@example.com',
            'password': 'secretaltered',
        },
    )
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'username': 'alice_updated',
        'email': 'aliceupdt@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put('/users/9999999')
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY  # Assert


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'username': 'alice_updated',
        'email': 'aliceupdt@example.com',
        'id': 1,
    }
