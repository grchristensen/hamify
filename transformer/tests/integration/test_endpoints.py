import pytest
from app import app as flaskr


@pytest.fixture
def client():
    flaskr.app.config['TESTING'] = True

    with flaskr.app.app_context():
        with flaskr.app.test_client() as client:
            yield client


def test_convert_spam_to_ham(client):
    client.post("/spam", data={"content": "This is not a spam message"})
    response = client.get("ham/1")

    assert response.status_code == 200
    assert response.json["success"]


def test_ham_not_found(client):
    response = client.get("ham/4")

    assert response.status_code == 404
