from windows.window import Window
from game_state import GameState
from windows.clickable import Clickable


class ExitButton(Clickable):
    def click(self, game_state: GameState):
        raise SystemExit


class ExitMenu(Window):

    def update(self, game_state: GameState):
        self.content[(int(self.width / 2 - 2), int(self.height / 2))] = "EXIT"
        self.create_border("8")
        self.clickables = [ExitButton(int(self.width / 2 - 2), int(self.height / 2), ["EXIT"])]
