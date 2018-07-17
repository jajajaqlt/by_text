import json
import sys
from langdetect import detect
import pdb

input_file = sys.argv[1]
with open(input_file) as f:
    papers = json.load(f)['papers']

count = 0
for paper in papers:
    count += 1
    title = paper['title']
    abstract = paper['paperAbstract']
    try:
        title_lang = detect(title) if title != '' else 'empty_title'
        abstract_lang = detect(abstract) if abstract != '' else 'en'
    except:
        pdb.set_trace()
    if title_lang != 'en' or abstract_lang != 'en':
        print('count is %s' % count)
        print('title_lang: %s' % title_lang)
        print(title)
        print('abstract_lang: %s' % abstract_lang)
        print(abstract)

# as a result, langdetect is slow and error-prone