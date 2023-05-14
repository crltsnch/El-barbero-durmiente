from barberia import *

class Cliente:
    def __init__(self, id):
        self.id = id
    
    async def afeitar(self, barberia):
        async with barberia.fila:
            print(f"El cliente {self.id} se sienta en la fila de espera")
            async with barberia.silla:
                print(f"El cliente {self.id} está siendo atendido por el barbero")
                await asyncio.sleep(2)
                print(f"El cliente {self.id} terminó de ser afeitado y se va de la barberia")
                