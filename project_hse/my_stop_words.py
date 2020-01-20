from project_funcs import *

with open('частотные_леммы.txt', 'r', encoding='utf-8') as file:  # топ-150 по словарю О. Н. Ляшевской, С. А. Шарова
    lemmas = str_to_list(file.readline())

with open('частотные_сл_сл.txt', 'r', encoding='utf-8') as file:  # топ-150 по словарю О. Н. Ляшевской, С. А. Шарова
    props = str_to_list(file.readline())

freq = []

for el in lemmas:
    if el not in freq:
        freq.append(el)
    for elem in props:
        if elem not in freq:
            freq.append(elem)

total_list = set(freq + stop_words())

my_stop_words = []  # конечный лист

for i in total_list:
    my_stop_words.append(i.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
