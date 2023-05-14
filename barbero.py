from barberia import *

class Barbero:
    def __init__(self):
        self.durmiendo = True
    
    async def trabajar(self, barberia):
        while True:
            print("El barbero está durmiendo")
            async with barberia.fila:
                print("El barbero se ha despertado")
                self.durmiendo = False
                async with barberia.silla:
                    print("El barbero está afeitando a un cliente")
                    await asyncio.sleep(2)
                    print("El barbero terminó de afeitar a un cliente")
                self.durmiendo = True