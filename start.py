#!/usr/bin/python3
#def main():
#	print ("Welcome to closest to 21")
import random
class Player:
   'Common base class for all employees'
   empCount = 0

	def __init__(self, name,isai):
		self.name = name
		self.hold = False
		self.isai = isai
		self.curnumber=0
		self.ainumberaim=random.radint(15,21)
		self.activeplayers=0
	def dealNumber(self,number):
		#set new number value
		self.curnumber=self.curnumber+number
	def askhold(self):
		ask=input("player {0}! Your value is currently: {1}. Do you hold? y for yes n for no" format(unicode(self.player.name,'utf-8'),unicode(self.player.curnumber,'utf-8')))
		if ask=='y':
			self.hold=True
		elif ask=='n':
		else: 
			print ("Not valid answer...")
			self.askhold()
	def askai(self):
		print("AI turn:")
		if ainumberaim<curnumber:
			print("Ai got the value %d it choose to not continiue."%curnumber)
			self.hold=True
		else:
			print("Ai got the value %d it choose to continiue."%curnumber)
class Game:
	def __init__(self,):
		self.playerlist=[]
		self.game=True
		print ("hello, lets play: Closest to 21")
		print ("choose how many players, if only one player there will be 1 AI")

	def Runnloop(self):
		#run game turn
		self.activeplayers=len(self.playerlist)
		print("There are currently " +players+"players")
		for player in self.playerlist
		while self.game:
			for player in self.playerlist:
				if not player.hold:
					player.askhold()
					player.dealnumber(random.radint(1,13))
					self.game=True
					if player.curnumber == 21:
						player.hold=True
						self.activeplayers-=1
						print("You got to 21! Auto holding...")
					elif player.curnumber>21:
						player.hold=True
						self.activeplayers-=1
						print("You got over 21. Bether luck next time. Auto holding...")
				else:

					self.
					print ("player {0} is holding with value: {1}"format(unicode(self.player.name,'utf-8'),unicode(self.player.curnumber,'utf-8')))
				#to see if game has ended
				
			print("End turn...")

		
	def playeraction(self):
		pass
	def addPlayers(self):
		#settup players
		try:
			players=int(input("Number of players(1-10):"))
		except Exception as e:
			print ("Not a valid input need valid number...")
			self.addPlayers()
		x=0
		if players and players!=1 and players<10 and players <=1:	
			for x in range(players):
				playername= input("Player name:")
				player=Player(playername,False)
				self.playerlist.append(player)
				
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
game.Runnloop()