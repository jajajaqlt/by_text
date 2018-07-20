import sys
import re
from collections import Counter

# num_patt = r' [-+]?[\d,]*\.?\d+([eE][-+]?\d+)?'

input_file = sys.argv[1]
output_file = sys.argv[2]
threshold = int(sys.argv[3])

with open(input_file) as f:
    venues = f.readlines()

venue_counts = Counter(venues)
sorted_venue_counts = sorted(venue_counts.items(), key=lambda kv: kv[1], reverse=True)

if '.' in output_file and '..' not in output_file:
    output_file = output_file.split('.')[0] + '_' + str(threshold) + output_file.split('.')[-1]
else:
    output_file = output_file + '_' + str(threshold)

out = open(output_file, 'w')

index = 0
for count in sorted_venue_counts:
    if count[1] < threshold:
        break
    out.write(count[0].strip() + ' ' + str(index) + '\n')
    index += 1

out.close()