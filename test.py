d1 = {'a':1}

d2 = {'b':2}

import json
def write_file():
    with open('sample.json','a') as sample:
        for dict in [d1,d2]:
            sample.write('{}\n'.format(json.dumps(dict)))

def read_file():
    with open('sample.json','r') as sample:
        for line in sample:
            line = json.loads(line.strip())
        print(line)

write_file()
read_file()