from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organizacao do teste)
    response = client.get('/')  # Act (acao do teste)
    assert response.status_code == HTTPStatus.OK  # Assert (verifica o teste)
    assert response.json() == {'message': 'Olá Mundo'}  # verifica resposta
