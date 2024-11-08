from http.server import BaseHTTPRequestHandler, HTTPServer

class LoggingHandler(BaseHTTPRequestHandler):
    def _log_request(self):
        # Get the request body length and read the body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else "(No Body)"
        
        # Explicitly print each component to stdout
        print("Method:", self.command)
        print("Path:", self.path)
        print("Headers:", self.headers)
        print("Body:", body)
        print("=" * 50)

    def do_GET(self):
        self._log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"200 OK - GET request received")

    def do_POST(self):
        self._log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"200 OK - POST request received")

    def do_PUT(self):
        self._log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"200 OK - PUT request received")

    def do_DELETE(self):
        self._log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"200 OK - DELETE request received")

if __name__ == "__main__":
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, LoggingHandler)
    print("Starting server on port 8080...")
    httpd.serve_forever()