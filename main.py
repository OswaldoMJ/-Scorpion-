print("Nombre: Walter Oswaldo Matul Jeatas, Carnet: 1562923")
 
 
import os 

mi_ubicacion = os.getcwd()
if os.path.exists("modulos"):
    print("La carpeta ya existe")
else:
    os.mkdir(mi_ubicacion + "\\modulos")
    archivo = open('./modulos/prueba.txt','w')
    archivo.write('Hola mundo')
    archivo.close() 