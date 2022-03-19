try:
    # Este error es que no se puede dividir por 0
    # print(10/0)
    lista = [2,5]
    # accedo a un dato fuera de rango de la lista: error tambien
    print(lista[9])
except Exception as ex:
    # ex: contiene el nombre de la exception explicada
    print(ex)
finally:
    print("Este finaly siempre se ejecuta")