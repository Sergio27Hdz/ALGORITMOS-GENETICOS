import random
import math
from random import randint

#GENERACION DE POBLACION 
#1.Recibe como entrada el tamaño de la población y genera como salida una lista de cromosomas.
obj_entrada= int(input("Introduce la cantidad de objetos totales: "))
pob_entrada = int(input("Introduce el tamano de la poblacion: "))
objetos= (2**obj_entrada)-1
aptitud_total=0
aptitudes={} #crea diccionario vacío
lista_apt=[]
mejor_cromosoma=''
mejor_aptitud=0
repeticion=5
li_rul = []
lista_rul= []


lista = range(1,objetos)
poblacion = random.sample(lista, k=pob_entrada)
print("\n[GENERACION DE POBLACION]\n")
print(poblacion)

#.append =  agregar en lo ultimo de la lista el elemento()
lista_bin = []
for i in poblacion:
  binario=bin(i)[2:] 
  binario=binario.zfill(obj_entrada) 
  lista_bin.append(binario)

print("\nLISTA DE BINARIO")
print(lista_bin)

lista= range(1,70)
peso_de_objetos= random.sample(lista, k= obj_entrada) #Se crean los valores del peso de la mochila
lista= range(1,90)
ganancia_de_objetos= random.sample(lista, k= obj_entrada) #Se crean los valores de la ganancia de la mochila
cap_mochi = random.randint(100, 350)  #Se crea la capacidad de la mochila

print("\nCAPACIDAD MOCHILA") 
print(cap_mochi)
print("\nPESO DE OBJETOS")
print(peso_de_objetos)
print("\nGANANCIA DE OBJETOS")
print(ganancia_de_objetos)
#EVALUACION
#2-Recibe como entrada una lista de cromosomas y una instancia del problema de la mochila (capacidad, valores y pesos de los objetos); devuelve un diccionario donde cada elemento tiene la forma (cromosoma, aptitud). 



for i in range(repeticion):
  aptitud_total=0
  for cromosoma in lista_bin:
      aptitud=0.0
      peso=0.0
      for i in range(0,obj_entrada):
          aptitud+=int(cromosoma[i])*ganancia_de_objetos[i] #Dentro de esta instrucción se encuentra almacenando las aptitudes generadas por la ganancia de los objetos
          peso+=int(cromosoma[i])*peso_de_objetos[i]
      if peso > cap_mochi:
          aptitud=0.0
      if aptitud> mejor_aptitud:
        mejor_aptitud= aptitud
        mejor_cromosoma=cromosoma
      lista_apt.append(aptitud)
      aptitudes[cromosoma]=aptitud #guarda la aptitud teniendo como clave el numero binario
      aptitud_total+=aptitud

  print("_________________________________________\n") 
  print("_________________________________________\n")  
  print("[EVALUACION GENERACION ACTUAL]\n")
  for i in range(len(lista_apt)):
    print(lista_apt[i], "     ", lista_bin[i])

  print("Aptitud Total: ", aptitud_total, "\n")
  print("\n_________________________________________\n")  


  #SELECCIÓN   
  #Recibe como entrada un diccionario de elementos con la forma (cromosoma, aptitud) y devuelve el conjunto de parejas a cruzar. Es importante calcular el número de parejas adecuado para reemplazar a la generación actual.  

  
  for i in lista_apt:
    li_rul.append(math.ceil((i/aptitud_total)*100))

  
  ruleta_unit=0
  for cromosoma in aptitudes:
    ruleta_unit=int(math.ceil((aptitudes[cromosoma]/aptitud_total)*100))
    for i in range(0,ruleta_unit):
      lista_rul.append(cromosoma)
  random.shuffle(lista_rul)



  print("_________________________________________\n")  
  print ("[SELECCION]\n")
  for i in range(len(lista_bin)):
    print("Al cromosoma ",lista_bin[i], "le corresponden ", li_rul[i],"espacios")
  print("\n_________________________________________\n")  



  #CRUZA  
  #Recibe como entrada el conjunto de parejas a cruzar y devuelve la lista de cromosomas hijos.  Recuerda que se debe establecer un punto de cruce. Tip: en Python, considera el slicing en cadenas.  


  punto_cruce= randint(1, obj_entrada-1)
  #random.randint(1,obj_entrada-2)
  hijos=[]

  h= int(len(poblacion)/2)
  print("_________________________________________\n")  
  print('[CRUCE]')
  print('El punto de cruce escogido es', punto_cruce)

  for  i in range(h):
  
    madre=random.choice(lista_rul)#Saca un elemento de la ruleta de manera aleatoria para ser mamá y papá
    while True: #verificar si  el padre no es lo mismo que la madre, SINO se             repite
      padre=random.choice(lista_rul)
      if(padre != madre):
        break
      
    primer_hijo=madre[:punto_cruce] + padre[punto_cruce:] #Combinamos las cadenas usando las cromosomas.
    segundo_hijo=padre[:punto_cruce] + madre[punto_cruce:]
    hijos.append(primer_hijo) #Almacenamos a los hijos.
    hijos.append(segundo_hijo)
    print('Papas ', padre, ' ', madre, ' generan hijos ', primer_hijo, ' y ', segundo_hijo)
  
  print("_________________________________________\n")  

  li_rul.clear()
  lista_rul.clear()
  #MUTACIÓN   
  #Recibe como entrada la lista de cromosomas hijos y devuelve estos cromosomas mutados de acuerdo con una probabilidad establecida. Para saber qué genes mutar, se barre cada cromosoma y por cada gen se obtiene un número aleatorio entre 0 y 1. Si este número es menor o igual a la probabilidad de mutación, se muta el gen (0 se cambia por 1 y viceversa)

  prob_mut=random.randint(1,3)/10.0

  lista_bin.clear()

  for cromosoma in hijos:
    crom_mut=''
    for gen in cromosoma:
      resultado=random.randint(1,10)/10.0
      if(resultado <= prob_mut):
        crom_mut+=str(abs(int(gen)-1)) #se cambia 
      else:
        crom_mut+=gen
    lista_bin.append(crom_mut)

  print("_________________________________________\n")  
  print('[MUTACION]')
  for i in range(len(lista_bin)):
    print('Mutacion ', i+1, ': ', lista_bin[i])
  print("_________________________________________\n")  
  print("_________________________________________\n") 
  print("[NUEVA GENERACION]\n") 
  print(lista_bin) #hijos ya mutados



  hijos.clear()
  lista_apt.clear()


aptitud_total=0
for cromosoma in lista_bin:
  aptitud=0.0
  peso=0.0
  for i in range(0,obj_entrada):
    aptitud+=int(cromosoma[i])*ganancia_de_objetos[i] #Dentro de esta instrucción se encuentra almacenando las aptitudes generadas por la ganancia de los objetos
    peso+=int(cromosoma[i])*peso_de_objetos[i]
  if peso > cap_mochi:
    aptitud=0.0
  if aptitud> mejor_aptitud:
    mejor_aptitud= aptitud
    mejor_cromosoma=cromosoma
  lista_apt.append(aptitud)
  aptitudes[cromosoma]=aptitud #guarda la aptitud teniendo como clave el numero binario
  aptitud_total+=aptitud




print("_________________________________________\n") 
print("_________________________________________\n") 

print ("[MEJOR APTITUD]: ", mejor_aptitud)
print ("[MEJOR CROMOSOMA]: ", mejor_cromosoma)
