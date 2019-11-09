#!/usr/bin/python3
#def main():
#	print ("Welcome to closest to 21")

class Player:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name):
      self.name = name
      

class Ai:
	def __init__(self, name):
		self.name=name

class Game:
	def __init__(self,playerlist,numplayers):
		self.playerlist=playerlist
	def startGame(self):
		#starts the game
		pass
	def randomNumber(self):
		#pick a random number from 1 to 13
		pass
	def Runnloop(self):
		#run a game turn
		pass


#settup
print ("hello, lets play: Closest to 21")
print ("choose how many players, if only one player there will be 1 AI")
players=input()
for num(players) 
playername= input()
playerlist
player = Player(playername)


game=new Game(playerlist)
