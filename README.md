# Chess AI Minimax Project
### Benjamin Wolff


## Introduction
This project was my implementation of a chess-playing Minimax AI (with Alpha-Beta pruning).

The only code I am responsible for is the code in [`AI.py`](AI.py), and some small modifications I made to [`chess.py`](chess.py) and [`board.py`](board.py). 
I used this existing project to test my knowledge and implementation of the Minimax algorithm, 
combining my passion for artificial intelligence with my love of chess.

I am not responsible for any other features of the code (the chess engine, GUI, etc.).
The existing code is available in the repository here: https://github.com/aiatuci/ChessAI.

## How to Set Up and Play Against the Agent
Follow the directions in the [README file](https://github.com/aiatuci/ChessAI#readme) of the linked repo 
 to set up the virtual environment:

However, instead of running
```
pip3 install -r requirements
```

from the command line, you should run:

```
pip3 install -Iv pygame==2.01
pip3 install -Iv pygame-menu==3.5.8
```
since the most updated versions of pygame-menu are not compatible with the chess engine.

## Some Notes About the Work
* Based on the nature of the engine and the algorithm, this minimax AI 
may take a while to make a move, even with the alpha-beta pruning that should decrease the time taken
   * With a depth of 3, each of the AI's move may take up to 20 seconds
* Based on the evaluation function (which simply measures material advantage), the agent has limitations on its abilities, especially with moves early in the game
    * A better and more accurate heuristic evaluation function based on chess knowledge could lead to improvements
    * Similarly, using a higher depth may lead to stronger moves
* The depth can be adjusted by changing the number 3 (default) in line 136 of [`chess.py`](chess.py)

