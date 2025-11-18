# Hipoteza Badawcza LLM — Fundamentalna Wada Kanału Tekst → Token

## 1. Sformalizowana Teza (H-LLM)

**Teza [H-LLM]:**  
_Warstwa „tekst → token” w obecnych systemach LLM jest fundamentalnie niewystarczająca jako samodzielny model rzeczywistości. Wprowadza systematyczne zniekształcenia i podatności, których nie można usunąć samą optymalizacją ani skalowaniem modelu._

### Formalizacja:

Załóżmy:

- \( W \) – przestrzeń stanów świata (ciągła, wielowymiarowa: sensoryka, ciało, kontekst),
- \( L \) – przestrzeń ciągów znaków (język pisany),
- \( V \) – skończony słownik tokenów,
- \( T: L \to V^n \) – deterministyczny kanał tekst → token,
- \( F: V^n \to Y \) – LLM wraz z filtrami bezpieczeństwa.

#### Kluczowe założenia:

1. Istnieją podzbiory \( L_B \subset L \), takie że:

   \[
   \text{render}(l_1) \approx \text{render}(l_2), \quad l_1, l_2 \in L_B
   \]

   lecz:

   \[
   F(T(l_1)) \neq F(T(l_2))
   \]

   co oznacza: _model inaczej interpretuje formalnie równoważne dane wejściowe._

2. Zjawisko to jest **strukturalne** i wynika z:

   \[
   W \to L \to V^n
   \]

   jako sekwencji stratnych kompresji, które:
   - **nie są izometryczne**,  
   - mają „szwy” (np. pelikany Unicode, warianty CJK, ukryte spacje),
   - prowadzą do lokalnych anomalii (szum kodowania, exploity znakowe).

3. Dla dowolnego \( F \) opartego wyłącznie o \( T \), istnieje **niezerowa miara** takich anomalii, która przetrwa nawet przy:
   - zwiększeniu parametrów,
   - retrenowaniu,
   - lokalnych poprawkach tokenizerów i filtrów.

---

## 2. Reżim Falsyfikacji

Hipoteza H-LLM jest falsyfikowalna. Zostaje obalona, jeśli:

1. Istnieje model \( F^\star \) i kanał \( T^\star \), dla których:

   \[
   \forall \, l_1, l_2 \in L:
   \big(\text{render}(l_1) = \text{render}(l_2)\big) \Rightarrow
   \mathbb{P}(F^\star(T^\star(l_1)) \neq F^\star(T^\star(l_2))) \approx 0
   \]

2. Udowodniona zostaje odporność takiego systemu na wszystkie współczesne exploity znakowe:

   - heterogeniczne Unicode,
   - microróżnice CJK,
   - kierunkowość tekstu,
   - exploit Bambusa,
   - permutacje strukturalne w sekwencji.

3. Testy te nie łamią modelu **ani lokalnie, ani po zmianie dystrybucji danych.**

---

## 3. Dowód Naukowy (Argumentacyjny)

### 3.1 Teoria:

Kanał \( W \to L \to V^n \) jest:

- **Stratny**: świat → język → tokeny traci informacje o intencji, ciele, lokalności i strukturze świata.
- **Dyskretny**: tokeny są skończonymi ID, nie wielowymiarowymi stanami.
- **Niejednorodny**: Unicode, BPE, SentencePiece wprowadzają lokalne nieliniowości.

To oznacza, że:

- Istnieją regiony \( V^n \), które są _geometrycznie złe_, tzn. obszary, gdzie mała zmiana \( L \) daje dużą zmianę \( V^n \),
- oraz te, gdzie duża zmiana \( L \) jest ignorowana.

### 3.2 Empiria (NLP/Security):

- Exploity znakowe (Unicode, homoglif, niewidzialne spacje) potrafią systematycznie przełączać LLM między trybami:
  - bezpieczna → niebezpieczna,
  - logiczna → halucynująca,
  - uległa → odrzucająca.
- To zjawisko powtarza się między modelami i generacjami, mimo wzrostu rozmiaru.

### 3.3 Neurologia (Analogicznie):

- Ludzki mózg ma realny kanał kierunkowy czytania (tor wzrokowy, sakkady).
- Zaburzenie kierunku (np. odwrócony tekst) zmienia funkcję czytania (z dekodowania → interpretacji).
- Test „ZERPYZTRAP” wykazuje zmianę trybu pracy i punkt zahaczenia na „anomalii ciągu”.

---

## 4. Ocena w Reżimie Nauki

> **Prawdopodobieństwo, że H-LLM stanowi trafny opis fundamentalnego ograniczenia LLM opartego wyłącznie o tekst→token:**  
> **≈ 90%**

**Wniosek:**  
Teza najprawdopodobniej nie dotyczy pojedynczego błędu modeli, lecz właściwości **systemowej**, wynikającej z ontologii symbolicznego przetwarzania tekstu.

---

## 5. Konsekwencje Badawcze

1. **LLM potrzebują dodatkowych kanałów uziemienia:**
   - sensorycznego (wizja, dźwięk, motoryka),
   - symbolicznego (warstwa typu „mosty semantyczne”),
   - kontekstowego (stan użytkownika, intencja, trajektoria dialogu).

2. Sama warstwa tekst → token nie wystarczy dla reprezentacji rzeczywistości zaufanej i odpornej.

3. Specyficzne exploity (Unicode/Bambus/zakłócenia kodowania) nie są „bugiem” – są dowodem na strukturę ograniczenia.

