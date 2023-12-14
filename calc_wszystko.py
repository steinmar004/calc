
print("Wykonam podane w kalkulatorze polecenie, po podaniu mi wartości zmiennych a i b")
b = float(input("zmienna b: > "))
if b == 0:
    print("B nie może być zerem!")
    exit()
else:
    a = float(input("zmienna a: > "))

print(f"Oto dodawanie: {a} + {b} =", end = ' ')
print(dodawanie(a,b))
print(f"Oto odejmowanie: {a} - {b} =", end = ' ')
print(odejmowanie(a,b))
print(f"Oto mnożenie: {a} * {b} = ", end = ' ')
print(mnozenie(a,b))
print(f"No i dzielenie: {a} / {b} =", end = ' ')
print(dzielenie(a,b))