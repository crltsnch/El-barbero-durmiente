# El-barbero-durmiente

El link a mi repositorio es: [GitHub](https://github.com/crltsnch/El-barbero-durmiente)

#Archivo `barberia.py`

```
import asyncio

class Barberia:
    def __init__(self):   #dos atributos: silla y fila
        self.silla = asyncio.Lock()    #lock para la silla
        self.fila = asyncio.Semaphore(4)  #semaforo para controlar la acantidad de clientes en la fila
```

#Archivo `cliente.py`

```
from barberia import *

class Cliente:
    def __init__(self, id):  #atributo identificador del cliente
        self.id = id
    
    async def afeitar(self, barberia):
        async with barberia.fila:   #adquirir permiso del semaforo  par aentrar a la barbería
            print(f"El cliente {self.id} se sienta en la fila de espera")
            async with barberia.silla:   #asquierir permiso del lock para sentarse en la silla
                print(f"El cliente {self.id} está siendo atendido por el barbero")
                await asyncio.sleep(2)  #simular el tiempo que tarda el barbero en afeitar al cliente
```

#Archivo `barbero.py`

```
from barberia import *

class Barbero:
    def __init__(self):
        self.durmiendo = True
    
    async def trabajar(self, barberia):
        while True:
            print("El barbero está durmiendo")
            async with barberia.fila:   #permiso del semaforo para entrar a la barbería
                print("El barbero se ha despertado")
                self.durmiendo = False
                async with barberia.silla:  #permiso del lock para sentarse en la silla del barbero
                    print("El barbero está afeitando a un cliente")
                    await asyncio.sleep(2)  #simular el tiempo de afeitado
                    print("El barbero terminó de afeitar a un cliente")
```

#Archvio `main.py`

```
async def main():
    barberia = Barberia()  #creamos intancia barberia
    barbero = Barbero()  #creamos instancia barbero
    clientes = [Cliente(i) for i in range(10)]  #creamos una lista de 10 clientes
    tareas_clientes = [cliente.afeitar(barberia) for cliente in clientes]  #creamos una lista de tareas de los clientes llamando al método afeitar
    tarea_barbero = barbero.trabajar(barberia)  #llamar al método trabajar del barero y ejecutarlo en un bucle infinito
    await asyncio.gather(tarea_barbero, *tareas_clientes) #esperamos a que todas las tareas (afeitado de cliente sy trabajo del barbero) se completen

if __name__ == '__main__':
    asyncio.run(main())  #ejecutamos con asyncio
    
```    
