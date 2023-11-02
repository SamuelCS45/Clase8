
'''
hasta ahora hemos


trabajado con variabales
que permiten almacenar
un unico valor
'''

edad = 15

altura = 1.88

nombre = "Samuel"

etado = True

'''
En python podemos
usar una variable
que almacena una 
coleccion de datos
y luego ascenderla 
usando un subindice
'''

# Lista de enteros
lista1= [10, 5, 3, 9]

# Lista de decimales
lista2 = [1.78, 2.66, 1.55, 89.4]

# Lista de string
lista3 = ["Lunes","Martes","Miercoles"]


'''
lista de elementos
de disitinto tipo
'''

lista4 = ["Samuel",45,1.92,False]


if __name__ == '__main__':

    '''
    Cantidad de elementos de cada lista:
    '''
    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1)
    lista1[0] = 1
    print()
    print(lista1)

    print(lista1[0])





















