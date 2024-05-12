from datetime import datetime

# fecha completa con año mes dia hora minuto y segundo
def time_complete():
    time = datetime.now()
    time = time.replace(microsecond=0)
    return time

# funcion que agrega cada exepcion que ocurra y la registra en el archivo de texto
def exeptions(exepcion):
    file = open("exeptions.txt",'a')
    error = f"{time_complete()}: {exepcion}"
    file.write('\n'+error)