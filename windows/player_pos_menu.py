from windows.window import Window
from game_state import GameState


class PlayerPosMenu(Window):
    def update(self, game_state: GameState):
        self.content = {}
        self.content[(1, 1)] = "X::"
        self.content[(4, 1)] = str(game_state.player.x)
        self.content[(1, 2)] = "Y::"
        self.content[(4, 2)] = str(game_state.player.y)
        self.create_border("0")
