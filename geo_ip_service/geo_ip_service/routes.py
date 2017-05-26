
import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

from geo_ip_service.views import index

################################################

def setup_routes(app):
    app.router.add_get('/', index)
