def breakingRecords(scores: list):
    total_scores = [0, 0]
    lowest_score = scores[0]
    highest_score = scores[0]
    for n in scores:
        if n > highest_score:
            highest_score = n
            total_scores[0] += 1
        elif n < lowest_score:
            lowest_score = n
            total_scores[1] += 1
    return total_scores 

print(breakingRecords([10,5,20,20,4,5,2,25,1]))