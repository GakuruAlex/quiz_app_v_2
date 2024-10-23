# Quiz App #

## Description ##

This ia quiz project. The questions are fetched from Open Trivia Api with params: amount=10, category=18 and type=boolean. Its a True or False system. True is marked by a button with "✓" and False with "x". If the answer is correct the canvas changes to green else red before the next question and score is increased by one.

![Quiz App](images/Quiz_app.png)

## Prerequisite ##

clone repository

```bash
git clone https://github.com/GakuruAlex/quiz_app_v_2.git
```

Change to project dir

```bash
cd quiz_app_v_2
```

Create virtual environment in the project dir

```bash
python -m venv env_name
```

Activate env

```bash
source env_name/bin/activate    #On macOs and Linux
```

```bash
env_name\Scripts\activate #0n Windows
```

## Installation ##

Run

```bash
pip install -r requirements.txt
```

## Usage ##

From the project dir rin the terminal un

```bash
python main.py
```

## Authors ##

[Gakuru Alex](https://github.com/GakuruAlex)

## License ##

This project is licensed under the terms of the MIT license. See LICENSE.md
