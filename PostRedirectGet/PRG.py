from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qs

memory=[]

form='''<!DOCTYPE html>
  <title>Post Redirect Get</title>
  <form method="POST">
    <textarea name="mkIsTheBest"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class messagehandler(BaseHTTPRequestHandler):
	def do_POST(self):
		l=int(self.headers.get('Content-length',0))
		d=self.rfile.read(l).decode()
		message=parse_qs(d)["mkIsTheBest"][0]
		message=message.replace("<","&lt")
		memory.append(message)
		self.send_response(303)
		self.send_header('Location','/')
		self.end_headers()
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html;charset=utf-8')
		self.end_headers()
		message1=form.format("\n".join(memory))
		self.wfile.write(message1.encode())
		
		
if __name__=='__main__':
	server_address=('',8000)
	httpd=HTTPServer(server_address,messagehandler)
	httpd.serve_forever()				
