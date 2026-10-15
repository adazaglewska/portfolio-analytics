liczba_lat = 10
stopa = 0.05
kapital = 10000
wartosc = kapital

for rok in range(1, liczba_lat + 1):
    wartosc_lokaty = kapital * (stopa + 1) ** rok 
    print(f"Rok {rok}: {wartosc_lokaty:.2f} zł")


for rok in range(1, liczba_lat + 1):
    wartosc = wartosc * (1 + stopa)
    print(f"Rok {rok}: {wartosc:.2f} zł")