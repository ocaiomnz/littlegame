'''
Class Room - a room in an adventure game.

This class is part of the "World of Zuul" application. 
"World of Zuul" is a very simple, text based adventure game.  

A "Room" represents one location in the scenery of the game.  It is 
connected to other rooms via exits.  The exits are labelled north, 
east, south, west.  For each direction, the room stores a reference
to the neighboring room, or null if there is no exit in that direction.

@author  Michael Kolling and David J. Barnes
@version 2008.03.30
'''
class Room:

	'''
	Create a room described "description". Initially, it has
	no exits. "description" is something like "a kitchen" or
	"an open court yard".
	@param description The room's description.
	'''
	def __init__(self, description):
		self.description = description
		self.__northExit = None
		self.__southExit = None
		self.__eastExit = None
		self.__westExit = None
		self.__upExit = None
		self.__downExit = None
		

	'''
	Define the exits of this room.  Every direction either leads
	to another room or is null (no exit there).
	@param north The north exit.
	@param east The east east.
	@param south The south exit.
	@param west The west exit.
	'''
	def setExits(self, north = None, east = None, south = None, west = None, up = None, down = None):
		if north != None:
			self.setNorth(north)
		if east != None:
			self.setEast(east)
		if south != None:
			self.setSouth(south)
		if west != None:
			self.setWest(west)
		if up != None:
			self.setUp(up)
		if down != None:
			self.setDown(down)
			
	
	def getExist(self, direction):
		if direction == 'north':
			self.__northExit = None
		elif direction == 'east':
			self.__eastExit = None
		elif direction == 'west':
			self.__westExit = None
		elif direction == 'south':
			self.__southExit = None
		elif direction == 'up':
			self.__upExit = None
		elif direction == 'down':
			self.__downExit = None

	def getNorth(self):
		return self.__northExit
	
	def getEast(self):
		return self.__eastExit
	
	def getSouth(self):
		return self.__southExit
	
	def getWest(self):
		return self.__westExit
	
	def getUp(self):
		return self.__upExit

	def getDown(self):
		return self.__downExit
	
	def setNorth(self,north):
		if north is not None:
			self.__northExit = north
		
	
	def setEast(self,east):
		if east is not None:
			self.__eastExit = east
		
		
	def setWest(self,west):
		if west is not None:
			self.__westExit = west
		
		
	def setSouth(self,south):
		if south is not None:
			self.__southExit = south
	
	def setUp(self, up):
		if up is not None:
			self.__upExit = up

	def setDown(self, down):
		if down is not None:
			self.__downExit = down


	'''
	@return The description of the room.
	'''
	def getDescription(self):
		return self.description
