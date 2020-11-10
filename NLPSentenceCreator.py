from googletrans import Translator
import itertools
import random 


'''
SentenceCreator
Wrapper for googletranslate python library to generate similar sentences.

Given a sentence in any language, SentenceCreator generates similar sentences by leveraging the googletranslation library.
The algorithm translates the original sentence to another language (up to `seqdepth` times), and then back to the original language. This results in similar but not exactly lexically equivalent sentences.
This appraoch might be useful to generate new data for undersampled classes (which was the idea that motivated this work)

Example: 
    e.g. for [en]->[es]->[en]
    'The house is on fire, call the firemen!' (en) -> '¡La casa está en llamas, llama a los bomberos!' (es) -> 
    '¡The house is on fire, call the fire department!' (en, final)

Usage:
    import NLPSentenceCreator
    sc = NLPSentenceCreator.SentenceCreator()
    sentence = 'The house is on fire, call the firemen!'
    sc.CreateSimilarSentences(sentence)
    
    
    >{'The house is burning, call the firefighters!',
     'The house is lit, call the firefighters!',
     'The house is on fire, call the fire department!',
     'The house is on fire, call the fireman!',
     'The house is on fire, call the firemen!'}

Params for CreateSimilarSentences:
   originalsentence <str> : Sentence for which we want to generate similar sentences
   n <int> : Number of similar sentence to retrieve
   seqdepth <int> : initial number of translations before going back to original language. If `n` different sentences are not found at depth level `seqdepth`, the algorithm automatically searches for combinations of translations in deeper levels. 
   seed <int> : random seed
   caseSensitive <bool> : true will consider lowercase and uppercase sentences as different sentences. False will consider them as the same sentence.
   verbose <bool> : Defines the verbosity of the process. Set to true to understand how the solution was achieved
   maxseqdepth <int> : maximum depth to explore for similar sentences. Used as a stopping variable when different sentences can't be found in the specified conditions.
   
xfold
Nov 2020
'''
class SentenceCreator:
    def __init__(self):
        self.swaplangs = ['it','es','hu','fr','bg','af','ar','pa','de','el'] 
        self.translator = Translator()
        
        
    def _generateCombos(self, depth = 1, langList = None, seed = None):
        if(seed is not None):
            random.seed(seed)
        if(langList is None):
            langList = self.swaplangs
        combs = list(itertools.combinations(langList, depth))
        return combs
            
    def CreateSimilarSentences(self, originalsentence, 
                               seqdepth = 1, 
                               n = 5, 
                               seed = None, 
                               caseSensitive = False, 
                               verbose = False,
                               maxseqdepth = 4):

        try:
            originallan = self.translator.detect(originalsentence)
            if(verbose): print('Original language', originallan.lang)
        except Exception as ex:
            print('[!] Error, please try again', ex)
            return 

        tor = set([])
        samplescombs = set([])

        currentdepth = seqdepth
        while(len(tor)<n):
            
            #stopping breakpoint in case we get to this depth
            if(currentdepth>=maxseqdepth):
                print('Maxdepth stopping threshold (',maxseqdepth,') activated, stopping search. It could be that the sentence\
                       you are trying to translate is too short and translations are very similar. If you want to search\
                       deeper, increase the stopping threshold `maxseqdepth`.')
                break
            
            
            selcombs = self._generateCombos(depth = currentdepth, langList = self.swaplangs, seed = seed)
            if(verbose): print('generated combos', selcombs)

            for i in range(len(selcombs)):
                cs = random.choice(selcombs)
                del selcombs[selcombs.index(cs)]
                if(verbose): print('>Selected', cs)

                sentence = originalsentence
                for c in cs:
                    try:
                        sentence = self.translator.translate(sentence, dest=c)
                        sentence = sentence.text
                        if(verbose): print('\t[',c,'] Sentence ', sentence)
                    except Exception as ex:
                        print('[!?] Ignored error', ex)
                        continue
                        
                #sentence here is the results of applying the 'n' translations presneted in cs
                try:
                    sentence = self.translator.translate(sentence, dest=originallan.lang)
                    sentence = sentence.text
                    
                    if(not caseSensitive): sentence = sentence.lower()
                    if(verbose): print('\tFINAL [',originallan.lang,'] Sentence ', sentence)
                    tor.add(sentence)
                    if(len(tor)==n):
                        return tor
                except Exception as ex:
                    print('[!?] Ignored error', ex)
                    continue

            #if we get here, means that we already explored all combos for currentdepth,
            #... lets go deeper!
            currentdepth +=1    
            
            
            
        return tor

 # ALLLANGUAGES = {'af': 'afrikaans','sq': 'albanian','am': 'amharic','ar': 'arabic','hy': 'armenian','az': 'azerbaijani','eu': 'basque','be': 'belarusian','bn': 'bengali','bs': 'bosnian','bg': 'bulgarian','ca': 'catalan','ceb': 'cebuano','ny': 'chichewa','zh-cn': 'chinese (simplified)','zh-tw': 'chinese (traditional)','co': 'corsican','hr': 'croatian','cs': 'czech','da': 'danish','nl': 'dutch','en': 'english','eo': 'esperanto','et': 'estonian','tl': 'filipino','fi': 'finnish','fr': 'french','fy': 'frisian','gl': 'galician','ka': 'georgian','de': 'german','el': 'greek','gu': 'gujarati','ht': 'haitian creole','ha': 'hausa','haw': 'hawaiian','iw': 'hebrew','he': 'hebrew','hi': 'hindi','hmn': 'hmong','hu': 'hungarian','is': 'icelandic','ig': 'igbo','id': 'indonesian','ga': 'irish','it': 'italian','ja': 'japanese','jw': 'javanese','kn': 'kannada','kk': 'kazakh','km': 'khmer','ko': 'korean','ku': 'kurdish (kurmanji)','ky': 'kyrgyz','lo': 'lao','la': 'latin','lv': 'latvian','lt': 'lithuanian','lb': 'luxembourgish','mk': 'macedonian','mg': 'malagasy','ms': 'malay','ml': 'malayalam','mt': 'maltese','mi': 'maori','mr': 'marathi','mn': 'mongolian','my': 'myanmar (burmese)','ne': 'nepali','no': 'norwegian','or': 'odia','ps': 'pashto','fa': 'persian','pl': 'polish','pt': 'portuguese','pa': 'punjabi','ro': 'romanian','ru': 'russian','sm': 'samoan','gd': 'scots gaelic','sr': 'serbian','st': 'sesotho','sn': 'shona','sd': 'sindhi','si': 'sinhala','sk': 'slovak','sl': 'slovenian','so': 'somali','es': 'spanish','su': 'sundanese','sw': 'swahili','sv': 'swedish','tg': 'tajik','ta': 'tamil','te': 'telugu','th': 'thai','tr': 'turkish','uk': 'ukrainian','ur': 'urdu','ug': 'uyghur','uz': 'uzbek','vi': 'vietnamese','cy': 'welsh','xh': 'xhosa','yi': 'yiddish','yo': 'yoruba','zu': 'zulu'}

        