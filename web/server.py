from waitress import serve

from listsite.wsgi import application

if __name__ == '__main__':
    print("Starting server")
    serve(application, port='8000')
