#!/bin/bash

while IFS="" read -r p || [ -n "$p" ]
do
  DATE="`date +%y`_`date +%m`_`date +%d`_`date +%H`_`date +%M`_`date +%s`.har"
  filename=har_$DATE
  site="`basename $p`"
  site=${site//.com/}
  site=${site//www.}
  filename="${site}_${DATE}"
  path=/home/acd/cdn/logs/$filename
  mitmdump -s "/home/acd/cdn/python/har_extractor.py" --set hardump=$path > /dev/null 2>&1 &
  sleep 1
  export set https_proxy=localhost:8080
  export set http_proxy=localhost:8080
  google-chrome $p --headless --disable-gpu --dump-dom --aggressive-cache-discard
  kill $(lsof -t -i:8080)
done <"/home/acd/cdn/metadata/urls.txt"
