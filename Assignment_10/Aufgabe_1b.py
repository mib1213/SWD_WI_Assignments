vA = [1, 2, 3]
vB = [2, 3, 4]

def vector_addition_wrong(vA, vB):
    result = [None] * len(vA)
    for i in range(1, len(vA)):
        result[i] = vA[i] + vB[i]
    return result

def vector_addition_correct(vA, vB):
    return [a + b for a, b in zip(vA, vB)]

print(vector_addition_wrong(vA, vB))
print(vector_addition_correct(vA, vB))