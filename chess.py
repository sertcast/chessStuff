'''

all the files are from http://www.pgnmentor.com/files.html
(don't know how else to credit them)
'''

playersFile = open("players.txt", "r")
players = playersFile.read().split("\n")
playersFile.close()

openingsFile = open("openings.txt", "r")
openings = openingsFile.read().split("\n")
openingsFile.close()

player1 = open("players/" + players[0], "r")
a = player1.read().split("\n\n")
player1.close()
