from select import select


class Lapiz:
    color = ''
    contiene_borrador = False

    # mothod '__init__' es como el metodo constructor.
    def __init__(self, color, borrador):
        self.color = color
        self.contiene_borrador = borrador

# Esto es un objeto de clase
lapiz_generico = Lapiz("Grafito", True)
print(lapiz_generico.color)

## metodos y atributos privados : se antepone dos 'guin bajos' -> '__bla...'
class Usuario:

    def __init__(self, username, password, email) -> None:
        self.username = username
        ## atributo privado: '__name_atributo'
        self.__password = self.__generar_password(password)
        self.email = email
    
    # Este metodo privado solo puede ser accedido desde la clase, NO desde la instancia
    def __generar_password(self, password):
        return password.upper()

    def get_password(self):
        return self.__password

user = Usuario("Alan", "pass1234", "add@exc.cl")
# los atributos privados no se pueden leer ni ser accedidos
#print(user.password) <-- error por ser privado
print(user.get_password())

## ---------------------
# variables de clases son globales y modificables sin crear instancia
class Circulo():

    # Estas variables son modificables desde la instancia
    # Por lo que como convencion se les agrega un guin bajo
    # para quienes las encuentren no las modifiquen
    _pi = 3.1416

    def __init__(self, radio) -> None:
        self.radio = radio
        # formula area circulo : pi * r^2
        self.area = self._pi * (radio ** 2)
    
    def get_area(self):
        return self.area

# Accedo a un atributo global de clase sin tener que crear una instancia
print(Circulo._pi)

# Instancio Clase
circulo = Circulo(4)
print(circulo.get_area())