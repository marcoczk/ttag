from game_state import GameState


class Window:
    def __init__(self, width: int, height: int, posX: int, posY: int, visible: bool = True):
        self.height = height
        self.width = width
        self.posX = posX
        self.posY = posY
        self.content = {}
        self.visible = visible

    def update(self, game_state: GameState):
        pass

    def pass_key(self, key: str, game_state: GameState):
        if key == "h":
            self.visible = not self.visible
        self.update(game_state)

    def true_click_pos_at_game(self, posX: int, posY: int, game_state: GameState) -> tuple[int, int]:
        true_posX = game_state.focusX + posX - int(game_state.game_window_width / 2) - game_state.game_window_baseX
        true_posY = game_state.focusY + posY - int(game_state.game_window_height / 2) - game_state.game_window_baseY
        return true_posX, true_posY

    def get_menu_base(self, console_width: int, console_height: int) -> tuple[int, int]:
        menu_baseX = self.posX if self.posX >= 0 else console_width + self.posX
        menu_baseY = self.posY if self.posY >= 0 else console_height + self.posY
        return menu_baseX, menu_baseY

    def true_click_pos_at_menu(self, posX: int, posY: int, console_width: int, console_height: int) -> tuple[int, int]:
        baseX, baseY = self.get_menu_base(console_width, console_height)
        return posX - baseX, posY - baseY

    def pass_click(self, posX: int, posY: int, console_width: int, console_height: int, game_state: GameState):
        pass

    def create_border(self, wall: str):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if y == 0 or x == 0 or y == self.height - 1 or x == self.width - 1:
                    self.content[(x, y)] = wall

    def render(self, game_state: GameState) -> list[list[chr]]:
        result = []
        for y in range(0, self.height):
            line = ""
            for x in range(0, self.width):
                if len(line) > x:
                    line = line + self.content.get((x, y), "")
                else:
                    line = line + self.content.get((x, y), " ")
            result.append(line)
        return result
