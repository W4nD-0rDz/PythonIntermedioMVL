'''
1. Crear un programa en python que esté dividido en cuatro módulos distintos. 
Los módulos empleados y clientes deberán estar ubicados en un paquete llamado usuarios, el módulo inicio y 
productos deberán estar contenidos en una carpeta que se llame ej5 y que contenga también el paquete usuarios.
2. El módulo clientes deberá darle la posibilidad al usuario de registrar un nuevo cliente o ver los datos de algún cliente.
3. Al registrar un nuevo cliente deberá, por medio de una función llamada gestionar, pedirle nombre y id y almacenar el objeto en una lista llamada clientes.
4. Si el usuario desea ver el cliente, le pedirá el id del cliente y led mostrará el nombre y id correspondiente.
5. El módulo empleados hará exactamente lo mimo que el anterior, pero al registrar un empleado le pedirá nombre y número de legajo.
6. El módulo productos le dará la posibilidad al usuario de registrar un nuevo producto o ver el stock de un producto.
7. Si ingresa un nuevo producto, el sistema le pedirá, por medio de una función llamada gestionar, nombre de producto, precio y cantidad.
8. Al ingresar un nuevo producto se almacenará en una lista llamada productos. 
Si al ingresarlo el mismo ya existe, sumará la cantidad ingresada a la que se encuentra en memoria.
9. Si ingresa la opción de ver stock, el sistema le pedirá el nombre del producto y le informará la cantidad que existe del mismo. 
Además, si la cantidad es menor a 100, le informará que hay que comprar de ese producto.
10. El módulo inicio es el que se ejecutará para correr el programa. Le dará al usuario un mensaje que diga "Papelera Norte" y le preguntará al usuario si quiere gestionar productos, usuarios o ver todo.
11. Si selecciona productos, ejecutará la función gestionar del módulo productos.
12. Si selecciona la opción usuarios, le preguntará si quiere gestionar clientes o empleados. 
De acuerdo con su elección ejecutará la función gestionar del módulo cliente o empleados según corresponda.
13. Si elije ver todo, el sistema le pedirá que indique si quiere ver productos, clientes o empleados. 
Según su elección, le imprimirá todos los datos almacenados en memoria.
IMPORTANTE: OPTIMIZAR LO MÁS POSIBLE EL USO DE MEMORIA A PARTIR DE LA IMPORTACIÓN.
'''