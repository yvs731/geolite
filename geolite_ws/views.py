
import os
import json
import re

from aiohttp import web

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

from gip import Gip

# must be in config file
db_path = '/root/data/maxmind/GeoLite2-City.mmdb'


async def index(request):
    
    resp_txt = ''

    query = request.query
    
    if not 'ip' in query:
        return web.Response(text='')
    

    ip = query['ip']
    
    rx = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    
    if len(re.findall(rx, ip)) == 0:
        return web.Response(text='wrong ip')
    
    gp = Gip(db_path)
    
    ip_info = gp.get_info(ip)
    
    if ip_info:
        resp_txt = json.dumps(ip_info, indent=4, sort_keys=True)


    return web.Response(text=resp_txt)

