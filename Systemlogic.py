#!/usr/bin/python3
#def main():
#	print ("Welcome to closest to 21")
import random
class Player:
	def __init__(self, name,isai):
		#playername
		self.name = name
		#stop handing to me
		self.hold = False
		#I am not real
		self.isai = isai
		#current number player have
		self.curnumber=0
		#AI risk managment
		self.ainumberaim=random.randint(15,21)
		self.aimax=0

	def dealNumber(self,number):
		#set new number value
		self.curnumber=self.curnumber+number
	def askhold(self):
		ask=input("player {0}! Your value is currently: {1}. Do you hold? y or n: ".format(self.name,self.curnumber))
		if ask=='y':
			self.hold=True
			return True
		elif ask=='n':
			return False
		else: 
			print ("Not valid answer...")
			self.askhold()
			return False
	def askai(self):
		#ron tries to make a chanse to go closer it might go over if player beat their number in a atempt to win
		print("player %s turn:"%self.name)
		if self.ainumberaim<self.curnumber:
			print("ron got the value %d it choose to not continue."%self.curnumber)
			self.hold=True
			return True
		elif self.curnumber < self.aimax and self.curnumber <=20:
			print("ron got the value %d it choose to not continue."%self.curnumber)
			return True
		else:
			print("ron got the value %d it choose to continue."%self.curnumber)
			return False
	def aimaxincrease(self, newnumb):
		if self.aimax< newnumb:
			self.aimax=newnumb
		return self.aimax

class Game:
	def __init__(self,):
		#list of players
		self.playerlist=[]
		#game state
		self.game=True
		#how many players ingame
		self.activeplayers=0
		#aimax 
		self.aimaxgame=0
		self.first=""
		print ("hello, lets play: Closest to 21")
		print ("choose how many players, if only one player there will be 1 ron")

	def Runnloop(self):
		#all active players
		self.activeplayers=len(self.playerlist)
		print("There are " +str(self.activeplayers)+"players")

		#start the loop
		while self.game:
			#run game turn
			for player in self.playerlist:
				if not player.hold:
					if player.hold:
						print("Holding player...")
						continue
					player.dealNumber(random.randint(1,13))
					self.game=True
					#if player is lucky
					if player.curnumber == 21:
						player.hold=True
						self.activeplayers-=1
						print("Player"+player.name+" got to 21! Auto holding...")
						continue
					#if player gets over the threshold
					elif player.curnumber>21:
						player.hold=True
						self.activeplayers-=1
						print("You got over 21. Bether luck next time. Auto holding...")
						continue
					r=False
					if player.isai:
						r =player.askai()
					else:
						r = player.askhold()

					if r:
						self.activeplayers-=1
				else:
					print ("player {0} is holding with the value: {1}".format(player.name,player.curnumber))
					self.activeplayers-=1
				self.aimaxgame=player.aimaxincrease(player.curnumber)
				if player.curnumber==self.aimaxgame:
					self.first=player.name
			#to see if game has ended
			if self.activeplayers<=0:
				self.game=False
				continue
			print("End turn...")
		print("Game over!")
		print("Results:")
		print("Firstplace goes to:"+self.first+". with the number: "+str(self.aimaxgame))
			
		
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
		if players and players >1 and players<10:	
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
def main():
	game=Game()
	game.addPlayers()
	game.Runnloop() 
if __name__=="__main__":
	main()