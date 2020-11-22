import zad1
import zad2
import zad3
import zad4
import zad5

print("....:::::KALKULATOR RELIABILITY::::....\n")


def menu():
    print("::MENU::")
    print("1 - Zadanie 1")
    print("2 - Zadanie 2")
    print("3 - Zadanie 3")
    print("4 - Zadanie 4")
    print("5 - Zadanie 5")
    print("6 - Koniec")
    print("0 - Menu")
    return "....::::::.... "


print(menu())
while True:
    operacja = input("Co wybierzesz? ")
    if operacja == "1":
        print(":::Wybrałeś zadanie 1:::\n"), zad1.problem(), zad1.find_reliability()
    elif operacja == "2":
        print(":::Wybrałeś zadnie 2:::\n"), zad2.problem(), zad2.find_system_reliability()
    elif operacja == "3":
        print(":::Wybrałeś zadanie 3:::\n"), zad3.problem(), zad3.find_pc_reliability()
    elif operacja == "4":
        print(":::Wybrałeś zadanie 4:::\n"), zad4.problem(), zad4.find_system_reliability()
    elif operacja == "5":
        print(":::Wybrałeś zadanie 5:::\n"), zad5.problem(), zad5.find_satelite_reliability()
    elif operacja == "6":
        break
    elif operacja == "0":
        print(menu())
    else:
        break