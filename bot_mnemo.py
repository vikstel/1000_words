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

# random_words = words[:5]
# print(random_words)
# for word in random_words:
#     answer = f'{word[0]}\n{word[2]}\n{word[1]}'
#     print(answer)
#     print('-' * 30)

@dp.message(Command(commands=['start']))
async def start_commands(message: Message):
    random_words = words[:5]
    for word in random_words:
        text_to_answer = f'<b>{word[0]}</b>\n' \
                             f'{word[2]}\n' \
                            f'<b>{word[1]}</b>'

        await message.answer(text_to_answer)


if __name__ == '__main__':
    dp.run_polling(bot)