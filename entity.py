from enum import Enum


class EntityProperties(Enum):
    INTERACTIVE = 1


class GameEntity:
    def __init__(self, x: int, y: int, val: str, label: str = "", props: [EntityProperties] = []):
        self.x = x
        self.y = y
        self.label = val if label == "" else label
        self.val = val
        self.props: list[EntityProperties] = props
        self.spells: list[str] = []

    def pass_key(self, key: str, game_state: object):
        pass


class EntityArray:
    def __init__(self):
        self.entities: dict[(int, int), list[GameEntity]] = {}

    def add_entity(self, entity: GameEntity):
        if (entity.x, entity.y) in self.entities.keys():
            self.entities[(entity.x, entity.y)].append(entity)
        else:
            self.entities[(entity.x, entity.y)] = [entity]

    def remove_entity(self, entity: GameEntity):
        self.entities_at(entity.x, entity.y).remove(entity)

    def list_all(self) -> [GameEntity]:
        return [entity for entity_list in self.entities.values() for entity in entity_list]

    def entities_at(self, x: int, y: int) -> list[GameEntity]:
        return self.entities.get((x, y), [])

