"""
Extraccion de atributos privados por medio de: Method y Propiedad.
@property convierte un metodo en propiedad. Pero se ejecuta tal cual como method.
"""
class Usuario:

    def __init__(self, username, password) -> None:
        self.username = username
        self.__password = self.__generar_password(password)
    
    def __generar_password(self, password):
        return password.upper()

    # Retornar un atributo privado por medio de un Method.
    def get_password(self):
        return self.__password
    
    # @property -> transforma el Method en Propiedad 
    # Retorna un atributo privado por medio de una Propiedad.
    @property
    def password(self):
        return self.__password

user = Usuario("Alan", "pass1234")
# Extraccion de atributo por medio de Method.
print(user.get_password())
# Extraccion de atributo por medio de Propiedad.
print(user.password)


"""
Method Static para usarlos como atributos no modificables a diferencia del ejemplo de _pi
"""
class Circulo:

    # Este atributo es modificable
    # _pi = 3.1416

    # Esto es un methodo estatico que le pertenece a la clase, por lo que 
    # puede ser accedida desde afuera sin primero instanciar.
    # Pero la gracia de este metodo que a diferencia del atributo el codigo
    # no deja alterar su valor, solo llamarla.
    @staticmethod # SI es necesario este decorador para que el metodo sea 'static'.
    def pi():
        return 3.1416

    # Es como el constructor
    def __init__(self, radio) -> None:
        self.radio = radio
        # Atributo privado: '__bla...'
        self.__area = self.pi() * (radio ** 2)
    
    def get_area(self):
        return self.__area

# Accedo a un Method statico que le pertenece a la clase, instancia tambien.
print(Circulo.pi())

circulo = Circulo(4)
print(circulo.get_area())