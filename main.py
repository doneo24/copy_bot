import os
from telegram.ext import Updater, CommandHandler
from llama_index import GPTVectorStoreIndex

from llama_index import StorageContext, load_index_from_storage
storage_context = StorageContext.from_defaults(persist_dir="./")
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Doneo CopyBot ist bereit. Verwende /frage <dein Thema>")

def frage(update, context):
    prompt = " ".join(context.args)
    if not prompt:
        update.message.reply_text("Bitte gib deine Frage nach dem Befehl /frage ein.")
        return
    response = query_engine.query(prompt)
    update.message.reply_text(response.response)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("frage", frage))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()