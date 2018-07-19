import json
import re
import sys
import pdb

input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file) as f:
    papers = json.load(f)['articles']

# title_letters_thres = 0.9
# abstract_letters_thres = 0.9

titles_out = 0
abstracts_out = 0
empty_abstracts_out = 0

index = -1
out_indices = []
for paper in papers:
    index += 1
    out_flag = False
    title = paper['title'].strip()
    abstract = paper['paperAbstract'].strip()

    ### replaces numbers with #
    num_patt = r'[-+]?[\d,]*\.?\d+([eE][-+]?\d+)?'
    title = re.sub(num_patt, '#', title)
    abstract = re.sub(num_patt, '#', abstract)

    ### deals with brackets surrounding title
    title_surrounding_brackets = r'^\[.+\].$'
    if re.search(title_surrounding_brackets, title) != None:
        title = title[1:-2]

    ### deals with html tags and latex tags
    tag_patt1 = r'<(\w+)\b[^>]{,40}>'
    tag_patt2 = r'</\w+>'
    title = re.sub(tag_patt1, ' ', title)
    title = re.sub(tag_patt2, ' ', title)
    abstract = re.sub(tag_patt1, ' ', abstract)
    abstract = re.sub(tag_patt2, ' ', abstract)

    ### change non-breakable space, newline(line feed)
    # \u00a0, \n, \t
    nbsp = '\u00a0'
    newline = '\n'
    tab = '\t'
    succ_space = ' +'
    title = re.sub(nbsp, ' ', title)
    title = re.sub(newline, ' ', title)
    title = re.sub(tab, ' ', title)
    title = re.sub(succ_space, ' ', title)
    # paper['title'] = title

    abstract = re.sub(nbsp, ' ', abstract)
    abstract = re.sub(newline, ' ', abstract)
    abstract = re.sub(tab, ' ', abstract)
    abstract = re.sub(succ_space, ' ', abstract)
    # paper['paperAbstract'] = abstract

    ### deal with the special tokens, convert special tokens to question marks (?)
    title_specials_thres = 0.9
    abstract_specials_thres = 0.98

    title_specials = 0
    title = list(title)
    for i, c in enumerate(title):
        code = ord(c)
        if code > 127:
            title_specials += 1
            title[i] = '?'
    paper['title'] = ''.join(title)
    paper['title_percent'] = 1 - title_specials / len(title)
    # if len(title) == 0 or paper['title_percent'] < title_specials_thres:
    #     paper['title_out'] = True
    #     titles_out += 1

    abstract_specials = 0
    abstract = list(abstract)
    for i, c in enumerate(abstract):
        code = ord(c)
        if code > 127:
            abstract_specials += 1
            abstract[i] = '?'
    paper['paperAbstract'] = ''.join(abstract)
    paper['abstract_percent'] = 1 - abstract_specials / len(abstract) if len(abstract) != 0 else 1
    # if len(abstract) == 0 or paper['abstract_percent'] < abstract_specials_thres:
    #     if len(abstract) != 0:
    #         empty_abstracts_out += 1
    #         paper['abstract_out'] = True
            abstracts_out += 1


print('%i titles, %i out, %f percent' % (len(papers), titles_out, titles_out / len(papers)))
print('%i abstracts, %i out, %f percent' % (len(papers), abstracts_out, abstracts_out / len(papers)))
# print('empty abstracts are %i' % empty_abstracts_out)
#
# import pdb
# pdb.set_trace()

print('start writing file')
with open(output_file, 'w') as f:
    json.dump({'papers': papers}, f, indent=2, ensure_ascii=False)


#     ### those are final statistics code but won't contain conversion code
#     title_letters = 0
#     abstract_letters = 0
#     for c in title:
#         code = ord(c)
#         if code > 127:
#             out_flag = True
#             break
#         elif code >= 97 and code <= 122 or code == 32:
#             title_letters += 1
#     if title_letters / len(title) < title_letters_thres:
#         out_flag = True
#     if out_flag:
#         paper['filter_out'] = True
#         out_indices.append(index)
#         continue
#     if abstract == '':
#         continue
#     for c in abstract:
#         code = ord(c)
#         if code > 127:
#             out_flag = True
#             break
#         elif code >= 97 and code <= 122 or code == 32:
#             abstract_letters += 1
#     if abstract_letters / len(abstract) < abstract_letters_thres:
#         out_flag = True
#     if out_flag:
#         paper['filter_out'] = True
#         out_indices.append(index)
#
# print(out_indices)
# import pdb
# pdb.set_trace()
