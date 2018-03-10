"""Define routes."""


def includeme(config):
    """App routes."""
    config.add_static_view(
        'static',
        'pyramid_learning_journal:static',
        cache_max_age=3600
    )
    config.add_route('home', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('new', '/journal/new-entry')
    config.add_route('edit', '/journal/{id:\d+}/edit-entry')
    config.add_route('delete', '/journal/{id:\d+}/delete-entry')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('api', '/api')
