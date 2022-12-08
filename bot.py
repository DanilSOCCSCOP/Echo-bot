import logging
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import settings

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.INFO,
                    filename = "bot.log"
                    )

def start_bot(updater: Updater, CallbackContext):
    bottext = f"Hello {updater.message.chat.first_name}!\n\nI'm EchoBot, write me something)" 
    logging.info(f"User {updater.message.chat.username} press start")
    updater.message.reply_text(bottext)

def chat(updater: Updater, CallbackContext):
	text = updater.message.text
	logging.info(text)

	updater.message.reply_text(text)

def main():
    updtr = Updater(settings.TOKEN_TELEGRAM)

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()

if __name__ == "__main__":
    logging.info("Bot started")
    main()