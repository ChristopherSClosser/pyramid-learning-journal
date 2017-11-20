"""."""

import pytest
from pyramid import testing

from pyramid_learning_journal.models import (MyModel)
from pyramid_learning_journal.models.meta import Base


@pytest.fixture
def configuration(request):
    """Set up a Configurator instance.

    This instance sets up a pointer to the location of the
    database.
    It also includes the models from your app's model package.
    Finally it tears everything down, including the in-memory SQLite
    database.

    This configuration will persist for the duration of my PyTest run. 
    """
    config = testing.setUp(settings={
        'sqlalchemy.url':
        'postgres://postgres:1357@localhost:5432/pyramid_learning_journal'
        })
    config.include("pyramid_learning_journal.model")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


