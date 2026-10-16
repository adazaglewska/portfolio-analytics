# PLAN NAUKI — Portfolio & Market Analytics Platform

## Jak używać tego pliku
- [x] = zrobione, [ ] = do zrobienia
- Na starcie każdej sesji wklejam do czatu: ostatni wpis z LEARNING_LOG.md
  + aktualną sekcję miesiąca z tego pliku (widać, co następne).
- Jeśli mentor proponuje temat spoza planu — STOP. Plan rządzi, nie pamięć czatu.

---

## CAŁA ŚCIEŻKA (~12 miesięcy)

- [ ] Miesiąc 1 — Podstawy Pythona i Gita (mini-zadania finansowe)  ← TU JESTEŚ
- [ ] Miesiąc 2 — requests, JSON, pandas: ingest z API NBP do CSV
- [ ] Miesiąc 3 — Databricks: notebooki, SQL, tabele Delta, wstęp do PySparka
- [ ] Miesiąc 4–6 — Medallion (bronze/silver/gold), model gwiazdy, testy, CI/CD, Power BI
- [ ] Miesiąc 7–8 — Optymalizacja + certyfikat Databricks Data Engineer Associate
- [ ] Miesiąc 9 — Podstawy Fabric (Direct Lake, shortcut do warstwy gold)
- [ ] Miesiąc 10 — Dane fundamentalne z SEC (kilka spółek, ograniczony zakres)
- [ ] Miesiąc 11–12 — AI: RAG po raportach 10-K, ai_query, agent o portfelu

---

## MIESIĄC 1 — Podstawy Pythona i Gita (szczegółowo)

### A. Fundament Pythona (zaznacz sama, co już umiesz)
- [x] uruchamianie skryptu .py w VS Code
- [x] zmienne i typy (int, float, str, bool)
- [x] operatory arytmetyczne i print()
- [x] listy i indeksy (ceny[0], ceny[i])
- [x] pętla for z range() i len()
- [x] kumulowanie wartości (nadpisywanie w pętli)
- [x] pętla z indeksami i porównywanie bieżącego z poprzednim (ceny[i-1])
- [x] stopa zwrotu (wzór na dziennej zmianie cen)

### B. Dziś (piatek) — w trakcie
- [ ] zbieranie wyników do listy: .append()
- [ ] funkcje agregujące: max(), min(), sum()
- [ ] stopa łączna z cen + zagadka 7,02% vs 7,00%
- [ ] instrukcja warunkowa: if / elif / else (ochrona przed za krótką listą)
- [ ] obsługa błędów: try / except (ochrona przed ceną 0)

### C. Reszta miesiąca 1 — do zrobienia
- [ ] funkcje: def, return, parametry vs argumenty (pakowanie logiki)
- [ ] f-stringi i formatowanie liczb/procentów (np. "{:.2%}")
- [ ] słowniki: dict, klucz→wartość (odpowiednik lookupu / tabeli słownikowej)
- [ ] enumerate() i zip() — czytelniejsze pętle zamiast range(len())
- [ ] listy składane (list comprehension) — krótszy zapis pętli  [opcjonalnie]
- [ ] moduły i import: math, datetime (daty sesji GPW/NYSE)
- [ ] czytanie i zapis prostych plików tekstowych (open / write)
- [ ] mini-podsumowanie: policz metryki portfela w czystych funkcjach

### D. Git z terminala (przez cały miesiąc, małymi krokami)
- [x] git init / git status
- [x] git add / git commit -m / git push
- [ ] git log (historia commitów)
- [ ] .gitignore (co NIE trafia do repo)
- [ ] git pull / git clone (pobieranie zmian i repo)
- [ ] podstawy gałęzi: git branch, git checkout -b, merge  [koniec miesiąca]

---

## Zasady projektu (przypomnienie)
- Zero kosztów, tylko darmowe narzędzia.
- Dane publiczne (NBP, FRED, GUS, Yahoo Finance), nie z pracy.
- Fikcyjny, edukacyjny portfel — nie rekomendacje inwestycyjne.