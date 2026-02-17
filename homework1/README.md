# CS4300 – Homework 1

## Project layout

```
homework1/
├── src/
│   ├── task1.py   # Hello World
│   ├── task2.py   # Variables & Data Types
│   ├── task3.py   # Control Structures
│   ├── task4.py   # Functions & Duck Typing
│   ├── task5.py   # Lists & Dictionaries
│   ├── task6.py   # File Handling
│   └── task7.py   # Package Management (requests)
├── tests/
│   ├── test_task1.py
│   ├── test_task2.py
│   ├── test_task3.py
│   ├── test_task4.py
│   ├── test_task5.py
│   ├── test_task6.py
│   └── test_task7.py
├── task6_read_me.txt
├── pyproject.toml
└── README.md       ← you are here
```

## Setup

```bash
# 1. Activate your virtual environment (run this every time you open a container)
source ~/myEnvironment/bin/activate

# 2. Install dependencies
pip install pytest requests
```

## Running the scripts

```bash
# From the homework1/ directory:
python src/task1.py
python src/task2.py
# ... and so on
```

## Running all tests

```bash
# From the homework1/ directory:
pytest
```

Run a single test file:

```bash
pytest tests/test_task3.py -v
```

## Pushing to GitHub

```bash
# From /home/student/ (after cloning your repo):
cd cs4300
git add homework1/
git commit -m "Complete homework 1"
git push origin main
```
