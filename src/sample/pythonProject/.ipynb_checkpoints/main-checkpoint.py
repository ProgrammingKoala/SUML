

exitOption = False

while not exitOption:
    print()
    print("1 - Dodawanie")
    print("2 - Odejmowanie")
    print("3 - Mnożenie")
    print("4 - Dzielenie")
    print("5 - Wyjdź")
    print()

    try:
        option = int(input("Wybierz opcję: "))
        print()

        if option == 1:
            print("Dodajesz dwie liczby")
            a = int(input("Podaj pierwszą liczbę: "))
            b = int(input("Podaj drugą liczbę: "))
            print(f"Wynik dodawania to: {a + b}")
        elif option == 2:
            print("Odejmujesz dwie liczby")
            a = int(input("Podaj pierwszą liczbę: "))
            b = int(input("Podaj drugą liczbę: "))
            print(f"Wynik odejmowania to: {a - b}")
        elif option == 3:
            print("Mnożysz dwie liczby")
            a = int(input("Podaj pierwszą liczbę: "))
            b = int(input("Podaj drugą liczbę: "))
            print(f"Wynik mnożenia to: {a * b}")
        elif option == 4:
            print("Dzielisz dwie liczby")
            a = int(input("Podaj pierwszą liczbę: "))
            b = int(input("Podaj drugą liczbę: "))
            if(b == 0):
                raise ZeroDivisionError
            print(f"Wynik dzielenia to: {a / b}")
        elif option == 5:
            exitOption = True
        else:
            print("Błędna wartość. Spróbuj ponownie.")
    except ValueError:
        print("Wybrałeś nieprawidłową opcję. Spróbuj ponownie.")
    except Exception:
        print("Nieznany błąd. Spróbuj ponownie")