def isLeap(year) -> str:
    return "12" if (year % 400==0) or (year%4==0 and year%100!=0) else "13"

def dayOfProgrammer(year):
    
    if year == 1918:
        return "26.09.1918"
    else: 
        return isLeap(year) + f".09.{str(year)}"
    
