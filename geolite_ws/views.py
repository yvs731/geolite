
import os
import json
import re

from aiohttp import web

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)


from gip import Gip
from log import Log

# must be in config file
db_path = '/root/data/maxmind/GeoLite2-City.mmdb'

################################################

async def variable_handler(request):
    return web.Response(
        text="Hello, {}".format(request.match_info['ips']))
    
################################################

async def index(request):
    """ processes request and 
        output ip info in json format """
    
    resp_txt = ''

    query = request.query 
    
    if not 'ip' in query:
        return web.Response(text='')
    

    ip = query['ip']
    
    rx = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' 
    if len(re.findall(rx, ip)) == 0:
        msg = 'wrong ip'
        Log.write(msg)
        return web.Response(text=msg)
    
    gp = Gip(db_path)
    
    ip_info = gp.get_info(ip)
          
    if ip_info:
        
        if len(list(query.keys())) > 1: # if one need only part 
                                        # of the ip info
            d = dict()
            for key in query:
                if key == 'ip':
                    continue
                if not key in ip_info:
                    continue
                d[key] = ip_info[key]
            
            resp_txt = json.dumps(d, 
                                  indent=4, 
                                  sort_keys=True)
            
        else:                            
            resp_txt = json.dumps(ip_info, 
                                  indent=4, 
                                  sort_keys=True)


    return web.Response(text=resp_txt)

