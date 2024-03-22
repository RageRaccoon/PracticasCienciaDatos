def bubble_sort(arr):
    n = len(arr)
    # Recorrer todos los elementos en la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Pedir al usuario que ingrese la lista de números
entrada = input("Ingresa la lista de números separados por espacios: ")
lista_entrada = [int(x) for x in entrada.split()]

print("\nLista original:")
print(lista_entrada)

# Ordenar la lista utilizando Bubble Sort
bubble_sort(lista_entrada)

print("\nLista ordenada:")
print(lista_entrada)
