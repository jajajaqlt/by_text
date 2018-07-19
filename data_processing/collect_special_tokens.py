import sys
import json

input_file = sys.argv[1]

with open(input_file) as f:
    papers = json.load(f)['articles']

title_tokens_count = 0
title_special_tokens = []
title_special_tokens_count = 0
abstract_tokens_count = 0
abstract_special_tokens = []
abstract_special_tokens_count = 0

for paper in papers:
    title = paper['title']
    title_tokens_count += len(title)
    for c in title:
        if ord(c) > 127:
            title_special_tokens.append(c)
            title_special_tokens_count += 1

    abstract = paper['paperAbstract']
    abstract_tokens_count += len(abstract)
    for c in abstract:
        if ord(c) > 127:
            abstract_special_tokens.append(c)
            abstract_special_tokens_count += 1

print('total title tokens: %i, special title tokens: %i, percentage: %.3f' % (
title_tokens_count, title_special_tokens_count, title_special_tokens_count / title_tokens_count))

print('total abstract tokens: %i, special abstract tokens: %i, percentage: %.3f' % (
abstract_tokens_count, abstract_special_tokens_count, abstract_special_tokens_count / abstract_tokens_count))

# doing statistics
from collections import Counter
title_counter = Counter(title_special_tokens)
abstract_counter = Counter(abstract_special_tokens)

print(title_counter)
print(abstract_counter)

from langdetect import detect
for key in title_counter.keys():
    try:
        lang = detect(key)
        title_counter[key] = lang
    except:
        print('unrecognized character: %s'% (key))

for key in abstract_counter.keys():
    try:
        lang = detect(key)
        abstract_counter[key] = lang
    except:
        print('unrecognized character: %s'% (key))

print(title_counter)
print(abstract_counter)

