FROM python:3

WORKDIR /home/mglps/Documents/DSCC/pro/dscc/monolit_cache_docker

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir 

COPY . .

# CMD [ "gunicorn",  "config.wsgi", " -b 0.0.0.0:8000" ]
# CMD [ "python",  "./manage.py", "runserver" ]
