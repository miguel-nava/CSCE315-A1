# Author: Miguel Nava
# UIN:722006885
# Assignment: Individual assignment: game leaderboard tracker
import fileinput
import operator

######## Dictionaries ##############
Player = { }
PlayerPlays = {}
PlayerFriends = {}
PlayerVictories = {}
Game = {}
GameVictories = {}
####################################


######## Assignment Methods ########
def AddPlayer (playerID, playerName): 
    if str.isdigit(playerID): 						
        if playerID >= 0:								 
			if '\"' not in playerName:   					
				Player[int(playerID)] = playerName
				PlayerPlays[int(playerID)] = {}														# Initialization of dictionaries inside 
				PlayerVictories[int(playerID)] = {}													# of dictionaries
	
def AddGame (gameID, gameName):
	if str.isdigit(gameID): 						
		if (gameID >= 0):								 
			if '\"' not in gameName:  
				Game[int(gameID)] = gameName
				GameVictories[int(gameID)] = {}														# Initialization of dictionary for victories

def AddVictory(gameID, victoryID, victoryName, victoryPoints):
	if str.isdigit(gameID) and str.isdigit(victoryID): 						
		if int(gameID) >= 0 and int(victoryID) >= 0:								 
			if '\"' not in victoryName and int(gameID) in Game:										# assures that the game exists 
				GameVictories[int(gameID)][int(victoryID)] = (victoryName, int(victoryPoints) )
	
def Plays(playerID, gameID, playerIGN):
	if str.isdigit(gameID) and str.isdigit(playerID): 						
		if int(gameID) >= 0 and int(playerID) >= 0:								 
			if int(playerID) in Player and int(gameID) in Game:
				if int(gameID) in PlayerPlays[int(playerID)]:
					PlayerPlays[int(playerID)][int(gameID)].append(playerIGN)						# This method checks to see if a list of plays 
				else:																				# for the player has been started. If it has,
					PlayerPlays[int(playerID)][int(gameID)] = [playerIGN]							# then it appends, if not then it creates the list 
	
def AddFriends(playerID1, playerID2):
	if int(playerID1)  in PlayerFriends:															# Players are added to each others' friends list 
		PlayerFriends[int(playerID1)].append(int(playerID2))										
	else:
		PlayerFriends[int(playerID1)] = [int(playerID2)]
		
	if int(playerID2) in PlayerFriends:
		PlayerFriends[int(playerID2)].append(int(playerID1))
	else:
		PlayerFriends[int(playerID2)] = [int(playerID1)]
	
def WinVictory(playerID, gameID, victoryID):
	if int(gameID) in PlayerVictories[int(playerID)]:
		PlayerVictories[int(playerID)][int(gameID)].append(int(victoryID))
	else:
		PlayerVictories[int(playerID)][int(gameID)] = [int(victoryID)]

def FriendsWhoPlay(playerID, gameID):
	list = PlayerFriends[int(playerID)]																# Receives all the player's friends from the list 
	for i in list: 																					# amongst them it figures out if they have any similar 
		if gameID in PlayerPlays[int(playerID)]:													# gameID's in order to determine if they play together or not 
			if gameID in PlayerPlays[i]:
				print Player[i] + " plays " + Game[int(gameID)] + " with " + Player[int(playerID)]

def ComparePlayers(playerID1, playerID2, gameID):
	if gameID in PlayerPlays[int(playerID1)]:
		if gameID in PlayerPlays[int(playerID2)]:
			total = 0																				# Compares players on the basis of victories in a game 
			print "\t" + Game[int(gameID)]															# and how many points they have in that game 
			
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

def SummarizePlayer(playerID):
	print "\t" + Player[int(playerID)]																# Gathers information about individual players such as 
																									# friends, games and points from those games 
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

def SummarizeGame(gameID):
	print "\t" + Game[int(gameID)]
	
	print "---------------"
	print "Players" 
	for pID in PlayerPlays:																			#
		if int(gameID) in PlayerPlays[pID]:
			print "  " + Player[pID]
	
	print "---------------"
	completed = 0 
	print "Victories: Completed"
	for vicID in GameVictories[int(gameID)]:
		for pID in PlayerVictories:
			if int(gameID) in PlayerVictories[pID]:
				if vicID in PlayerVictories[pID][gameID]:
					completed +=1
		print "  " + GameVictories[int(gameID)][vicID][0] + ": " + `completed` 
		completed = 0

def SummarizeVictory(gameID, victoryID):
	print "\tVictory: " + GameVictories[int(gameID)][int(victoryID)][0]
	players_play = 0.0
	players_win = 0.0
	
	print "---------------"
	print "Players who have achieved victory"
	for pID in PlayerVictories:
		if int(gameID) in PlayerVictories[pID]:
			if int(victoryID) in PlayerVictories[pID][int(gameID)]:
				print "  " + Player[pID]															# Tracks players who have won and also the players who 
				players_win += 1																	# have played the game 
			players_play += 1
			
	print "---------------" 
	print "Who won / Who played: " + `(players_win/players_play)*100` 

def VictoryRanking():
	list = {}
	points = 0 
	print "\tVictory Rankings"
	
	print "---------------" 
	for pID in Player:																							
		if pID in PlayerVictories:																	# Victory Ranking is done by calculating the players'
			for gID in PlayerVictories[pID]:														# total points and putting them in a dictionary 
				for vicID in PlayerVictories[pID][gID]:												# with their points as the key and their name is as 
					points += GameVictories[gID][vicID][1]											# the information. 
		list[points] = Player[pID]
		points = 0 																					# The dictionary is then sorted from smallest to greatest 
																									# based on the key and they are listed in descending order 
	sorted_list = sorted(list.items(), key=operator.itemgetter(0))									# so that they come out with the highest scorer first 
	count = 1
	for i in range(len(sorted_list)-1,-1,-1):
		print `count` + ". " + sorted_list[i][1] + " --- " + `sorted_list[i][0]`
		count += 1		
##################################	


	
######## Other Methods ###########
def callMethod(m, a):
	if len(a) == 0:
		m();
	elif len(a) == 1:																				# This method is just to call a method based on different 
		m(a[0])																						# argument amounts. m is the method to be called and 
	elif len(a) == 2:																				# a is an array that holds the arguments in order 
		m(a[0], a[1])
	elif len(a) == 3:																				# We only go up to a = 4 because that the highest argument 
		m(a[0], a[1], a[2])																			# function. a = 0 is the lowest 
	elif len(a) == 4:
		m(a[0], a[1], a[2], a[3])
	
def parse(elements):
	element = elements.partition(" ")
	args = {}
	if(element[0] is ""):
		pass
	else:
		method = globals()[element[0]]																# gets function
		argNum = method.func_code.co_argcount														# gets number of args in the function
		for i in range(0,argNum-1):			
			if ( "\"" not in element[2][0]):
				element = element[2].partition(" ")													# partitioning is done according to the number of 
				args[i] = element[0]																# arguments. Also it watches out for double quotes 
			else:																					# in order to prevent seperation of the string 
				element = element[2].split("\"")
				args[i] = element[1]
				element = element[2].partition(" ")
		if ( "\"" not in element[2][0]):
			args[argNum-1] = element[2]																# doesn't partition the last element because it does not need to
		else:																						# the last element is added at the end of the loop 
			args[argNum-1] = element[2].split("\"")[1]
		callMethod(method, args)																	# Once line is parsed, it calls the method by calling callMethod()
##################################

	
for line in fileinput.input():																		# stdin, reads file line by line 
    parse(line)	 																					# calls function to parse line 
