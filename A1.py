# Author: Miguel Nava
# Assignment: Individual assignment: game leaderboard tracker
import fileinput
import inspect

Player = {}
Game = {}


#FIXME make sure to convert playerID from string to integer at some point 
def AddPlayer (playerID, playerName): 
    if str.isdigit(playerID): 		# checks if ID is an int
        if playerID >= 0:					# checks if ID is positive 
			if '\"' not in playerName:   			# checks for double quotes		
				Player[int(playerID)] = playerName
	return
	
#AddGame <Game ID> <Game Name>
	#Adds game to data base with a positive integer indentifier 
	#Name is given as string, can contain special characters except double quotes 
def AddGame (gameID, gameName):
	Game[gameID] = gameName

#AddVictory <Game ID> <Victory ID> <Victory Name> <Victory Points>
	#Add victory to the game denoted by the Game ID
	#Victory ID is just to identify the victory 
	#Victory name is given as string, cannot contain double quotes
	#The points indicate what the victory is worth
def AddVictory(gameID,victoryID, victoryName,victoryPoints):
	print gameID
	# print victoryID
	# print victoryName
	# print victoryPoints
	
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
	
def callMethod(m, a):
	if len(a) == 0:
		m();
	elif len(a) == 1:
		m(a[0])
	elif len(a) == 2:
		m(a[0], a[1])
	elif len(a) == 3:
		m(a[0], a[1], a[2])
	elif len(a) == 4:
		m(a[0], a[1], a[2], a[3])
	
def parse(elements):
	element = elements.partition(" ")
	args = {}
	if(element[0] is ""):
		pass
	else:
		method = globals()[element[0]]					# gets function
		argNum = method.func_code.co_argcount			# gets number of args in the function
		for i in range(0,argNum-1):			
			if ( "\"" not in element[2][0]):
				element = element[2].partition(" ")
				args[i] = element[0]
				print element[0]
			else:
				element = element[2].split("\"")
				args[i] = element[1]
				element = element[2].partition(" ")
				print element[1]
		if ( "\"" not in element[2][0]):
			args[argNum-1] = element[2]
		else:
			args[argNum-1] = element[2].split("\"")[1]
		callMethod(method, args)
	
for line in fileinput.input():				# stdin, reads file line by line 
    parse(line)

print Player 
print Game
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
