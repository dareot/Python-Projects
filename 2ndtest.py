from io import open

class calculator:
    def __init__(self):
        pass

    def menu2(self):
        while True:
            print("\n1. Suma")
            print("2. Resta")
            print("3. Multiplicacion")
            print("4. Division")
            print("5. Regresar")
            print("\n6. Salir")
            try:
                option2 = int(input("\nIngrese el numero de la operacion que desea realizar: "))

            except:
                print("\nOpcion incorrecta!")
                print("Por favor, introduzca una opcion valida")
                continue

            if option2 in range(1, 6):
                self.process2(option2)

            elif option2 == "6":
                break

            else:
                print("\nOpcion incorrecta!")
                print("Por favor, introduzca una opcion valida")

    def singup(self):
        user_data = open("user_data.txt", "a")
        username = input("\nIngrese su nombre de usuario: ")
        user_data.write(username+'\n')
        user_data.close()
        password_data = open("password_data.txt", "a")
        password = input("Ingrese su clave: ")
        password_data.write(password+'\n')
        password_data.close()
        menu()

    def login(self):
        username = input("\nIntroduzca su nombre de usuario: ")
        user_data = open("user_data.txt", "r")
        search = user_data.readlines()
        if username+'\n' in search:
            password = input("Introduzca su clave: ")
            password_data = open("password_data.txt","r")
            search = password_data.readlines()
            if password+"\n" in search:
                print("\nLa sesion se ha iniciado correctamente")
                self.menu2()
            else:
                print("\nLa sesion no se ha podido iniciar")
                print("Recuerde tener cuidado con las letras mayusculas y minusculas")
                print("Por favor, introduzca correctamente su clave")
        else:
            print("\nLa sesion no se ha podido iniciar")
            print("Recuerde tener cuidado con las letras mayusculas y minusculas")
            print("Por favor, introduzca correctamente su nombre de usuario")
            menu()

    def plus(self):
        print("\nSuma:")
        first_plus = int(input("Ingrese el primer numero: "))
        second_plus = int(input("Ingrese el segundo numero: "))
        third_plus = first_plus + second_plus
        print("\nEl resultado de la suma es: ", third_plus)

    def minus(self):
        print("\nResta:")
        first_minus = int(input("Ingrese el primer numero: "))
        second_minus = int(input("Ingrese el segundo numero: "))
        third_minus = int(first_minus - second_minus)
        print("\nEl resultado de la resta es: ", third_minus)

    def multi(self):
        print("\nMultiplicacion:")
        first_multi = int(input("Ingrese el primer numero: "))
        second_multi = int(input("Ingrese el segundo numero: "))
        third_multi = int(first_multi * second_multi)
        print("\nEl resultado de la multiplicacion es: ", third_multi)

    def div(self):
        print("\nDivision:")
        first_div = int(input("Ingrese el primer numero: "))
        second_div = int(input("Ingrese el segundo numero"))
        third_div = int(first_div / second_div)
        print("\nEl resultado de la division es: ", third_div)

    def process(self, option):
        if option == "1":
            self.singup()

        elif option == "2":
            self.login()


    def process2(self, option2):
        if option2 == "1":
            self.plus()

        elif option2 == "2":
            self.minus()

        elif option2 == "3":
            self.multi()

        elif option2 == "4":
            self.div()

        elif option2 == "5":
            menu()


def menu():
    ddd = calculator()
    while True:
        print("\n1. Registrar Usuario")
        print("2. Iniciar sesion")
        print("3. Salir")
        option = input("\nIntroduzca una opcion: ")
        if option == "1":
            ddd.singup()
        elif option == "2":
            ddd.login()
        elif option == "3":
            break
        else:
            print("\nOpcion incorrecta!")
            print("Por favor, introduzca una opcion valida")

menu()
