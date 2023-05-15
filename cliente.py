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
                print(f"El cliente {self.id} terminó de ser afeitado y se va de la barberia")
                