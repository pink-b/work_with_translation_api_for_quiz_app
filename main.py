import requests
import json

#file = open('responce_quiz.json', 'a')
#file.write('[')
for i in range(238):
    r = requests.get('https://opentdb.com/api.php?amount=50&category=12&token=00a52376acf42ccf514212454ee170898b658397f94ff7ed73a5af8275a09c1a')
    m = r.json()
    print(m)
    with open('quizjson2/g.json', 'a') as file:
        json.dump(r.json(), file, indent=2, ensure_ascii=False)
        file.write(',')

#file = open('responce_quiz.json', 'a')
#file.write(']')

