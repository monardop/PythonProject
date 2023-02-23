def maxCost(cost: list, labels: list, dailyCount: int) -> int:
    # Write your code here
    suma_diaria = []
    cantidad_aceptada = 0
    suma = 0

    for i in range(len(cost)):
        if labels[i] == "legal":
            cantidad_aceptada += 1
        suma += cost[i]
        if cantidad_aceptada == dailyCount:
            suma_diaria.append(suma)
            suma = 0
            cantidad_aceptada = 0
    try:
        return max(suma_diaria)
    except ValueError:
        return 0

lista = []
max(lista)
        