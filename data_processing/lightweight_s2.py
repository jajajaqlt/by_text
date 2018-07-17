import sys
import json

in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file) as f:
    papers = json.load(f)['papers']

for paper in papers:
    del paper['id']
    authors = paper['authors']
    for author in authors:
        del author['name']
    del paper['outCitations']
    del paper['s2Url']

with open(out_file, 'w') as f:
    json.dump({'short_papers': papers}, f, indent=2)

