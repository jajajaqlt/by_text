import json
import sys
import pdb

input_file = sys.argv[1]
with open(input_file) as f:
    papers = json.load(f)['papers']

title_letters_thres = 0.9
abstract_letters_thres = 0.9

index = -1
out_indices = []
for paper in papers:
    index += 1
    out_flag = False
    title = paper['title'].lower()
    if title == '':
        out_flag == True
    abstract = paper['paperAbstract'].lower()
    title_letters = 0
    abstract_letters = 0
    for c in title:
        code = ord(c)
        if code > 127:
            out_flag = True
            break
        elif code >= 97 and code <= 122 or code == 32:
            title_letters += 1
    if title_letters / len(title) < title_letters_thres:
        out_flag = True
    if out_flag:
        paper['filter_out'] = True
        out_indices.append(index)
        continue
    if abstract == '':
        continue
    for c in abstract:
        code = ord(c)
        if code > 127:
            out_flag = True
            break
        elif code >= 97 and code <= 122 or code == 32:
            abstract_letters += 1
    if abstract_letters / len(abstract) < abstract_letters_thres:
        out_flag = True
    if out_flag:
        paper['filter_out'] = True
        out_indices.append(index)

print(out_indices)
import pdb
pdb.set_trace()

#