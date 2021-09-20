def IsIn(pattern,grid):
    # if(len(pattern)==1):
    #     return True
    for i in range(len(grid) - len(pattern)+1):
        for j in range(len(pattern)-1):
            if(pattern[j] in grid[i+j] and  grid[i+j].find(pattern[j]) ==  grid[i+j+1].find(pattern[j+1])):
                pass
            else:
                break
        else:
            return True
    return False


t = int(input().strip())
for i in range(t):
    R,C = list(map(int,(input().strip().split())))
    grid = []
    for i in range(R):
        grid.append(input().strip())

    r,c = list(map(int,(input().strip().split())))
    pattern = []
    for i in range(r):
        pattern.append(input().strip())
    
    print( "YES" if   IsIn(pattern,grid) else "NO")