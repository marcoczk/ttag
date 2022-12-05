from entity import EntityArray, GameEntity


class GameState:
    def __init__(self, entities: EntityArray = EntityArray(),
                 focusX: int = 0, focusY: int = 0, MAP_WIDTH=150, MAP_HEIGHT=150,
                 game_window_baseX: int = 0,
                 game_window_baseY: int = 0,
                 game_window_width: int = 40,
                 game_window_height: int = 40):
        self.game_window_height = game_window_height
        self.game_window_width = game_window_width
        self.game_window_baseY = game_window_baseY
        self.game_window_baseX = game_window_baseX
        self.entities = entities
        self.focusX = focusX
        self.focusY = focusY
        self.MAP_WIDTH = MAP_WIDTH
        self.MAP_HEIGHT = MAP_HEIGHT
        self.player: GameEntity = None
