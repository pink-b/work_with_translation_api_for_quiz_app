import json,time,random,pycountry
import os
from google_trans_new import google_translator
from  googletrans  import  Translator
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
def my_translator(file,lang,m=0):
    try:
        directory = os.listdir(file)
        directory.sort()

        if not os.path.exists(os.path.abspath(file + '-' + lang)):
            os.mkdir(file + '-' + lang)

        directory_translations = os.listdir(file + '-' + lang)
        if len(directory_translations) != 0:
            directory_translations.sort()
            dir_len = json.load(open('quizjson/' + directory_translations[-1]))
            dir_len = len(dir_len['questions'])

            if m < dir_len:
                g = len(directory_translations) - 1
            if m == dir_len:
                g = len(directory_translations)
        if len(directory_translations) == 0:
            g = 0

        for el in range(g, len(directory)):
            if len(directory_translations) != 0:
                dir_len = json.load(open('quizjson/' + directory_translations[-1]))
                dir_len = len(dir_len['questions'])
                if m < dir_len:
                    data = json.load(open(file + '-' + lang + '/' + directory[el]))
                if m == dir_len:
                    data = json.load(open(file + '/' + directory[el]))
            if len(directory_translations) == 0:
                data = json.load(open(file + '/' + directory[el]))

            translator = Translator()  # Первый_вызов_апи

            l = translator.detect(data['questions'][0]['question'])
            if l[0] != 'ru':
                m = 0
            time.sleep(random.randint(1, 7))

            while m != len(data['questions']):
                question = data['questions'][m]['question']
                translated_question = translator.translate(question, lang_tgt='ru', lang_src='en')
                data['questions'][m]['question'] = translated_question

                time.sleep(random.randint(1, 7))  # Первая_пауза

                answer = data['questions'][m]['correct_answer']
                if type(answer) != bool:
                    if not answer.isdigit():
                        translator = Translator()  # Второй_вызов_апи

                        answer = translator.translate(answer, lang_tgt='ru', lang_src='en')
                        data['questions'][m]['correct_answer'] = answer

                        time.sleep(random.randint(1, 7))  # Вторая_пауза

                if 'incorrect_answers' in data['questions'][m]:
                    translated_wrong_answers = []
                    for j in range(len(data['questions'][m]['incorrect_answers'])):
                        answer = data['questions'][m]['incorrect_answers'][j]['answer']

                        translator = Translator()  # Третий_вызов_апи

                        translated_wrong_answer = translator.translate(answer, lang_tgt='ru', lang_src='en')
                        translated_wrong_answers.append(translated_wrong_answer)

                        time.sleep(random.randint(1, 10))  # Третья_пауза

                        for k in range(len(translated_wrong_answers)):
                            data['questions'][m]['incorrect_answers'][j]['answer'] = translated_wrong_answers[j]
                with open(file + '-' + lang + '/' + directory[el], 'w') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(data['questions'][m])
                m += 1
                with open('save_changes.txt', 'w') as u:
                    u.write(str(m))
    except:
        my_translator('quizjson', 'ru', int(m))
        print("restart")

with open('save_changes.txt') as p:
    lines = p.readlines()

m = int(lines[0])
print(m)

my_translator('quizjson','ru', int(m))