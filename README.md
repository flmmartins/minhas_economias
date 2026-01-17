# How to run

Instal python 3.11

Installing with pyenv:

```
pyenv install 3.11
pyenv locall 3.11
```

Setup virtual environment:

```
pyenv virtualenv minhaseconomias
pyenv activate minhaseconomias
```

Install

```
pip install -r requirements.txt
```

Run

```
python3 convert.py
```

# How to generate requirements.txt


```
pip install pip-tools
```

Edit requirements.in and then generate requirements.txt

```
pip-compile
```

# How to upgrade python

Change Pipfile to version


```
 brew upgrade pipenv
 pipenv --python 3.11
 pip install pipenv
 pipenv update
 pipenv upgrade

```
