def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivote = arr[len(arr) // 2]  
    izquierda = [x for x in arr if x < pivote]  
    medio = [x for x in arr if x == pivote]    
    derecha = [x for x in arr if x > pivote]   

    return quick_sort(izquierda) + medio + quick_sort(derecha)

# Pedir al usuario que ingrese la lista de números
entrada = input("Ingresa la lista de números separados por espacios: ")
lista_entrada = [int(x) for x in entrada.split()]

print("\nLista original:")
print(lista_entrada)

# Ordenar la lista utilizando Quick Sort
lista_ordenada = quick_sort(lista_entrada)

print("\nLista ordenada:")
print(lista_ordenada)
