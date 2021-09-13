# Importamos la librería para leer archivos json
import json

# Abrimos el archivo master en modo lectura ('r') con todos los id de los archivos descargados
with open('master.json', 'r') as f:
    # Guardamos en la variable lista el contenido de master
    lista = json.load(f)

# En este ejemplo se representa cómo se asignaría a la lista archivos específicos
#lista = ['2095303', '2169202'] 

# Abrimos el archivo tryall.json en modo lectura ('w'), si no está creado previamente
# se crea en este momento, se puede cambiar nombre a este archivo
with open('tryall.json', 'w') as outfile: 

    # Iniciamos un contador para ir marcando cuántos archivos llevamos unidos
    contador = 0
    # Esta variable ayuda a guardar el nombre del archivo anterior para 
    # corroborar si no se está repitiendo con el anterior
    helper = 0
    # Esta variable nos indica que tenemos que escribir dentro del documento lo que hay
    # dentro del archivo actual
    update =  True

    # Recorremos toda la lista de archivos descargados
    for names in lista: 
  
        # Abrimos cada archivo         
        with open(f'{names}.json') as infile:
            # Leemos los primeras 3 líneas
            infile.readline()
            infile.readline()
            infile.readline()
            # Guardamos el contenido de la 4° que tiene el número del thread
            # en una variable temportal
            temp = infile.readline()
            # Comprobamos si helper tiene el mismo contenido que temp
            if helper != temp:
                # Si es diferente se puede hacer la actualización ya que no se va 
                # a tener threads repetidos
                update = True
                # asignamos el nuevo contenido a la variable persistente 
                helper = temp
            # Si tienen el mismo contenido entonces no se hace la actualización
            else:
                update = False

        # Abrimos nuevamente el archivo
        with open(f'{names}.json') as infile: 
            # Si el post no está repetido entra         
            if update == True:
                # Se escribe el contenido completo del thread en el archivo de salida
                outfile.write(infile.read()) 

        # Se aumenta el contador ya que se escribió un documento nuevo
        contador+=1
        # Se imporime el contador con el nombre del archivo leído
        print(contador, names)
        # Se pone un salto de página para escribir el contenido del archivo siguiente
        outfile.write("\n") 