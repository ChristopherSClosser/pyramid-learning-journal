"""Views for learning journal."""
from pyramid.response import Response
import io 
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    """Display the list of entries."""
    res = os.open(os.path.join(HERE, 'data/index.html')).read()
    return Response(res)


def detail_view(request):
    """Display a detail view of entry."""
    res = os.open(os.path.join(HERE, 'data/detail.html')).read()
    return Response(res)
    pass


def create_view(request):
    """Display create a list entry."""
    pass


def update_view(request):
    """Display the update entry."""
    pass
