import asyncio

class Barberia:
    def __init__(self):
        self.silla = asyncio.Lock()
        self.fila = asyncio.Semaphore(4)
    
    