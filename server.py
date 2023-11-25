from http.server import BaseHTTPRequestHandler, HTTPServer

import handler


class Server:
    def __init__(self, ip='', port=8000):
        self.ip = ip
        self.port = port

    def __run(self, ip, port, server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
        server_address = (ip, port)
        self.httpd = server_class(server_address, handler_class)
        self.httpd.serve_forever()

    def start_server(self):
        self.__run(self.ip, self.port, handler_class=handler.HttpGetHandler)

    def close_server(self):
        self.httpd.server_close()
