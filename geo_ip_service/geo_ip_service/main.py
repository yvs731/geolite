
import os
import argparse
from logging import warning

from aiohttp import web

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

from geo_ip_service.routes import setup_routes

parser = argparse.ArgumentParser()

parser.add_argument("--action", action='store', type=str)
parser.add_argument("--host", action='store', type=str)
parser.add_argument("--port", action='store', type=str)
parser.add_argument("--dbpath", action='store', type=str)


args = parser.parse_args()

if args.action:
    if args.action == 'start':

        if args.host:
            print('host == ', args.host)
            host = args.host
        else:
            host = '185.86.79.214' # default value
            
        if args.port:
            print('port == ', args.port)
            port = args.port
        else:
            port = '80' # default value
            
        if args.dbpath:            
            print('dbpath == ', args.dbpath)
             
            app = web.Application()
        
            setup_routes(app)
            
            port = int(port)
        
            web.run_app(app,
                        host=host, 
                        port=port)
        else:
            warning('dbpath argument is required.')
            warning('usage: --dbpath {path}')
    
warn('action is not defined (use --action start')    
    
    
    
    
    
    
    
    