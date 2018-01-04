"""Test learning journal."""

import os
from pyramid import testing
from pyramid.response import Response
import unittest
import pytest
from bs4 import BeautifulSoup
from faker import Faker
import datetime
from pyramid.config import Configurator
import transaction
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid_learning_journal.models.meta import Base
from pyramid_learning_journal.models import (
    MyModel,
    get_tm_session,
)
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
        # import pdb; pdb.set_trace()
        self.home = self.testapp.get('/')
        self.new_entry = self.testapp.get('/journal/new-entry')
        self.entry_detail = self.testapp.get('/journal/1')
        self.edit_entry = self.testapp.get('/journal/1/edit-entry')

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
        extyp = '<p>Created'
        assert extyp in self.entry_detail

    def test_edit_entry_view_200(self):
        """test_edit_entry_view_200."""
        assert self.edit_entry.status_code == 200

    def test_edit_entry_route_contains_heading(self):
        """test_edit_entry_route_contains_heading."""
        assert b'<h1>Edit entry:</h1>' in self.edit_entry.body


def test_home_route_get_request_200_ok(testapp):
    """Home route == 200."""
    response = testapp.get('/')
    assert response.status_code == 200


def test_home_route_get_no_entries_has_no_sections(testapp):
    """Ain't no children there."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('content')[0]
    assert not content.findChildren()


def test_home_route_get_no_entries_has_sections(testapp, fill_my_database):
    """One section."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('section')
    assert len(content) == 1


def test_home_route_with_many_entries_has_sections(testapp, fill_my_other_database):
    """Ton of entries."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('section')
    assert len(content) == 21


def test_create_view_post_empty_is_empty_dict(dummy_request):
    """POST requests without data should return an empty dictionary."""
    dummy_request.method = "POST"
    response = create_view(dummy_request)
    assert response == {}


def test_home_with_one_entry(testapp, fill_my_database):
    """Home has one entry."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('section')
    assert len(content) == 22


def test_home_with_many_entries(testapp, fill_my_other_database):
    """Home has many entries."""
    response = testapp.get('/')
    html = response.html
    content = html.find_all('section')
    assert len(content) == 42


def test_add_new_entry_200(testapp, dummy_request):
    """New entry == 200."""
    dummy_request.method = testapp.get('/journal/new-entry')
    assert dummy_request.response.status == '200 OK'


@pytest.fixture
def new_entry_response():
    """Set fixture for new entry page."""
    request = testing.DummyRequest()
    response = create_view(request)
    return response


def test_new_entry_view_returns_response_given_request(new_entry_response):
    """Home view returns a Response object when given a request."""
    assert isinstance(new_entry_response, dict)


FAKE_STUFF = Faker()
FAKE_ENTRIES = [MyModel(
    title=FAKE_STUFF.text(20),
    markdown=FAKE_STUFF.text(250),
    created=datetime.datetime.now(),
) for x in range(25)]


@pytest.fixture
def dummy_req(db_session):
    """Make a fake HTTP request."""
    return testing.DummyRequest(dbsession=db_session)


@pytest.fixture
def add_models(dummy_req):
    """Add entries to a dummy request."""
    dummy_req.dbsession.add_all(FAKE_ENTRIES)


@pytest.fixture(scope="session")
def configuration(request):
    """Set up a Configurator instance."""
    config = testing.setUp(settings={
        'sqlalchemy.url': os.environ.get('TEST_DATABASE')
    })
    config.include('.models')
    config.include('.routes')

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a session for interacting with the test database."""
    SessionFactory = configuration.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope="session")
def testapp(request):
    """Create a test application to use for functional tests."""
    from webtest import TestApp

    def main(global_config, **settings):
        """Function returns a fake Pyramid WSGI application."""
        settings['sqlalchemy.url'] = os.environ.get('TEST_DATABASE')
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')
        config.add_static_view(name='static',
                               path='pyramid_learning_journal:static')
        config.scan()
        return config.make_wsgi_app()

    app = main({})

    SessionFactory = app.registry['dbsession_factory']
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def teardown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(teardown)
    return TestApp(app)


@pytest.fixture
def fill_test_db(testapp):
    """Set fake entries to the db for a session."""
    SessionFactory = testapp.app.registry['dbsession_factory']
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add_all(FAKE_ENTRIES)

    return dbsession


def test_filling_fake_db(add_models, db_session):
    """Check for entries added to db."""
    assert len(db_session.query(MyModel).all()) == 67


def test_list_view_returns_dict(dummy_req):
    """Test list view returns a dict when called."""
    assert type(list_view(dummy_req)) == dict


def test_detail_view_returns_dict_with_db(db_session, dummy_req):
    """Test detail view returns a dict when called."""
    fake = MyModel(
        title=u'Stuff',
        markdown=u'Some thing goes here.',
        created=datetime.datetime.now(),
    )
    db_session.add(fake)
    fakeid = str(db_session.query(MyModel)[0].id)
    dummy_req.matchdict['id'] = fakeid
    response = detail_view(dummy_req)
    assert type(response) == dict


def test_update_view_returns_dict_with_db(dummy_req, db_session):
    """Test edit view returns a dict when called with a db."""
    fake = MyModel(
        title=u'Stuff',
        markdown=u'Some thing goes here.',
        created=datetime.datetime.now(),
    )
    db_session.add(fake)
    fakeid = str(db_session.query(MyModel)[0].id)
    dummy_req.matchdict['id'] = fakeid
    response = update_view(dummy_req)
    assert type(response) == dict


def test_detail_view_with_id_raises_except(dummy_req):
    """Test proper error raising with non matching id on detail view."""
    dummy_req.matchdict['id'] = '9000'
    with pytest.raises(HTTPNotFound):
        detail_view(dummy_req)


def test_update_view_with_id_raises_except(dummy_req):
    """Test proper error raising with non matching id on update view."""
    dummy_req.matchdict['id'] = '9000'
    with pytest.raises(HTTPNotFound):
        update_view(dummy_req)
