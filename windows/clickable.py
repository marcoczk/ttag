from game_state import GameState

class Clickable:
    def __init__(self, posX: int, posY: int, label: list[str]):
        self.label = label
        self.height = len(label)
        self.width = len(label[0])
        self.posY = posY
        self.posX = posX

    def is_clicked(self, clickX: int, clickY: int) -> bool:
        if self.posX <= clickX <= self.posX + self.width and self.posY <= clickY <= self.posY + self.height:
            return True
        return False

    def click(self, game_state: GameState):
        pass