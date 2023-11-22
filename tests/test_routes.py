def test_index_page(test_app):
    """
    GIVEN a Flask application
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    with test_app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Main Page" in response.data


def test_account_page(test_app):
    """
    GIVEN a Flask application
    WHEN the '/account' route is requested (GET)
    THEN check that the response is valid
    """
    with test_app.test_client() as client:
        response = client.get('/account')
        assert response.status_code == 200
        assert b"Personal Account" in response.data


def test_auth_page_proxy(test_app):
    """
    GIVEN a Flask application
    WHEN the '/auth' route is requested (GET)
    THEN check that the response is valid
    """
    with test_app.test_client() as client:
        response = client.get('/auth')
        assert response.status_code == 200
        # Check for some content specific to the auth page
