from datetime import datetime
from os import path

# fecha completa con año mes dia hora minuto y segundo
def time_complete():
    time = datetime.now()
    time = time.replace(microsecond=0)
    return time

def exeptions(exepcion):
    ruta_errores = path.join("exeptions.txt")
    file = open(ruta_errores,'a')
    error = f"{time_complete()}: {exepcion}"
    file.write('\n'+error)