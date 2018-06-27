'''
0. title string
1. paperAbstract
2. authors list
3. outCitations list # the papers this paper cites
4. year int
5. venue string
6. journalName
7. sources: list (DBLP or Medline or empty)
8. id
9. - inCitations # the papers citing this paper
'''

import sys
import json

ss_file = sys.argv[1]
ss_js_file = sys.argv[2]

with open(ss_file) as f:
    lines = f.readlines()

extracted_fields = ['id', 'title', 'paperAbstract', 'authors', 'year', 'venue', 'journalName', 'outCitations', 'sources']
line_count = 0
papers = []

for line in lines:
    line_count += 1
    if line_count % 1000 == 0:
        print(line_count)
    paper = json.loads(line)
    new_paper = {field: paper[field] if field in paper else None for field in extracted_fields}
    papers.append(new_paper)
    # print(json.dumps(js, indent=2, ensure_ascii=False) + '\n')

with open(ss_js_file, 'w') as f:
    json.dump({'papers': papers}, f, ensure_ascii=False, indent=2)