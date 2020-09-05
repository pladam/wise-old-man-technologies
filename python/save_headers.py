from datetime import datetime
import json
import psycopg2
from urllib.parse import urlparse


class AddHeader:
    def __init__(self):
        self.num = 0

    def response(self, flow):
        
        conn = None
        try:
            conn = psycopg2.connect(" user=acd dbname=acd ")
        except:
            print ("I am unable to connect to the database")
        
        f = open("/home/acd/cdn/headers.log", "a")
        #print (flow.request.url, file=f)        
        headers = flow.response.headers 
        cdn = None
        for h in headers: 
            if h == 'x-cache':
                x_cache = headers[h];
            if h == 'x-served-by':
                x_served_by = headers[h];
        cur = conn.cursor()
        url = urlparse(flow.request.url)
        data = {'time':datetime.now().isoformat(), 'x_cache':x_cache, 'url':flow.request.url, 'netloc':url.netloc, 'x_served_by':x_served_by, 'size':str(len(flow.response.raw_content))} 
        
        #log to file 
        print(json.dumps(data), file=f)
        
        #insert to PG
        cur.execute("""INSERT INTO cdn(t,x_cache,url,netloc,x_served_by,size) VALUES (%(time)s, %(x_cache)s, %(url)s, %(netloc)s, %(x_served_by)s, %(size)s)""", data)
        conn.commit()
        
        

addons = [
    AddHeader()
]
