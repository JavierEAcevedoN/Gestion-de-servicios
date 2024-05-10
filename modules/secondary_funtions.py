from datetime import datetime

# fecha completa con año mes dia hora minuto y segundo
def time_complete():
    time = datetime.now()
    time = time.replace(microsecond=0)
    return time