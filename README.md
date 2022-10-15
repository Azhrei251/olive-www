## To run locally ##
python manage.py runserver host:port

## To run via waitress (prod) ##
python listsite/server.py

## Run via docker ##
- run docker-build.sh
- either via docker compose or docker run start the server with port 8000 available and appropriate environment variables provided

## Environment variables ##
Locally via .env or normal environment vars. In the docker image only via environment variables.

- DEBUG: Django debug flag, True/False
- SECRET_KEY: Django secret key. To generate see https://saasitive.com/tutorial/generate-django-secret-key/
- DB_NAME: Your db name
- DB_USER: Your db user
- DB_PASSWORD: Your db password
- DB_HOST: Your db host
- DB_PORT: Your db port

## To generate migrations ##
- python manage.py makemigrations
- python manage.py migrate

## Initial setup ##
1. Perform database migrations
    - run python manage.py migrate
2. Create a superuser
    - via python manage.py createsuperuser --email $email --username $username
    - via python manage.py shell: User.objects.create_superuser(username='$username', password='$password', email='$email')
3. Crate an application via  http://host/admin/
    - Create an application. Should be public, Resource owner password-based.
    - Note the clientId/clientSecret
