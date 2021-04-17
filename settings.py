class Settings:
	"""A class to store all settings for Alein Invasion."""

	def __init__(self):
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		# pygame uses (R,G,B) tuple
		self.bg_color = (230, 230, 230)

		self.ship_speed = 1 # For simplicity, use only integer values
		self.ship_limit = 3

		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3

		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# fleet direction of 1 represents right; -1 represents left
		self.fleet_direction = 1