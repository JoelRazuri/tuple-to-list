"""
    Escribir una función que reciba una lista de tuplas (Apellido, Nombre, 
    Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero 
    el nombre, luego la inicial con un punto, y luego el apellido.
"""


def lista_nombres(tupla):

    lista = []

    for apellido, nombre , inicial in tupla:
        texto = f"{nombre} {inicial}. {apellido}"
        lista.append(texto)
    
    return lista


print(lista_nombres((('Rodriguez','Patricio','J'),('Rázuri','Axel','J'),('Lentner','Federico','D'))))