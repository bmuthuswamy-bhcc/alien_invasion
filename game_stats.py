class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.game_active = True
		self.reset_stats()

	def reset_stats(self):
		"""Initialize statistics that can change during the same."""
		self.ships_left = self.settings.ship_limit
		self.score = 0