global childlist, adultlist, elderchilds, deadlist
childlist = list()
adultlist = list()
elderlist = list()
deceasedlist = list()


class subject:
    def __init__(self, name, lastname, id, date, age, gender, country, status):
        self.name = name
        self.lastname = lastname
        self.id = id
        self.date = date
        self.age = age
        self.gender = gender
        self.country = country
        self.status = status


    def show(self):
        print("\nname: ", self.name)
        print("last name: ", self.lastname)
        print("id: ", self.id)
        print("date: ", self.date)
        print("age: ", self.age)
        print("gender: ", self.gender)
        print("status: ", self.status, "\n")


def menu():
    global option
    while True:
        print("\n*covid-19*")
        print("\n1. add to system")
        print("2. change status")
        print("3. see cases")
        print("4. search case")
        print("5. diagnosis")
        print("6. delete list")
        print("7. see quantity")
        print("\n8. exit")
        try:
            option = int(input("choose an option (1-8): "))

        except:
            print("please, be serious :/")
            print("choose a VALID option")
            continue

        if option in range(1, 8):

            process(option)

        elif option == 8:
            break

        else:
            print("please, be serious :/")
            print("choose a VALID option")


def menu1():
    global option1
    print("\n*add to system*")
    print("\n1. child")
    print("2. adult")
    print("3. elder")
    print("4. deceased")
    print("\n5. return")

    try:
        option1 = int(input("choose an option(1-5): "))
    except:
        print("please, be serious :/")
        print("choose a VALID option")

    if option1 in range(1, 5):
        process1(option1)

    elif option1 == 5:
        menu()

    else:
        print("please, be serious :/")
        print("choose a VALID option")


def menu2():
    while True:
        print("\nchange status")
        print("\n1. change status to dead ")
        print("2. change status to infected")
        print("3. change status to safe")
        print("\n4. return")
        try:
            option2 = int(input("choose an option (1-4): "))
        except:
            print("please, be serious :/")
            print("choose a VALID option")
            continue

        if option2 in range(1, 4):
            process2(option2)

        elif option2 == 4:
            menu()

        else:
            print("please, be serious :/")
            print("choose a VALID option")


def menu3():
    while True:
        print("\n*see cases*")
        print("\n1. infected")
        print("2. safe")
        print("3. deceased")
        print("4. child")
        print("5. adult")
        print("6. elders")
        print("7. all cases")
        print("\n8. return")
        try:
            option3 = int(input("choose an option (1-7): "))
        except:
            print("please, be serious :/")
            print("choose a VALID option")
            continue

        if option3 in range(1, 8):
            process3(option3)

        elif option3 == 8:
            menu()

        else:
            print("please, be serious :/")
            print("choose a VALID option")


def menu6():
    while True:
        print("\n*delete a list*")
        print("\n1. child list")
        print("2. adult list")
        print("3. elder list")
        print("4. deceased list")
        print("5. all lists")
        print("\n6. return")
        try:
            option6 = int(input("choose an option (1-6): "))
        except:
            print("please, be serious :/")
            print("choose a VALID option")
            continue

        if option6 in range(1, 6):
            process6(option6)

        elif option6 == 6:
            menu()

        else:
            print("please, be serious :/")
            print("choose a VALID option")


def menu7():
    while True:
        print("\n*quantity in lists*")
        print("\n1. child list")
        print("2. adult list")
        print("3. elder list")
        print("4. deceased list")
        print("5. infected")
        print("6. all lists")
        print("\n7. return")
        try:
            option7 = int(input("choose an option (1-6): "))
        except:
            print("please, be serious :/")
            print("choose a VALID option")
            continue

        if option7 in range(1, 7):
            process7(option7)

        elif option7 == 7:
            menu()

        else:
            print("please, be serious :/")
            print("choose a VALID option")

