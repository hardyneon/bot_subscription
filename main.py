import logging
import asyncio
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# === Настройки ===
API_TOKEN = "8498437370:AAGXEr_IbQ4Xpe0Z5danKdyxjc-9MVke1SI"  # вставь токен сюда
PRIVATE_CHAT_LINK = "https://t.me/+examplechat"  # ссылка на твой закрытый чат
SUPPORT_CONTACT = "@NektoAdmin"

# Включаем логи
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# Создаём бота и диспетчер
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Купить доступ")],
        [KeyboardButton(text="О сообществе")],
        [KeyboardButton(text="Поддержка")]
    ],
    resize_keyboard=True
)

# === Хэндлеры ===

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(
        "👋 Привет!\n"
        "Я бот для доступа в закрытое сообщество по интересам.\n\n"
        "🔐 Здесь ты можешь оформить подписку и попасть в приватный чат.",
        reply_markup=main_menu
    )

@dp.message(F.text.contains("Купить доступ"))
async def buy_access(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Криптовалюта"), KeyboardButton(text="Банковская карта")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Для оплаты выбери способ:\n\n"
        "— Криптовалюта (USDT TRC20, TON, BTC)\n"
        "— Банковская карта (P2P)\n",
        reply_markup=kb
    )

@dp.message(F.text.in_(["Криптовалюта", "Банковская карта"]))
async def process_payment(message: types.Message):
    await message.answer(
        "✅ Спасибо! Оплата успешно получена.\n\n"
        f"🎉 Вот твоя ссылка в приватный чат:\n👉 {PRIVATE_CHAT_LINK}",
        reply_markup=main_menu
    )

@dp.message(F.text.contains("О сообществе"))
async def about(message: types.Message):
    await message.answer(
        "🔐 Наше сообщество — это закрытый чат, где мы общаемся на самые открытые темы.\n\n"
        "👥 Доступ только по подписке.\n"
        "💬 Внутри — личный контент и живое общение."
    )

@dp.message(F.text.contains("Поддержка"))
async def support(message: types.Message):
    await message.answer(f"📞 По всем вопросам: {SUPPORT_CONTACT}")

@dp.message(F.text.contains("Назад"))
async def back(message: types.Message):
    await message.answer("🔙 Главное меню", reply_markup=main_menu)

# === Запуск ===
async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

