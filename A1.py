# Author: Miguel Nava
# Assignment: Individual assignment: game leaderboard tracker
import fileinput

Player = { }
PlayerPlays = {}
PlayerFriends = {}
PlayerVictories = {}
Game = {}
GameVictories = {}

def AddPlayer (playerID, playerName): 
    if str.isdigit(playerID): 		# checks if ID is an int
        if playerID >= 0:					# checks if ID is positive 
			if '\"' not in playerName:   			# checks for double quotes		
				Player[int(playerID)] = playerName
				PlayerPlays[int(playerID)] = {}
				PlayerVictories[int(playerID)] = {}
	return
	
#AddGame <Game ID> <Game Name>
def AddGame (gameID, gameName):
	Game[int(gameID)] = gameName
	GameVictories[int(gameID)] = {}

#AddVictory <Game ID> <Victory ID> <Victory Name> <Victory Points>
def AddVictory(gameID, victoryID, victoryName, victoryPoints):
	GameVictories[int(gameID)][int(victoryID)] = (victoryName, int(victoryPoints) )
	
#Plays <Player ID> <Game ID> <Player IGN>
def Plays(playerID, gameID, playerIGN):
	if int(gameID) in PlayerPlays[int(playerID)]:
		PlayerPlays[int(playerID)][int(gameID)].append(playerIGN)
	else:
		PlayerPlays[int(playerID)][int(gameID)] = [playerIGN]
	
#AddFriends <Player ID1> <Player ID2>
def AddFriends(playerID1, playerID2):
	if int(playerID1)  in PlayerFriends:
		PlayerFriends[int(playerID1)].append(int(playerID2))
	else:
		PlayerFriends[int(playerID1)] = [int(playerID2)]
		
	if int(playerID2) in PlayerFriends:
		PlayerFriends[int(playerID2)].append(int(playerID1))
	else:
		PlayerFriends[int(playerID2)] = [int(playerID1)]
	
#WinVictory <Player ID> <Game ID> <Victory ID>
def WinVictory(playerID, gameID, victoryID):
	if int(gameID) in PlayerVictories[int(playerID)]:
		PlayerVictories[int(playerID)][int(gameID)].append(int(victoryID))
	else:
		PlayerVictories[int(playerID)][int(gameID)] = [int(victoryID)]
#FriendsWhoPlay <Player ID> <Game ID>
def FriendsWhoPlay(playerID, gameID):
	list = PlayerFriends[int(playerID)]
	for i in list: 
		if gameID in PlayerPlays[int(playerID)]:
			if gameID in PlayerPlays[i]:
				print Player[i] + " plays " + Game[int(gameID)] + " with " + Player[int(playerID)]

#ComparePlayers <Player ID1> <Player ID2> <Game ID>
def ComparePlayers(playerID1, playerID2, gameID):
# Print report comparing player 1 and player 2's Victory records and total Victory scores for the given game. The given game is guaranteed to have been played by both players.
	if gameID in PlayerPlays[int(playerID1)]:
		if gameID in PlayerPlays[int(playerID2)]:
			total = 0
			print "\t" + Game[int(gameID)]
			print "---------------"
			print Player[int(playerID1)]
			for i in PlayerVictories[playerID1][gameID]:
				total += GameVictories[int(gameID)][i][1]
				print " " + GameVictories[int(gameID)][i][0]
			print "Total points : " + `total`
			
			total = 0
			print "---------------"
			print Player[int(playerID2)]
			for j in PlayerVictories[playerID2][gameID]:
				total += GameVictories[int(gameID)][j][1]
				print " " + GameVictories[int(gameID)][j][0]
			print "Total points : " + `total`

#SummarizePlayer <Player ID>
def SummarizePlayer(playerID):
	print "\t" + Player[int(playerID)]
	
	print "---------------"
	print "Friends"
	for i in PlayerFriends[int(playerID)]:
		print "  " + Player[i] 
		
	print "---------------"
	total_points = 0
	points = 0
	print "Games: Points"
	for i in PlayerPlays[int(playerID)]:
		if i in PlayerVictories[int(playerID)]:
			for j in PlayerVictories[int(playerID)][i]:
				points += GameVictories[i][j][1]
		print "  " + Game[i] + ": " + `points`
		total_points += points
		points = 0
		
	print "---------------"
	print "Total points"
	print "  " + `total_points`
#SummarizeGame <Game ID>
def SummarizeGame(gameID):
# Print a record of all players who play the specified game and the number of times each of its victories have been accomplished.
	
	pass

#SummarizeVictory <Game ID> <Victory ID>
def SummarizeVictory(gameID, victoryID):
# Print a list of all players who have achieved a Victory, and the percentage of players who play that game who have the Victory.
	pass

#VictoryRanking
def VictoryRanking():
# Print a summary ranking all players by their total number of gamer points.
	pass
	
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
			else:
				element = element[2].split("\"")
				args[i] = element[1]
				element = element[2].partition(" ")
		if ( "\"" not in element[2][0]):
			args[argNum-1] = element[2]
		else:
			args[argNum-1] = element[2].split("\"")[1]
		callMethod(method, args)
	
for line in fileinput.input():				# stdin, reads file line by line 
    parse(line)


# print Player 
# print Game
# print GameVictories
# print PlayerPlays
# print PlayerVictories
# print PlayerFriends