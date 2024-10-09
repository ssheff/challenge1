# adding module to support arguments passing 
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        response_content = '''
        <html>
        <head><title>Simple Web Server</title></head>
        <body>
        <h1>Welcome to my Python Web Server!</h1>
        <p>This server is listening on port {}.</p>
        <p>Server info:</p>
        <ul>
          <li>Client IP: {}</li>
          <li>Path requested: {}</li>
          <li>Server Address: {}:{}</li>
        </ul>
        </body>
        </html>
        '''.format(server.server_port, self.client_address[0], self.path, self.server.server_name, server.server_port)
        self.wfile.write(response_content.encode('utf-8'))

# Define a function to handle argument parsing 
# 	•	--host: Host to bind the server to. Default is 0.0.0.0, which allows the server to listen on all available interfaces.
#   •	--port: Port to bind the server to. Default is 8000.
def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple Python Web Server")
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind the server to')
    parser.add_argument('--port', type=int, default=8000, help='Port to bind the server to')
    return parser.parse_args()

# Main code
if __name__ == "__main__":
    args = parse_arguments()

    # Set up the HTTP server with user-specified host and port
    #   •	The server address is dynamically set based on the parsed --host and --port values.
    server_address = (args.host, args.port)
    server = HTTPServer(server_address, SimpleHandler)

    print(f"Starting server on {args.host}:{args.port}...")
    server.serve_forever()
