from calculator import Calculator

exitOption = False
calculator = Calculator()
while not exitOption:
    print()
    print("1 - Dodawanie")
    print("2 - Odejmowanie")
    print("3 - Mnożenie")
    print("4 - Dzielenie")
    print("5 - Wyjdź")
    print()

    try:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        option = int(input("Wybierz opcję: "))
        print()

        if option == 1:
            print("Dodajesz dwie liczby")
            print(f"Wynik dodawania to: {calculator.add(a,b)}")
        elif option == 2:
            print("Odejmujesz dwie liczby")
            print(f"Wynik odejmowania to: {calculator.subtract(a,b)}")
        elif option == 3:
            print("Mnożysz dwie liczby")
            print(f"Wynik mnożenia to: {calculator.multiply(a,b)}")
        elif option == 4:
            print("Dzielisz dwie liczby")
            print(f"Wynik dzielenia to: {calculator.divide(a, b)}")
        elif option == 5:
            exitOption = True
        else:
            print("Błędna wartość. Spróbuj ponownie.")
    except ValueError:
        print("Wybrałeś nieprawidłową opcję. Spróbuj ponownie.")
    except Exception:
        print("Nieznany błąd. Spróbuj ponownie")