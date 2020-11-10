# Create similar sentences
This repository contains a simple wrapper built on top of the googletranslate pytohn library to generate similar sentences.
Given a sentence in any language, SentenceCreator generates similar sentences by leveraging the googletranslation library.
The algorithm translates the original sentence to another language (up to `seqdepth` times), and then back to the original language. This results in similar but not exactly lexically equivalent sentences.

For instance, this is the process used to generate a similar sentence to `The house is on fire, call the firemen!'`:
```
(original, en) 'The house is on fire, call the firemen!'
(first translation, es) '¡La casa está en llamas, llama a los bomberos!'
(translate back to original lan, en) '¡The house is on fire, call the fire department!' 
>output: '¡The house is on fire, call the fire department!' 
```
Sentences are translated to a random language selected form the set of available languages. If not enough different sentences are obtained after the translation process, the algorithm automatically concatenates a random number of translations in order to obtain new ones. Following previous example, that could be:
```
(original, en) 'The house is on fire, call the firemen!'
(first translation, es) '¡La casa está en llamas, llama a los bomberos!'
(second translation, de) 'Das Haus brennt, rufen Sie die Feuerwehr!'
...
(after n translations)
...
(translate back to original lan, en) '¡The house is burning, call the fire department!'
>output: '¡The house is on fire, call the fire department!' 
```

