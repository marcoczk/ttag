from entity import GameEntity
from game_state import GameState


class Player(GameEntity):

    def pass_key(self, key: str, game_state: GameState):
        newx = self.x
        newy = self.y
        if key == "w":
            newy = max(self.y - 1, 0)
        elif key == "s":
            newy = min(self.y + 1, game_state.MAP_HEIGHT)
        if key == "a":
            newx = max(self.x - 1, 0)
        elif key == "d":
            newx = min(self.x + 1, game_state.MAP_WIDTH)
        if not game_state.entities.entities_at(newx, newy):
            game_state.entities.remove_entity(self)
            self.x = newx
            self.y = newy
            game_state.entities.add_entity(self)
        game_state.focusX = self.x
        game_state.focusY = self.y
