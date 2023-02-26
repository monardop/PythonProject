# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#
def angryProfessor(k: int, a: list[int]) -> str:
    count = 0
    a.sort()
    for student in a:
        if student <= 0:
            count += 1
            if count == k:
                return "NO"
    return "YES"
    
        
    

