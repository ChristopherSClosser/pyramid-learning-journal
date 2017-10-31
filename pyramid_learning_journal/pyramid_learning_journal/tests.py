import unittest
import transaction

from pyramid import testing
from pyramid_learning_journal.views.default import (
    list_view,
    detail_view,
    update_view,
    create_view
)

# def test_list_view_returns_200():
