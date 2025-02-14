import logging
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


async def start(update: Update, context):
    logger.info(f"Пользователь {update.effective_user.id} запустил бота")
    await update.message.reply_text("Привет! Я простой бот.")


async def echo(update: Update, context):
    logger.info(
        f"Пользователь {update.effective_user.id} отправил сообщение: {update.message.text}"
    )
    await update.message.reply_text(update.message.text)


def main():
    logger.info("Запуск бота...")
    token = os.getenv("BOT_TOKEN")
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()


if __name__ == "__main__":
    main()
