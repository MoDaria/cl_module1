from project_funcs import *
from download_links_from_lenta import link_db  # словарь с ссылками, можно из csv файла

count = 0  # счетчик количества статей для генерации названий
for key in link_db.keys():
    links = link_db.get(key)
    for el in links:
        count += 1
        raw_link = get_html(el)
        generate_name(count, raw_link)
