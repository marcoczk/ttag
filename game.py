from entity import GameEntity
from player import Player
from game_state import GameState
from windows.window import Window
from windows.player_pos_menu import PlayerPosMenu
from windows.entity_explorer_menu import EntityExplorerMenu
from windows.game_window import GameWindow
from windows.exit_menu import ExitMenu
from windows.spell_menu import SpellMenu
from levels.read_level import read_level


class Game:
    def __init__(self, game_state: GameState = None, menus: list[Window] = [], CONSOLE_WIDTH=60, CONSOLE_HEIGHT=60):
        self.game_state: GameState = game_state if game_state is not None else GameState(MAP_WIDTH=80, MAP_HEIGHT=80)
        self.windows: list[Window] = menus
        self.CONSOLE_WIDTH = CONSOLE_WIDTH
        self.CONSOLE_HEIGHT = CONSOLE_HEIGHT

    def initialize(self):

        level = read_level("levels/test.png")
        sizeY, sizeX = (len(level), len(level[0]))
        for y in range(0, sizeY):
            for x in range(0, sizeX):
                if level[y][x] == "X":
                    self.game_state.entities.add_entity(GameEntity(x, y, "W"))
        self.game_state.MAP_WIDTH = sizeX
        self.game_state.MAP_HEIGHT = sizeY

        playerOb = Player(40, 40, "X", "player")
        self.game_state.focusX = playerOb.x
        self.game_state.focusY = playerOb.y

        self.game_state.entities.add_entity(playerOb)
        self.game_state.player = playerOb
        self.windows = []
        self.game_state.game_window_baseX = 0
        self.game_state.game_window_baseY = 0
        self.game_state.game_window_width = self.CONSOLE_WIDTH-15
        self.game_state.game_window_height = self.CONSOLE_HEIGHT
        self.windows.append(GameWindow(
            self.game_state.game_window_width,
            self.game_state.game_window_height,
            self.game_state.game_window_baseX,
            self.game_state.game_window_baseY))
        # self.windows.append(PlayerPosMenu(10, 10, 0, 0))
        self.windows.append(SpellMenu(15, self.CONSOLE_HEIGHT, -15, 0))
        # self.windows.append(EntityExplorerMenu(20, 6, -20, 0))
        self.windows.append(ExitMenu(10, 5, -10, -5))

        self.game_state.player.spells = ["fireball"]

        for menu in self.windows:
            menu.update(self.game_state)

    def pass_key(self, key: str):
        for menu in self.windows:
            menu.pass_key(key, self.game_state)

    def pass_click(self, posX: int, posY: int, console_width: int, console_height: int):
        for menu in self.windows:
            menu.pass_click(posX, posY, console_width, console_height, self.game_state)
