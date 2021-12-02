class GameStats():
    """track information about games"""

    def __init__(self, ai_settings):
        """initial sum"""
        # self.ships_left = self.ai_settings.ship_limit
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        # self.ships_left = self.ai_settings.ship_limit
        self.high_score = 0
    def reset_stats(self):
        """initial information"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

