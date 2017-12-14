"""Journal tests."""

import pytest
from pyramid import testing
from pyramid_learning_journal.views.default import (
    list_view,
    detail_view,
    update_view,
    create_view
)


@pytest.fixture
def dummy_request():
    """Dummy request fixture to use throughout file."""
    return testing.DummyRequest()


def test_list_view_response_status_code_200(dummy_request):
    """test_list_view_response_status_code_200."""
    response = list_view(dummy_request)
    assert response.status_code == 200


def test_detail_view_response_status_code_200(dummy_request):
    """test_detail_view_response_status_code_200."""
    response = detail_view(dummy_request)
    assert response.status_code == 200


def test_create_view_response_status_code_200(dummy_request):
    """test_create_view_response_status_code_200."""
    response = create_view(dummy_request)
    assert response.status_code == 200


def test_create_update_response_status_code_200(dummy_request):
    """test_create_update_response_status_code_200."""
    response = update_view(dummy_request)
    assert response.status_code == 200


def test_list_view_response_is_html(dummy_request):
    """test_list_view_response_is_html."""
    response = list_view(dummy_request)
    assert response.content_type == 'text/html'


def test_list_view_response_has_proper_content(dummy_request):
    """test_list_view_response_has_proper_content."""
    response = list_view(dummy_request)
    assert b'<title>Learning Journal</title>' in response.body
