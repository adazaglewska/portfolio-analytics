kapital = 10000
stopa = 0.05 
liczba_lat = 10
liczba_okresow = liczba_lat * 12 
stopa_miesieczny = stopa / 12


wynik_koncowy = kapital * (1 + stopa) ** liczba_lat
zysk = wynik_koncowy - kapital
stopa_zwrotu = (zysk / kapital) * 100

wynik_koncowy_kapitalizacji_miesiecznej = kapital * (1 + stopa_miesieczny) ** liczba_okresow

print(f"Wynik koncowy: {wynik_koncowy:.2f} zl")
print(f"Zysk: {zysk:.2f} zl")
print(f"Stopa zwrotu: {stopa_zwrotu:.2f} %")

print(f"wynik kapitalizacji miesiecznej: {wynik_koncowy_kapitalizacji_miesiecznej:.2f} zl")



