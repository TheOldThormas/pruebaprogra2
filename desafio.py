print("este es un programa para agregar nombre y precio a un archivo a traves de una variable de tipo directorio")
archivo=open("desafio.txt","a")# Abrir el archivo en modo append
contador=0
Biblioteca ={}
while contador<10000000:
    libro = input("para finalizar escriba (n) sino escriba el nombre del libro   ")
    contador+=1
    if libro == "n":
        break
    else:
        precio=int(input("coloque el precio del libro mencionado  "))
        Biblioteca[libro] = precio
archivo.write(str(Biblioteca))# escribir el archivo
archivo.close()# Cerrar el archivo

print("verción 2 de un programa para agregar nombres y precios a un archivo utilizando un diccionario")

archivo = open("desafio.txt", "a")# Abrir el archivo en modo append
Biblioteca = {} 

while True:# cambiar el tipo de variable para ahorrarce el contador en la funcion repetir
    libro = input("Para finalizar, escriba 'n'. De lo contrario, escriba el nombre del libro:   ")
    if libro == "n":
        break
    else:
        precio = int(input("Ingrese el precio del libro:    "))
        Biblioteca[libro] = precio #agrega esa información al diccionario Biblioteca, donde el nombre del libro se convierte en la clave y el precio se convierte en el valor asociado.

archivo.write(str(Biblioteca)) # escribir el archivo


opción = input('¿Desea ver lo que ha guardado? (s/n): ')
if opción.upper() == 'S':
    print(Biblioteca)
else:
    print('Adiós')


archivo.close() # Cerrar el archivo