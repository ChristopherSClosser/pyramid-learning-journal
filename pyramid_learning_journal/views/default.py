"""Views for learning journal."""
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.response import Response
from pyramid.view import view_config
from ..data.entries import ENTRIES
from ..models import MyModel
import datetime
import os

HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='../templates/home.jinja2')
def list_view(request):
    """Display the list of entries."""
    query = request.dbsession.query(MyModel)
    entries = query.order_by(MyModel.created.desc()).all()
    return {'entries': entries}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Display a detail view of entry."""
    ident = int(request.matchdict['id'])
    entry = request.dbsession.query(MyModel).get(ident)
    if not entry:
        raise HTTPNotFound
    return {"entry": entry}


@view_config(route_name='new', renderer='../templates/entry.jinja2')
def create_view(request):
    """Display create a list entry."""
    return {}


@view_config(route_name='edit', renderer='../templates/edit.jinja2')
def update_view(request):
    """Display the update entry."""
    ident = int(request.matchdict['id'])
    entry = request.dbsession.query(MyModel).get(ident)
    if not entry:
        raise HTTPNotFound
    return {"entry": entry}
