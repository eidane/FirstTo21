#!/usr/bin/python3
#def main():
#	print ("Welcome to closest to 21")

class Player:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name,isai):
      self.name = name
      self.hold = False
      self.isai = isai


class Game:
	def __init__(self,):
		self.playerlist=[]
		print ("hello, lets play: Closest to 21")
		print ("choose how many players, if only one player there will be 1 AI")
	def startGame(self):
		#starts the game
		pass
	def randomNumber(self):
		#pick a random number from 1 to 13
		pass
	def Runnloop(self):
		#run a game turn
		pass
	def playeraction(self):
		pass
	def addPlayers(self):
		#settup
		try:
			players=int(input("Number of players:"))
		except Exception as e:
			print ("Not a valid input need valid number:")
			self.addPlayers()
		x=0
		if players and players!=1 and players<10 and players <=1:	
			while x < players:
				playername= input("Player name:")
				player=Player(playername,False)
				self.playerlist.append(player)
				x+=1
		elif players==1:
			playername= input("Player name:")
			player=Player(playername,False)
			self.playerlist.append(player)
			aiplayer=Player("Ron",True)
			self.playerlist.append(aiplayer)
		elif players>10:
			print ("Invalid imput, to many players")
			self.addPlayers()
		elif players<=0:
			print("end game...")
		else:
			print ("Error on imput")
			self.addPlayers()

#Start

game=Game()
game.addPlayers()