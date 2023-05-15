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
                self.durmiendo = True