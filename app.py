"""."""

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import io
# from views.default import list_view
HERE = os.path.dirname(__file__)


def hello_world(request):

    res = io.open(os.path.join(HERE, 'pyramid_learning_journal/templates/home.html')).read()
    # io.close()
    return Response(res)


if __name__ == '__main__':
    config = Configurator()
    config.add_route('home', '/')
    config.add_view(hello_world, route_name='home')
    app = config.make_wsgi_app()
    server = make_server('localhost', 6543, app)
    server.serve_forever()
