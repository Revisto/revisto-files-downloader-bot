from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import setting

def video_downloader(update, context):
    file_name = update.message.audio.file_name
    file = context.bot.getFile(update.message.audio.file_id)
    file.download(setting.save_location + file_name)
    update.message.reply_text("Done, bro")

def main():
    updater = Updater(setting.telegram_access_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.video, video_downloader))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
