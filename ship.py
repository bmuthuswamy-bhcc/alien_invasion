import pygame

class Ship:
	"""A class to manage the player's ship"""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		# get the bounding box of the screen as a rectangle
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its bounding box
		self.ship = pygame.image.load('images/ship.bmp')
		self.rect = self.ship.get_rect()

		# Start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		# Movement flag (say for continuous movement)
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.rect.x -= self.settings.ship_speed
		self.blitme()

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.ship, self.rect)

	def center_ship(self):
		"""Center the ship on the screen."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

