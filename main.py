# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce

lista = list(range(15,100))

print(lista)

def listaDeNumeros(listilla): 
    resultado = list(filter((lambda x: x % 2), listilla)) 
    print(resultado)
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(resultado)



listaDeNumeros(lista)