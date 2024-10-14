import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, CallbackContext
from io import BytesIO
from config import TG_token as tg_token
from tiktok import download_tiktok_video
from insta import format_instagram_url, dowload_reels

# Предполагаем, что эти функции уже определены и работают корректно:
# - identify_platform(url): определяет, TikTok или Instagram Reels.
# - download_tiktok_video(url): скачивает видео с TikTok и возвращает байты.
# - format_instagram_url(url): форматирует URL Instagram для скачивания.
def identify_platform(url):
    if "instagram.com/reel/" in url:
        return "Instagram Reels"
    elif "tiktok.com" in url:
        return "TikTok"
    else:
        return "Unknown platform"
async def handle_message(update: Update, context: CallbackContext):
    url = update.message.text
    platform = identify_platform(url)
    chat_id = update.message.chat_id

    if platform == "Instagram Reels":
        formatted_url = format_instagram_url(url)
        if formatted_url:
            video_data = dowload_reels(formatted_url)
            if video_data:
                with open(video_data, 'rb') as video_file:  # Открываем файл для чтения
                    await context.bot.send_video(chat_id=chat_id, video=video_file)
                await update.message.reply_text("Видео из Instagram успешно отправлено!")
            else:
                await update.message.reply_text("Не удалось скачать видео из Instagram.")
        else:
            await update.message.reply_text("Некорректный URL Instagram Reels.")
    elif platform == "TikTok":
        video_data = download_tiktok_video(url)
        if video_data:
            with open(video_data, 'rb') as video_file:  # Открываем файл для чтения
                await context.bot.send_video(chat_id=chat_id, video=video_file)
            await update.message.reply_text("Видео из Instagram успешно отправлено!")
        else:
            await update.message.reply_text("Не удалось скачать видео из TikTok.")
    else:
        await update.message.reply_text("Платформа не поддерживается. Пожалуйста, отправьте ссылку на TikTok или Instagram Reels.")

def main():
    # Создаем экземпляр Application и передаем токен вашего бота
    application = Application.builder().token(f"{tg_token}").build()

    # Добавляем обработчик сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()

