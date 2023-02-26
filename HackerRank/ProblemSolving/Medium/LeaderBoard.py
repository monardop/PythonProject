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

print(climbingLeaderboard([100,90,90,80], [70,80,105]))

