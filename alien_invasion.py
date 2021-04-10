import sys
import pygame

# from settings.py, import Settings class
# this works because settings.py is in the
# *same folder* as alien_invasion.py
from settings import Settings

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()
		# Create a pygame display window whose dimensions are defined
		# by the tuple (X,Y)
		# Note that set_mode returns a SURFACE that we assign to
		# the variable screen so that it is accessible from all methods
		# in the class.
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		"""Start the main game loop."""
		while True:
			# Watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# Make the most recently drawn screen visible.
			# When we move game elements around the screen,
			# pygame.display.flip() continually updates the display
			# to show the new positions of game elements.
			pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance and run the game.
	ai = AlienInvasion()
	ai.run_game()

