from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.add_route('foos_index', '/foos')
    config.add_route('foos_create', '/foos/create') # TODO POST /foos
    config.add_route('foos_new', '/foos/new')
    config.add_route('foos_show', '/foos/{id}')
    config.add_route('foos_edit', '/foos/{id}/edit')
    config.add_route('foos_update', '/foos/{id}/update') # TODO PUT/PATCH /foos/{id}
    config.add_route('foos_destroy', '/foos/{id}/destroy') # TODO DELETE /foos/{id}
    config.scan()
    return config.make_wsgi_app()
