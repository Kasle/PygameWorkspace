def translate(value, a, b, A, B):
    firstScale = b - a
    secondScale = B-A
    position = value - a
    position = position / float(firstScale)
    return secondScale * position + A
