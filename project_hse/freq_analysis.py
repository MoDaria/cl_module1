from project_funcs import *
from categories_help_file import tags  # лист названий категорий
from collections import defaultdict as dd
from operator import itemgetter

# считаю частотность лемм по каждой категории
for tag in tags:
    with open(os.getcwd() + '\\Lemmas' + '\\{}_lemmatize.txt'.format(tag), 'r', encoding='utf8') as file:
        corpus = file.readlines()
        twf = dd(int)
        data = {'Word': 'Frequency'}
        for w in corpus:
            twf[w] += 1 / len(corpus)
        sorted_frequency_table = sorted(twf.items(), key=itemgetter(1), reverse=True)
        for word, freq in sorted_frequency_table[:100]:
            appendvalue(data, word.strip('\r\n'), "%.5f" % freq)
    save_freq(tag, data)


