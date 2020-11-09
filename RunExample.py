import importlib
import NLPSentenceCreator
importlib.reload(NLPSentenceCreator)
sc = NLPSentenceCreator.SentenceCreator()

#1.1 Simple execution
sentence = 'The house is on fire, call the firemen!'
sc.CreateSimilarSentences(sentence)

#1.2 Simple params
sentence = 'The house is on fire, call the firemen!'
sc.CreateSimilarSentences(sentence, n=10, verbose=True, seed=42)

#1.3 Forcing deeper translations
sentence = 'The house is on fire, call the firemen!'
sc.CreateSimilarSentences(sentence,
                    n = 5, 
                    seqdepth=5,
                    maxseqdepth=6,
                    seed=42,
                    caseSensitive=False)

#1.4 Generate similar sentences for other languages too
sentence = '¡La casa está en llamas, llama a los bomberos!'
sc.CreateSimilarSentences(sentence,
                    n = 5, 
                    seqdepth=5,
                    maxseqdepth=6,
                    seed=42,
                    caseSensitive=False,
                    verbose = True)