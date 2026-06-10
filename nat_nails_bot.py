import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ===== ВСТАВЬ СЮДА СВОЙ ТОКЕН =====
BOT_TOKEN = "8538322962:AAE1ADkV8QNL_WLiBWVl8lIErk5W-xBHDZE"
# ===================================

logging.basicConfig(level=logging.INFO)

# Главное меню (кнопки)
def main_keyboard():
    keyboard = [
        [KeyboardButton("💅 Записаться"), KeyboardButton("💰 Прайс")],
        [KeyboardButton("📍 Адрес"),      KeyboardButton("📞 Связаться")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# /start и /menu — главное меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я бот nail-мастера Натальи.\n\nВыбери, что тебя интересует:",
        reply_markup=main_keyboard()
    )

# /book — записаться
async def book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 *Запись на маникюр*\n\n"
        "Напиши желаемую дату и время, например:\n"
        "_«Хочу записаться в субботу в 14:00»_\n\n"
        "Или позвони/напиши напрямую — контакты в разделе 📞 Связаться.",
        parse_mode="Markdown"
    )

# /price — прайс
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 *Прайс-лист*\n\n"
        "• Маникюр без покрытия — 800 ₽\n"
        "• Маникюр + гель-лак — 1500 ₽\n"
        "• Снятие покрытия — 300 ₽\n"
        "• Педикюр — 1800 ₽\n"
        "• Наращивание — 2500 ₽\n\n"
        "_Цены могут меняться, уточняйте при записи._",
        parse_mode="Markdown"
    )

# /address — адрес
async def address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📍 *Адрес*\n\n"
        "г. Москва, ул. Примерная, д. 1\n"
        "м. Центральная (5 мин пешком)\n\n"
        "🕐 Режим работы: пн–сб 10:00–20:00",
        parse_mode="Markdown"
    )

# /contact — связаться
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 *Контакты*\n\n"
        "Телефон/WhatsApp: +7 (999) 123-45-67\n"
        "Instagram: @nat_nails\n"
        "Или пишите прямо сюда в бот 💬",
        parse_mode="Markdown"
    )

# Обработка кнопок главного меню
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💅 Записаться":
        await book(update, context)
    elif text == "💰 Прайс":
        await price(update, context)
    elif text == "📍 Адрес":
        await address(update, context)
    elif text == "📞 Связаться":
        await contact(update, context)
    else:
        await update.message.reply_text(
            "Воспользуйся кнопками меню ниже 👇",
            reply_markup=main_keyboard()
        )

# Запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CommandHandler("book", book))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("address", address))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("✅ Бот запущен!")
    app.run_polling()
