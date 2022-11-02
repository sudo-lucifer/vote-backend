#!/bin/sh

cd /app 
exec gunicorn --bind '[::]:5000' -w 2 --threads 4 pastebin.wsgi:app
