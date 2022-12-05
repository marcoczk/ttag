import random

puzzles = [
[
"XX XX",
"X   X",
"     ",
"X   X",
"XX XX"],
[
"XXXXX",
"X   X",
"     ",
"X   X",
"XXXXX"],
[
"XX XX",
"X   X",
"X   X",
"X   X",
"XX XX"],
[
"XX XX",
"X   X",
"X   X",
"X   X",
"X   X",
"X   X",
"X   X",
"X   X",
"XX XX"],
[
"XX XXX XX",
"X       X",
"         ",
"X       X",
"X   X   X",
"X       X",
"         ",
"X       X",
"XX XXX XX"]
]


# def generate_level(width: int, height: int) -> list[list[chr]]:
#     room_poss = list()
#     for i in range(0, 5):
#         pos = (random.randint(0, width), (0, height))
#         if pos in room_poss:
#             continue
#         room_poss.append(pos)
#     return level
