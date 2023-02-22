def formingMagicSquare(s):
    ls_possible_square = [
        [[2,9,4],[7,5,3],[6,1,8]],
        [[2,7,6],[9,5,1],[4,3,8]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[8,1,6],[3,5,7],[4,9,2]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[4,9,2],[3,5,7],[8,1,6]],
    ] 
    cost = 0
    min_cost = 72
    for x in ls_possible_square:
        for i in range(3):
            for j in range(3):
                cost += abs(x[i][j] - s[i][j])
        if cost < min_cost:
            min_cost = cost        
        cost = 0
    return min_cost