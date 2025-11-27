# Source - https://stackoverflow.com/a
# Posted by Johnny Abou Haidar, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-27, License - CC BY-SA 4.0

from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
           self.path = '/index.html'
        elif self.path == "/main":
           self.path = '/main.html'
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
