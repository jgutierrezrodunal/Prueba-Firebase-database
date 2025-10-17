import os
import sys

if __package__ in (None, ""):
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))   #Copiado y pegado del código del profe, había un error que no existía módulo data y esto lo arregló...

from data.firebase_service import Database


def main():
    
    fb = Database()

    fb.create(123, "monitor", "Asus", "vg249")
    fb.create(456, "Mouse", "Logitech", "G502")

    fb.read(123)
    fb.read(456)

    fb.updt(123, "vg249PLUS")
    fb.updt(456, "G502 ULTRA")

    fb.dlt(123)
    fb.dlt(456)

if __name__=='__main__':
    main()