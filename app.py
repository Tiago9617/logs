import csv
entrada = 'entrada.log'
salida = "salida.log"
archivo = open(entrada, 'r')
lineas = csv.reader(archivo)
salida1 = open(salida, 'w')

   
def run():
    logs= []
    opcion = str(input("""Escoja alguno de estos logs
            ERROR
            INFO
            WARN
            """))
    for leer in lineas:
        
        logs.append(leer)##anexo a la lista cada log del archivo original

    for numero in range(202):##cantidad de pociones en la lista logs
        
        cadena = str(logs[numero])##extraigo la cadena en la posicion indicada
        
        posicion = str(logs[numero]).find(opcion.upper())##obtengo la posicion donde se encuentran uno de los logs que el usuario quiere escribir
        
        if opcion.upper() in cadena[posicion:posicion+len(opcion.upper())]:## pregunto si el dato ingresado se encuentra en la cadena
            salida1.write(cadena.strip("[""]''"))##escribo el log en el archivo
            salida1.write("\n")##salto de linea
    print(f"{opcion} {entrada} {salida}")
    archivo.close()
    salida1.close()
if __name__ == '__main__':
    run()   