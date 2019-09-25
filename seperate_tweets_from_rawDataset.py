import json
from pprint import pprint

with open('twitter.json') as f:
    d = json.load(f)
    texts = []
    for data in d:
    	texts.append(data['text'])

    print(texts[:100000000000000000000])