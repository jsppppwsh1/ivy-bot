from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Ivy is alive")


def run():
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    server.serve_forever()


def keep_alive():
    thread = Thread(target=run)
    thread.start()
