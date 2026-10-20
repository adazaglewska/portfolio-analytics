ceny = [100, 110, 99, 105]

lista_stop_zwrotu = []
for i in range(1, len(ceny)):
    cena_dzis = ceny[i]
    cena_wczoraj = ceny[i - 1]
    stopa_zwrotu = ((cena_dzis - cena_wczoraj) / cena_wczoraj) 
    lista_stop_zwrotu.append(stopa_zwrotu)
    print(f"Dzień {i}: {stopa_zwrotu:.2%}")

print(lista_stop_zwrotu)
max_dzienna_stopa = max(lista_stop_zwrotu)
print(max_dzienna_stopa)

suma_dzienna_stop = sum(lista_stop_zwrotu)
print(suma_dzienna_stop)

stopa_laczna_cen = (ceny[-1] - ceny[0]) / ceny[0]
print(stopa_laczna_cen)