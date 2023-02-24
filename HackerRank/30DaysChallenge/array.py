# invertir e imprimir un array de enteros de la manera a b c d e...
def invertir_array(nros: list):
    cadena = ""
    for n in range(-1, -len(nros)-1, -1):
        cadena += str(nros[n]) + " "
    print(cadena.strip())

invertir_array([1,2,3,4])