from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from unionA import union
from Private_APSP1 import ASPS
import networkx as nx


class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index1.html"
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
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data)
            if json_data["type"] == "union":
                result = union(json_data["content"], 16)
                json_result = json.dumps(result)
                # send it back
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json_result.encode())
            elif json_data["type"] == "apsp":
                print("json_data:", json_data)
                graph = nx.Graph()
                for edge in json_data["content"]:
                    graph.add_edge(int(edge["fromId"]), int(edge["toId"]), weight=int(edge["label"]))
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok"}).encode())
                # print("graph:", graph)
                # result = ASPS(graph)
                # print("result:", result)
                # json_result = json.dumps(result)
                # # send it back
                # self.send_response(200)
                # self.send_header("Content-type", "application/json")
                # self.end_headers()
                # self.wfile.write(json_result.encode())
        except Exception as e:
            file_to_open = b"File Not Found"
            print("error:", e)
            self.send_response(404)


httpd = HTTPServer(("localhost", 8080), Serv)
httpd.serve_forever()
