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
    authors = p['authors']
    if len(authors) == 0:
        # print(p['id'])
        # print(p['title'])
        print(p)
        print('\n')
    # for a in authors:
    #     # check one author has only 1 id
    #     if len(a['ids']) > 1 or paper_count % 1000 == 0:
    #         print(a['name'])
    #         print(a['ids'])
    #         print('\n')

        # check one id associates one author
        # to be done when making the list