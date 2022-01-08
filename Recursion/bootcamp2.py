def MboardTriominoes(n):
    if n<2:
        return 0
    if n==2:
        return 1
    return 4 * MboardTriominoes(n//2) +1

print(MboardTriominoes(8))