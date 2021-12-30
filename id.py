import json
import os


directive = os.listdir('quizjson')
directive.sort()
for el in directive:
    data_0 = json.load(open('quizjson/' + el))
    final_file = {'category':data_0[0]['category'],'category_id':directive.index(el),'questions':[]}
    final_file['questions'] = data_0
    data = final_file
    print(data)
    print('                                                            ')
    questions = data['questions']
    # m = open('quizjson/' + el, 'w')
    #m.write('[')
    for i in range(len(questions)):
        questions[i]["id"] = i
        inc_ans = questions[i]["incorrect_answers"]
        del questions[i]['category']
        for j in range(len(inc_ans)):
            questions[i]["incorrect_answers"][j] = {'id':j,'answer':questions[i]['incorrect_answers'][j]}
        print(questions[i])
    with open('quizjson/' + el, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

