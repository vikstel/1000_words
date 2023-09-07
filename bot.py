import json
import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
from config import TOKEN


token = TOKEN
bot = Bot(token, parse_mode='HTML')
dp = Dispatcher()


with open('words.json', 'r', encoding='utf-8') as file:
    words = json.load(file)

# for word in words:
#     print(word[0], word[1], word[2])


@dp.message(Command(commands=['start']))
async def start_commands(message: Message):
    random_words = words[:5]
    for word in random_words:
        text_to_answer = f'<b>{word[0]}</b>\n' \
                             f'{word[2]}\n' \
                            f'{word[1]}</b>'

    await message.answer(text_to_answer)


if __name__ == '__main__':
    dp.run_polling(bot)