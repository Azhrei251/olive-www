from waitress import serve

from web.wsgi import application

if __name__ == '__main__':
    print("Starting server")
    serve(application, port='8000', threads=16)
