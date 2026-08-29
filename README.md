# CodSoft Artificial Intelligence Internship

This repository contains the projects completed as part of my Artificial Intelligence internship at CodSoft.

## Internship Tasks

- [x] Task 1 - Rule-Based Chatbot
- [x] Task 2 - Tic-Tac-Toe AI
- [x] Task 3 - Image Captioning

---

## Task 1 - Rule-Based Chatbot

### Project Description

A simple rule-based chatbot developed using Python. The chatbot interacts with the user through the terminal and provides predefined responses based on the user's input.

### Features

- Responds to greetings
- Responds to basic questions
- Provides information about the chatbot
- Handles thank-you messages
- Allows the user to exit the conversation
- Uses predefined rules and pattern matching

### Technologies Used

- Python
- Functions
- Conditional statements
- String processing
- While loop

### How to Run

    python Task1_Chatbot/chatbot.py

---

## Task 2 - Tic-Tac-Toe AI

### Project Description

A console-based Tic-Tac-Toe game where a human player competes against an AI opponent. The AI uses the Minimax algorithm to evaluate possible moves and select the best move.

### Features

- Human vs AI gameplay
- Player uses X
- AI uses O
- Minimax algorithm for AI decision-making
- Detects wins
- Detects draws
- Checks invalid moves
- Option to play again

### Technologies Used

- Python
- Minimax algorithm
- Functions
- Conditional statements
- Loops

### How to Run

    python Task2_TicTacToe/tic_tac_toe.py

---

## Task 3 - Image Captioning

### Project Description

An AI-based image captioning application that analyzes an image and generates a natural-language description of its content using a pre-trained BLIP image captioning model.

### Features

- Accepts an image file path
- Analyzes the image using a pre-trained AI model
- Generates a descriptive caption
- Handles invalid image paths
- Allows multiple images to be processed
- Provides an option to exit the program

### Technologies Used

- Python
- PyTorch
- Transformers
- Torchvision
- Pillow
- BLIP pre-trained image captioning model

### How to Run

First install the required libraries:

    pip install transformers torch torchvision pillow

Then run:

    python Task3_ImageCaptioning/image_captioning.py

Enter the path of an image when prompted.

### Example

    Enter the path of an image:
    C:\Users\Vaibhav\Downloads\cat.webp

    Generated Caption:
    a cat with blue eyes laying on a bed

---

## Repository Structure

    CODSOFT_TASKSNO
    │
    ├── Task1_Chatbot
    │   └── chatbot.py
    │
    ├── Task2_TicTacToe
    │   └── tic_tac_toe.py
    │
    ├── Task3_ImageCaptioning
    │   └── image_captioning.py
    │
    └── README.md

## Internship

These projects were completed as part of the CodSoft Artificial Intelligence Internship.
