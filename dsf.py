from google_trans_new import google_translator
import ast,time,json,random,os
from googletrans import Translator
translator = Translator()
h = ['bear','panda','hello my friend nice to see you']
print(type(h))
m = translator.translate(h,dest ='ru')
print(type(m))
print(m)
m = m.replace('»','\'')
m = m.replace(' ','\'')

print(m)
m = eval(m)
print(type(m))
#print(m[0][3])

