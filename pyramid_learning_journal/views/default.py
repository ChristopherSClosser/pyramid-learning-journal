"""Views for learning journal."""

from pyramid.security import remember, forget, NO_PERMISSION_REQUIRED
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config, forbidden_view_config
from pyramid_learning_journal.security import is_authenticated
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


@view_config(
    route_name='new',
    renderer='../templates/entry.jinja2',
    permission='secret',
)
# @forbidden_view_config(renderer='../templates/nonentry.jinja2')
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


@view_config(
    route_name='edit',
    renderer='../templates/edit.jinja2',
    permission='secret',
)
# @forbidden_view_config(renderer='../templates/nonedit.jinja2')
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


@view_config(route_name='login', renderer='../templates/login.jinja2')
@forbidden_view_config(renderer='../templates/nonentry.jinja2')
def login(request):
    """."""
    if request.method == 'GET':
        return {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if is_authenticated(username, password):
            headers = remember(request, username)
            return HTTPFound(request.route_url('home'), headers=headers)
        return {}


@view_config(route_name='logout')
def logout(request):
    """."""
    headers = forget(request)
    return HTTPFound(request.route_url('home'), headers=headers)
