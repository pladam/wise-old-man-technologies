#!/bin/bash
#pip3 install mitmproxy 
#pip3 install psycopg2 

DATE="`date +%y`_`date +%m`_`date +%d`_`date +%H`_`date +%M`_`date +%s`.har"
filename=har_$DATE
path=/home/acd/cdn/logs/$filename
mitmdump -s "/home/acd/cdn/python/har_extractor.py" --set hardump=$path > /dev/null 2>&1 &
#mitmproxy -s "/home/acd/cdn/python/har_extractor.py" --set hardump=$path

