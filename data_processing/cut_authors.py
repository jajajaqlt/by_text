import sys
import re
from collections import Counter

# num_patt = r' [-+]?[\d,]*\.?\d+([eE][-+]?\d+)?'

input_file = sys.argv[1]
output_file = sys.argv[2]
threshold = int(sys.argv[3])

with open(input_file) as f:
    lines = f.readlines()

author_ids = []
invalid_authors = []

for line in lines:
    line = line.split(' ')[-1]
    # match = re.search(num_patt, line)
    # if match != None:
    try:
        author_id = int(line)
        author_ids.append(author_id)
    except:
        invalid_authors.append(line)


author_id_counts = Counter(author_ids)
sorted_author_id_counts = sorted(author_id_counts.items(), key=lambda kv: kv[1], reverse=True)

if '.' in output_file and '..' not in output_file:
    output_file = output_file.split('.')[0] + '_' + str(threshold) + output_file.split('.')[-1]
else:
    output_file = output_file + '_' + str(threshold)

out = open(output_file, 'w')

for count in sorted_author_id_counts:
    if count[1] < threshold:
        break
    out.write(str(count[0]) + '\n')

out.close()