def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Dividir la lista en mitades
    mitad = len(arr) // 2
    mitad_izquierda = arr[:mitad]
    mitad_derecha = arr[mitad:]
    
    # Recursivamente ordenar cada mitad
    mitad_izquierda = merge_sort(mitad_izquierda)
    mitad_derecha = merge_sort(mitad_derecha)
    
    # Combinar las mitades ordenadas
    return fusionar(mitad_izquierda, mitad_derecha)

def fusionar(izquierda, derecha):
    fusionado = []
    indice_izquierda, indice_derecha = 0, 0
    
    # Comparar elementos de ambas mitades y agregar al resultado fusionado
    while indice_izquierda < len(izquierda) and indice_derecha < len(derecha):
        if izquierda[indice_izquierda] < derecha[indice_derecha]:
            fusionado.append(izquierda[indice_izquierda])
            indice_izquierda += 1
        else:
            fusionado.append(derecha[indice_derecha])
            indice_derecha += 1
    
    # Agregar los elementos restantes de las mitades no vacías
    fusionado.extend(izquierda[indice_izquierda:])
    fusionado.extend(derecha[indice_derecha:])
    
    return fusionado

# Pedir al usuario que ingrese la lista de números
entrada = input("Ingresa la lista de números separados por espacios: ")
lista_entrada = [int(x) for x in entrada.split()]

print("\nLista original:")
print(lista_entrada)

# Ordenar la lista utilizando Merge Sort
lista_ordenada = merge_sort(lista_entrada)

print("\nLista ordenada:")
print(lista_ordenada)
