"""."""


def test_home_route_get_request_200_ok(testapp):
    """."""
    response = testapp.get('/')
    assert response.status_code == 200
