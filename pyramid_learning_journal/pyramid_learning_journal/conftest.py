"""."""

from pyramid.config import Configurator
from pyramid.testing import DummyRequest
from pyramid_learning_journal.models.meta import Base
import pytest

import os


def main(global_config, **settings):
    settings["sqlalchemy.url"] = os.environ["TESTDB"]
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
    from WebTest import TestApp
    app = main({})

    SessionFactory = app.registry['dbsession_factory']
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)
    return TestApp(app)