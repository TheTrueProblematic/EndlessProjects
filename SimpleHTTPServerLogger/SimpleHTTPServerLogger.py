
# Importing the necessary libraries
# The http.server module in Python provides HTTP servers for script-based web servers
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# Here comes our custom HTTP request handler, it extends BaseHTTPRequestHandler
class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    # Almost there! This function handles any GET request.
    # It logs the request then sends a 200 OK back to the caller
    def do_GET(self):
        logging.info(f"GET request,\nPath: {str(self.path)}\nHeaders: {str(self.headers)}")
        self.send_response(200)

# Here is where the orchestra starts to come together - this function sets up and starts the server
def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler):
    # Configure server address and port. Here, we are running localhost on port 8000
    server_address = ('', 8000)

    # Logging configuration - Print out logs to the console
    logging.basicConfig(level=logging.INFO)
    
    # Instantiate the server, and bind it to the server address
    httpd = server_class(server_address, handler_class)
    logging.info(f"Starting httpd...\n")
    
    # Try to run the server, unless keyboard interrupt happens
    try:
        httpd.serve_forever() # Party until the lights go out!
    except KeyboardInterrupt: # Except when the party gets crashed
        pass
    httpd.server_close() # Time to clean up! Close the server.
    logging.info('Stopping httpd...\n') # Let all know party is officially over.

# A python script isn't a proper script unless it checks if it's running standalone
if __name__ == '__main__':
    run() # If so, let's get this party started!

