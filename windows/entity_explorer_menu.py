from windows.window import Window
from game_state import GameState
from windows.game_window import GameWindow


class EntityExplorerMenu(Window):

    def update(self, game_state: GameState):
        self.create_border("8")

    def pass_click(self, posX: int, posY: int, console_width: int, console_height: int, game_state: GameState):
        self.content = {}
        trueX, trueY = self.true_click_pos_at_game(posX, posY, game_state)
        self.content[(1, 1)] = "X::"
        self.content[(4, 1)] = str(trueX)
        self.content[(1, 2)] = "Y::"
        self.content[(4, 2)] = str(trueY)

        entities_at_click = game_state.entities.entities_at(trueX, trueY)
        if len(entities_at_click) == 0:
            self.content[(1, 3)] = "No entities"
        i = 0
        for entity in entities_at_click:
            self.content[(1, 3 + i)] = "ObjectType::"
            self.content[(13, 3 + i)] = entity.label
            i = i + 1

        for y in range(0, self.height):
            for x in range(0, self.width):
                if y == 0 or x == 0 or y == self.height - 1 or x == self.width - 1:
                    self.content[(x, y)] = "8"
