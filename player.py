from entity import GameEntity
from game_state import GameState


class Player(GameEntity):

    def pass_key(self, key: str, gamestate: GameState):
        newx = self.x
        newy = self.y
        if key == "w":
            newy = max(self.y - 1, 0)
        elif key == "s":
            newy = min(self.y + 1, gamestate.MAP_HEIGHT)
        if key == "a":
            newx = max(self.x - 1, 0)
        elif key == "d":
            newx = min(self.x + 1, gamestate.MAP_WIDTH)
        if not gamestate.entities.entities_at(newx, newy):
            gamestate.entities.remove_entity(self)
            self.x = newx
            self.y = newy
            gamestate.entities.add_entity(self)
        gamestate.focusX = self.x
        gamestate.focusY = self.y
