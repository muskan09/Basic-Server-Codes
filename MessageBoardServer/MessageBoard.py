#!/usr/bin/env python3
from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qs

form='''<!DOCTYPE html>
  <title>Message Board Server</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="MuskanMessage"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
</html>  
'''
class MESSAGE(BaseHTTPRequestHandler):
	def do_POST(self):
		length=int(self.headers.get('Content-length',0))
		data=self.rfile.read(length).decode()
		message=parse_qs(data)["MuskanMessage"][0]
		self.send_response(200)
		self.send_header('Content-type','text/plain;charset=utf-8')
		self.end_headers()
		self.wfile.write(message.encode())
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html;charset=utf-8')
		self.end_headers()
		self.wfile.write(form.encode())
		
		
if __name__=='__main__':
	server_address=('',8000)
	httpd=HTTPServer(server_address,MESSAGE)
	httpd.serve_forever()				
