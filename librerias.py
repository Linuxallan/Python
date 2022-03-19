import random
# random para numeros entre los que yo entrego por parametros
aleatorio = random.randint(1, 100)
print(aleatorio)

# random para una lista
lista = [12, True, "fdfd", False]
alea = random.choice(lista)
print(alea)

## saver la hora acutual
import datetime
print(datetime.datetime.now())

## trabajar con opciones del systema como con la bbara de progreso
import sys
import time
# importacion 'time' es solo para que en este ejemplo se haga un delay en la barra de progreso
for i in range(100):
    time.sleep(0.01)
    #sys.stdout.write("-")
    sys.stdout.write("\r%d %%" % i)
    sys.stdout.flush()


## resivir argumentos que vienen al ejecutar nuestro script
import sys
print(sys.argv)
# para pasar augumentos aqui al ejecutar el comando:
# 'python3 librerias.py' en la consola se le deben agregar parametros asi:
# 'python3 librerias.py param_1 param_2 etc...'
if(len(sys.argv) == 1):
    print("agrega a lo menos un argumento")
else:
    print(sys.argv)