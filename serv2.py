from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from unionB import union
from Private_APSP2 import ASPS

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index2.html"
        try:
            file_to_open = open(self.path[1:], "rb").read()
            self.send_response(200)
        except:
            file_to_open = b"File Not Found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(file_to_open)

    # make a post method that is getting a json of array of numbers and return it
    def do_POST(self):
        try:
            # get the data from the client
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data)
            if json_data['type'] == 'union':
                result = union(json_data, 16)
                json_result = json.dumps(result)
                # send it back
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json_result.encode())
            elif json_data['type'] == 'apsp':
                result = ASPS(json_data['content'])
                json_result = json.dumps(result)
                # send it back
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json_result.encode())
        except:
            file_to_open = b"File Not Found"
            self.send_response(404)
    
    

httpd = HTTPServer(("localhost", 8081), Serv)
httpd.serve_forever()