This appraoch can be useful to generate new data for undersampled classes (the original idea that motivated this repository), or to create similar responses for e.g.automated decision systems or Chatbots. Also, this code was inspired after reading an article on [hanlding imbalanced data](https://www.analyticsvidhya.com/blog/2020/11/handling-imbalanced-data-machine-learning-computer-vision-and-nlp/).


## Table of contents
* [Installation and Requirements](#Installation-and-Requirements)
* [Usage](#Usage)
* [Examples](#Examples)
* [Virtual environment](#Create-a-virtual-environment)
* [About error "'NoneType' object has no attribute 'group'"](#About-error-NoneType-object-has-no-attribute-group)

# Installation and Requirements
Use the file `requirements.txt` to install all requirements using pip. A python installation >= 3.7 was used! Similar sentences are usually generated quite fast!
```
pip install -r requirements.txt
```

# Usage
To use the library, is as simple as creating a `SentenceCreator` object and ask for similar sentences:
``
import NLPSentenceCreator
sc = NLPSentenceCreator.SentenceCreator()
sentence = 'The house is on fire, call the firemen!'
sc.CreateSimilarSentences(sentence)
>output:{'The house is burning, call the firefighters!',
     'The house is lit, call the firefighters!',
     'The house is on fire, call the fire department!',
     'The house is on fire, call the fireman!',
     'The house is on fire, call the firemen!'}
``
## Params:
There are various parameters that can be passed to `CreateSimilarSentences` function and that modify its execution. Optional parameters are found in between parenthesis:
<ul>
     <li>originalsentence:str :- Sentence for which we want to generate similar sentences</li>
     <li>(n:int) :- Number of similar sentence to retrieve. The sentence generator will run until it generated `n` unique sentences or the `maxseqdepth` threshold is reached.</li>
     <li>(seed:int) :- seed for the random generator.</li>
     <li>(caseSensitive:bool) :- If True lowercase and uppercase sentences are considered different sentences. If false, otherwise.</li>
     <li>(verbos:bool:) :- Defines the verbosity of the process. Set this to True to get a full printed log of the process.</li>
     <li>(seqdepth:int) :- number of translations performed before going back to original language. If `n` different sentences are not found at depth level `seqdepth`, the algorithm automatically searches for combinations of languages to create new translations. For instance, default searches are performed at `seqdepth=1` (meaning only one trasnlation is performed before re-translating the sentence to the original language, as in the example [en]->[es]->[en]). Setting `seqdepth=2` will result in two consecutive random translations, which may result in different original sentences, e.g. [en]->[es]->[de]->[en]. </li>
     <li>(maxseqdepth:int) :- Maximum depth to explore for similar sentences. Used as a stopping variable when the goal can't be found in the specified conditions.</li>
</ul>
       

# Examples
All examples are included in the the jupyter notebook `RunExamples.ipynb` included in the project. Here I include some of them:
## Simple example
```
import NLPSentenceCreator
sc = NLPSentenceCreator.SentenceCreator()
sentence = 'The house is on fire, call the firemen!'
sc.CreateSimilarSentences(sentence, n=10, seed=42)

output:
     [Out] : {'the house is burning, call the firefighters!',
     'the house is burning, the firefighters are calling!',
     'the house is lit, call the firefighters!',
     'the house is on fire, call the fire department!',
     'the house is on fire, call the firefighter!',
     'the house is on fire, call the firefighters!',
     'the house is on fire, call the fireman!',
     'the house is on fire, call the firemen!',
     'the house is on fire, firefighters are calling!',
     'the house is on fire, the firefighters are calling!'}
```
## Simple verbose example
Simple example erquesting for 10 similar sentences, using verbose and specifying a seed value 
```
import NLPSentenceCreator
sc = NLPSentenceCreator.SentenceCreator()
sentence = 'The house is on fire, call the firemen!'
sc.CreateSimilarSentences(sentence, n=10, verbose=True, seed=42)
>output:
     Original language en
     generated combos [('it',), ('es',), ('hu',), ('fr',), ('bg',), ('af',), ('ar',), ('pa',), ('de',), ('el',)]
     >Selected ('es',)
          [ es ] Sentence  ¡La casa está en llamas, llama a los bomberos!
          FINAL [ en ] Sentence  the house is on fire, call the fire department!
     >Selected ('it',)
          [ it ] Sentence  La casa sta andando a fuoco, chiamate i pompieri!
          FINAL [ en ] Sentence  the house is on fire, call the firemen!
     ...
     
     [Out] : {'the house is burning, call the firefighters!',
     'the house is burning, the firefighters are calling!',
     'the house is lit, call the firefighters!',
     'the house is on fire, call the fire department!',
     'the house is on fire, call the firefighter!',
     'the house is on fire, call the firefighters!',
     'the house is on fire, call the fireman!',
     'the house is on fire, call the firemen!',
     'the house is on fire, firefighters are calling!',
     'the house is on fire, the firefighters are calling!'}
```
## Example using another language
In this example we start with a Spanish sentence, and define we are interested in translations of depth 5 (`seqdepth=5`) and not case sensitive (`caseSensitive=False`). As we see, the results are also provided in the sentence's original language.
```
import NLPSentenceCreator
sc = NLPSentenceCreator.SentenceCreator()
sentence = '¡La casa está en llamas, llama a los bomberos!'
sc.CreateSimilarSentences(sentence,
                    n = 5, 
                    seqdepth=5,
                    maxseqdepth=6,
                    seed=42,
                    caseSensitive=False,
                    verbose = True)
output: 
     Original language es
     generated combos [('it', 'es', 'hu', 'fr', 'bg'), ('it', 'es', 'hu', 'fr', 'af'), ('it', 'es', 'hu', 'fr', 'ar'), ('it', 'es', 'hu', 'fr', 'pa'), ('it', 'es', 'hu', 'fr', 'de'), .......... 
     ...
     >Selected ('it', 'hu', 'bg', 'af', 'pa')
          [ it ] Sentence  La casa è in fiamme, chiama i vigili del fuoco!
          [ hu ] Sentence  A ház ég, hívja a tűzoltókat!
          [ bg ] Sentence  Къщата гори, обадете се на пожарникарите!
          [ af ] Sentence  Die huis brand, skakel die brandweer!
          [ pa ] Sentence  ਘਰ ਨੂੰ ਅੱਗ ਲੱਗੀ ਹੋਈ ਹੈ, ਫਾਇਰ ਵਿਭਾਗ ਨੂੰ ਬੁਲਾਓ!
          FINAL [ es ] Sentence  ¡la casa está en llamas, llame a los bomberos!
     >Selected ('it', 'hu', 'fr', 'af', 'el')
          [ it ] Sentence  La casa è in fiamme, chiama i vigili del fuoco!
          [ hu ] Sentence  A ház ég, hívja a tűzoltókat!
          ...
     ...
     ...
     [Out] : {'la casa está en llamas, ¡llama a los bomberos!',
      '¡la casa está en llamas, apaga el fuego! ¡llame al departamento!',
      '¡la casa está en llamas, el fuego se está apagando! ¡llame al departamento!',
      '¡la casa está en llamas, llama al bombero!',
      '¡la casa está en llamas, llame a los bomberos!'}

```

# Create a virtual environment
It is often recommended to create a virtual environment before installing any new libraries or a github repository to not mess with your python installations. Here I used python3.7 to not mess with the local python libraries before installing the new python libs. Short cheatsheet in bash:
```bash
python -m venv .venv
source .venv/bin/activate
```
And in powershell:
```powershell
py -m venv .venv
.venv\scripts\activate
```
To exit the venv, just type `deactivate`.

# About error "'NoneType' object has no attribute 'group'"
This is a common problem on Google's side; it happens when Google sends you directly the raw token. More on this [here](https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group)
