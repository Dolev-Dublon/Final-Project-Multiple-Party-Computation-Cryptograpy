from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from unionA import unionA
from Private_APSP1 import ASPS1
import networkx as nx
from connections import Init_connection

server_socket = Init_connection()


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
                result = unionA(
                    json_data["content"], 32, server_socket=server_socket
                )  #
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
                    graph.add_edge(
                        int(edge["fromId"]),
                        int(edge["toId"]),
                        weight=int(edge["label"]),
                    )
                print("graph:", graph)
                result = ASPS1(graph, server_socket_dont_touch=server_socket)
                print("result:", result)
                edges_fromId_toId_label = []
                for u, v, data in result.edges(data=True):
                    print("u:", u, "v:", v, "data:", data)
                    edges_fromId_toId_label.append(
                        {"fromId": u, "toId": v, "label": data["weight"]}
                    )
                    
                result = edges_fromId_toId_label
                print("result:", result)
                json_result = json.dumps(result)
                # send it back
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json_result.encode())
        except Exception as e:
            file_to_open = b"File Not Found"
            print("error:", e)
            self.send_response(404)


print("http://localhost:8080")
httpd = HTTPServer(("localhost", 8080), Serv)
httpd.serve_forever()
