# simple_server.py
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver

PORT = 8000
Handler = SimpleHTTPRequestHandler

print(f"Starting server on http://localhost:{PORT}")
print("Serving files from the current directory...")

# Create the server instance
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # Keep the server running until you press Ctrl+C
    httpd.serve_forever()
