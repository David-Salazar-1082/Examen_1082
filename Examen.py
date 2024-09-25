class Inventario1082:
        ID_Inventario=0
        Productos=""
        Precios=""
        Encargados=""
        Horarios=""
        Cant_Empl=0
        Empleado_Del_Mes=""
    
    # zona de funciones
        def Altas(self):
            print("Los datos se guardaron correctamente")
        def Bajas(self):
            print("Los datos se borraron correctamente")
        def Mostrar_Datos(self):
            print("Datos del Inventario")
            print(f"Id :{El_Men.ID_Inventario}")
            print(f"Productos:  {El_Men.Productos}")
            print(f"Precios :{El_Men.Precios}")
            print(f"Encargados :{El_Men.Encargados}")
            print(f"Horarios :{El_Men.Horarios}")
            print(f"Cant de empleados :{El_Men.Cant_Empl}")
            print(f"Empleado del mes :{El_Men.Empleado_Del_Mes}")
        def Inventario_Lista(self):
            Inventario_Lista1=("MotherBoard","Fuente de alimentacion","Tarjeta Grafica","Procesador","Ventilador")
            for x in Inventario_Lista1:
                print(x)
        def Inventario_Tupla(self):
            Inventario_Tuplas1=("3000", "2500", "2000","1500","1000")
            for x in Inventario_Tuplas1:
                print(x)
        def Inventario_Diccionario(self):
            Inventario_Diccionario1 = {"Lunes": "9:00-5:00","Martes": "9:00-5:00","Miercoles": "$9:00-5:00",
            "Jueves": "$9:00-5:00", "Viernes": "$9:00-5:00",}
            for x, y in Inventario_Diccionario1.items():
                print(x,":",y)
        
# zona de creacion de objetos
El_Men=Inventario1082()
#zona de usando objeto
El_Men.ID_Inventario=1100
El_Men.Productos=" 5"
El_Men.Precios=" 3000-1000$"
El_Men.Encargados=" 5"
El_Men.Horarios=" 8 Horas"
El_Men.Cant_Empl=" 111"
El_Men.Empleado_Del_Mes=" David Salazar"
El_Men.Mostrar_Datos()
print("Productos en existencia\n")
El_Men.Inventario_Lista()
print("Precios\n")
El_Men.Inventario_Tupla()
print("Horarios\n")
El_Men.Inventario_Diccionario()
El_Men.Altas()
El_Men.Bajas()