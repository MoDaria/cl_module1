import requests
from bs4 import BeautifulSoup as bs
import re
import os
from nltk.corpus import stopwords
import pymorphy2
import csv


def get_html(url):  # получить страницу сайта
    import time
    while True:
        try:
            page = requests.get(url)
            return page.text
        except TimeoutError:
            time.sleep(30.00)


def get_soup(rawlink):  # страница через bs4
    bsite = bs(rawlink, "html.parser")
    return bsite


def calendar(yearoff, start=2019, end=2020, defyear=2019, defmonth=12): #yearoff = True - можно указывать только месяца/
#False - можно указывать годы
    list_31 = [1, 3, 5, 7, 8, 10, 12]
    num_month = 12
    data = list()
    year_viskas = False
    if yearoff == True:
        year = defyear
        num_month = defmonth
        for month in range(1, num_month + 1):
            if month == 2:
                if year_viskas:
                    N = 29
                else:
                    N = 28
            elif month in list_31:
                N = 31
            else:
                N = 30
            for day in range(1, N + 1):
                sep_month, sep_day = '/', '/'
                if month < 10:
                    sep_month = '/0'
                if day < 10:
                    sep_day = '/0'
                ymd = [str(year), sep_month, str(month), sep_day, str(day)]
                ymd_str = ''.join(ymd)
                data.append(ymd_str)
    else:
        start = int(start)
        end = int(end)
        for year in range(start, end):
            year_viskas = False
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                year_viskas = True
            for month in range(1, num_month + 1):
                if month == 2:
                    if year_viskas:
                        N = 29
                    else:
                        N = 28
                elif month in list_31:
                    N = 31
                else:
                    N = 30
                for day in range(1, N + 1):
                    sep_month, sep_day = '/', '/'
                    if month < 10:
                        sep_month = '/0'
                    if day < 10:
                        sep_day = '/0'
                    ymd = [str(year), sep_month, str(month), sep_day, str(day)]
                    ymd_str = ''.join(ymd)
                    data.append(ymd_str)
    return data


def appendvalue(d, key, value):  # добавляет значение по ключу словаря
    if key in d.keys():
        d[key] += [value]
    else:
        d[key] = [value]


def category(link):  # ищет название категории в коде страницы
    first = 'title: \'.+\''
    second = '[а-яА-Я ]+'
    raw = str(re.findall(first, link))
    text = re.findall(second, raw)
    result = ''
    for el in text:
        result = el.lower()
    return result


def get_article(link):  #ищет статью в коде страницы
    import re
    page = get_soup(link)
    fish = str(page.findAll('p'))
    res = re.findall('[А-Яа-я ]+', fish)
    result = ''
    for el in res:
        result += el
    return result


def generate_name(number, html):  # генератор файлов со статьями
    start = 'News2019/'
    file_name = start + 'article{}.txt'.format(number)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html)


def files_counter(path='news'):  # считает кол-во сохраненных статей
    result = path
    master_path = os.getcwd()
    news_path = "\\News2019"
    tags_path = '\\Tags2019'
    news = len(os.listdir(master_path + news_path))
    tags = len(os.listdir(master_path + tags_path))
    if result == 'news':
        result = news
    else:
        result = tags
    return result


def upload_html(number):  # генератор названий файлов со статьям
    start = 'News2019/'
    file_name = start + 'article{}.txt'.format(number)
    with open(file_name, 'r', encoding='utf-8') as file:
        res = file.read()
    return res


def writing_tagfile(list_of_texts):  # генератор названий файлов по категориям
    start = 'Tags2019/'
    for key in list_of_texts.keys():
        file_name = start + 'tag_{}.txt'.format(key)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.writelines("%s\n" % texts for texts in list_of_texts.get(key))


def writing_lemmafiles(name, data): # генератор названий файлов с леммами
    start = 'Lemmas/'
    file_name = start + '{}_lemmatize.txt'.format(name)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines("%s\n" % words for words in data)


def find_tag(tag):  # ищет файлы с категориями
    master_path = os.getcwd()
    tags_path = '\\Tags2019'
    texts = []
    file_name = master_path + tags_path + '\\tag_{}.txt'.format(tag)
    if 'tag_{}.txt'.format(tag) in os.listdir(master_path + tags_path):
        with open(file_name, 'r', encoding='utf-8') as file:
            for lines in file:
                res = lines[:-1]
                texts.append(res)
    return texts


def str_to_list(data):  # конвертер строк в списки
    return data.split()


def list_to_str(data):  # конвертер списков в строки
    result = str()
    for el in data:
        result += el
        result += ' '
    return result


def stop_words():  # быстрый вызов стоп-слов nltk
    return stopwords.words('russian')


def delete_sw(texts, sw=stopwords.words('russian')):  # чистит от стоп-слов
    result = []
    for text in texts:
        if isinstance(text, str):
            text = str_to_list(text)
        for word in text:
            if word not in sw:
                result.append(word)
    return result


def lemma(text):  # лемматизация от pymorphy
    res = list()
    morph = pymorphy2.MorphAnalyzer()
    for word in text:
        p = morph.parse(word)[0]
        res.append(p.normal_form)
    return res


def save_freq(tag, info): # сохраняет частотные списки
    master_path = os.getcwd()
    tags_path = '\\freq'
    file_name = master_path + tags_path + '\\{}_freq.csv'.format(tag)
    with open(file_name, 'w', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in info.items():
            writer.writerow([key, value])