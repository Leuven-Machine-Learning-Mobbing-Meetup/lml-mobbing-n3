from http.server import HTTPServer, BaseHTTPRequestHandler
import json

PORT = 8001
msg = {'msg':'Hello!'}
json_string = json.dumps(msg)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json_string.encode(encoding='utf_8'))

httpd = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
print('Starting server at port: http://localhost:' + str(PORT))
httpd.serve_forever()