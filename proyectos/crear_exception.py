# Mi clase debe heredar de 'Exception'
# url de License: https://choosealicense.com/licenses/mit/
class MiException(Exception):
    def __init__(self):
        self.message = "Esta exception se ejecuto."
    
    def __str__(self):
        return self.message

def validar_rango(number):
    return number > 0 and number < 256

def validar_valor_ingresado(val):
    try:
        # 'isinstance' valida que el primer parametro ingresado sea de tipo clase
        # igual al segundo parametro ingresado; osea validar que un valor sea de 
        # un tipo de clase, en este caso: 'int'
        return isinstance(int(val), int)
    except Exception as error:
        return False

def validar_valor(number, call_back = None):
    try:
        if validar_valor_ingresado(number) and validar_rango(number):
            return True
        else:
            raise MiException()
    except Exception as error:
        if call_back is not None:
            call_back()
        else:
            print(error)

def call_back_function():
    print("Este call_back se ejecuta al haber un error")

number = int(input("Escribe numero: "))      

print(validar_valor(number, call_back_function))