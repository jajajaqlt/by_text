import sys
import re

num_patt = r'[-+]?[\d,]*\.?\d+([eE][-+]?\d+)?'

input_file = sys.argv[1]
output_file = sys.argv[2]
threshold = float(sys.argv[3])

with open(input_file) as f:
    lines = f.readlines()

s2_ids = []

for line in lines:
    # s2 id universal length 40 chars
    s2_id = line[:40]
    percent = float(re.search(num_patt, line).group(0))
    if percent > threshold:
        s2_ids.append(s2_id)

if '.' in output_file and '..' not in output_file:
    output_file = output_file.split('.')[0] + '_' + str(threshold) + output_file.split('.')[-1]
else:
    output_file = output_file + '_' + str(threshold)

out = open(output_file, 'w')

for i, id in enumerate(s2_ids):
    out.write(id + ' ' + str(i) + '\n')

out.close()