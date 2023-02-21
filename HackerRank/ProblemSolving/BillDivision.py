def bonAppetit(bill, k, b):
    anna_bill = (sum(bill) - bill[k]) // 2
    if anna_bill == b:
        print("Bon Appetit")
    else:
        print(b - anna_bill)
