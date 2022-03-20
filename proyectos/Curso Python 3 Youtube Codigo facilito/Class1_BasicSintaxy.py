print("hio")

# --- Variables se almacenan en RAM
variable = 3 * 7
print(variable)

curso = "Estamos en Youtube curso"

# No mayusculas inicio nombre variable
#Haber = "Variable mal escrita por mayuscula"

# Es preferible escribir variables con '_'
variable_bien_escrita = "todo en minuscula y _ para separar palabras"
print(curso, variable_bien_escrita)

number_one = 4
number_two = 10 # abajo se re define su valor
number_two = -50
suma = number_one + number_two
print(suma)

number_float = 13.34565
number_thre = 44
number_division = number_thre / number_float
print(number_division)
# Regresa un numero entero, redondeado, No Float
number_division = number_thre // number_float
print(number_division)

# Exponencial de un numero
number_one = 3
number_two = 5
number_exponential = number_two ** number_one
print(number_exponential)

# ------ Strings
string_one = "What's up!"
string_two = 'doble comillas "asi" dentro del las comillas simples'
print(string_one, " -- " ,string_two)
print(string_one + " -- " + string_two)
string_thre = "hola salto de lines \nhola desde segunda linea"
print(string_thre)

### Union de string Dynamica <3 GENIALLLLLLLLLLLLLLLL
string_one = "Alan"
string_two = "Youtube"
print("Hola %s desde %s" %(string_one, string_two))
print("Total: %s, de los numeros %s y %s" %((number_one+ number_two), number_one, number_two))
print("Otra forma de Total: {}, de los numeros {} y {}".format((number_one+number_two), number_one, number_two))

string_one = "Caracteres transformar a lista"
# Al transformar un string a una lista puedo acceder a sus caracteres desde posicion 0
string_transform_lista = string_one[0]
print(string_transform_lista)
# Recorrer desde adelante a atras (con numeros negativos)
string_transform_lista = string_one[-1]
print(string_transform_lista)
# recorrer un conjunto de caracteres (sub lista)
print(string_one[4:20])
# recorrer conjunto caracteres desde adelante a atras
print(string_one[-7:-1])
# string leido completo desde adelante a atras
print(string_one[::-1])

