from game_state import GameState
from windows.window import Window


class Renderer:
    def __init__(self, CONSOLE_WIDTH: int, CONSOLE_HEIGHT: int):
        self.CONSOLE_WIDTH = CONSOLE_WIDTH
        self.CONSOLE_HEIGHT = CONSOLE_HEIGHT

    def render(self, game_state: GameState, menus: list[Window]) -> list[str]:
        lines = []
        for y in range(0, self.CONSOLE_HEIGHT):
            curr_line = list()
            for x in range(0, self.CONSOLE_WIDTH):
                curr_line = curr_line + list(" ")
            lines.append(curr_line)

        for menu in menus:
            if not menu.visible:
                continue
            menu_render = menu.render(game_state)
            menu_baseX, menu_baseY = menu.get_menu_base(self.CONSOLE_WIDTH, self.CONSOLE_HEIGHT)
            for y in range(menu_baseY, menu_baseY + menu.height):
                for x in range(menu_baseX, menu_baseX + menu.width):
                    lines[y][x] = menu_render[y - menu_baseY][x - menu_baseX]

        result = []
        for y in range(0, self.CONSOLE_HEIGHT):
            result.append(''.join(lines[y]))
        return result
