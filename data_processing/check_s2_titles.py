import sys
import json

s2_js_file = sys.argv[1]

with open(s2_js_file) as f:
    papers = json.load(f)['papers']

paper_count = 0
for p in papers:
    paper_count += 1
    if paper_count % 1000 == 0:
        print(paper_count)
    # original check
    # if p['title'] == '' or p['title'] is None:
    #     print(p)
    if p['venue'].lower() != p['journalName'].lower():
        print(p['venue'])
        print(p['journalName'])
        print('---------->')
