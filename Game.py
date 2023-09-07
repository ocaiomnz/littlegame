'''
This class is the main class of the "World of Zuul" application. 
"World of Zuul" is a very simple, text based adventure game.  Users 
can walk around some scenery. That's all. It should really be extended 
to make it more interesting!

To play this game, create an instance of this class and call the "play"
method.

This main class creates and initialises all the others: it creates all
rooms, creates the parser and starts the game.  It also evaluates and
executes the commands that the parser returns.

@author  Michael Kolling and David J. Barnes
@version 2008.03.30
'''

from Parser import Parser
from Room import Room
class Game:
        
	'''
	Create the game and initialise its internal map.
	'''
	def __init__(self):
		self.__createRooms()
		self.__parser = Parser()
		self.__currentRoom
	'''
	Create all the rooms and link their exits together.
	'''
	def __createRooms(self):
		# create the rooms
		outside = Room("Fora da universidade")
		theatre = Room("Dentro da biblioteca")
		pub = Room("Dentro do bar do campus")
		lab = Room("no laboratório de computação")
		office = Room("na administração do laboratório de computação")
		
		deposito = Room('No depósito do laboratório da universidade')
		porao = Room('No porão da universidade')

        
		# initialise room exits
		outside.setExits(None, theatre, lab, pub, None, porao)
		theatre.setExits(None, None, None, outside, None,None)
		pub.setExits(None, outside, None, None, None, None)
		lab.setExits(outside, office, None, None, deposito, None)
		office.setExits(None, None, None, lab, None, None)
		deposito.setExits(None, None, None, None, None, lab)
		porao.setExits(None, None, None, None, outside, None)

		self.__currentRoom = outside  ## start game outside

	'''
	Main play routine.  Loops until end of play.
	'''
	def play(self):          
		self.__createRooms()
		self.__printWelcome()

		## Enter the main command loop.  Here we repeatedly read commands and
		## execute them until the game is over.
                
		finished = False
		while (not finished):
			command = self.__parser.getCommand()
			finished = self.__processCommand(command)
		print("Thank you for playing.  Good bye.")

	'''
	Print out the opening message for the player.
	'''
   
	def __printWelcome(self):
		print("\nWelcome to the World of Zuul!")
		print("World of Zuul is a new, incredibly boring adventure game.")
		print("Type 'help' if you need help.\n")
        
		print("You are " + self.__currentRoom.getDescription())
        
		exits = self.currentRoom()
		print("Exits: " + exits)


	'''
	Given a command, process (that is: execute) the command.
	@param command The command to be processed.
	@return true If the command ends the game, false otherwise.
	'''
	def __processCommand(self, command):
		wantToQuit = False

		if(command.isUnknown()):
			print("I don't know what you mean...")
			return False

		commandWord = command.getCommandWord()
		if(commandWord == "help"):
			self.__printHelp()
		elif (commandWord == "go"):
			self.__goRoom(command)
		elif (commandWord == "quit"):
			wantToQuit = self.__quit(command)

		return wantToQuit

    # implementations of user commands:

	'''
	Print out some help information.
	Here we print some stupid, cryptic message and a list of the 
	command words.
	'''
	def __printHelp(self):
		print("You are lost. You are alone. You wander")
		print("around at the university.\n")
		print("Your command words are:")
		print("   go quit help")

	'''
	Try to go to one direction. If there is an exit, enter
	the new room, otherwise print an error message.
	'''
	
	def __goRoom(self, command):
		if(not command.hasSecondWord()):
            # if there is no second word, we don't know where to go...
			print("Go where?")
			return

		direction = command.getSecondWord()

        # Try to leave current room.
        
		nextRoom = None
		if (direction == "north"):
			nextRoom = self.__currentRoom.getNorth()
		if (direction == "east"):
			nextRoom = self.__currentRoom.getEast()
		if (direction == "west"):
			nextRoom = self.__currentRoom.getWest()
		if (direction == "south"):
			nextRoom = self.__currentRoom.getSouth()
		if (direction == "up"):
			nextRoom = self.__currentRoom.getUp()
		if (direction == "down"):
			nextRoom = self.__currentRoom.getDown()
		if (nextRoom == None):
			print("There is no door!")
		else:
			self.__currentRoom = nextRoom
            
			print("You are " + self.__currentRoom.getDescription())
			exits = self.currentRoom()
            
			print("Exits: " + exits)

	''' 
	"Quit" was entered. Check the rest of the command to see
	whether we really quit the game.
	@return true, if this command quits the game, false otherwise.
	'''
	def __quit(self, command):
		if(command.hasSecondWord()):
			print("Quit what?")
			return False
		else:
			return True  # signal that we want to quit

	def printLocationInfo(self):
		print(f'Current room: {self.currentRoom()}')
	
	def currentRoom(self):
		exits = ""
		if(self.__currentRoom.getNorth() != None):
			exits += "north "
		if(self.__currentRoom.getEast() != None):
			exits += "east "
		if(self.__currentRoom.getSouth() != None):
			exits += "south "
		if(self.__currentRoom.getWest() != None):
			exits += "west "
		if(self.__currentRoom.getUp() != None):
			exits += "up "
		if(self.__currentRoom.getDown() != None):
			exits += "down "
		return exits