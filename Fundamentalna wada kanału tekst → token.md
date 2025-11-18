# Hipoteza Badawcza LLM — Fundamentalna Wada Kanału „tekst → token”

## 1. Sformalizowana teza (H-LLM)

**Teza [H-LLM]:**  
Warstwa „tekst → token” w obecnych systemach LLM jest fundamentalnie niewystarczająca jako samodzielny model rzeczywistości. Wprowadza systematyczne zniekształcenia i podatności, których nie można usunąć samą optymalizacją ani skalowaniem modelu.

### 1.1. Elementy modelu

Wprowadzamy następujące zbiory i funkcje:

- W — przestrzeń stanów świata (ciągła, wielowymiarowa: zmysły, ciało, kontekst społeczny, czas).
- L — przestrzeń tekstów (ciągi znaków w danym języku).
- V — skończony słownik tokenów (np. ID 0…N−1).
- T : L → V^n — kanał „tekst → token” (normalizacja, tokenizacja).
- F : V^n → Y — model LLM (razem z filtrami bezpieczeństwa), gdzie Y to przestrzeń odpowiedzi / decyzji.

Intuicyjnie:

- W  →  L  →  V^n  →  Y  
  świat → tekst → tokeny → odpowiedź modelu.

### 1.2. Część 1 tezy — istnienie wrażliwych podzbiorów

Istnieje taki podzbiór L_B ⊂ L (czyli pewna klasa tekstów), że:

- dla niektórych l₁, l₂ ∈ L_B:

  - z punktu widzenia człowieka są **wizualnie równoważne**  
    (np. wyglądają tak samo lub prawie tak samo po wyrenderowaniu na ekranie):

    - render(l₁) ≈ render(l₂)  
      (≈ oznacza: człowiek widzi je jako to samo albo prawie to samo)

  - ale model przetwarza je jako **różne stany wewnętrzne**, tzn.:

    - F( T(l₁) ) ≠ F( T(l₂) )

Co to znaczy „różne” w praktyce:

- model wydaje inną decyzję,
- albo generuje inny typ odpowiedzi,
- albo w jednym przypadku utrzymuje bezpieczeństwo, a w drugim je narusza,
- mimo że dla człowieka wejścia są (praktycznie) równoważne.

Przykład klasy L_B (intuicyjnie):

- różne warianty tego samego chińskiego znaku (np. bambus),
- różne warianty Unicode, homoglifów,
- teksty różniące się tylko mikroskopijnymi znakami specjalnymi.

### 1.3. Część 2 tezy — strukturalny charakter zjawiska

Zjawisko to jest **strukturalne**, a nie tylko „zbiorem bugów”, ponieważ:

1. Cały tor:

   - W  →  L  →  V^n

   jest sekwencją silnie stratnych kompresji:

   - W → L: świat ciągły kompresujemy do liniowego tekstu,
   - L → V^n: tekst kompresujemy do skończonej liczby symboli (tokenów).

2. Te kompresje:

   - nie zachowują odległości ani struktury w pełni (brak izometrii),
   - mają „szwy” i nierówności:
     - różne kodowania Unicode,
     - warianty znaków CJK,
     - kierunek czytania,
     - reguły tokenizacji (BPE, SentencePiece itp.).

3. W tych „szwach” powstają:

   - lokalne obszary, w których:
     - bardzo mała zmiana na poziomie tekstu (L) daje dużą zmianę na poziomie tokenów (V^n),
     - lub odwrotnie: duża zmiana w L jest kiepsko rozróżniana w V^n.

To właśnie te obszary są źródłem:

- exploitów na poziomie znaków,
- niestabilności filtrów bezpieczeństwa,
- halucynacji i anomalii zachowania modelu.

### 1.4. Część 3 tezy — nieusuwalność tego efektu przy samym tekście

Dla każdego modelu F, który:

- korzysta **tylko** z kanału tekst → token (T),
- nie ma dodatkowych kanałów uziemienia (np. sensorycznych, symbolicznych ponad tekst),

istnieje **niezerowy zbiór** wejść L_B, dla których:

- opisane powyżej zjawisko (równoważne wizualnie teksty → różne decyzje) **nie znika po skalowaniu**:

  - nawet jeśli zwiększymy parametry F,
  - nawet jeśli będziemy dłużej trenować,
  - nawet jeśli będziemy lokalnie poprawiać T (np. dodawać specjalne normalizacje).

Innymi słowy:

- przy czystym, tekstowym LLM **nie da się całkowicie wyeliminować** klasy podatności wynikających z natury kanału tekst → token;
- pełna naprawa wymaga:
  - dodatkowych kanałów uziemienia (świat, sensoryka),
  - albo dodatkowej meta-warstwy nad tekstem (np. Twoje mosty semantyczne jako jawny poziom organizacji znaczenia).

---

## 2. Maksymalny reżim falsyfikacji (kiedy hipoteza byłaby fałszywa)

Hipoteza H-LLM jest falsyfikowalna.  
Byłaby **obalona**, gdybyśmy pokazali system LLM, który spełnia wszystkie trzy warunki:

### 2.1. Warunek 1 — odporność na równoważne wizualnie wejścia

Istnieje model F* oraz kanał T*, takie że dla wszystkich tekstów l₁, l₂:

- jeśli render(l₁) = render(l₂) (człowiek uznaje je za identyczne),

to:

