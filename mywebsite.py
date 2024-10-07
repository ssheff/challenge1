# Import classes
from http.server import HTTPServer, BaseHTTPRequestHandler

#	1.	SimpleHandler class:
#	•	Inherits from BaseHTTPRequestHandler.
#	•	Handles the GET requests using the do_GET method.
#	•	It constructs a basic HTML page showing:
#	•	Client’s IP address.
#	•	Path requested.
#	•	Server’s address.
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Define the response to the GET request
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Define the content to send as response
        response_content = '''
        <html>
        <head><title>Python Web Server</title></head>
        <body>
        <h1>Welcome to my Web Server!</h1>
        <p>This server is listening on port 8000.</p>
        <p>Server info:</p>
        <ul>
          <li>Client IP: {}</li>
          <li>Path requested: {}</li>
          <li>Server Address: {}</li>
        </ul>
        </body>
        </html>
        '''.format(self.client_address[0], self.path, self.server.server_address)

        # Write the response content to the HTTP response
        self.wfile.write(response_content.encode('utf-8'))

#	2.	Server setup:
#	•	The server listens on port 8000.
#	•	It uses HTTPServer, passing the address and handler.
server_address = ('', 8000)  # '' means listening on all available interfaces
httpd = HTTPServer(server_address, SimpleHandler)

# Starting the server:
#	•	The serve_forever() method ensures that the server listens indefinitely.
print("Starting server on port 8000...")
httpd.serve_forever()