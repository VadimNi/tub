cd ask &&
gunicorn --log-file error.log --access-logfile acc.log --log-level debug -b 0.0.0.0:8000  -D ask.wsgi
