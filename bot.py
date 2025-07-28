import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes
from transliterator import Transliterator
from config import Config

# Configuration du logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self):
        self.config = Config()
        self.transliterator = Transliterator()
        self.application = None

    def setup_application(self):
        self.application = Application.builder().token(self.config.telegram_token).build()
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_error_handler(self.error_handler)
        logger.info("Application setup complete")

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        welcome_message = (
            f"👋 Salut {user.first_name or 'utilisateur'} !\n\n"
            "🤖 Ce bot est destiné à ceux qui n’arrivent pas à choisir un nom sur Facebook.\n"
            "Il génère des noms visuellement similaires à l'alphabet latin.\n\n"
            "⚠️ Vous êtes **seul responsable** de l'utilisation que vous ferez de ce bot.\n"
            "L'auteur décline toute responsabilité en cas d'abus.\n\n"
            "Envoyez un texte pour voir sa version stylisée.\n"
            "Tapez /help pour plus d’infos."
        )
        await update.message.reply_text(welcome_message)
        logger.info(f"[START] UserID={user.id} | FullName={user.full_name} | Username=@{user.username}")

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_message = (
            "📖 Aide - Bot de Translittération\n\n"
            "Ce bot convertit les caractères latins en caractères cyrilliques visuellement similaires.\n\n"
            "🔤 Exemples:\n"
            "• 'hello' → 'неӏӏо'\n"
            "• 'WORLD' → 'ШОГӀԂ'\n"
            "• 'Test123' → 'Теѕт123'\n\n"
            "✨ Fonctionnalités:\n"
            "• Respect de la casse\n"
            "• Préservation des chiffres et caractères spéciaux\n"
            "• Réponse instantanée\n\n"
            "Envoyez simplement votre texte pour commencer!"
        )
        await update.message.reply_text(help_message)
        logger.info(f"[HELP] UserID={update.effective_user.id}")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user = update.effective_user
            user_id = user.id
            user_name = user.full_name
            username = user.username or "N/A"
            input_text = update.message.text.strip()

            logger.info(f"[MSG] From: {user_name} (ID: {user_id}, @{username}) | Message: {input_text}")

            if len(input_text) > 4096:
                await update.message.reply_text("❌ Le message est trop long (4096 caractères max).")
                logger.warning(f"[LONG_MSG] User {user_id} | Message ignoré")
                return

            transliterated_text = self.transliterator.transliterate(input_text)
            await update.message.reply_text(transliterated_text)
            logger.info(f"[RESULT] User {user_id} | Output: {transliterated_text[:50]}...")
        except Exception as e:
            logger.error(f"[ERROR] handle_message | {e}")
            await update.message.reply_text("❌ Une erreur s'est produite. Réessayez.")

    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.error(f"Update {update} caused error {context.error}")
        if update and update.message:
            await update.message.reply_text("❌ Une erreur inattendue s'est produite. Réessayez.")

    def start(self):
        try:
            self.setup_application()
            logger.info("Bot ready and listening for updates!")
            self.application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
        except Exception as e:
            logger.error(f"Error starting bot: {e}")
            raise

if __name__ == "__main__":
    bot = TelegramBot()
    bot.start()
