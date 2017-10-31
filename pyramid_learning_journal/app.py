"""."""

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
      '''
      Model
      View
      Layer
      '''
      return Response('Hello World!<br>I guess this works...')


if __name__ == '__main__':
      config = Configurator()
      config.add_route('home', '/')
      config.add_view(list_view, route_name='home')
      app = config.make_wsgi_app()
      server = make_server('localhost', 6543, app)
      server.serve_forever()