def searchcase():
    id = input("id: ")
    for a in childlist:
        if a.id == id:
            print("\nname: ", a.name)
            print("last name: ", a.lastname)
            print("id: ", a.id)
            print("date: ", a.date)
            print("age: ", a.age)
            print("gender: ", a.gender)
            print("country: ", a.country)
            print("status: ", a.status, "\n")

    for a in adultlist:
        if a.id == id:
            print("\nname: ", a.name)
            print("last name: ", a.lastname)
            print("id: ", a.id)
            print("date: ", a.date)
            print("age: ", a.age)
            print("gender: ", a.gender)
            print("country: ", a.country)
            print("status: ", a.status, "\n")

    for a in elderlist:
        if a.id == id:
            print("\nname: ", a.name)
            print("last name: ", a.lastname)
            print("id: ", a.id)
            print("date: ", a.date)
            print("age: ", a.age)
            print("gender: ", a.gender)
            print("country: ", a.country)
            print("status: ", a.status, "\n")

    menu()


def addtosystemchild():
    name = input("name: ")
    lastname = input("last name: ")
    id = input("id: ")
    date = input("date: ")
    age = int(input("age: "))
    gender = input("gender: ")
    country = input("country: ")
    status = input("status? (infected/safe): ")
    newchild = subject(name, lastname, id, date, age, gender, country, str.lower(status))
    childlist.append(newchild)
    menu()


def addtosystemadult():
    name = input("name: ")
    lastname = input("last name: ")
    id = input("id: ")
    date = input("date: ")
    age = int(input("age: "))
    gender = input("gender: ")
    country = input("country: ")
    status = input("status? (infected/safe): ")
    str.lower(status)
    newadult = subject(name, lastname, id, date, age, gender, country, str.lower(status))
    adultlist.append(newadult)
    menu()


def addtosystemelder():
    name = input("name: ")
    lastname = input("last name: ")
    id = input("id: ")
    date = input("date: ")
    age = int(input("age: "))
    gender = input("gender: ")
    country = input("country: ")
    status = input("status? (infected/safe): ")
    newelder = subject(name, lastname, id, date, age, gender, country, str.lower(status))
    elderlist.append(newelder)
    menu()

def addtosystemdead():
    name = input("name: ")
    lastname = input("last name: ")
    id = input("id: ")
    date = input("date: ")
    age = int(input("age: "))
    gender = input("gender: ")
    country = input("country: ")
    status = "dead"
    newdead = subject(name, lastname, id, date, age, gender, country, status)
    deceasedlist.append(newdead)
    menu()


def showchildcases():
    for childs in childlist:
        childs.show()
    menu()


def showelderscases():
    for elders in elderlist:
        elders.show()
    menu()


def showadultcases():
    for adults in adultlist:
        adults.show()
    menu()


def showdeceasedcases():
    for deads in deadlist:
        deads.show()
    menu()


def showinfectedcases():
    status = "infected"
    for a in childlist:
        if a.status == status:
            print("\nname: ", a.name)
            print("last name: ", a.lastname)
            print("id: ", a.id)
            print("date: ", a.date)
            print("age: ", a.age)
            print("gender: ", a.gender, "\n")


    for a in adultlist:
        if a.status == status:
            print("\nname: ", a.name)
            print("last name: ", a.lastname)
            print("id: ", a.id)
            print("date: ", a.date)
            print("age: ", a.age)
            print("gender: ", a.gender, "\n")


    for a in elderlist:
        if a.status == status:
            print("\nname: ", a.name)
            print("last name: ", a.lastname)
            print("id: ", a.id)
            print("date: ", a.date)
            print("age: ", a.age)
            print("gender: ", a.gender, "\n")


    menu()


