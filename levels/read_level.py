from PIL import Image


def read_level(name: str) -> list[list[str]]:
    result = []
    im = Image.open(name)  # Can be many different formats.
    pix = im.load()
    width, height = im.size

    for y in range(0, height):
        line = []
        for x in range(0, width):
            if pix[x, y] == (0, 0, 0, 0):
                line.append(" ")
            else:
                line.append("X")
        result.append(line)
    return result
