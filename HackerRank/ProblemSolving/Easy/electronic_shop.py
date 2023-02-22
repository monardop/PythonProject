def getMoneySpent(keyboards, drives, b):
    max_budget = 0
    if len(keyboards) > len(drives):
        for keyboard in keyboards:
            for usb in drives:
                price = keyboard + usb
                if price <= b and price > max_budget:
                    max_budget = price  
    else:
        for usb in drives:
            for keyboard in keyboards:
                price = keyboard + usb
                if price <= b and price > max_budget:
                    max_budget = price
    if max_budget == 0:
        return -1
    else:
        return max_budget  
