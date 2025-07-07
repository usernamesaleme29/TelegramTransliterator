"""
Keep-alive server to prevent the bot from sleeping on Replit.
"""

import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

logger = logging.getLogger(__name__)

class KeepAliveHandler(BaseHTTPRequestHandler):
    """HTTP handler for keep-alive requests."""
    
    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response_data = {
                'status': 'alive',
                'service': 'telegram-transliteration-bot',
                'timestamp': datetime.now().isoformat(),
                'message': 'Bot is running successfully'
            }
            
            self.wfile.write(json.dumps(response_data, indent=2).encode())
        
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            health_data = {
                'status': 'healthy',
                'uptime': 'running',
                'timestamp': datetime.now().isoformat()
            }
            
            self.wfile.write(json.dumps(health_data, indent=2).encode())
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')
    
    def log_message(self, format, *args):
        """Override to reduce logging noise."""
        # Only log important messages
        if '200' not in str(args):
            logger.info(f"Keep-alive server: {format % args}")

def keep_alive():
    """Start the keep-alive HTTP server."""
    try:
        server = HTTPServer(('0.0.0.0', 5000), KeepAliveHandler)
        logger.info("Keep-alive server started on port 5000")
        server.serve_forever()
    except Exception as e:
        logger.error(f"Error starting keep-alive server: {e}")
        raise
