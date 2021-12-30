import json,time,random
import os
from google_trans_new import google_translator
#from  googletrans  import  Translator
LANGUAGES = {
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'he': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'or': 'odia',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'ug': 'uyghur',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu'}
def my_translator2(file,lang,m=0):
    directory = os.listdir(file)
    directory.sort()

    if not os.path.exists(os.path.abspath(file + '-' + lang)):
        os.mkdir(file + '-' + lang)

    directory_translations = os.listdir(file + '-' + lang)
    #ориентируется с какого файла нужно начинать перевод при запуске программы
    if len(directory_translations) != 0:
        directory_translations.sort()
        dir_len = json.load(open(file + '/' + directory_translations[-1]))
        dir_len = len(dir_len['questions'])

        if m < dir_len:
            g = len(directory_translations) - 1
        if m == dir_len:
            g = len(directory_translations)
    if len(directory_translations) == 0:
        g = 0

    for el in range(g, len(directory)):

        #десериализует джисун в словарь питона для разных ситуаций в программе
        if len(directory_translations) != 0:
            dir_len = json.load(open('quizjson/' + directory_translations[-1]))
            dir_len = len(dir_len['questions'])
            if m < dir_len:
                data = json.load(open(file + '-' + lang + '/' + directory[el]))
            if m == dir_len:
                data = json.load(open(file + '/' + directory[el]))
        if len(directory_translations) == 0:
            data = json.load(open(file + '/' + directory[el]))

        translator = google_translator()  # Первый_вызов_апи

        #обнуляем значение в save_changes если начался новый файл
        l = translator.detect(data['questions'][0]['question'])
        print(data['questions'][0]['question'])
        if l[0] != 'ru':
                m = 0
        time.sleep(random.randint(1, 7))

        while m != len(data['questions']):
                a = 0
                n = 0
                departure = {}
                while True:
                    n += len(data['questions'][m]['question'])
                    answer = data['questions'][m]['correct_answer']
                    if type(answer) != bool:
                        if not answer.isdigit():
                            n += len(answer)

                    if 'incorrect_answers' in data['questions'][m]:
                        for j in range(len(data['questions'][m]['incorrect_answers'])):
                            if type(data['questions'][m]['incorrect_answers'][j]['answer']) != bool:
                                if not data['questions'][m]['incorrect_answers'][j]['answer'].isdigit():
                                    n += len(data['questions'][m]['incorrect_answers'][j]['answer'])

                    if  a >= 4000 or (a+n) > 4000:
                        print('break')
                        break

                    h = {0:data['questions'][m]['question']}
                    if type(answer) != bool:
                        if not answer.isdigit():
                            h[1] = data['questions'][m]['correct_answer']
                    if 'incorrect_answers' in data['questions'][m]:
                        for j in range(len(data['questions'][m]['incorrect_answers'])):
                            if type(data['questions'][m]['incorrect_answers'][j]['answer']) != bool:
                                if not data['questions'][m]['incorrect_answers'][j]['answer'].isdigit():

                                    h[2] = [data['questions'][m]['incorrect_answers'][j]['answer']]
                    departure[data['questions'][m]['id']] = h
                    print(departure)


                    a += n
                    n = 0
                    m = m + 1
        print('end')

a = my_translator2('quizjson','ru')