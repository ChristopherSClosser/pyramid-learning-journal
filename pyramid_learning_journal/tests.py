"""Journal tests."""

import pytest
from pyramid import testing
from pyramid.response import Response
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


@pytest.fixture
def home_response():
    """Set fixture for home page."""
    request = testing.DummyRequest()
    response = list_view(request)
    return response


@pytest.fixture
def entry_response():
    """Set fixture for individual entry page."""
    request = testing.DummyRequest()
    response = detail_view(request)
    return response


@pytest.fixture
def edit_entry_response():
    """Set fixture for edit entry page."""
    request = testing.DummyRequest()
    response = update_view(request)
    return response


@pytest.fixture
def new_entry_response():
    """Set fixture for new entry page."""
    request = testing.DummyRequest()
    response = create_view(request)
    return response


def test_home_view_returns_response_given_request(home_response):
    """Home view returns a Response object when given a request."""
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, Response)


def test_home_view_is_good(home_response):
    """Home view hass a 200 ok."""
    request = testing.DummyRequest()
    response = list_view(request)
    assert response.status_code == 200


def test_home_view_returns_proper_content(home_response):
    """Home view returns the actual content from the html."""
    request = testing.DummyRequest()
    response = list_view(request)
    expected_text = '<div class="entries">'
    assert expected_text in response.text


def test_new_entry_view_returns_response_given_request(new_entry_response):
    """New entry view returns a Response object when given a request."""
    request = testing.DummyRequest()
    response = create_view(request)
    assert isinstance(response, Response)


def test_new_entry_view_is_good(new_entry_response):
    """New entry view hass a 200 ok."""
    request = testing.DummyRequest()
    response = create_view(request)
    assert response.status_code == 200


def test_new_entry_view_returns_proper_content(new_entry_response):
    """New entry view returns the actual content from the html."""
    request = testing.DummyRequest()
    response = create_view(request)
    expected_text = '<title>New Entry</title>'
    assert expected_text in response.text


def test_edit_entry_view_returns_response_given_request(edit_entry_response):
    """Edit entry view returns a Response object when given a request."""
    request = testing.DummyRequest()
    response = update_view(request)
    assert isinstance(response, Response)


def test_edit_entry_view_is_good(edit_entry_response):
    """Edit entry view hass a 200 ok."""
    request = testing.DummyRequest()
    response = update_view(request)
    assert response.status_code == 200


def test_edit_entry_view_returns_proper_content(edit_entry_response):
    """Edit entry view returns the actual content from the html."""
    request = testing.DummyRequest()
    response = update_view(request)
    expected_text = '<title>Edit Entry</title>'
    assert expected_text in response.text


def test_entry_view_returns_response_given_request(entry_response):
    """Entry view returns a Response object when given a request."""
    request = testing.DummyRequest()
    response = detail_view(request)
    assert isinstance(response, Response)


def test_entry_view_is_good(entry_response):
    """Entry view hass a 200 ok."""
    request = testing.DummyRequest()
    response = detail_view(request)
    assert response.status_code == 200


def test_entry_view_returns_proper_content(entry_response):
    """Entry view returns the actual content from the html."""
    request = testing.DummyRequest()
    response = detail_view(request)
    expected_text = '<title>Entry Detail</title>'
    assert expected_text in response.text
