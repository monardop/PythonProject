def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    cost = round(meal_cost + meal_cost*(tip_percent/100) + meal_cost * (tax_percent/100), 0)

    print(int(cost))
    
solve(10.25, 17, 5)