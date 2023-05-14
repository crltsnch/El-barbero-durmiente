from barberia import *

class Barbero:
    def __init__(self):
        self.durmiendo = True
    
    async def trabajar(self, barberia):
        while True:
            print("El barbero está durmiendo")
            async with barberia.fila:
                print("El barbero se ha despertado")
                