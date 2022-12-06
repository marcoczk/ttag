from windows.window import Window
from game_state import GameState
from windows.clickable import Clickable
from entity import GameEntity


class Fireball(Clickable):
    def click(self, game_state: GameState):
        fireball = GameEntity(game_state.player.x + 1, game_state.player.y + 1, "F")
        game_state.entities.add_entity(fireball)


class SpellMenu(Window):

    def update(self, game_state: GameState):
        self.create_border("~")
        spells = game_state.player.spells
        self.clickables = []
        for i in range(0, len(spells)):
            self.content[(2, i + 1)] = spells[i]
            self.clickables.append(Fireball(2, i + 1, ["fireball"]))
