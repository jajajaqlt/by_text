import sys
import json

ss_file = sys.argv[1]

with open(ss_file) as f:
    lines = f.readlines()

# for line in lines:
#     print(line)

# print('done')
# sys.exit()

for line in lines:
    js = json.loads(line)
    # print(js)
    # print(json.dumps(js, indent=2) + '\n')
    print(json.dumps(js, indent=2, ensure_ascii=False) + '\n')
    # input('type to continue>')
