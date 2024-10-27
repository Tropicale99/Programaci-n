''' 
Strings
Definicion: Un String es una cadena de caracteres
'''
# s = "yo soy tu padre "
'''
Dentro de un string pueden existir caracteres especiales que permiten incluir 
saltos de linea (\n), comillas (\” \’) y tabuladores (\t) las "\t" son espacios como las sidentaciones.
'''
s = " Luke ... \n\t \" yo soy tu padre \""
# print (s)
# >>> Luke ...
#                "yo soy tu padre "
''''
Para pedir un string al usuario se utiliza la funcion input(), y para castearlo se
usa int(), float(), complex() y boolean().
'''
'''
pedir string
a = input (" Ingrese input ")

Ejemplos para castear string
a_int = int (a) = indicar que es un número entero
a_float = float (a) = indicar que es valores con decimales o fraccionarios
a_complex = complex (a ) = indicar números complejos, es decir,
          números que tienen una parte real y una parte imaginaria
a_bool = bool ( a) = indica si un tipo de dato que permite almacenar dos valores True o False 
'''
'''
La comparacion entre dos strings es caracter a caracter (==, ! = (indica "no igual" y se usa para
comparar si dos valores u objetos son diferentes), <, <=, >,>=) segun formato ASCII (orden casi alfabetico).

" hola " == " hola " # >>> True
" hola " == "oli " # >>> False
" hola " != "oli " # >>> True
" hola " < "oli" # >>> True
" hola " > "a" # >>> True

'''
# Podemos acceder a una caracter especıfico del string mediante su ındice, pero
# no modificarlo
# y  o     s  o  y     t  u     p  a  d  r  e
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
#-15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

'''
Funcion len() permite conocer el largo de un string (numero de caracteres). Ası
podemos recorrer un string de largo cualquiera.

s = input (" Ingrese string : ")
j = 0
while (j < len (s) ):
# while: sirve para ejecutar un bloque de código repetidamente mientras se cumpla una condición.
print (s[j ])
j += 1

'''
# s = input (" Ingrese string : ")
# j = 0
# while (j < len (s) ):
#     print (s[j ])
#     j += 1

'''
Para recorrer un string tambien podemos utilizar el comando for (que es una
alternativa a usar whiles).
DIFERENCIA: el while se usa cuando no se conoce el número de repeticiones
mientras que el for se usa cuando se sabe de antemano

'''
# s = input (" Ingrese string : ")
# for i in s:
#     print (i)

'''
Finalmente existen 4 operadores basicos para trabajar con strings.
• a + b → Concatena a y b.
• n * a → Concatena n veces a.
• a in b → Es True ssi a es parte de b.
• a not in b → Es True ssi a no es parte de b.

'''
# a = " hola "; b = " chao "
# print (a+b ) # >>> hola chao (con espacio)
# print (3 * a ) # >>> holaholahola (con espacio)
# print ("ol" in a) # >>> True porque "ol" está dentro de "hola" = a
# print ("ol" not in b ) # >>> True porque "ol" NO está dentro de "chao"

#Ejercicio para poner solo valores pares

'''
def quitar_pares (s ): # funciona con ASCII
    ret = "" #return: sirve para salir y devolver un valor
    i = 0
    while (i < len (s) ):
        if(i % 2 == 1) : # solo agrego posiciones impares
        # el % sirve para hacer el módulo de la división 
        # de dos variables y almacenar el resultado en la primera
            ret += s [i]
        i += 1  
    return ret

Llamamos a la funcion con un string cualquiera
print ( quitar_pares ("yo soy tu padre "))
'''
# En Python, los vectores i, j y k son vectores unitarios
# que se utilizan para definir el sentido positivo de los ejes cartesianos x, y y z

#Ejercicio para invertir una palabra
'''
def invertir ( s):
    ret = "" # String nulo !
    for c in s :
        ret = c + ret
    return ret

llamamos a la funcion con un string cualquiera
print ( invertir ("yo soy tu padre ") )
'''
#Ejercicio para invertir un input
def invertir ( s):
    ret = "" # String nulo !
    for c in s :
        ret = c + ret
    return ret

print ( invertir ("yo soy tu padre ") )

input("Escribe la palabra a invertir ")











