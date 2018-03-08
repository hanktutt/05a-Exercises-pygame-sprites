#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first few lines for you as an example


'''
import sys, logging, pygame	# imports the sys, logging, and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

logging.basicConfig(level=logging.CRITICAL) #a debugging class used in python
logger = logging.getLogger(__name__) #variable used to identifty the debugger

screen_size = (800,600) #variable that we make a tuple for the size of the screen
FPS = 60 #variable we create for FPS
red = (255,0,0) #creating color red with rgb
black = (0,0,0) #creating color variable

class Block(pygame.sprite.Sprite): #creating a class for Block
	def __init__(self, position, direction): #creating a function for init so it will run automatically
		pygame.sprite.Sprite.__init__(self)#initializing the init function
		self.image = pygame.Surface((50, 50))#giving self an image called in the class
		self.image.fill(red) #filling the image with red
		self.rect = self.image.get_rect()#calling self to get rect
		(self.rect.x,self.rect.y) = position #creating a tuple for position
		self.direction = direction #creating a variable for direction

	def update(self): #function made to call for update
		(dx,dy) = self.direction #setting dx,dy to = self direction
		self.rect.x += dx #giving the x value a direction
		self.rect.y += dy #giving y value a direction
		(WIDTH,HEIGHT) = screen_size #tuple set to screen size
		if self.rect.left > WIDTH: #if statement for paramteters of left of rect
			self.rect.right = 0 #setting right = to 0
		if self.rect.right < 0: #if statement for paramteters of right of rect
			self.rect.left = WIDTH #setting left = to 0
		if self.rect.top > HEIGHT: #if statement for paramteters of top of rect
			self.rect.bottom = 0 #setting top = to 0
		if self.rect.bottom < 0: #if statement for paramteters of bottom of rect
			self.rect.top = HEIGHT #setting bottom = to 0


def main(): #creating new function called main
	pygame.init() #starting initialzing pygmae
	screen = pygame.display.set_mode(screen_size) #setting the screen size of our game to be equal to variable screen
	clock = pygame.time.Clock() #creating a variable for clock

	blocks = pygame.sprite.Group() #creating a group for blocks
	block = Block((200,200),(-1,1)) #initializing block with init values
	blocks.add(block) #add block to our pygame

	while True: #creating continous Loop
		clock.tick(FPS) #Setting cpu to not go faster than 60
		screen.fill(black) #fill screen black

		for event in pygame.event.get(): #a set numbered loop for an event in pygame
			if event.type == pygame.QUIT: #if statment saying if that event is quit
				pygame.quit() #quit pygame
				sys.exit(0) #exit system

		blocks.update() #update blocks group
		blocks.draw(screen)#draw the blcoks on the screen
		pygame.display.flip()#pygame code used to randomly fill pixels

if __name__ == '__main__': #if statement used to initialize pygame
	main() #call main