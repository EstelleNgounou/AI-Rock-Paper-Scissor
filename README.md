Rock, Paper, Scissors with AI
Welcome to the Rock, Paper, Scissors game with AI! In this game, you can play against a simple AI 
that learns from your previous moves and attempts to predict and counter your next move using a 
basic probability-based machine learning approach.

How to Play
When you start the game, you will be prompted to enter your name.
The AI will then ask if you'd like to play a round of Rock, Paper, Scissors.
After entering your choice (rock, paper, or scissors), the AI will randomly select its move in the beginning.
Once there are more than 3 moves in the game, the AI will start tracking your previous choices and try to predict your next move using probabilities.
The AI will counter your most frequent move in the past by selecting the winning choice against it.
You can keep playing until you choose to stop the game.
How Machine Learning is Implemented
Basic Machine Learning Approach:
In this game, the "machine learning" implementation is quite basic and works by 
observing your choices over time and calculating the probability of each move (rock, paper, or scissors).

Data Collection: Each time you make a move, your choice is stored in a list (userlist).

Probability Calculation: After each move, the AI tracks how many times you've chosen rock, paper, or scissors. This is done by counting 
the occurrences of each move in the userlist and calculating the probabilities for each one.

For example, if you've chosen rock 3 times, paper 2 times, and scissors 1 time, the AI calculates the probability of each move as:

Probability of rock = 3/6 (50%)
Probability of paper = 2/6 (33.3%)
Probability of scissors = 1/6 (16.7%)
Prediction and Counter: Once enough data is collected (more than 3 moves), the AI predicts your next move based on the most 
frequent choice you've made. It then selects the counter move to beat your most frequent move. For example:

If you choose rock most often, the AI will play paper (which beats rock).
If you choose paper most often, the AI will play scissors.
If you choose scissors most often, the AI will play rock.
Limitations:
The AI's strategy is based purely on probabilities and will only become effective after a few rounds of play.
Early on, the AI plays randomly until it gathers enough data.
The machine learning part is very simple, and the AI doesn't "learn" dynamically over time or adjust to 
new strategies beyond the current session.

Feel free to play and beat the AI!
