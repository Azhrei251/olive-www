![example workflow](https://github.com/azhrei251/olive-www/actions/workflows/docker-image.yml/badge.svg)

## To run locally ##
python manage.py runserver host:port

## To run via waitress (prod) ##
python listsite/server.py

## Run via docker ##
- run docker build --tag olive-www .
- either via docker compose or docker run start the server with port 8000 available and appropriate environment variables provided

## Environment variables ##
Locally via .env or normal environment vars. In the docker image only via environment variables.

- DEBUG: Django debug flag, True/False
- SECRET_KEY: Django secret key. To generate see https://saasitive.com/tutorial/generate-django-secret-key/
- ALLOWED_HOSTS: Comma delimited list of hosts
- DEFAULT_FROM_EMAIL: Email to use for contact for "from:" field
- EMAIL_HOST: Your SMTP Host
- EMAIL_HOST_USER: Your SMTP username
- EMAIL_HOST_PASSWORD: Your SMTP password
- EMAIL_PORT: Your SMTP port
- EMAIL_USE_TLS: Whether to us TLS or not
- DB_NAME: Your db name
- DB_USER: Your db user
- DB_PASSWORD: Your db password
- DB_HOST: Your db host
- DB_PORT: Your db port
- BASICAUTH_USERS: Comma delimited key:value pairs for users that are allowed to access basic auth resources

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
