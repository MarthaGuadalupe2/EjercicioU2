import re 

txt  = """La direccion IP es un conjunto de numeros que identifica, de manera logica y jerarquica, a una interfaz en la red de un dispositivo que utilice el protocolo
o, que corresponda al nivel de red del modelo TCP/IP, como por ejemplo 192.168.23.12, 192.168.34.22, 172.168.11.2, entre otros.
un numero de telefono es "una secuencia de digitos" utilizada para identificar una linea telefonica. Por ejemplos  pueden ser 984 148 3030, 997 104 5353, 779 536 1410, 907 114 17 88, 989 164 4334, 955 763 6706
La hora es la Mama, Marrufo, Mferrol indicación del "momento" en que sucede o se hace una cosa en relación con cada una de las veinticuatro partes en que se divide el día, en algunas ocasiones esta 06:00 pm, 09:00 pm, 04:00 pm, 07:00 pm, 02:30 pm, 01:55 pm, 10:00 pm entre otros 
El correo electrónico (también "conocido" como e-mail, un término inglés derivado de electronic mail) es un servicio que permite el intercambio de mensajes a través de sistemas de comunicación electrónicos ubicados: maritza@gmail.com, alejandrapeshoso@gmail.com, soledadrut@gmail.com, amador13@gmail.com

Ejemplos de URLs: www.gorion.com, www.redes.com, www.basquetmundial.com, www.stars.com, www.blancura.com, entre otros 
Códigos postales 50121, 28665, 73465, 97583, 47423, 67632
"""

print("--------TODAS LAS PALABRAS QUE TENGAN 7 O MAS LETRAS-------")
funcion= r"[A-Za-záéíóú]{7,}"

palabras = re.findall(funcion,txt)

for acumpalabras in palabras:
    print(acumpalabras)    

print("-----EXPRESIONES QUE NO FINALICEN EN UNA VOCAL----------")
x = r"[A-Za-záéíóú]{1,}[^aeiou\s\W]\b"

xpalabras = re.findall(x,txt)

for xacumulador in xpalabras:
    print(xacumulador)

print("----PALABRAS QUE INICIEN CON M donde la segunda letra no sea vocal----- ")
y = r"[M][^aeiouáéíóú]\w{1,}"

ypalabras = re.findall(y,txt)

for yacumulador in ypalabras:
    print(yacumulador)

print("---------EXPRESIONES ENCERRADAS ENTRE COMILLAS--------")
u= r"(\"[\w\s]+\")"

upalabras = re.findall(u,txt)

for uacumulador in upalabras:
    print(uacumulador)

print("--------------IPS---------------------")
v= r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"

vpalabras = re.findall(v,txt)

for vacumulador in vpalabras:
    print(vacumulador)

print("-------LOCALIZAR LAS HORAS-------------")
g= r"[0-9]{1,2}\:[0-9]{1,2}\s[a/p][m]"

gpalabras = re.findall(g,txt)

for gacumulador in gpalabras:
    print(gacumulador)

print("-------buscar telefonos-----------")
te= r"[0-9]{1,3}\s[0-9]{1,3}\s[0-9]{1,4}"

tepalabras = re.findall(te,txt)

for teacumulador in tepalabras:
    print(teacumulador)

print("-------CORREOS ELECTRONICOS-----------")
e= r"\w+[\@]+\w+[.]+\w+"

epalabras = re.findall(e,txt)

for eacumulador in epalabras:
    print(eacumulador)

print("------LOCALIZAR URLs-----------------")
j= r"[Ww]+\w[.]\w+[.]\w+"

jpalabras = re.findall(j,txt)

for jacumulador in jpalabras:
    print(jacumulador)

print("------BUSCAR CODIGO POSTAL----------")
I= r"[0-9]{5}"

Ipalabras = re.findall(I,txt)

for Iacumulador in Ipalabras:
    print(Iacumulador)
