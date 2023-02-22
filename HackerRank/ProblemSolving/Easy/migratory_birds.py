"""
Given an array of bird sightings where every element represents a bird type id, 
determine the id of themost frequently sighted type. If more than 1 type 
has been spotted that maximum amount, return the smallest of their ids.
"""

def migratoryBirds(arr: list) -> int:
    """
    :param arr: type of birds
    :return:
    The lowest most common type of bird sighted
    """
    # Types: 1-5
    type_bird = []
    for type in range(1, 6):
        type_bird.append(arr.count(type))
    return type_bird.index(max(type_bird)) + 1
    