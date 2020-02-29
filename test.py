class alquilar:

    def __init__(self):
        self.nombre = input("\n"+"Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.cedula = input("Ingrese su numero de cedula: ")

    def libro(self):
        self.libro = input("\n"+"Ingrese el titulo del libro: ")
        self.autor = input("Ingrese el autor del libro: ")
        self.editorial = input("Ingrese la editorial del libro: ")

    def fecha(self):

        self.fecha = input("\n"+"Ingrese la fecha de alguiler: ")
        while True:
            self.dias = int(input("Ingrese la cantidad de dias en alquiler: "))

            if self.dias >7:
                print("La cantidad maxima es de 7 dias")
                self.dias=7

            elif self.dias <1:
                print("La cantidad minima es de 1 dia")
                self.dias = 1

            else:
                break
                pass



    def mostrar(self):
        print(str(("\n"+"Nombre: ")+self.nombre))
        print(str(("Apellido: ")+self.apellido))
        print(str(("C.I: ")+self.cedula))
        print(str(("Nombre del libro: ")+self.libro))
        print(str(("Autor: ") + self.autor))
        print(str(("Editorial: ") + self.editorial))
        print(str(("Fecha de alquiler: ")+self.fecha))
        print("El alquiler es de: ", self.dias, " dias")

    def menu(self):
        print(str(("\n"+"ID:")+self.nombre+(" ")+self.apellido))
        print(str(("C.I: ")+self.cedula))
        while True:
            print("")
            print("Ingrese una opcion")

            print("\n"+"1. Agregar Libro")
            print("2. Mostrar datos")
            print("3. Salir")
            print("")

            try:
                opc = int(input(""))

            except ValueError as ve:
                print("Por favor, introduzca una opcion valida")
                continue

            if opc in range(1, 2):
                self.proceso(opc)

            elif opc == 3:
                break

            else:
                print("Por favor, introduzca una opcion valida")

    def proceso(self, opc):
        if opc == 1:
            self.libro()
            self.fecha()

        elif opc == 2:
            self.mostrar()

print("Bienvenido")
alquilar1=alquilar()
alquilar1.menu()