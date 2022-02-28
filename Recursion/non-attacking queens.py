
def place_a_queen(n):
    def solve_n_queens(row):
       
        if row == n:
            
            result.append(col_placements[:])
            return
        for col in range(n):
            if all(
                abs(col - c) not in (0,row-i) 
                for i,c in enumerate(col_placements[:row])):
                    col_placements[row] = col
                    solve_n_queens(row+1)

    result = []
    col_placements = [0 for i in range(n)]

    solve_n_queens(0)

    print(result)

place_a_queen(10)