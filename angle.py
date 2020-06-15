import math

def angleB(a, b, c):
    # ここから書きましょう
    ab = [a[0] - b[0], a[1] - b[1]]
    bc = [c[0] - b[0], c[1] - b[1]]

    inner_product = ab[0] * bc[0] + ab[1] * bc[1]
    size_ab = math.sqrt(ab[0] ** 2 + ab[1] ** 2)
    size_bc = math.sqrt(bc[0] ** 2 + bc[1] ** 2)

    answer = math.degrees(math.acos(inner_product / (size_ab * size_bc)))
    return math.floor(answer)

print(angleB([0,0],[1,1],[1,0]))
print(angleB([4,3],[4,0],[0,0]))
print(angleB([6,5],[9,5],[4,1]))