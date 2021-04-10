import sys
import pygame

# from settings.py, import Settings class
# this works because settings.py is in the
# *same folder* as alien_invasion.py
from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()
		# Create a pygame display window whose dimensions are defined
		# by the tuple (X,Y).  Note that in pygame, (0,0) is the
		# the TOP-LEFT corner of the screen, bottom-right corner of
		# the screen has coordinates (self.settings.screen_width,
		# self.settings.screen_height)

		# Note that set_mode returns a SURFACE that we assign to
		# the variable screen so that it is accessible from all methods
		# in the class.
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)

	def run_game(self):
		"""Start the main game loop."""
		while True:
			self.check_events()
			self.update_screen()

	def check_events(self):
		"""Watch for keyboard and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self.check_keydown_events(event)				
			elif event.type == pygame.KEYUP:
				self.check_keyup_events(event)
		
	def check_keydown_events(self, event):
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True

	def check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False


	def update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.update()
		# Make the most recently drawn screen visible.
		# When we move game elements around the screen,
		# pygame.display.flip() continually updates the display
		# to show the new positions of game elements.
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance and run the game.
	ai = AlienInvasion()
	ai.run_game()

