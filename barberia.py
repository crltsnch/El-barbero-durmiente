import asyncio

class Barberia:
    def __init__(self):   #dos atributos: silla y fila
        self.silla = asyncio.Lock()    #lock para la silla
        self.fila = asyncio.Semaphore(4)  #semaforo para controlar la acantidad de clientes en la fila
        
    
    