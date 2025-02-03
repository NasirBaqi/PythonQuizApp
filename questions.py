questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0
    },
    {
        "topic": "Loops",
        "question": "What does this code output?",
        "code": "i = 1\nwhile i < 4:\n    print(i)\n    i += 1",
        "options": ["1 2 3", "0 1 2", "1 2 3 4", "Infinite loop"],
        "answer": 0
    },
    {
        "topic": "Lists",
        "question": "What is the result of this code?",
        "code": "a = [1, 2, 3]\nb = a\na.append(4)\nprint(b)",
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "[4, 2, 3]", "Error"],
        "answer": 1
    },
    {
        "topic": "Strings",
        "question": "What does this print?",
        "code": "print('hello'.capitalize())",
        "options": ["Hello", "hello", "HELLO", "Error"],
        "answer": 0
    },
    {
        "topic": "Functions",
        "question": "What will this function return?",
        "code": "def add(x, y=10):\n    return x + y\nprint(add(5))",
        "options": ["15", "5", "Error", "None"],
        "answer": 0
    },
    {
        "topic": "OOP",
        "question": "What will be the output?",
        "code": "class Test:\n    def __init__(self):\n        self.x = 5\nobj = Test()\nprint(obj.x)",
        "options": ["5", "None", "Error", "self.x"],
        "answer": 0
    }
]
