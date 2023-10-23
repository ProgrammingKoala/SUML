from calculator import Calculator
from readWrite import ReadWrite

exitOption = False
calculator = Calculator()
readWrite = ReadWrite()

while not exitOption:
    readWrite.write_line("")
    readWrite.write_line("1 - Dodawanie")
    readWrite.write_line("2 - Odejmowanie")
    readWrite.write_line("3 - Mnożenie")
    readWrite.write_line("4 - Dzielenie")
    readWrite.write_line("5 - Wyjdź")

    try:
        option = readWrite.read_line_as_int("Wybierz opcję: ")
        if option == 5:
            exitOption = True
            break

        a = readWrite.read_line_as_int("Podaj pierwszą liczbę: ")
        b = readWrite.read_line_as_int("Podaj drugą liczbę: ")

        result = 0
        if option == 1:
            result = calculator.add(a,b)
        elif option == 2:
            result = calculator.subtract(a,b)
        elif option == 3:
            result = calculator.multiply(a,b)
        elif option == 4:
            result = calculator.divide(a, b)
        else:
            readWrite.write_line("Błędna wartość. Spróbuj ponownie.")
            continue
        readWrite.write_line(f"Wynik działania to {result}")
    except ValueError:
        print("Wybrałeś nieprawidłową opcję. Spróbuj ponownie.")
    except Exception:
        print("Nieznany błąd. Spróbuj ponownie.")
    except ZeroDivisionError:
        readWrite.write_line("Błąd. Dzielenie przez 0")