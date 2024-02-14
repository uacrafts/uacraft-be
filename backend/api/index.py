import os
from django.core.wsgi import get_wsgi_application
from http.server import BaseHTTPRequestHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()

app = application

#class handler(BaseHTTPRequestHandler):
#
#    def do_GET(self):
#        self.send_response(200)
#        self.send_header('Content-type', 'text/plain')
#        self.end_headers()
#        self.wfile.write('Hello, world!'.encode('utf-8'))
#        return