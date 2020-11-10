# NLP_HandlingImbalancedData
Some solutions to handle/create imbalanced classes in NLP

# Installation and Requirements (python >= 3.7)
### 1. Create the virtual environment and requirements.txt file
First, create a virtual environment using python3.7 (or higher) to not mess with the local python libraries. The virtual environment is not included in the project because of size. To do so in bash:
```bash
python -m venv .venv
source .venv/bin/activate
```
And in powershell:
```powershell
py -m venv .venv
.venv\scripts\activate
```
Once the virtual enviroment is created, we can install the project requirements included in the file `requirements.txt` using `pip`:
```
pip install -r requirements.txt
```

# About error "'NoneType' object has no attribute 'group'"
This is a common problem on Google's side, it happens when Google sends you directly the raw token. More on this [here](https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group)
