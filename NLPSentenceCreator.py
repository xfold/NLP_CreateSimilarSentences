from googletrans import Translator
import itertools
import random 

   # LANGUAGES = {'af': 'afrikaans','sq': 'albanian','am': 'amharic','ar': 'arabic','hy': 'armenian','az': 'azerbaijani','eu': 'basque','be': 'belarusian','bn': 'bengali','bs': 'bosnian','bg': 'bulgarian','ca': 'catalan','ceb': 'cebuano','ny': 'chichewa','zh-cn': 'chinese (simplified)','zh-tw': 'chinese (traditional)','co': 'corsican','hr': 'croatian','cs': 'czech','da': 'danish','nl': 'dutch','en': 'english','eo': 'esperanto','et': 'estonian','tl': 'filipino','fi': 'finnish','fr': 'french','fy': 'frisian','gl': 'galician','ka': 'georgian','de': 'german','el': 'greek','gu': 'gujarati','ht': 'haitian creole','ha': 'hausa','haw': 'hawaiian','iw': 'hebrew','he': 'hebrew','hi': 'hindi','hmn': 'hmong','hu': 'hungarian','is': 'icelandic','ig': 'igbo','id': 'indonesian','ga': 'irish','it': 'italian','ja': 'japanese','jw': 'javanese','kn': 'kannada','kk': 'kazakh','km': 'khmer','ko': 'korean','ku': 'kurdish (kurmanji)','ky': 'kyrgyz','lo': 'lao','la': 'latin','lv': 'latvian','lt': 'lithuanian','lb': 'luxembourgish','mk': 'macedonian','mg': 'malagasy','ms': 'malay','ml': 'malayalam','mt': 'maltese','mi': 'maori','mr': 'marathi','mn': 'mongolian','my': 'myanmar (burmese)','ne': 'nepali','no': 'norwegian','or': 'odia','ps': 'pashto','fa': 'persian','pl': 'polish','pt': 'portuguese','pa': 'punjabi','ro': 'romanian','ru': 'russian','sm': 'samoan','gd': 'scots gaelic','sr': 'serbian','st': 'sesotho','sn': 'shona','sd': 'sindhi','si': 'sinhala','sk': 'slovak','sl': 'slovenian','so': 'somali','es': 'spanish','su': 'sundanese','sw': 'swahili','sv': 'swedish','tg': 'tajik','ta': 'tamil','te': 'telugu','th': 'thai','tr': 'turkish','uk': 'ukrainian','ur': 'urdu','ug': 'uyghur','uz': 'uzbek','vi': 'vietnamese','cy': 'welsh','xh': 'xhosa','yi': 'yiddish','yo': 'yoruba','zu': 'zulu'}

class SentenceCreator:
    def __init__(self):
        self.swaplangs = ['it','es','hu','fr','bg','ca','af','ar','pa','de','el'] 
        self.translator = Translator()
    
    
    def SimilarSentences(self, originalsentence, seqdepth = 1, n = 10, seed = None):
        if(seed is not None):
            random.seed(seed)
            
        combs = [[k] for k in self.swaplangs]
        if(seqdepth>1):
            combs = list(itertools.combinations(self.swaplangs, seqdepth))
        if(n > len(combs)):
            n = len(combs)

        
        originallan = self.translator.detect(originalsentence)
        print('original language', originallan.lang)
        selcombs = random.sample(combs, n)
        tor = []
        print(selcombs)
        print('original snetence: ',originalsentence)
        for combs in selcombs:
            sentence = originalsentence
            for c in combs:
                print('processing', c)
                sentence = self.translator.translate(sentence, dest=c)
                sentence = sentence.text
                print('\t',sentence)
            print('back to english', originallan.lang, ':', sentence )
            sentence = self.translator.translate(sentence, dest=originallan.lang)
            tor.append(sentence.text)
        return tor
        