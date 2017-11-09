"""."""

from datetime import datetime
from pyramid_learning_journal.models import MyModel
from pyramid_learning_journal.views.default import (
    list_view,
    detail_view,
    update_view,
    create_view
    )


def test_home_route_get_request_200_ok(testapp):
    """."""
    response = testapp.get('/')
    assert response.status_code == 200


def test_home_route_get_no_entries_has_no_sections(testapp):
    """."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('content')[0]
    assert not content.findChildren()


def test_home_route_get_no_entries_has_sections(testapp, fill_my_database):
    """."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('section')
    assert len(content) == 1


def test_home_route_with_many_entries_has_sections(testapp, fill_my_other_database):
    """."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('section')
    assert len(content) == 20


def test_create_view_post_empty_is_empty_dict(dummy_request):
    """POST requests without data should return an empty dictionary."""
    dummy_request.method = "POST"
    response = create_view(dummy_request)
    assert response == {}


def test_home_with_one_entry(testapp, fill_my_database):
    """."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('section')
    assert len(content) == 1


def test_home_with_many_entries(testapp, fill_my_other_database):
    """."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('section')
    assert len(content) == 20


def test_add_new_entry_200(testapp, dummy_request):
    """."""
    dummy_request.method = testapp.get('/journal/new-entry')
    assert dummy_request.response.status == '200 OK'