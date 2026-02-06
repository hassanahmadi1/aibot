from telegram.ext import Application, MessageHandler, filters
from classifier import classify_text

TOKEN = "8471961306:AAGbgc-TejQCKAqLLLjeDTrIxqnE0kNBsKA"

async def handle_message(update, context):
    text = update.message.text
    label, confidence = classify_text(text)

    if confidence < 0.6:
        label = "other"

    await update.message.reply_text(
        f"📌 نوع پیام: {label}\n"
        f"🔍 اطمینان: {confidence:.2f}"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()