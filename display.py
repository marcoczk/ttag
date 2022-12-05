import tcod
from game import Game
from renderer import Renderer


def display() -> None:
    CONSOLE_WIDTH = 60
    CONSOLE_HEIGHT = 60
    game = Game(CONSOLE_WIDTH=CONSOLE_WIDTH, CONSOLE_HEIGHT=CONSOLE_HEIGHT)
    game.initialize()
    renderer = Renderer(CONSOLE_WIDTH, CONSOLE_HEIGHT)
    tileset = tcod.tileset.load_tilesheet(
        "res/fonts/Anikki_square_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437,
    )
    console = tcod.Console(CONSOLE_WIDTH, CONSOLE_HEIGHT, order="F")
    with tcod.context.new(
            columns=console.width, rows=console.height, tileset=tileset,
    ) as context:
        event_type = ""
        console.clear()
        while True:
            screen = renderer.render(game.game_state, game.windows)
            for y in range(0, CONSOLE_HEIGHT):
                console.print(0, y, screen[y])
            context.present(console)
            console.clear()
            for event in tcod.event.wait():
                context.convert_event(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
                elif isinstance(event, tcod.event.KeyDown):
                    if event.sym == tcod.event.KeySym.ESCAPE:
                        raise SystemExit()
                elif event.type == "TEXTINPUT":
                    key = event.text
                    game.pass_key(key)
                elif event.type == "MOUSEBUTTONDOWN":
                    tile_pos = event.tile
                    game.pass_click(tile_pos.x, tile_pos.y, CONSOLE_WIDTH, CONSOLE_HEIGHT)
