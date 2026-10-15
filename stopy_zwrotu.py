ceny = [100, 102, 99, 105, 107]

# stopa zwrotu dnia = (cena dziś / cena wczoraj − 1) × 100%

for i in range(1, len(ceny)):
    cena_dzis = ceny[i]
    cena_wczoraj = ceny[i - 1]
    stopa_zwrotu_dnia = (cena_dzis / cena_wczoraj - 1) * 100
    print(f"Dzień {i+1}: {stopa_zwrotu_dnia:.2f} %")