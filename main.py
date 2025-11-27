from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
           self.path = '/index.html'
        elif self.path == "/main":
           self.path = '/main.html'
        elif self.path =='/data':
           self.path="/data.json"
        try:
           file_to_open = open(self.path[1:]).read()
           self.send_response(200)
        except:
           file_to_open = "File not found"
           self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
    

    

httpd = HTTPServer(('0.0.0.0',8080),Serv)
httpd.serve_forever()

# http://192.168.0.60:8080/data
