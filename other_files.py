import json

collection = []
data = json.load(open('responce_quiz2.json'))
for i in range(281):
    #list = data[i]['results']
    for j in range(50):
        list2 = data[i]['results'][j]['category']
        list2 = list2.replace(' ', '')
        if list2 in collection:
            with open('quiz.json2/' + str(list2) + '.json', 'a') as m:
                json.dump(data[i]['results'][j], m, indent=2, ensure_ascii=False)
                m.write(',')
        else:
            with open('quiz.json2/' + str(list2) + '.json', 'w') as m:
                json.dump(data[i]['results'][j], m, indent=2, ensure_ascii=False)
                m.write(',')
        #list2 = list2.replace(' ','')
        collection += list2.split()

list2 = data[0]['results'][0]['category']
print(str(list2) + '.json')

print(data[0]['results'][0]['category'])
print(data[0]['results'][0])
#print(collection)'''

print(data[0]['results'][3]['category'])

