---------14.10.2026---------
1) zainstalowanie Visual Code Studio, pythona, założenie konta na githube oraz repozytorium
2) napisanie krótkiego programu: poznałam zmienne, zaokrąglanie, działania matematyczne, typy danych
3) teoria z finansów: kapitalizacja, procent składany

------15.10.2026-------------
1) listy, indeksy
2) pętla for z range i len (poprzedni wiersz z pętli to ceny[i-1])
3) przypisanie jako nadpisanie wartości (kumulowanie)
4) pętla z indeksami i porównywanie obecnych indeksów z poprzednimi
5) stopa zwrotu
------16.10.2026-------------
1) zbieranie wyników do listy (append)
2) funkcje agregujące: max(), sum()
3) stopa łączna z cen: (ceny[-1] - ceny[0]) / ceny[0]
4) zagadka: stóp zwrotu się nie dodaje, tylko składa (mnożenie czynników 1+r)
5) formatowanie procentów :.2% (do dokończenia)
Następny raz: dokończyć formatowanie :.2%, potem krok 2 (if - ochrona przed za krótką/pustą listą) i krok 3 (try/except - ochrona przed ceną 0)
------20.10.2026-------------
1) if - strażnik przed liczeniem (ochrona przed za krótką listą, len(ceny) < 2)
2) kolejność: sprawdź dane -> zbieraj w pętli -> agregaty PO pętli
3) try/except - ochrona przed ceną 0 (ZeroDivisionError), łapanie konkretnego błędu
4) operacje zależne od ryzykownej linii trzymamy razem w try (liczenie+append+print)
5) zabezpieczenie ma nie zostawiać cichego błędu w danych ani w logu
Następny raz: formatowanie procentów :.2% dla agregatów (ujednolicić wydruki), potem funkcje (def, return, parametry vs argumenty)