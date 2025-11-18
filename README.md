# hipotezy_nadawcze_LLM

Repozytorium **hipotezy_nadawcze_LLM** jest laboratorium badawczym dla wielu, równolegle rozwijanych hipotez dotyczących tego, *jak* LLM nadają, odbierają i zniekształcają informację w kanale „tekst → token → odpowiedź”.  
To **nie** jest repo typu „produkt”, tylko **warsztat naukowy**: miejsce, w którym kod, dane i dokumentacja służą przede wszystkim testowaniu i falsyfikacji założeń.

---

## 1. Cel repozytorium

Celem repozytorium jest zbudowanie uporządkowanej przestrzeni do pracy nad hipotezami „nadawczymi” LLM, czyli dotyczącymi:

- tego, jak LLM przekształcają nadany tekst w wewnętrzne reprezentacje,  
- tego, gdzie w tym procesie pojawiają się szumy, szwy i exploity,  
- tego, jakie dodatkowe warstwy (mosty semantyczne, sensoryka, meta-język) są potrzebne, żeby kanał „nadawczy” był bardziej zgodny z rzeczywistością.

Każda hipoteza jest traktowana jak niezależny obiekt badawczy: ma swoją specyfikację, reżim falsyfikacji, eksperymenty i raporty.

---

## 2. Przykładowe klasy hipotez

W repozytorium mogą pojawiać się między innymi hipotezy:

- o **fundamentalnych ograniczeniach warstwy „tekst → token”** jako modelu rzeczywistości (np. H-LLM),  
- o **mostach semantycznych** jako nadawczych meta-ramach nad LLM (np. H-SEM),  
- o **kierunkowości czytania i kolejności tokenów** jako syntetycznym „nerwie wzrokowym” modeli (np. H-DIR),  
- o **szumie w tablicy kodowania Unicode / CJK** jako źródle exploitable zniekształceń (np. H-UNICODE),  
- o **uziemianiu nadawania** w dodatkowych kanałach (wizja, telemetria, stany użytkownika).

Repo nie narzuca liczby ani formatu hipotez; ważne jest, żeby każda była jasno zdefiniowana i miała choć minimalny plan falsyfikacji.

---

## 3. Struktura repozytorium (rama)

Docelowo struktura może wyglądać następująco:

- `docs/hypotheses/`  
  Opisy hipotez w formie plików `.md`, np.  
  `H-LLM_text_token.md`, `H-SEM_bridges.md`, `H-DIR_reading.md`, `H-UNICODE_noise.md`.  
  Każdy plik powinien zawierać: tezę, kontekst, reżim falsyfikacji, aktualny status.

- `experiments/hypotheses/<ID>/`  
  Katalogi z eksperymentami dla danej hipotezy (`<ID>` to skrót hipotezy, np. `H-LLM`).  
  Tu trafiają skrypty, notebooki, konfiguracje oraz pliki typu `PLAN.md` i `RESULTS.md`.

- `data/hypotheses/<ID>/`  
  Dane testowe związane z hipotezą: pary tekstów, warianty Unicode, korpusy syntetyczne, statystyki.  
  Dane powinny być zanonimizowane, jeśli pochodzą z realnych logów.

- `src/hypotheses/<ID>/`  
  Kod pomocniczy: generatory danych, analizatory tokenizacji, wrappery na modele, narzędzia do porównywania zachowania LLM.

Rzeczywista struktura może być prostsza na początku; ważne jest, aby **nazewnictwo i ścieżki jednoznacznie łączyły kod z konkretną hipotezą**.

---

## 4. Minimalny workflow badawczy

Dla **każdej** hipotezy zalecany jest powtarzalny workflow:

1. **Definicja hipotezy**  
   Plik `docs/hypotheses/<ID>.md` zawiera:  
   tezę, opis modelu pojęciowego, „maksymalny reżim falsyfikacji” (co obaliłoby hipotezę), oczekiwane konsekwencje.

2. **Plan eksperymentów**  
   W `experiments/hypotheses/<ID>/PLAN.md` opisane jest:  
   jakie dane i testy mogą hipotezę wzmocnić lub osłabić, jakie metryki będą mierzone.

3. **Implementacja testów**  
   W `src/hypotheses/<ID>/` i powiązanych katalogach `experiments` oraz `data` pojawia się kod:  
   generatory danych, wrappery na API modeli, skrypty do analizy różnic w tokenizacji i odpowiedziach.

4. **Uruchomienie i zapis wyników**  
   Wyniki eksperymentów (zarówno udanych, jak i „negatywnych”) są opisywane w `RESULTS.md` wraz z krótkim komentarzem:  
   czy wynik wspiera hipotezę, osłabia ją, czy wymaga jej przeformułowania.

5. **Aktualizacja statusu hipotezy**  
   W pliku hipotezy (`docs/hypotheses/<ID>.md`) aktualizowany jest `STATUS:`  
   — np. „wstępnie wsparta”, „częściowo obalona”, „wymaga redefinicji”.

---

## 5. Konwencja nazewnicza

Sugestia nazewnictwa:

- ID hipotez: `H-XXX`, gdzie `XXX` to krótki, czytelny skrót (np. `LLM`, `SEM`, `DIR`, `UNICODE`),  
- pliki dokumentacji: `docs/hypotheses/H-XXX_*.md`,  
- katalogi z eksperymentami: `experiments/hypotheses/H-XXX/`,  
- kod: `src/hypotheses/H-XXX/`.

Takie nazewnictwo umożliwia szybkie znalezienie całego „ekosystemu” danej hipotezy.

---

## 6. Status startowy

Na etapie tworzenia tego README repozytorium:

- jest przestrzenią do **budowy wielu hipotez nadawczych LLM**,  
- zakłada **wysoki reżim naukowy i falsyfikowalność** (każda hipoteza musi mieć jasno zdefiniowane warunki obalenia),  
- traktuje historię commitów jako część dokumentacji badawczej (opisy commitów powinny wskazywać, do której hipotezy się odnoszą i co dokładnie testują).

---

## 7. Jak kontrybuować

Jeśli dodajesz nową hipotezę:

1. Utwórz plik w `docs/hypotheses/` z jasną tezą i warunkami falsyfikacji.  
2. Załóż katalog w `experiments/hypotheses/<ID>/` i dodaj tam plan eksperymentów.  
3. Dodaj kod w `src/hypotheses/<ID>/` powiązany z tą hipotezą.  
4. Każdy commit opisuj w sposób czytelny („add initial tests for H-UNICODE homoglyph pairs”, „update H-LLM results after new red-teaming run”).

Repozytorium **hipotezy_nadawcze_LLM** ma być miejscem, gdzie LLM nie są „magiczne”, tylko stawiane pod lupą – tak, jak przystało na laboratorium hipotez.
