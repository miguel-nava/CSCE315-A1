# Miguel Nava
722006885

# Assignment1
Game Leaderboard Tracker

Will be writting my code in Python.
This will be my firt time coding in Python so I hope it comes out well. 

# Compiling
In order to compile the program you must run it in 

    compute.cse.tamu.edu

there you will navigate to the folder containing the program. Then you will type in 

    python A1.py < input.txt

this will feed in the input text file into the program. You may try any other input text file by just replacing the name. If no file is specified then the program will expect input from the command line. 


# Data Structure

The data structure used in the code was a dictionary data structure. This made it easy to index games, players, and victories simply by thier ID. Each element required a unique ID for their respective area which made it a simple choice to pick a dictionary data structure. 

The code also uses arrays inside the dictionaries in order to keep certain elements grouped together. For example, when adding a victory to a player, the dictionary was indexed to the player ID which contained another dictionary that was indexed based on game ID and inside there victories were added to an array in order to keep them under the same game. 
