import json
import re
import sys

input_file = sys.argv[1]
tag_patt = r'<(\w+)\b[^>]*>(.*?)</\1>'
tag_patt1 = r'<(\w+)\b[^>]{,40}>'
tag_patt2 = r'</\w+>'

with open(input_file) as f:
    papers = json.load(f)['papers']

title_tag_count = 0
title_tag_count1 = 0
title_tag_count2 = 0
abstract_tag_count = 0
abstract_tag_count1 = 0
abstract_tag_count2 = 0
total_count = len(papers)
for paper in papers:
    title = paper['title']
    abstract = paper['paperAbstract']
    if re.search(tag_patt, title) != None:
        title_tag_count += 1
    if re.search(tag_patt1, title) != None:
        title_tag_count1 += 1
        print('title tag1 ex: %s' % re.search(tag_patt1, title).group(0))
    if re.search(tag_patt2, title) != None:
        title_tag_count2 += 1
        print('title tag2 ex: %s' % re.search(tag_patt2, title).group(0))
    if re.search(tag_patt, abstract) != None:
        abstract_tag_count += 1
    if re.search(tag_patt1, abstract) != None:
        abstract_tag_count1 += 1
        print('abstract tag1 ex: %s' % re.search(tag_patt1, abstract).group(0))
    if re.search(tag_patt2, abstract) != None:
        abstract_tag_count2 += 1
        print('abstract tag2 ex: %s' % re.search(tag_patt2, abstract).group(0))

print('title tag count: %i, abstract tag count: %i, total count %i'%(title_tag_count, abstract_tag_count, total_count))
print('title pt1 count: %i, pt2 count %i; abstract pt1 count: %i, pt2 count: %i'% (title_tag_count1, title_tag_count2, abstract_tag_count1, abstract_tag_count2))