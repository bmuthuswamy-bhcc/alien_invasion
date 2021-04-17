import pygame.font

class Scoreboard:
	"""A class to report scoring information."""

	def __init__(self, ai_game):
		"""Initialize scorekeeping attributes."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Font settings for scoring information.
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None, 48)
		self.prep_score()

	def prep_score(self):
		"""Turn the score into an image."""
		score_str = "Score: " + str(self.stats.score) + " Lives: " + str(self.stats.ships_left)
		self.score_image = self.font.render(score_str, True,
			self.text_color, self.settings.bg_color)

		# Display score in top right of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)

	def update_score(self):
		self.stats.score += 10

