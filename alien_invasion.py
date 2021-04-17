import sys
from time import sleep # we will pause the game for a moment when a ship is hit

import pygame

# from settings.py, import Settings class
# this works because settings.py is in the
# *same folder* as alien_invasion.py
from settings import Settings
from game_stats import GameStats

from ship import Ship
from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard


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

		# Create an instance to store game statistics
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		self.ship = Ship(self)
		# keep track of bullets fired when we press spacebar by using Group
		# (a list with extra functionality)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def _ship_hit(self):
		"""Respond to the ship being hit by an alien.
		Subtract one from teh number of ships left, destory all existing
		aliens and bullets, create a new fleet and reposition the ship in the middle of the
		screen
		"""
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1

			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()

			sleep(1)
		else:
			self.stats.game_active = False

	def run_game(self):
		"""Start the main game loop."""
		while True:
			self._check_events()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
			else:
				print("Game Over!")
				sys.exit()
				
			self._update_screen()

	def _check_events(self):
		"""Watch for keyboard and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)				
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
		
	def _check_keydown_events(self, event):
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""

		# Aliens are RELENTLESS : if all aliens are destroyed a new fleet appears!
		if not self.aliens:
			# Destroy existing bullets and create new fleet
			self.bullets.empty()
			self._create_fleet()

		self.bullets.update() # bullets is a Pygame Group => calls each bullet's update method
			
		# Get rid of bullets that have gone past the top of the screen
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)		
		# For checking collisions between bullets and aliens, we
		# will use sprite.groupcollide() from Pygame.  Essentially,
		# it compares the bounding boxes (rectangles) from one group of Sprites
		# to another.  In our case, sprite.groupcollide() is going to compare the bounding
		# boxes of bullet(s) and alien(s), and return a dictionary containing
		# the bullets and aliens that have collided.
		# The final two True arguments tell pygame to delete any bullets and aliens
		# that have collided
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)		
		if len(collisions) != 0:
			self.sb.update_score()
			self.sb.prep_score()


	def _create_fleet(self):
		"""Create the fleet of aliens."""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		
		# Compute number of aliens that can fit in a row
		available_space_x = self.settings.screen_width - (2*alien_width)
		number_aliens_x = available_space_x // (2*alien_width)

		# Determine number of rows of aliens that fit on the screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		for row_number in range (number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _create_alien(self,alien_number,row_number):
		"""Create an alien and place it in the row."""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size;
		
		alien.x = alien_width + 2*alien_width*alien_number
		alien.rect.x = alien.x
		
		alien.y = alien_height + 2*alien_height*row_number
		alien.rect.y = alien.y

		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached an edge."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_aliens(self):
		"""Update the positions of all aliens in the fleet."""
		self._check_fleet_edges()
		self.aliens.update()

		# Look for alien-ship collisions: use spritecollideany
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
		self.sb.show_score()
		# Make the most recently drawn screen visible.
		# When we move game elements around the screen,
		# pygame.display.flip() continually updates the display
		# to show the new positions of game elements.
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance and run the game.
	ai = AlienInvasion()
	ai.run_game()

