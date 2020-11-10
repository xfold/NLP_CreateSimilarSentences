# Create similar sentences
This repository contains a simple wrapper built on top of the googletranslate pytohn library to generate similar sentences.
Given a sentence in any language, SentenceCreator generates similar sentences by leveraging the googletranslation library.
The algorithm translates the original sentence to another language (up to `seqdepth` times), and then back to the original language. This results in similar but not exactly lexically equivalent sentences.

For instance, this is the process used to generate a similar sentence to `The house is on fire, call the firemen!'`:
```
(original, en) 'The house is on fire, call the firemen!'
(first translation, es) '¡La casa está en llamas, llama a los bomberos!'
(translate back to original lan, en) '¡The house is on fire, call the fire department!' (en, final)
>output: '¡The house is on fire, call the fire department!' 
```

This appraoch can be useful to generate new data for undersampled classes (the original idea that motivated this repository), or to create similar responses for e.g.automated decision systems or Chatbots. Also, this code was inspired after reading an article on [hanlding imbalanced data](https://www.analyticsvidhya.com/blog/2020/11/handling-imbalanced-data-machine-learning-computer-vision-and-nlp/).


## Table of contents
* [Installation and Requirements](#Installation-and-Requirements)
* [Usage](#Usage)

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
There are some parameters that can be used to configure the execution of the `SentenceCreator`, listed and described next:
<ul>
     <li>aa</li>
     <li>bb</li>
</ul>
        
   originalsentence <str> : Sentence for which we want to generate similar sentences
   n <int> : Number of similar sentence to retrieve
   seqdepth <int> : initial number of translations before going back to original language. If `n` different sentences are not found at depth level `seqdepth`, the algorithm automatically searches for combinations of translations in deeper levels. 
   seed <int> : random seed
   caseSensitive <bool> : true will consider lowercase and uppercase sentences as different sentences. False will consider them as the same sentence.
   verbose <bool> : Defines the verbosity of the process. Set to true to understand how the solution was achieved
   maxseqdepth <int> : maximum depth to explore for similar sentences. Used as a stopping variable when different sentences can't be found in the specified conditions.

# Examples





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
