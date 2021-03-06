"""."""

from .default import (
    list_view,
    detail_view,
    create_view,
    update_view,
    delete_view,
    api_view,
)


def includeme(config):
    """List of views to include for the configurator object."""
    config.add_view(list_view, route_name='home')
    config.add_view(detail_view, route_name='detail')
    config.add_view(create_view, route_name='new')
    config.add_view(update_view, route_name='edit')
    config.add_view(delete_view, route_name='delete')
    config.add_view(api_view, route_name='api')
