import re
import sys
import json

'''
0. title string
1. paperAbstract
2. authors list
3. outCitations list # the papers this paper cites
4. year int
5. venue string
6. journalName # venue preferred
7. sources: list (DBLP or Medline or empty)
8. id
9. - inCitations # the papers citing this paper
'''

input_file = sys.argv[1]
# each line: s2_id title title_percent
titles_file = sys.argv[2]
# each line: author id1 id2
authors_file = sys.argv[3]
# each line: venue (skip if empty)
venues_file = sys.argv[4]
titles_list = []
authors_list = []
venues_list = []

with open(input_file) as f:
    lines = f.readlines()

features = ['id', 'title', 'paperAbstract', 'authors', 'year', 'venue', 'outCitations', 'sources']
papers = []

def format_author_entry(author):
    entry = author['name']
    for id in author['ids']:
        entry += ' ' + id
    return entry

for line in lines:
    paper = json.load(line)
    paper = {feature: paper[feature] for feature in features}

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
    paper['title_percent'] = 1 - title_specials / len(title) if len(title) != 0 else 1

    abstract_specials = 0
    abstract = list(abstract)
    for i, c in enumerate(abstract):
        code = ord(c)
        if code > 127:
            abstract_specials += 1
            abstract[i] = '?'
    paper['paperAbstract'] = ''.join(abstract)
    paper['abstract_percent'] = 1 - abstract_specials / len(abstract) if len(abstract) != 0 else 1

    ### write different feature lists
    titles_list.append(paper['id'] + ' ' + paper['title'] + ' ' + str(paper['title_percent']))
    if paper['venue'].strip() != '':
        venues_list.append(paper['venue'])
    for author in paper['authors']:
        authors_list.append(format_author_entry(author))

    ### adds the json paper entry
    papers.append(paper)

print('writing the new json file %s' % (input_file + '.json'))
with open(input_file + '.json', 'w') as f:
    json.dump({'papers': papers}, f, indent=2, ensure_ascii=False)

print('writing titles to a separate list')
with open(titles_file, 'w') as f:
    f.writelines('\n'.join(titles_list))

print('writing authors to a separate list')
with open(authors_file, 'w') as f:
    f.writelines('\n'.join(authors_list))

print('writing venues to a separate list')
with open(venues_file, 'w') as f:
    f.writelines('\n'.join(venues_list))

print('done for %s!' % input_file)
