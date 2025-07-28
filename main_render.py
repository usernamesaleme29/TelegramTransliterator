#!/usr/bin/env python3
"""
Main entry point for the Telegram transliteration bot.
Render-compatible version.
"""

import logging
import os
import sys
from threading import Thread
from bot_render import TelegramBot
from keep_alive import keep_alive

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Main function to start the bot."""
    try:
        logger.info("Starting Telegram transliteration bot...")
        
        # Start the keep-alive server in a separate thread
        keep_alive_thread = Thread(target=keep_alive, daemon=True)
        keep_alive_thread.start()
        logger.info("Keep-alive server started")
        
        # Initialize and start the bot
        bot = TelegramBot()
        bot.start()
        
    except Exception as e:
        logger.error(f"Critical error in main: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()