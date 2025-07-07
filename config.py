"""
Configuration management for the Telegram bot.
"""

import os
import logging

logger = logging.getLogger(__name__)

class Config:
    """Configuration class for the bot."""
    
    def __init__(self):
        """Initialize configuration from environment variables."""
        self.telegram_token = self._get_telegram_token()
        self.log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        self.max_message_length = int(os.getenv('MAX_MESSAGE_LENGTH', '4096'))
        
        # Validate configuration
        self._validate_config()
        
        logger.info("Configuration loaded successfully")
    
    def _get_telegram_token(self) -> str:
        """Get Telegram bot token from environment variables."""
        # Try different possible environment variable names
        token_vars = ['TELEGRAM_TOKEN', 'BOT_TOKEN', 'TOKEN']
        
        for var in token_vars:
            token = os.getenv(var)
            if token:
                logger.info(f"Found Telegram token in {var}")
                return token
        
        # If no token found, raise an error
        raise ValueError(
            "No Telegram bot token found! Please set one of the following environment variables: "
            f"{', '.join(token_vars)}"
        )
    
    def _validate_config(self):
        """Validate the configuration."""
        if not self.telegram_token:
            raise ValueError("Telegram token is required")
        
        if not self.telegram_token.startswith(('bot', 'BOT')):
            # Add 'bot' prefix if not present (some tokens require this)
            logger.warning("Token doesn't start with 'bot', but proceeding...")
        
        if self.max_message_length <= 0:
            raise ValueError("Max message length must be positive")
        
        # Validate log level
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if self.log_level not in valid_levels:
            logger.warning(f"Invalid log level {self.log_level}, using INFO")
            self.log_level = 'INFO'
        
        logger.info(f"Configuration validated - Max message length: {self.max_message_length}")
    
    def get_config_summary(self) -> dict:
        """Get a summary of the configuration (without sensitive data)."""
        return {
            'token_set': bool(self.telegram_token),
            'token_length': len(self.telegram_token) if self.telegram_token else 0,
            'log_level': self.log_level,
            'max_message_length': self.max_message_length
        }
