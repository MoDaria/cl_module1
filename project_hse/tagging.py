from project_funcs import *

all_tags = {'russia': [], 'world': [], 'ussr': [], 'economics': [], 'army': [], 'science': [], \
'culture': [], 'sport': [], 'internet': [], 'values': [], 'travel': [], 'life': [], \
'home': [], 'without_category': []}

count = files_counter()  # всего статей

for numeral in range(1, count+1):
    raw_link = upload_html(numeral)  # открываю скаченные в download_htmls_to_local статьи
    header = category(raw_link)  # Нахожу названия категорий
    text = get_article(raw_link)  # Нахожу текст статьи
    if header == 'россия':
        appendvalue(all_tags, 'russia', text)
        print("Добавил текст в", header)
    elif header == 'мир':
        appendvalue(all_tags, 'world', text)
        print("Добавил текст в", header)
    elif header == 'бывший ссср':
        appendvalue(all_tags, 'ussr', text)
        print("Добавил текст в", header)
    elif header == 'экономика':
        appendvalue(all_tags, 'economics', text)
        print("Добавил текст в", header)
    elif header == 'силовые структуры':
        appendvalue(all_tags, 'army', text)
        print("Добавил текст в", header)
    elif header == 'наука и техника':
        appendvalue(all_tags, 'science', text)
        print("Добавил текст в", header)
    elif header == 'культура':
        appendvalue(all_tags, 'culture', text)
        print("Добавил текст в", header)
    elif header == 'спорт':
        appendvalue(all_tags, 'sport', text)
        print("Добавил текст в", header)
    elif header == 'интернет и сми':
        appendvalue(all_tags, 'internet', text)
        print("Добавил текст в", header)
    elif header == 'ценности':
        appendvalue(all_tags, 'values', text)
        print("Добавил текст в", header)
    elif header == 'путешествия':
        appendvalue(all_tags, 'travel', text)
        print("Добавил текст в", header)
    elif header == 'из жизни':
        appendvalue(all_tags, 'life', text)
        print("Добавил текст в", header)
    elif header == 'дом':
        appendvalue(all_tags, 'home', text)
        print("Добавил текст в", header)
    else:
        appendvalue(all_tags, 'without_category', text)  # на некоторых страницах не видит категорию
        print("Добавил текст в Без темы")

writing_tagfile(all_tags)
