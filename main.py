from barberia import *
from cliente import *
from barbero import *

async def main():
    barberia = Barberia()
    barbero = Barbero()
    clientes = [Cliente(i) for i in range(10)]
    tareas_clientes = [cliente.afeitar(barberia) for cliente in clientes]
    tarea_barbero = barbero.trabajar(barberia)
    await asyncio.gather(tarea_barbero, *tareas_clientes)

if __name__ == '__main__':
    asyncio.run(main())