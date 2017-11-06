"""Views for learning journal."""
from pyramid.response import Response
from pyramid.view import view_config
from entries import ENTRIES
import io
import os
from entries import ENTRIES
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

HERE = os.path.dirname(__file__)



@view_config(route_name='home', renderer='../templates/home.jinja2')

def list_view(request):
    """Display the list of entries."""
    return {'entries': ENTRIES}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Display a detail view of entry."""
    ident = int(request.matchdict['id'])
    for entry in ENTRIES:
        if entry['id'] == ident:
            return {'entry': entry}


@view_config(route_name='new', renderer='../templates/entry.jinja2')
def create_view(request):
    """Display create a list entry."""

    return {}


def update_view(request):
    """Display the update entry."""
    return {}
