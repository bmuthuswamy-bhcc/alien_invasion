import pygame

class Ship:
	"""A class to manage the player's ship"""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		# get the bounding box of the screen as a rectangle
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its bounding box
		self.ship = pygame.image.load('images/ship.bmp')
		self.ship_rect = self.ship.get_rect()

		# Start each new ship at the bottom center of the screen
		self.ship_rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.ship, self.ship_rect)

