import sys
import json
from langdetect import detect

input_file = sys.argv[1]
s2_ids_file = sys.argv[2]
authors_names_ids_file = sys.argv[3]
venues_file = sys.argv[4]

with open(input_file) as f:
    papers = json.load(f)['papers']

s2_ids = []
authors_names_ids = []
venues = []

def format_author_entry(author):
    entry = author['name']
    for id in author['ids']:
        entry += ' ' + id
    return entry

for paper in papers:
    s2_ids.append(paper['id'])
    if paper['venue'].strip() != '':
        venues.append(paper['venue'])
    for author in paper['authors']:
        authors_names_ids.append(format_author_entry(author))

print('writing %s' % s2_ids_file)
with open(s2_ids_file, 'w') as f:
    f.writelines('\n'.join(s2_ids))

print('writing %s' % authors_names_ids)
with open(authors_names_ids_file, 'w') as f:
    f.writelines('\n'.join(authors_names_ids))

print('writing %s' % venues_file)
with open(venues_file, 'w') as f:
    f.writelines('\n'.join(venues))

