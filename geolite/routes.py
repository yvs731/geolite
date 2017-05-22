
import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

from geolite.views import index
from geolite.views import variable_handler

################################################

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/{name}/', variable_handler)