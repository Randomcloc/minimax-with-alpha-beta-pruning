# Minimax with Alpha-Beta Pruning
This repository demonstrates the usage of the Minimax algorithm in a deterministic game of Tic Tac Toe. 



## Why Tic-Tac-Toe?

The reason this particular game was selected was because it is not only widely known, but also because, as mentioned, it is a deterministic game. A game is deterministic if the resolution of player actions leads to completely predictable outcomes. Tic-Tac-Toe, unlike something like Monopoly, has explicitly defined game states which can be evaluated for each player objectively. By selecting a deterministic game, we are ensuring that the Minimax algorithm works as it's supposed to.



## Human Vs. AI

The game is implemented in such a way that the human player always controls where the 'X' goes (and also is always to go first), and the AI is controlling where the 'O' goes. The evaluation time for the recommended move for the human player is shown as well as the X and Y co-ordinates of the move itself. It is up to the human whether they wish to listen to the algorithm or go their own way! Since it's a very simplistic game, the choices the human player makes are usually just as good as the recommended moves.



## The MiniMax Algorithm

This algorithmn works off the principle of adversarial search. This means that the algorithm assumes that the two players participating in the game are, for all intents and purposes, the perfect players. There are two functions in this algorithm: min and max. The max function wants to pick the moves that will be the best for itself and the worst for the opponent min, whereas min is doing the same, but going the other way. Min does not want Max to win and this leads to a tug-of-war between the two perfect opponents. 

In this algorithm, we make Max be the AI, and Min be the human. The algorithm assumes that the human will play the best possible move in every scenario and tries to fend off and still win against the human player (which is why it knows what the best move for the human will be as well). In a given game state, depending on whether it is Max's turn or Min's turn, ***every possible move is examined*** leading from the one game state, and the best move is picked.

If it is Max's turn, the algorithm will pick the successor state which has the highest evaluation metric. Conversely, if it is Min's turn, the algorithm will pick the state which has the lowest evaluation metric.



## The Evaluation Metric

In this simple deterministic game, it is clear that we need no weighted functions which analyzes every move deeply. A simple metric as follows will suffice: If 'X' wins, the evaluation will return -1 (since 'X', the human, is Min). If 'O' wins, the evaluation will return 1 (since the computer is Max). In case of a Tie, return 0.

The Minimax algorithm uses this evaluation metric to figure out the quality of a ply based on whose turn it is. Note that ***every successor game state*** needs to be examined in order to find the best possible move for each player.



## Alpha-Beta Pruning

