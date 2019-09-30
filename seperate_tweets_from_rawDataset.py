import json
from pprint import pprint

with open('filename.json') as f:
    d = json.load(f)
    texts = []
    for data in d:
    	texts.append(data['text'])

    print(texts[0:])
