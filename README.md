# Tic-Tac-Toe AI

This project implements a Tic-Tac-Toe game with an AI that plays optimally using the Minimax algorithm.

## Table of Contents
- [Description](#description)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Functions](#functions)
- [Outcomes](#outcomes)
- [License](#license)

## Description
This project involves developing a Tic-Tac-Toe game where players can compete against an AI. The AI uses the Minimax algorithm to make optimal moves. The graphical interface allows users to interact with the game easily.

## Technologies Used
- Python 3.11
- Pygame
- Minimax Algorithm

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/tic-tac-toe-ai.git
    ```
2. Navigate to the project directory:
    ```sh
    cd tic-tac-toe-ai
    ```
3. Ensure you have Python 3.11 installed. If not, download and install it from [Python's official website](https://www.python.org/downloads/).
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. To start the game, run:
    ```sh
    python runner.py
    ```
2. Play against the AI using the graphical interface that appears.

## Project Structure
- `runner.py`: Contains the code to run the graphical interface for the game.
- `tictactoe.py`: Contains all of the logic for playing the game and making optimal moves.
- `requirements.txt`: Contains the list of packages required for the project.

## Functions
- **player(board)**: Returns which player's turn it is (X or O).
- **actions(board)**: Returns a set of all possible actions that can be taken on the board.
- **result(board, action)**: Returns a new board state after taking the given action.
- **winner(board)**: Returns the winner of the game if there is one.
- **terminal(board)**: Returns a boolean indicating whether the game is over.
- **utility(board)**: Returns the utility of the board (1 if X wins, -1 if O wins, 0 if tie).
- **minimax(board)**: Returns the optimal move for the current player.

## Outcomes
- Developed an AI that plays Tic-Tac-Toe optimally.
- Ensured immutability of game states to facilitate Minimax algorithm's efficiency.
- Created a user-friendly graphical interface for the game.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
