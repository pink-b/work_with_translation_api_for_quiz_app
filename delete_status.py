import json

data = json.load(open('quizjson2/g.json'))
print(data)
print(len(data))

#m = open('test.json', 'w')
for i in range(5):
    del data[i]['response_code']
print(data)
with open('quizjson2/g.json', 'w') as m:
    json.dump(data, m, indent=2, ensure_ascii=False)
m.close()