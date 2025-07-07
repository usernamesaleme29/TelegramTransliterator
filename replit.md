# Telegram Latin-to-Cyrillic Transliteration Bot

## Overview

This is a Telegram bot that automatically converts Latin characters to visually similar Cyrillic characters. The bot is designed to run continuously on Replit and provides real-time transliteration services through Telegram's messaging platform.

## System Architecture

The application follows a modular architecture with clear separation of concerns:

- **Bot Layer**: Handles Telegram API interactions and message processing
- **Transliteration Engine**: Core logic for character conversion
- **Configuration Management**: Centralized configuration handling
- **Keep-Alive Service**: HTTP server to prevent hosting platform sleep
- **Logging System**: Comprehensive logging for monitoring and debugging

## Key Components

### 1. Main Application (`main.py`)
- Entry point that orchestrates the entire system
- Initializes logging configuration
- Starts the keep-alive server in a separate thread
- Launches the Telegram bot

### 2. Telegram Bot (`bot.py`)
- Handles Telegram API integration using python-telegram-bot library
- Manages command handlers (`/start`, `/help`)
- Processes text messages for transliteration
- Implements error handling and user feedback

### 3. Transliteration Engine (`transliterator.py`)
- Core transliteration logic with visual character mapping
- Maintains a comprehensive Latin-to-Cyrillic character table
- Preserves case sensitivity and non-alphabetic characters
- Handles both lowercase and uppercase character conversion

### 4. Configuration Management (`config.py`)
- Centralized configuration from environment variables
- Validates required settings (Telegram token)
- Provides default values for optional settings
- Supports multiple token environment variable names

### 5. Keep-Alive Service (`keep_alive.py`)
- HTTP server providing health check endpoints
- Prevents the application from sleeping on hosting platforms
- Offers `/` and `/health` endpoints for monitoring
- Returns JSON responses with status information

## Data Flow

1. **User Input**: User sends a message to the Telegram bot
2. **Message Processing**: Bot receives the message through webhook/polling
3. **Transliteration**: Text is processed through the transliteration engine
4. **Character Mapping**: Each Latin character is mapped to its Cyrillic equivalent
5. **Response**: Converted text is sent back to the user via Telegram

## External Dependencies

### Required Libraries
- `python-telegram-bot`: Telegram Bot API wrapper
- `logging`: Built-in Python logging (standard library)
- `http.server`: HTTP server for keep-alive functionality (standard library)
- `threading`: Multi-threading support (standard library)

### External Services
- **Telegram Bot API**: Core messaging functionality
- **Hosting Platform**: Designed for Replit deployment
- **Environment Variables**: Configuration through platform secrets

## Deployment Strategy

### Environment Variables
- `TELEGRAM_TOKEN`: Bot token from @BotFather (required)
- `LOG_LEVEL`: Logging verbosity (optional, default: INFO)
- `MAX_MESSAGE_LENGTH`: Maximum message length (optional, default: 4096)

### Deployment Steps
1. Clone repository to Replit
2. Set `TELEGRAM_TOKEN` in Replit Secrets
3. Run `python main.py` to start the bot
4. Keep-alive server automatically starts on port 8080

### Monitoring
- Log files generated (`bot.log`)
- Health check endpoints available
- Real-time logging to stdout

## Changelog

- July 07, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.