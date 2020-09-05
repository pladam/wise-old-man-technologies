#!/usr/bin/env python3

import json
import pprint
import sys
from urllib.parse import urlparse

from haralyzer import HarParser, HarPage

pp = pprint.PrettyPrinter(indent=4)

with open('/home/acd/cdn/logs/har_20_06_25_23_55_1593129351.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

print ("hello")

hosts = {}
size = {}

for page in har_parser.pages:
    assert isinstance(page, HarPage)
    for entry in page.entries:
        cdn = []
        headers = entry['response']['headers']
        #print(entry['response'], file=sys.stderr)
        cdn_str = None
        for h in headers: 
            if( h['name'] == 'x-cache'):
                url = urlparse(entry['request']['url'])
                hosts[url.netloc] = 1
                #print(url, file=sys.stderr)
                cdn_str = h['value']
                cdn.append(cdn_str)
        if( cdn_str in size ):
            size[cdn_str] = size[cdn_str] + entry['response']['content']['size']
        else:
            size[cdn_str] = entry['response']['content']['size']
        
        print (cdn, "\t", entry['response']['content']['size'], "\t", entry['request']['url']) 

print (hosts)
print (size)

total = 0
for s in size.keys():
    total = total + size[s]
    
print (total)

for s in size.keys():
    print (s, size[s]/ total)