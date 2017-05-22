
import os
import argparse

from aiohttp import web

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

from geolite.routes import setup_routes

parser = argparse.ArgumentParser()

parser.add_argument("--ip", action='store', type=str)
parser.add_argument("--dbpath", action='store', type=str)

args = parser.parse_args()

if args.ip:
    print('ip == ', args.ip)
    ip = args.ip
else:
    ip = '185.86.79.214' # default value
    
if args.dbpath:
    
    print('dbpath == ', args.dbpath)
     
    app = web.Application()

    setup_routes(app)

    web.run_app(app,
                host=ip, 
                port=80)
    
else:
    print('dbpath argument required. usage: --dbpath {path}')
    
    
    
    
    
    
    
    
    
    