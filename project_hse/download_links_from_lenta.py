from project_funcs import *

# скачиваю ссылки на страницы со статьями за каждый день 2019 года
start_link = 'https://lenta.ru/'
end_link = calendar(False)  # изменить период для парсера. Смотри КАЛЕНДАРЬ
link_db = {'2019/01/01': []}
count = 0
for el in end_link:
    link = start_link + el
    page_raw = get_html(link)
    page = get_soup(page_raw)
    articles = page.findAll('h3')
    for text in articles:
        text = str(text)
        art_link = re.findall('\w+/\d+/\d+/\d+/\w+', text)  # почему подчеркивает регулярку? как правильно писать?
        full_link = start_link + str(*art_link)
        appendvalue(link_db, el, full_link)
        count += 1
        print(el)
print(count)

# сохранть как csv
# with open('2019links.csv', 'w', newline="") as csv_file:
#   writer = csv.writer(csv_file)
#    for key, value in link_db.items():
#        writer.writerow([key, value])
