from http.server import HTTPServer, BaseHTTPRequestHandler
class ECHO(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/plain; charset=utf-8')
		self.wfile.write(self.path[1:].encode())
		
if __name__=='__main__':
	server_address = ('', 8000)
	httpd = HTTPServer(server_address,ECHO)
	httpd.serve_forever()
 #open localhost:8000/anyword
