"""
Telegram bot implementation for Latin-to-Cyrillic transliteration.
Compatible version for Render deployment.
"""

import logging
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes
from transliterator import Transliterator
from config import Config

logger = logging.getLogger(__name__)

class TelegramBot:
    """Main Telegram bot class - Render compatible version."""
    
    def __init__(self):
        """Initialize the bot with configuration."""
        self.config = Config()
        self.transliterator = Transliterator()
        self.application = None
        
    def setup_application(self):
        """Setup the Telegram application with handlers."""
        # Create application
        self.application = Application.builder().token(self.config.telegram_token).build()
        
        # Add handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        
        # Add error handler
        self.application.add_error_handler(self.error_handler)
        
        logger.info("Application setup complete")
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /start command."""
        welcome_message = (
            "🤖 Bienvenue dans le Bot de Translittération Latin-Cyrillique!\n\n"
            "Envoyez-moi du texte en caractères latins et je le convertirai en "
            "caractères cyrilliques visuellement similaires.\n\n"
            "Tapez /help pour plus d'informations."
        )
        await update.message.reply_text(welcome_message)
        logger.info(f"Start command from user {update.effective_user.id}")
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /help command."""
        help_message = (
            "📖 Aide - Bot de Translittération\n\n"
            "Ce bot convertit les caractères latins en caractères cyrilliques "
            "visuellement similaires.\n\n"
            "🔤 Exemples:\n"
            "• 'hello' → 'неӏӏо'\n"
            "• 'WORLD' → 'ШОГӀԂ'\n"
            "• 'Test123' → 'Теѕт123'\n\n"
            "✨ Fonctionnalités:\n"
            "• Respect de la casse (majuscules/minuscules)\n"
            "• Préservation des chiffres et caractères spéciaux\n"
            "• Réponse instantanée\n\n"
            "Envoyez simplement votre texte pour commencer!"
        )
        await update.message.reply_text(help_message)
        logger.info(f"Help command from user {update.effective_user.id}")
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming text messages."""
        try:
            user_id = update.effective_user.id
            input_text = update.message.text
            
            logger.info(f"Message from user {user_id}: {input_text[:50]}...")
            
            # Check if message is too long
            if len(input_text) > 4096:
                await update.message.reply_text(
                    "❌ Erreur: Le message est trop long (maximum 4096 caractères)."
                )
                return
            
            # Transliterate the text
            transliterated_text = self.transliterator.transliterate(input_text)
            
            # Send the result
            await update.message.reply_text(transliterated_text)
            
            logger.info(f"Transliteration completed for user {user_id}")
            
        except Exception as e:
            logger.error(f"Error handling message: {e}")
            await update.message.reply_text(
                "❌ Une erreur s'est produite lors du traitement de votre message. "
                "Veuillez réessayer."
            )
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors."""
        logger.error(f"Update {update} caused error {context.error}")
        
        if update and update.message:
            await update.message.reply_text(
                "❌ Une erreur inattendue s'est produite. "
                "Veuillez réessayer dans quelques instants."
            )
    
    def start(self):
        """Start the bot with enhanced error handling for Render."""
        try:
            self.setup_application()
            logger.info("Starting bot polling...")
            
            # Use a more compatible polling setup for Render
            self.application.run_polling(
                allowed_updates=Update.ALL_TYPES,
                drop_pending_updates=True,
                timeout=20,
                poll_interval=2.0
            )
        except Exception as e:
            logger.error(f"Error starting bot: {e}")
            raise