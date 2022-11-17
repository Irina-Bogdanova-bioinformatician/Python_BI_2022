import re
from collections import defaultdict
import matplotlib.pyplot as plt

# 1. Распарсите файл references при помощи регулярных выражений и запишите оттуда все ftp ссылки в файл ftps

with open("references") as references, open("ftps", "w") as out:
    text = references.read()
    ftp_links = re.findall(r'(ftp\.[\w\./@:%_+~#=-]*\.(gz|md5|cram))', text)
    for new_group in ftp_links:
        out.write(new_group[0] + '\n')

# 2. Извлеките из рассказа  2430 A.D. все числа

with open("2430_A.D.txt") as story:
    text = story.read()
    numbers = re.findall(r'\d*[.,]?\d+', text)
    # print(numbers)

# 3. Из того же рассказа извлеките все слова, в которых есть буква a, регистр при этом не важен

words_with_a = re.findall(r'[a-z]*a+\.?[a-z]*', text, re.IGNORECASE)
# print(words_with_a)

# 4. Извлеките из рассказа все восклицательные предложения

exclamation_sentences = re.findall(r'[A-Z][^\.?!]*!', text)
# print(exclamation_sentences)

""" 5. Постройте гистограмму распределения длин уникальных слов (без учёта регистра, длина от 1) в тексте.
То есть по оси x идёт длина слова. По оси y идёт доля слов с такой длиной среди уникальных слов, найденных в тексте. 
При этом слова the и The считаются одним словом, то есть регистр не важен
"""

words = re.findall(r"\w+'?\w+|\w+\.?\w+", text, re.IGNORECASE)
unique_lowercase_words = set(list(map(lambda x: x.lower(), words)))
lengths_counts = defaultdict(int)
for word in unique_lowercase_words:
    lengths_counts[len(word)] += 1
lengths_fractions, total = {}, len(unique_lowercase_words)
for length, words_count in lengths_counts.items():
    lengths_fractions[length] = words_count / total * 100
barplot = plt.bar(lengths_fractions.keys(), lengths_fractions.values(), color='g')
plt.title("Word length distribution in '2430 A.D'")
plt.xlabel("Word length")
plt.ylabel("Fraction, %")
plt.show()

""" 6. Сделайте функцию-переводчик с русского на "кирпичный язык"
https://yandex.ru/q/question/kirpichnyi_iazyk_kak_govorit_cc88f9dc/
"""


def rus_to_brick_translator(string: str) -> str:
    translated_string = re.sub(r'([аеёиоуыэюяАЕЁИОУЫЭЮЯ])', r'\1k\1', string, flags=re.U)
    return translated_string


brick_Basho = rus_to_brick_translator("Хижина рыбака.Замешался в груду креветок Одинокий сверчок.")
# print(brick_Basho)
