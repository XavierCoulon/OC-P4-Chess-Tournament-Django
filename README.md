# Chess Tournament

Openclassrooms - DA Python - Project 4:
provide an app to manage a chess Swiss tournament:
- create players, update ranking
- create tournaments, rounds, matches,
- result matches,
- display reports regarding ranking, results...

This app has been built on an MVC approach.

## 1. Installation

```bash
git clone https://github.com/XavierCoulon/OC-P4-Chess-Tournament.git
cd OC-P4-Chess-Tournament
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python main.py
```
## 2. How to use the app

The app is meant to be used from terminal. To launch the program, use the following command line.
```bash
python main.py
```


Menus:
> Home menu _(access to the menus)_ 

> Players
- create a player
- change player's ranking
> Tournament

- create a new round
- result the last round
> Reports
  - lists of players, tournaments, rounds, matches...

## 3. How to generate  a flake8-html file

```bash
flake8 --format=html --htmldir=flake-report
```
- "index.html" will be stored in folder "flake-report".