'''
Crear un programa en python que:
1. De un mensaje inicial que diga "Bienvenido a la ANSES"
2. Le pida a través de un menú al usuario que seleccione entre las opciones registrarse, 
ver usuarios, ver datos, borrar usuario y salir del sistema.
3. Si selecciona la opción registrarse deberá almacenar en una lista llamada usuarios un objeto que contenga el nombre, el dni y la edad del usuario. 
Si la edad no es un valor numérico deberá ejecutar una excepción para que la reingrese.
4. El usuario deberá también ingresar una clave la cual deberá no podrá ser accesible desde fuera de la clase. 
Al ingresarla, deberá confirmarla y si lo hace correctamente le imprimirá un mensaje que diga "contraseña almacenada correctamente".
5. Todos los nombres ingresados deberán almacenarse en una lista llamada nombre.
6. Si el usuario selecciona la opción ver usuarios, deberán imprimirse desde la lista nombres todos los usuarios registrados hasta el momento.
7. Si selecciona la opción ver datos, el sistema le pedirá el dni del usuario que desea ver. 
Al ingresarlo le imprimirá todos los datos (nombre, edad, dni y contraseña). En caso que ingrese un dni que no se encuentra en el sistema, informárselo.
8. Si selecciona borrar usuario, el sistema le pedirá el nombre y lo eliminará de la lista nombres. 
En caso que ingrese un usuario que no se encuentra registrado, el programa se lo informará.
9. Si selecciona la opción salir, e le dará un mensaje de despedida y cerrará la ejecución del programa.
10. Todas las opciones deberán regresar al menú al terminar de ejecutarse.'''