def showsafecases():
    status = "safe"
    for a in childlist:
        if a.status == status:
            print("\nname: ", a.name)
            print("last name: ", a.lastname)
            print("id: ", a.id)
            print("date: ", a.date)
            print("age: ", a.age)
            print("gender: ", a.gender, "\n")


    for a in adultlist:
        if a.status == status:
            print("\nname: ", a.name)
            print("last name: ", a.lastname)
            print("id: ", a.id)
            print("date: ", a.date)
            print("age: ", a.age)
            print("gender: ", a.gender, "\n")


    for a in elderlist:
        if a.status == status:
            print("\nname: ", a.name)
            print("last name: ", a.lastname)
            print("id: ", a.id)
            print("date: ", a.date)
            print("age: ", a.age)
            print("gender: ", a.gender, "\n")


    menu()


def showallcases():

    for childs in childlist:
        childs.show()

    for elders in elderlist:
        elders.show()

    for adults in adultlist:
        adults.show()

    for deads in deadlist:
        deads.show()
    menu()

def process(option):
    if option == 1:
        menu1()

    elif option == 2:
        menu2()

    elif option == 3:
        menu3()

    elif option == 4:
        searchcase()

    elif option == 5:
        pass

    elif option == 6:
        menu6()

    elif option == 7:
        menu7()


def process1(option1):
    if option1 == 1:
        addtosystemchild()

    elif option1 == 2:
        addtosystemadult()

    elif option1 == 3:
        addtosystemelder()

    elif option1 == 4:
        addtosystemdead()

def process3(option3):
    if option3 == 1:
        showinfectedcases()

    elif option3 == 2:
        showsafecases()

    elif option3 == 3:
        showdeceasedcases()

    elif option3 == 4:
        showchildcases()

    elif option3 == 5:
        showadultcases()

    elif option3 == 6:
        showelderscases()

    elif option3 == 7:
        showallcases()


def process2(option2):
    if option2 == 1:
        pass

    elif option2 == 2:
        pass

    elif option2 == 3:
        pass

    elif option2 == 4:
        pass


def process6(option6):
    if option6 == 1:
        clearchildlist()

    elif option6 == 2:
        clearadultlist()

    elif option6 == 3:
        clearelderlist()

    elif option6 == 4:
        cleardeadlist()

    elif option6 == 5:
        clearalllist()


def process7(option7):
    if option7 == 1:
        childsquantity()

    elif option7 == 2:
        adultsquantity()

    elif option7 == 3:
        eldersquantity()

    elif option7 == 4:
        deathtoll()

    elif option7 == 5:
        infectedquantity()

    elif option == 6:
        allquantity()

def clearchildlist():
    childlist.clear()
    menu()


def clearadultlist():
    adultlist.clear()
    menu()


def clearelderlist():
    elderlist.clear()
    menu()


def cleardeadlist():
    deadlist.clear()
    menu()


def clearalllist():
    childlist.clear()
    adultlist.clear()
    elderlist.clear()
    deadlist.clear()
    menu()


def childsquantity():
    print("\nnumber of children's cases: ", len(childlist))
    menu()


def adultsquantity():
    print("\nnumber of adult's cases: ", len(adultlist))
    menu()


def eldersquantity():
    print("\nnumber of adult's cases: ", len(adultlist))
    menu()


def deathtoll():
    print("\ndeathtoll: ", len(deadlist))
    menu()


def infectedquantity():
    childcount = childlist.count("infected")
    print("\nInfected childs: ", childcount)

    adultcount = adultlist.count("infected")
    print("Infected adults: ", adultcount)

    elderscount = childlist.count("infected")
    print("Infected elders: ", elderscount)

    menu()


def allquantity():

    print("\nnumber of children's cases: ", len(childlist))
    print("number of adult's cases: ", len(adultlist))

    childcount = childlist.count("infected")
    print("\nInfected childs: ", childcount)

    adultcount = adultlist.count("infected")
    print("Infected adults: ", adultcount)

    elderscount = childlist.count("infected")
    print("Infected elders: ", elderscount)

    print("deathtoll: ", len(deadlist))


menu()