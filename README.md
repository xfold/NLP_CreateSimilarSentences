# Create similar sentences
This repository contains a simple wrapper built on top of the googletranslate pytohn library to generate similar sentences.
Given a sentence in any language, SentenceCreator generates similar sentences by leveraging the googletranslation library.
The algorithm translates the original sentence to another language (up to `seqdepth` times), and then back to the original language. This results in similar but not exactly lexically equivalent sentences.

This appraoch can be useful to generate new data for undersampled classes (the original idea that motivated this repository), or to create similar responses for e.g.automated decision systems or Chatbots.

## Table of contents
* [Installation and Requirements](#Installation-and-Requirements)
* [Virtual environment](#(optional)-Create-a-virtual-environment)
* [About error "'NoneType' object has no attribute 'group'"](#About-error-"'NoneType'-object-has-no-attribute-'group'")




# Installation and Requirements
Use the file `requirements.txt` to install all requirements using pip. A python installation >= 3.7 was used! Similar sentences are usually generated quite fast!
```
pip install -r requirements.txt
```

# (optional) Create a virtual environment
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
This is a common problem on Google's side, it happens when Google sends you directly the raw token. More on this [here](https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group)
