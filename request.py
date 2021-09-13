# Librería para la petición de los recursos HTTP
import requests
# Librería para leer archivos JSON
import json
# Librería para medir el tiempo
import time

# Esta variable  va a servir para conocer cuánto tiempo ha tardado en hacer todas las operaciones 
t1 = time.perf_counter()

# Mandamos un mensaje a consola para marcar el inicio
print("Ready to get request")

# Hacemos el primer request del archivo del board seleccionado
# --- Nota: el link está establecido con el board /pol/ si se quisiera descargar de otro board
# --- se reemplaza /pol/ por el nombre de otro board como por ejemplo /v/ de videogames
r = requests.get('https://a.4cdn.org/pol/archive.json')

# Guardamos en una variable el contenido del json 
arch_j = r.json()

# Creamos un archivo llamado master donde va a venir la lista de los id de todos los threads a descargar
# En ese mismo paso se abre en modo de escritura ('w') 
with open('master.json', 'w') as f:
    # Se llama a la funcion dump que escribe dentro del archivo f el contenido del json 
    # en este caso arch_j, después se pone un ident para identar las líneas para su fácil lectura
    json.dump(arch_j, f, indent=2)

# Ahora asignamos a una variable el contenido del archivo con la función dumps
# dumps se usa para transformar la información a string, también se le da una identación de 2
archivo_master = json.dumps(arch_j, indent=2)
# Ahora se procede a imprimirlo en consola para verificar el contenido sin abrir el archivo
print(archivo_master)

# Ahora como ya tenemos toda la lista de threads en el archivo, procedemos a recorrerlos uno por uno
for code in arch_j:
    # Asignamos el contenido de la variable code a 'a'
    a = code
    # Imprimimos en consola para saber el nombre del thread a descargarse
    print(a)

    # En la variable temporal urlunica guardamos el enlace al thread a descargar 
    # usando la variable a para asignar el número del thread
    urlunica = f'https://a.4cdn.org/pol/thread/{a}.json'
    # Imprimimos el enlace para corroborar que esté correcto
    print(urlunica)

    # En la variable subr guardamos el nuevo request con ej json del nuevo thread
    subr = requests.get(urlunica)    
    # Imprimimos el request que nos va a imprimir 200 si fue exitoso o 404 si no existe
    print(subr)
    # Imprimimos cuánto tiempo se tardó en descargar el json del thread
    # --- Nota: en las pruebas que se hicieron puede llegar a tardar de 0.1s a 206s 
    print(a," done in ", subr.elapsed.total_seconds())

    # En caso que cuando lleguemos a descargar un archivo 404 al momento de imprimirlo
    # va a mandar una excepción al asignar un objeto nulo, por eso hacemos el try
    try:
        # Asignamos a la variable hilos el contenido del json
        hilos = subr.json()
    except:
        # Si está vacío imprime un mensaje que ya no existe
        print("thread ", a," 404'd")
    
    # Ya que tenemos el contenido del thread, creamos un archivo con su id para almacenar
    # el contenido localmente 
    with open(f'{a}.json', 'w') as f:
        # En el mismo caso de que esté vacío el archivo, va a mandar un error
        # por eso realizamos el try 
        try:
            # Escribimos el contenido del json en el archivo f
            json.dump(hilos, f, indent=2)
        except:
            # Si el archivo está vacío manda un mensaje de error
            print(a," file empty")
    
    # La api de 4chan menciona que se tienen que hacer requests de por al menos un segundo de diferencia
    # por eso mandamos a dormir el ciclo durante 1.5s para evitar cualquier tipo de conflictos,
    # se reocmienda verificar primero el tiempo de descarga para ajustar este valor de acuerdo a este
    time.sleep(1.5)

# Creamos otra variable para almacenar el contador de teimpo de ejecución
t2 = time.perf_counter()
# Imprimimos la diferencia entre las 2 variables de tiempo para conocer el tiempo de ejecución del script
print(f'Done in {t2-t1} seconds')

# En seguida se colocó un ejemplo de un request de un thread individual en caso que se requieran hacer pruebas

#r = requests.get('https://a.4cdn.org/pol/thread/268187198.json')
#print("done in ", r.elapsed.total_seconds())

# Este es un thread que no existe en caso que se necesite verificar el comporntamiento de get 
# en este caso

#https://a.4cdn.org/po/thread/577654.json