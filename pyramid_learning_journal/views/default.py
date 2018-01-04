"""Views for learning journal."""

from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config
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
    if request.POST:
        entry = MyModel(
            title=request.POST["title"],
            created=datetime.datetime.now(),
            markdown=request.POST["markdown"]
        )
        request.dbsession.add(entry)
        return HTTPFound(request.route_url('home'))
    return {}


@view_config(route_name='edit', renderer='../templates/edit.jinja2')
def update_view(request):
    """Display the update entry."""
    ident = int(request.matchdict["id"])
    entry = request.dbsession.query(MyModel).get(ident)
    if not entry:
        raise HTTPNotFound
    if request.POST:
        entry.title = request.POST["title"]
        entry.markdown = request.POST["markdown"]
        request.dbsession.flush()
        return HTTPFound(request.route_url('home'))

    form_fill = {
        "title": entry.title,
        "markdown": entry.markdown
    }
    return {"entry": form_fill}
