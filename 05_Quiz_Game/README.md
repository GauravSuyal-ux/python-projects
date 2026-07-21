# Python Quiz Game

A simple terminal-based Quiz Game built using Python. This project asks the user multiple-choice style questions (text-based answers), checks the answers, keeps track of the score, allows the user to replay the quiz, and shuffles the questions each time for a better experience.

This project was built as part of my Python Beginner Projects series to practice functions, loops, lists, input validation, and program flow.

---

# Features

 Menu-driven interface
 Multiple quiz questions stored in a nested list
 Answer validation (case-insensitive)
 Score tracking
 Displays final score out of total questions
 Question numbering using `enumerate()`
 Replay feature with input validation
 Random question order using `random.shuffle()`
 Input validation using `try-except`

---

# Technologies Used

- Python 3

---

# Project Structure

```
05_Quiz_Game/
│
├── quiz_game.py
└── README.md
```

---

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/python-projects.git
```

2. Navigate to the project folder:

```bash
cd python-projects/05_Quiz_Game
```

3. Run the program:

```bash
python quiz_game.py
```

---

# Sample Output

```
====== Python Quiz ======

1. Start Quiz
2. Exit

Please enter your choice: 1

Question 1:
Which state is known as Devbhoomi?
Enter your answer: uttarakhand
Correct!

Question 2:
Which city is known as Pink City?
Enter your answer: jaipur
Correct!

Question 3:
Which hill station is famous for Naini Lake?
Enter your answer: delhi
Incorrect!
The correct answer is: nainital

Your final score is: 2/3

Do you want to play again? (y/n):
```

---

# Concepts Practiced

- Variables
- Lists & Nested Lists
- Functions
- Function Parameters
- Return Values
- `if`, `elif`, `else`
- `while` loops
- `for` loops
- `enumerate()`
- `len()`
- `random.shuffle()`
- `try-except`
- Input Validation
- String Methods (`lower()`, `strip()`)

---

# Future Improvements

- Load questions from a file
- Add categories
- Add difficulty levels
- Support multiple-choice questions
- Display percentage score
- Timer for each question
- Store high scores

---

# Learning Outcome

This project helped me practice:

- Writing reusable functions
- Organizing program flow
- Using nested lists to store data
- Implementing replay functionality
- Validating user input
- Working with Python's `random` module
- Building a complete terminal-based application

---

## Author

**Gaurav Suyal**

GitHub: https://github.com/GauravSuyal-ux