from barberia import *
from cliente import *
from barbero import *

async def main():
    barberia = Barberia()  #creamos intancia barberia
    barbero = Barbero()  #creamos instancia barbero
    clientes = [Cliente(i) for i in range(10)]  #creamos una lista de 10 clientes
    tareas_clientes = [cliente.afeitar(barberia) for cliente in clientes]  #creamos una lista de tareas de los clientes llamando al método afeitar
    tarea_barbero = barbero.trabajar(barberia)  #llamar al método trabajar del barero y ejecutarlo en un bucle infinito
    await asyncio.gather(tarea_barbero, *tareas_clientes) #esperamos a que todas las tareas (afeitado de cliente sy trabajo del barbero) se completen

if __name__ == '__main__':
    asyncio.run(main())  #ejecutamos con asyncio