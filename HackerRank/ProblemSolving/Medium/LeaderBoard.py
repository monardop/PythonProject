def climbingLeaderboard(ranked: list[int], player: list[int]) -> list[int]:
    # Write your code here
    ranked = set(ranked)
    ranked = list(ranked)
    ranked.sort(reverse=True)
    positions = []
    for points in player:
        for rank in ranked:
            if points >= rank:
                positions.append(ranked.index(rank) + 1)
                break
        else:
            positions.append(len(ranked ) + 1)
    return positions



def climbingLeaderboard_alt(ranked, player):
    # Write your code here
    stack = []
    for i,r in enumerate(ranked):
        if i > 0 and ranked[i] == ranked[i-1]:
            continue
        stack.append(ranked[i])
        
    position = {}
    for i,p in enumerate(player):
        if p in position:
            position[p].append(i)
        else:
            position[p] = [i]
            
    newplayer = sorted(player)
    ranks = {}
    for i,p in enumerate(newplayer):
        while stack and stack[-1] <= p:
            stack.pop()
        if p not in ranks:
            ranks[p] = len(stack)+1
           
    return [ranks[p] for p in player]

print(climbingLeaderboard_alt([100,90,90,80], [70,80,105]))