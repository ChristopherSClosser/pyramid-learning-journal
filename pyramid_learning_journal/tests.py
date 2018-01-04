from pyramid import testing
from pyramid.response import Response
import unittest
import pytest
from bs4 import BeautifulSoup
from pyramid_learning_journal.views.default import (
    list_view,
    create_view,
    update_view,
    detail_view
)


class FunctionalTests(unittest.TestCase):
    """."""

    def setUp(self):
        """."""
        from pyramid_learning_journal import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)
        self.home = self.testapp.get('/')
        self.new_entry = self.testapp.get('/journal/new-entry')
        self.entry_detail = self.testapp.get('/journal/592')
        self.edit_entry = self.testapp.get('/journal/592/edit-entry')

    def test_home_view_200(self):
        """test_new_entry_view_200."""
        assert self.home.status_code == 200

    def test_home_route_contains_heading(self):
        """test_home_route_contains_heading."""
        assert b'<title>Learning Journal</title>' in self.home.body

    def test_home_route_contains_entries(self):
        """test_home_route_contains_entries."""
        soup = BeautifulSoup(self.home.body, "html.parser")
        res = [tag.name for tag in soup.find_all()]
        extyp = []
        for item in res:
            if item == 'section':
                extyp.append(item)
        assert len(extyp) == 24

    def test_new_entry_view_200(self):
        """test_new_entry_view_200."""
        assert self.new_entry.status_code == 200

    def test_new_entry_route_contains_heading(self):
        """test_new_entry_route_contains_heading."""
        assert b'<h2>Add a new entry:</h2>' in self.new_entry.body

    def test_entry_detail_view_200(self):
        """test_entry_detail_view_200."""
        assert self.entry_detail.status_code == 200

    def test_entry_detail_view_single_entry(self):
        """test_entry_detail_view_has_single_entry."""
        soup = BeautifulSoup(self.entry_detail.body, "html.parser")
        res = [tag.name for tag in soup.find_all()]
        extyp = []
        for item in res:
            if item == 'section':
                extyp.append(item)
        assert len(extyp) == 1

    def test_entry_detail_view_has_single_entry(self):
        """test_entry_detail_view_has_single_entry."""
        html = BeautifulSoup(self.entry_detail.body, 'html.parser')
        assert len(html.section) == 4

    def test_entry_detail_view_correct_entry(self):
        """test_entry_detail_view_correct_entry."""
        extyp = '<p>Created 2017-10-17T12:49:02.615079 </p>'
        assert extyp in self.entry_detail

    def test_edit_entry_view_200(self):
        """test_edit_entry_view_200."""
        assert self.edit_entry.status_code == 200

    def test_edit_entry_route_contains_heading(self):
        """test_edit_entry_route_contains_heading."""
        assert b'<h1>Edit entry:</h1>' in self.edit_entry.body


@pytest.fixture
def home_response():
    """Set fixture for home page."""
    request = testing.DummyRequest()
    response = list_view(request)
    return response


@pytest.fixture
def new_entry_response():
    """Set fixture for new entry page."""
    request = testing.DummyRequest()
    response = create_view(request)
    return response


def test_home_view_returns_response_given_request(home_response):
    """Home view returns a Response object when given a request."""
    assert isinstance(home_response, dict)


def test_new_entry_view_returns_response_given_request(new_entry_response):
    """Home view returns a Response object when given a request."""
    assert isinstance(new_entry_response, dict)
