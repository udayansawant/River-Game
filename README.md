# River-Game

# Introduction
It is an interactive Python game application that runs in the command line or terminal based on your OS. It starts by authenticating users and prompts the user for a 2D matrix input of 1's representing river & 0's representing land.

# Project Contents

* **welcome_note.txt** - is the text file containing the welcome note displayed at the beginning of the game
* **game_instructions.txt** - is the text file containing the instructions for the game.
* **Task_Training_Data.csv** - is the CSV file containing all the registered users
* **read_csv.py** - contains a single function which read the user information from the Task_Training_Data.csv file
* **authenticate_data.py** - imports the registered users from read_csv.py and contains multiple functions described below:
  * authenticate_user(): authenticates the users by prompting the user for a name and email to matches with registered users
  * show_welcome_note(): displays the welcome note if the users get into the game
  * show_game_instruction(): displays the game instructions if the user wants to play
  * get_matrix_input(): prompts the user to input a 2D matrix of 1's and 0's
* **game_functionality.py** - imports the 2D matrix input from authenticate_data.py and contains two functions to perform the game logic as described below:
  * find_river_size(): takes the 2D matrix as input and find the river sizes using a BFS(breadth-first search) algorithm.
  * guess_the_river_sizes(): takes the river_size array as input and prompt the user to guess the river size at each index. The user guesses are evaluated against the river_size array to determine the winning percentage of the user. 
* **run.py** - is the file executed to run the game.


	
