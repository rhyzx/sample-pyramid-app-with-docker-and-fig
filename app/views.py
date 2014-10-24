from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    Foo,
    )


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'app'}




conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_app_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

class FoosView: # TODO FoosController
    def __init__(self, request):
        self.request = request

    @view_config(route_name='foos_index', renderer='templates/foos/index.pt')
    def index(self):
        return {'foos': DBSession.query(Foo).all()}
    
    @view_config(route_name='foos_new', renderer='templates/foos/new.pt')
    def new(self):
        return {}
    
    @view_config(route_name='foos_show', renderer='templates/foos/show.pt')
    def show(self):
        id = self.request.matchdict.get('id')
        # TODO 404 not found
        foo = DBSession.query(Foo).filter(Foo.id==id).first()
        return {'foo': foo}
    
    @view_config(route_name='foos_edit', renderer='templates/foos/edit.pt')
    def edit(self):
        id = self.request.matchdict.get('id')
        foo = DBSession.query(Foo).filter(Foo.id==id).first()
        return {'foo': foo}
    
    @view_config(route_name='foos_create', request_method='POST')
    def create(self):
        dict = self.request.POST
        foo = Foo(name=dict.get('name'), body=dict.get('body'))
        DBSession.add(foo)
        DBSession.flush()
        return HTTPFound(location='/foos/%d' % foo.id)

    @view_config(route_name='foos_update', request_method='POST')
    def update(self):
        id = self.request.matchdict.get('id')
        dict = self.request.POST
        foo = DBSession.query(Foo).filter(Foo.id==id).first()
        foo.name = dict.get('name')
        foo.body = dict.get('body')
        DBSession.add(foo)
        DBSession.flush()
        return HTTPFound(location='/foos/%d' % foo.id)

    @view_config(route_name='foos_destroy', request_method='POST')
    def destroy(self):
        id = self.request.matchdict.get('id')
        DBSession.query(Foo).filter(Foo.id==id).delete()
        return HTTPFound(location='/foos')




