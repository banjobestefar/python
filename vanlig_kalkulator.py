def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Det går jo ikke å dele med 0, det vet du..."
    return x / y

def main():
    print("Jon's første kalkulator!")
    try:
        num1 = float(input("Skriv inn første tall: "))
        op = input("Velg operasjon (+, -, *, /): ")
        num2 = float(input("Skriv inn andre tall: "))
    except ValueError:
        print("Skriv inn gyldige tall.")
        return

    if op == '+':
        print("Resultat:", add(num1, num2))
    elif op == '-':
        print("Resultat:", subtract(num1, num2))
    elif op == '*':
        print("Resultat:", multiply(num1, num2))
    elif op == '/':
        print("Resultat:", divide(num1, num2))
    else:
        print("Ugyldig.")

if __name__ == "__main__":
    main()
