from project_funcs import *
from my_stop_words import my_stop_words
from categories_help_file import tags  # лист названий категорий

corpus_lemmas = []

for tag in tags:
    articles = find_tag(tag)
    corpus = delete_sw(articles)
    corpus_l = lemma(corpus)
    for l in corpus_l:
        for i in l:
            if i == ' 1234567890':  # можно было ударить рег выражением
                continue
        corpus_lemmas.append(l)
    corpus_final = delete_sw(corpus_lemmas, sw=my_stop_words)
    writing_lemmafiles(tag, corpus_final)
