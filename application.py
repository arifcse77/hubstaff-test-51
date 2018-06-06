""" Run server using Gevent """
from app import create_app
from gevent.wsgi import WSGIServer
from instance.config import CREDENTIALS

app = create_app(CREDENTIALS)

if __name__ == '__main__':
    host = "0.0.0.0"
    port = 5000

    if CREDENTIALS['ENV'] == "development":
        app.run(host=host, port=port, debug=True)
    else:
        http_server = WSGIServer((host, port), app)
        http_server.serve_forever()

