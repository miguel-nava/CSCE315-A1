# Author: Miguel Nava
# Assignment: Individual assignment: game leaderboard tracker
class Player:
	def f(self):
		print "hello world"
		return
#AddPlayer <Player ID> <Player Name>
	#Adds player to database with a positve integer identifier
	#Name is given as a string, can contain special characters except double quotes
def AddPlayer (playerID, playerName):
    if isinstance(playerID, int): 			# checks if ID is an int
        if playerID >= 0:					# checks if ID is positive 
            print playerID					# need to add to database 
    else:
        print "not integer"
		
    if '\"' not in playerName:   			# checks for double quotes 
        print playerName					# need to add name to database 
    else:
        print "string contains \""
    return

AddPlayer(1234,"miguel nava")
Player.f
	
#AddGame <Game ID> <Game Name>
	#Adds game to data base with a positive integer indentifier 
	#Name is given as string, can contain special characters except double quotes 
	
#AddVictory <Game ID> <Victory ID> <Victory Name> <Victory Points>
	#Add victory to the game denoted by the Game ID
	#Victory ID is just to identify the victory 
	#Victory name is given as string, cannot contain double quotes
	#The points indicate what the victory is worth
	
#Plays <Player ID> <Game ID> <Player IGN>
	# 
	#
#AddFriends <Player ID1> <Player ID2>
	#
	#
#WinVictory <Player ID> <Game ID> <Victory ID>
	#
	#
#FriendsWhoPlay <Player ID> <Game ID>
	#
	#
#ComparePlayers <Player ID1> <Player ID2> <Game ID>
	#
	#
#SummarizePlayer <Player ID>
	#
	#
#SummarizeGame <Game ID>
	#
	#
#SummarizeVictory <Game ID> <Victory ID>
	#
	#
#VictoryRanking
	#
	#