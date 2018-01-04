"""Setup for tests."""

from pyramid.config import Configurator
from pyramid.testing import DummyRequest
from pyramid_learning_journal.models.meta import Base
from pyramid import testing
import pytest
from pyramid_learning_journal.models import MyModel
import os
import datetime


def main(global_config, **settings):
    settings['sqlalchemy.url'] = os.environ.get('TEST_DATABASE')
    config = Configurator(settings=settings)
    config.add_static_view(name='static', path='pyramid_learning_journal:static')
    config.include('pyramid_jinja2')
    config.include('pyramid_learning_journal.routes')
    config.include('pyramid_learning_journal.models')
    config.scan()
    return config.make_wsgi_app()


@pytest.fixture
def testapp(request):
    """Fixture for a fully-configured test application."""
    from webtest import TestApp
    app = main({})

    SessionFactory = app.registry['dbsession_factory']
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)
    return TestApp(app)


@pytest.fixture
def fill_my_database(testapp):
    SessionFactory = testapp.app.registry["dbsession_factory"]
    session = SessionFactory()
    new_entry = MyModel(
        title="this is a test",
        markdown="this is some text to put in the body",
        created=datetime.datetime.now()
        )
    session.add(new_entry)
    session.commit()


@pytest.fixture
def fill_my_other_database(testapp):
    import faker
    FAKE = faker.Faker()
    SessionFactory = testapp.app.registry["dbsession_factory"]
    session = SessionFactory()
    allentries = []
    for i in range(20):
        allentries.append(
            MyModel(title=FAKE.text(20), markdown=FAKE.text(200))
        )
    session.add_all(allentries)
    session.commit()


@pytest.fixture
def dummy_request(testapp):
    """Instantiate a fake HTTP Request.
    complete with a database session.
    This is a function-level fixture, so every new request will have a
    new database session.
    """
    return testing.DummyRequest(dbsession=testapp)
