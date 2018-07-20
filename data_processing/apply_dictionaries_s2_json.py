import sys
import json
from collections import Counter

input_file = sys.argv[1]
output_file = sys.argv[2]
titles_file = sys.argv[3]
authors_file = sys.argv[4]
venues_file = sys.argv[5]

with open(input_file) as f:
    papers = json.load(f)['papers']

titles_dict = {}
with open(titles_file) as f:
    lines = f.readlines()
for line in lines:
    titles_dict[line[:40]] = int(line.split(' ')[1])

authors_list = []
with open(authors_file) as f:
    lines = f.readlines()
for line in lines:
    authors_list.append(int(line))
authors_dict = Counter(authors_list)

venues_dict = {}
with open(venues_file) as f:
    lines = f.readlines()
for line in lines:
    index_str = line.split(' ')[-1]
    index = int(index_str)
    venue = line[:-(len(index_str) + 1)]
    venues_dict[venue] = index

# import pdb; pdb.set_trace()
print('processing papers')
count = 0
for paper in papers:
    if count % 100 == 0:
        print(count)
    count += 1
    authors = paper['authors']
    author_ids = []
    for author in authors:
        ids = author['ids']
        for id in ids:
            id = int(id)
            if id in authors_dict:
                author_ids.append(id)
    paper['authors'] = author_ids

    venue = paper['venue']
    if venue in venues_dict:
        paper['venue'] = venues_dict[venue]
    else:
        paper['venue'] = None

    citations = paper['outCitations']
    citation_ids = []
    for cite in citations:
        if cite in titles_dict:
            citation_ids.append(titles_dict[cite])
    paper['outCitations'] = citation_ids

print('start writing')
with open(output_file, 'w') as f:
    json.dump({'papers': papers}, f, indent=2)

