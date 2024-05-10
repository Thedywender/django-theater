def test_get_authentication_token_using_wrong_credentials(client):
    response = client.post(
        "/api/generate-token", {"username": "admin", "password": "wrong"}
    )
    assert response.status_code == 400


def test_get_authentication_token(client):
    response = client.post(
        "/api/generate-token", {"username": "testuser", "password": "12345"}
    )
    assert response.status_code == 200
    assert "token" in response.json()
