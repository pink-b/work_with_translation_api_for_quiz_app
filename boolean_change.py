import json,os
directory = os.listdir('quizjson')
directory.sort()
for file in directory:
    data = json.load(open('quizjson/' + file))
    for i in range(len(data['questions'])):
        if data['questions'][i]['correct_answer'] == 'True':
            data['questions'][i]['correct_answer'] = True
        if data['questions'][i]['correct_answer'] == 'False':
            data['questions'][i]['correct_answer'] = False
        print(data['questions'][i])
    with open('quizjson/' + file, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)