from math import ceil
def lowestTriangle(trianglebase, area):
    return (ceil(area/trianglebase*2))

print(lowestTriangle(34, 999877))
print(lowestTriangle(8378, 42565))