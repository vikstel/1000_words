import json

with open('cards.json', 'r', encoding='utf-8') as file:
    words = json.load(file)
for word in words:
    text_to_answer = f'<b>{word.get("russian_word")}</b>\n'\
                     f'<b>{word.get("english_word")}</b>\n'\
                     f'{word.get("img_card")}\n'\
                     f'{word.get("sound_card")}'

    print(text_to_answer)