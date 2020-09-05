export set https_proxy=localhost:8080
export set http_proxy=localhost:8080

cat "/home/acd/cdn/metadata/urls.txt" | xargs -n 1 google-chrome --headless --disable-gpu --dump-dom --aggressive-cache-discard
kill $(lsof -t -i:8080)