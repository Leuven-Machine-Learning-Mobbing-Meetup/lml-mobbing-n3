from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8001

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, World!')

httpd = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
print('Starting server at port: http://localhost:' + str(PORT))
httpd.serve_forever()