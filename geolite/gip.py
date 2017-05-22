# -*- coding: utf-8 -*-

import os

import geoip2.database

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

from geolite.log import Log
from geolite.debug import Debug


class Gip:
    
    reader = None
    db_path = ''
    res = None
    
    ###########################################################
    
    def __init__(self, 
                 db_path):
        
        self.db_path = db_path # database file
        
        try:               
            self.reader = geoip2.database.Reader(self.db_path)          
        except:
            Log.write(Debug.exception_info())
            
    ############################################################
    
    def get_info(self, ip):
        """ returns information for given ip """
        
        res = dict()
        resp = None
        
        if not self.reader:
            return None
         
        if not ip:
            return None
            
        try:
            resp = self.reader.city(ip)
        except:
            Log.write(Debug.exception_info())
            return None
        
        if not resp:
            return None
        
        res['continent'] = dict()
        res['continent']['id'] = resp.continent.geoname_id
        res['continent']['name'] = resp.continent.name
        res['continent']['code'] = resp.continent.code
        
        res['country'] = dict()
        res['country']['id'] = resp.country.geoname_id
        res['country']['name'] = resp.country.name
        res['country']['iso_code'] = resp.country.iso_code
           
        res['city'] = dict()
        res['city']['id'] = resp.city.geoname_id
        res['city']['name'] = resp.city.name
           
        res['location'] = dict()
        res['location']['lat'] = resp.location.latitude
        res['location']['lon'] = resp.location.longitude
        
        res['timezone'] = resp.location.time_zone
           
        self.res = res
        
        return self.res
                 
    ############################################################
    
            
        
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        