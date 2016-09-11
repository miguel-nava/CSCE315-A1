# Author: Miguel Nava
# Assignment: Individual assignment: game leaderboard tracker
import fileinput

Player = {}
Game = {}


#FIXME make sure to convert playerID from string to integer at some point 
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

#AddGame <Game ID> <Game Name>
	#Adds game to data base with a positive integer indentifier 
	#Name is given as string, can contain special characters except double quotes 
def AddGame (gameID, gameName):
		print gameID
		print gameName
#AddVictory <Game ID> <Victory ID> <Victory Name> <Victory Points>
	#Add victory to the game denoted by the Game ID
	#Victory ID is just to identify the victory 
	#Victory name is given as string, cannot contain double quotes
	#The points indicate what the victory is worth
def AddVictory(gameID,victoryID, victoryName,victoryPoints):
	print gameID
	print victoryID
	print victoryName
	print victoryPoints
	
#Plays <Player ID> <Game ID> <Player IGN>
	# 
	#
def Plays(playerID, gameID, playerIGN):
	print "plays"
#AddFriends <Player ID1> <Player ID2>
	#
	#
def AddFriends(playerID1, playerID2):
	print "friends"
#WinVictory <Player ID> <Game ID> <Victory ID>
	#
	#
def WinVictory(playerID, gameID, victoryID):
	print "win victory"
#FriendsWhoPlay <Player ID> <Game ID>
	#
	#
def FriendsWhoPlay(playerID, gameID):
	print "friends who play"
#ComparePlayers <Player ID1> <Player ID2> <Game ID>
	#
	#
def ComparePlayers(playerID1, playerID2, gameID):
	print "comparing players"
#SummarizePlayer <Player ID>
	#
	#
def SummarizePlayer(playerID):
	print "summarize player"
#SummarizeGame <Game ID>
	#
	#
def SummarizeGame(gameID):
	print "sum game"
#SummarizeVictory <Game ID> <Victory ID>
	#
	#
def SummarizeVictory(gameID, victoryID):
	print "sum victory"
#VictoryRanking
	#
	#
def VictoryRanking():
	print "victory Ranking"
def parse(elements):
	element = elements.partition(" ")
	if(element[0] is ""):
		pass
	else:
		globals()[element[0]]
	
for line in fileinput.input():				# stdin, reads file line by line 
    parse(line)

# Trial and error stuff	
# arr = {}
# for i in range(0,10):
		# arr[i] = i+1
# print arr
# func = "AddPlayer"
# id = "1234"
# name = "miguel"

# methodToCall = globals()[func]
# methodToCall(id,name)
# methodToCall(1923,"luis")
