def countingValleys(steps, path):
    # Write your code here
    road_heigh, count_alert = 0, 0
    plane = True

    for letter in path:
        if letter == 'D':
            road_heigh -=1
        else:
            road_heigh += 1
        if plane and road_heigh < 0:
            count_alert +=1
            plane = False
        if road_heigh == 0:
            plane = True 
    return count_alert
print(countingValleys(8, "DUDDDUUDUU"))
        
        