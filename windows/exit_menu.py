from windows.window import Window
from game_state import GameState


class ExitMenu(Window):

    def update(self, game_state: GameState):
        self.content[(int(self.width/2 - 2), int(self.height/2))] = "EXIT"
        self.create_border("8")

    def pass_click(self, posX: int, posY: int, console_width: int, console_height: int, game_state: GameState):
        menu_clickX, menu_clickY = self.true_click_pos_at_menu(posX, posY, console_width, console_height)
        if menu_clickY == int(self.height/2) and menu_clickX in range(int(self.width / 2 - 2), int(self.width / 2 - 2) + 4):
            raise SystemExit

        # self.content[(1, 1)] = "X::"
        # self.content[(4, 1)] = str(menu_clickX)
        # self.content[(1, 3)] = "Y::"
        # self.content[(4, 3)] = str(menu_clickY)
