def pickingNumbers(a):
    a.sort()
 
    subsets = []
    for i, elem1 in enumerate(a):
        subset = [elem1]
        for j, elem2 in enumerate(a[i+1:]):
            try:
                elem3 = a[i+j]
                if abs(elem1, elem2)<=1 and abs(elem2, elem3)<=1:
                    subset.append(elem2)
            except IndexError:
                pass
        if len(subset) >= 2:
            subsets.append(subset)
    return max([len(subset) for subset in subsets])

