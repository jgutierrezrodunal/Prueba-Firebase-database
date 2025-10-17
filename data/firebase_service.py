
import firebase_admin                      
from firebase_admin import credentials, db 

cred = credentials.Certificate('data/Credencialesprueba.json')

firebase_admin.initialize_app(cred, {'databaseURL':'https://test-poo-37180-default-rtdb.firebaseio.com/'})


class Database:
    def __init__(self):
        pass

    def create(self, id, tipo, marca, modelo):
        ref = db.reference(f'/Productos/{id}')
        ref.push({'tipo': tipo,'marca': marca,'modelo': modelo})
                
    def read(self, id):
        ref = db.reference(f'/Productos/{id}')
        todos = ref.get()

        for key, val in todos.items():
            print(f"{key}: {val['tipo']},{val['marca']},{val['modelo']}")

    def updt(self, id, modelo):
        ref = db.reference(f'/Productos/{id}')
        ref.update({'nuevo modelo': modelo})

    def dlt(self, id):
        ref = db.reference(f'/Productos/{id}')
        ref.delete()






        