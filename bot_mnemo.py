import json
import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
from config import TOKEN


token = TOKEN
bot = Bot(token, parse_mode='HTML')
dp = Dispatcher()


with open('cards.json', 'r', encoding='utf-8') as file:
    words = json.load(file)


@dp.message(Command(commands=['start']))
async def start_commands(message: Message):
    random_words = words[:5]
    for word in random_words:
        text_to_answer = f'<b>{word.get("russian_word")}</b>\n' \
                         f'<b>{word.get("english_word")}</b>\n' \
                         f'{word.get("img_card")}\n' \
                         f'{word.get("sound_card")}'

        await message.answer(text_to_answer)


if __name__ == '__main__':
    dp.run_polling(bot)



