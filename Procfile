web: gunicorn tech_investement.wsgi
worker: celery -A tech_investement worker --loglevel=info
beat: celery -A tech_investement beat --loglevel=info
