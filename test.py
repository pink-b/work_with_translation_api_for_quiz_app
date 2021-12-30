from googletrans import Translator
import json

translator = Translator()
translation = translator.translate('build', dest='ru', src = 'en')
translation_2 = translator.detect('строить')
t = translator.detect(data['questions'][0])
print(translation_2.lang)
print(translation.text)
print(type(translation_2.lang))
'''data = json.load(open('quizjson/Animals.json'))
str = list(data['questions'][0]['incorrect_answers'][j]['answer'] for j in range(len(data['questions'][0]['incorrect_answers'])))
print(str)'''