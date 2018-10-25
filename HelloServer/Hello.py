from http.server import HTTPServer, BaseHTTPRequestHandler

class HELLO(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
