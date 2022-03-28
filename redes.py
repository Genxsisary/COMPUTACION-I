'''
Con la intención de hacer la web más social se han creado múltiples aplicaciones o sitios en Internet que
permiten compartir información y establecercomunicación entre grupos de personas, estos sitios son denominados REDES SOCIALES. Una empresa
de publicidad cuyo lema es “las empresas que invierten en publicidad, son las empresas que permanecen en la
mente de las personas”, quiere evaluar la posibilidad de colocar publicidad en alguna de las tres redes
sociales que considera de mayor uso o más comunes. Para ello se realiza una encuesta a un conjunto W de personas a quienes se les solicita
suministren la siguiente información:
NOMBRE, GÉNERO, EDAD Y RED SOCIAL MÁS UTILIZADA

Desarrolle un programa que procese la información, almacenada en un archivo de nombre REDES.TXT y
genere dos archivos de nombre USAREDSOCIAL.TXT y NOLASENCUESTADAS.TXT, con los nombres de los
usuarios que usan alguna de las tres redes sociales consideradas en el estudio o los que no usan ninguna de las redes sociales consideradas en el
estudio respectivamente, además determine e imprima por pantalla:

✓ Cantidad de personas que utilizan cada uno de las tres principales redes sociales
considerados en la encuesta
✓ Nombre y edad del primer usuario procesado que usa hi5

Consideraciones:
o El género se tomará como 1 =Femenino y 2 = Másculino
o Los valores para tipo de red social más utilizada son 1 =Facebook, 2 =Myspace, 3=Hi5 y
4=Ninguno u otro
o Mientras más usuarios usen una red social, esta se considera más rentable para hacer
publicidad

Actividades a Desarrollar:
1. Identifique los datos de entrada y salida, colocándolos en esta tabla con el tipo de
dato
'''

#Propósito: Ejercicio de listas y archivos
#Materia: Computación I 
#Sección: 02
#Autor: Génesis Ariana Camacho Orozco 
#Fecha: 22-03-2022

#Apertura del archivo
from io import open
arch = open('redes.txt','r')
arch2 = open('usaredsocial.txt', 'w')
arch3 = open('nousaredsocial.txt', 'w')

#Inicialización de las variables 
cont_facebook = 0 
cont_Myspace = 0 
cont_hi5 = 0 
cont_ningunared = 0 
band = 0 

#Proceso
for contenido in arch: 
    lista = contenido.split(",")
    nombre = lista[0]
    género = int(lista[1])
    edad = int(lista[2])
    red = int(lista[3].strip('\n'))

    #Cantidad de personas en las redes 
    if red == 1 :  #Facebook 
        cont_facebook += 1 
    elif red == 2 : 
        cont_Myspace += 1 #Myspace 
    elif red == 3 : 
        cont_hi5 += 1 #hi5 
        if band == 0: 
            nombre1 = nombre 
            edad1 = edad 
            band = 1 
    else :             #Ninguno 
        cont_ningunared +=1 


#Imprimiendo el archivo 
#Usa red social 
if red != 4: 
    arch2.writelines(nombre)

#No usa red social 
else: 
    arch3.writelines(nombre)

#Red de mayor uso 
mayor = cont_facebook
redmayor = 'Facebook'

if cont_Myspace > mayor: 
    redmayor = 'Myspace'
if cont_hi5 > mayor: 
    redmayor = 'hi5'

#Resultados 
print ('Persona 1 de hi:', nombre1, 'de', edad1, 'años')
print('Personas que usan Facebook:', cont_facebook)
print('Personas que usan Myspace', cont_Myspace)
print('Personas que usan hi5', cont_hi5)
print('Personas que no usan ninguna red', cont_ningunared)
print('Red de uso mayor', redmayor)

    
#Cierre del archivo
arch.close()
arch2.close()
arch3.close()