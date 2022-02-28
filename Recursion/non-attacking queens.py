def find_posiblepositions(n):
    possiblepositions = []
    board = [[0 for i in range(n)] for j in range(n)]

    def place_a_queen():
        