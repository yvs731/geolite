
from aiohttp import web
from routes import setup_routes

app = web.Application()

setup_routes(app)

web.run_app(app, host='185.86.79.214', port=80)
