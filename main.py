import problem_solutions.zad1 as zad1
import problem_solutions.zad2 as zad2
import problem_solutions.zad3 as zad3
import problem_solutions.zad4 as zad4
import problem_solutions.zad5 as zad5

from utils.console_utility import problem_description

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
        print(":::Wybrałeś zadanie 1:::\n"),  problem_description("./problem_descriptions/zad1.txt"), zad1.find_reliability()
    elif operacja == "2":
        print(":::Wybrałeś zadnie 2:::\n"),  problem_description("./problem_descriptions/zad2.txt"), zad2.find_system_reliability()
    elif operacja == "3":
        print(":::Wybrałeś zadanie 3:::\n"),  problem_description("./problem_descriptions/zad3.txt"), zad3.find_pc_reliability()
    elif operacja == "4":
        print(":::Wybrałeś zadanie 4:::\n"),  problem_description("./problem_descriptions/zad4.txt"), zad4.find_system_reliability()
    elif operacja == "5":
        print(":::Wybrałeś zadanie 5:::\n"), problem_description("./problem_descriptions/zad5.txt"), zad5.find_satelite_reliability()
    elif operacja == "6":
        break
    elif operacja == "0":
        print(menu())
    else:
        break