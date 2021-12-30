import json,os
directory = os.listdir('quizjson')
directory.sort()
for file in directory:
    data = json.load(open('quizjson/' + file))
    for i in range(len(data['questions'])):
        for j in range(len(data['questions'][i]['incorrect_answers'])):
            if data['questions'][i]['incorrect_answers'][j]['answer'] == 'True' or data['questions'][i]['incorrect_answers'][j]['answer'] == 'False':
                del data['questions'][i]['incorrect_answers'][j]
        if len(data['questions'][i]['incorrect_answers']) == 0:
            del data['questions'][i]['incorrect_answers']
        print(data['questions'][i])
    with open('quizjson/' + file , 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)