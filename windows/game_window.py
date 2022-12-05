from game_state import GameState
from windows.window import Window


class GameWindow(Window):

    def update(self, game_state: GameState):
        self.create_border("+")

    def pass_key(self, key: str, game_state: GameState):
        for entity in game_state.entities.list_all():
            entity.pass_key(key, game_state)

    def render(self, game_state):
        lines = []

        CURR_X = game_state.focusX
        CURR_Y = game_state.focusY

        X_OFFSET = int(self.width / 2)
        Y_OFFSET = int(self.height / 2)
        for y in range(0, self.height):
            curr_line = list()
            for x in range(0, self.width):
                curr_entities = game_state.entities.entities_at(CURR_X + x - X_OFFSET, CURR_Y + y - Y_OFFSET)
                if curr_entities:
                    curr_line.append(curr_entities[0].val)
                else:
                    curr_line.append(" ")
            lines.append(curr_line)

        for y in range(0, self.height):
            for x in range(0, self.width):
                content = self.content.get((x, y), "")
                if len(content) == 0: continue
                lines[y][x:x + len(content)] = list(content)

        return lines