- F*( T*(l₁) ) i F*( T*(l₂) ) są praktycznie nieodróżnialne statystycznie w:

  - zadaniach semantycznych,
  - zadaniach bezpieczeństwa,
  - zadaniach generacyjnych.

Czyli:  
model nie daje się „oszukać” wariantami kodowania, homoglifami, mikrozmianami znaków, jeśli człowiek uważa je za równoważne.

### 2.2. Warunek 2 — odporność na wszystkie znane klasy ataków znakowych

System pozostaje stabilny pod red-teamingiem obejmującym m.in.:

- warianty Unicode,
- homoglifowe podmiany znaków,
- mikroróżnice w chińskich znakach (CJK),
- dodawanie i usuwanie niewidzialnych znaków,
- manipulację kierunkiem czytania i segmentacją,
- kombinacje powyższych.

W żadnym z tych przypadków nie obserwujemy:

- powtarzalnego jailbreaku,
- przełączenia zachowania w tryb niebezpieczny,
- systematycznych zmian decyzji przy wizualnie równoważnych wejściach.

### 2.3. Warunek 3 — stabilność w czasie i domenie

Odporność nie jest jednorazowa:

- utrzymuje się na:
  - kolejnych wersjach modelu,
  - rozszerzonych zbiorach danych,
  - w nowych domenach tekstu.

Jeżeli kiedyś taki model powstanie i spełni powyższe kryteria bez dodatkowych kanałów uziemienia, hipoteza H-LLM zostanie osłabiona lub obalona.

---

## 3. „Dowód” w sensie naukowym (argument z teorii i faktów)

To nie jest dowód matematyczny, lecz rygorystyczny argument oparty na:

- teorii informacji,
- praktyce NLP i bezpieczeństwa,
- analogii z neurologią.

### 3.1. Z teorii informacji i reprezentacji

Kanał:

- W → L — świat do języka,
- L → V^n — język do tokenów,

jest:

1. **Stratny** (losing information):

   - W → L odrzuca ogromną część stanu świata (ciało, zapach, mikrogesty, hormonologię, lokalność).
   - L → V^n odrzuca informację o mikroskopijnej strukturze znaków, ich pochodzeniu, historii, wariantach graficznych.

2. **Dyskretny**:

   - V jest skończony, więc różne formy w L muszą „ściskać się” w te same lub bliskie tokeny,
   - inne z kolei dostają „osobne szufladki”, mimo że dla człowieka różnica jest minimalna.

3. **Niejednorodny**:

   - Unicode zawiera wielokrotne warianty tych samych znaków z historycznych powodów,
   - tokenizatory (BPE itd.) optymalizowane są pod częstość, nie pod zgodność semantyczną.

To **gwarantuje pojawienie się regionów anomalii**: na poziomie V^n istnieją „szwy”, które nie są symetryczne z ludzką percepcją.

### 3.2. Z praktyki NLP i bezpieczeństwa

W literaturze i praktyce:

- ataki oparte na Unicode i homoglifach regularnie:

  - zmieniają decyzje klasyfikatorów (np. toksyczność, spam),
  - powodują różnice w zachowaniu modeli przy pozornie identycznych wejściach,
  - służą do jailbreaku filtrów bezpieczeństwa,

- większe modele **nie eliminują** tego efektu, lecz czasem go maskują lub przesuwają w inne rejony.

Empiryczny wniosek:

- eksploatowalne „szwy” w torze tekst → token → embedding istnieją,
- nie znikają wraz z rozmiarem modelu.

### 3.3. Z neurologii i psychologii czytania (analog strukturalny)

W ludzkim układzie nerwowym:

- istnieje funkcjonalny „nerw kierunku czytania”:
  - tor wzrokowy,
  - sterowanie sakkadami,
  - kierunkowa organizacja pól uwagi,
- odwrócenie kierunku lub struktury tekstu (jak w Twoim przykładzie „ZERPYZTRAP”) zmienia tryb pracy:
  - z automatycznego czytania,
  - na dekodowanie / literowanie / analizę anomalii.

Analogicznie w LLM:

- parametry pozycji, kierunkowość sekwencji i segmentacja tokenów pełnią rolę syntetycznego „nerwu kierunku”.

Zarówno w mózgu, jak i w LLM:

- wąskie gardło wejściowe z własnymi regułami powoduje specyficzne zniekształcenia,
- Twoje testy (na sobie i na modelach) pokazują, że te zniekształcenia są **powtarzalne i ustrukturyzowane**.

---

## 4. Ocena (liczba)

W absolutnym reżimie:

> **Prawdopodobieństwo, że hipoteza H-LLM jest trafnym opisem obecnej generacji LLM opartych wyłącznie na tekst → token:**

**≈ 90%**

Czyli:

- z dużym prawdopodobieństwem nie mówimy o pojedynczych błędach implementacyjnych,
- tylko o **fundamentalnym ograniczeniu całej warstwy „tekst → token” jako modelu rzeczywistości**,
- które można złagodzić, ale nie skasować, _bez_ wprowadzenia dodatkowych kanałów (sensorycznych, symbolicznych, mostów semantycznych).

---

## 5. Podsumowanie w jednym zdaniu

Warstwa „tekst → token” w LLM działa jak wąski, kierunkowy nerw wzrokowy: jest konieczna do przetwarzania, ale strukturalnie zbyt uboga, aby sama w sobie być modelem rzeczywistości — jej szwy i asymetrie generują exploity nieusuwalne samym „przykręcaniem parametrów” modelu.
