import json


with open('words.json', 'r', encoding='utf-8') as file:
    words = json.load(file)

for word in words:
    # eng_word = word[0]
    # rus_word = word[1]
    # phrase = eng_word + '-' + rus_word
    with open('words.txt', 'a', encoding='utf-8') as f:
        f.write(word[0])
        f.write('\n')
for word in words:
    # eng_word = word[0]
    # rus_word = word[1]
    # phrase = eng_word + '-' + rus_word
    with open('words.txt', 'a', encoding='utf-8') as f:
        f.write(word[1])
        f.write('\n')
