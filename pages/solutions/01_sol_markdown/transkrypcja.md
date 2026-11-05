# Transkrypcja

Poniżej znajduje się zrzut ekranu zawierający ręczne notatki:

![Zrzut ekranu z ręcznymi notatkami](zrzut.png)

## Prompt użyty do wygenerowania tekstu przez AI

```text
Przepisz dokładnie treść widoczną na załączonym obrazie do formatu Markdown.

Zachowaj strukturę notatki, w tym:
- tytuły i nagłówki,
- akapity,
- listy punktowane i numerowane,
- wzory matematyczne,
- wyróżnienia tekstu.

Wzory matematyczne zapisz przy użyciu składni LaTeX. Krótkie wzory umieść między znakami $...$, a dłuższe wzory między znakami $$...$$.

Nie dopisuj informacji, których nie ma na obrazie. Jeżeli jakiś fragment jest nieczytelny, oznacz go jako [fragment nieczytelny].
```
## Finalna wersja notatki

### 11. Co to są kropki kwantowe i jakie mają właściwości?

- 0D struktura
- ruch elektronu ograniczony w trzech wymiarach
- najprostszy model – quantum box – kropka kwantowa w kształcie sześcianu, na zewnątrz potencjał nieskończony
- równanie Schrödingera:

$$
-\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}\right)\psi(x,y,z)=E\psi(x,y,z)
$$

- energia:

$$
E=\frac{\hbar^2\pi^2}{2m}\left(\frac{n_x^2}{L_x^2}+\frac{n_y^2}{L_y^2}+\frac{n_z^2}{L_z^2}\right)
$$

- stany energetyczne są zdegenerowane
- sferyczna kropka kwantowa $\Rightarrow$ rozłożenie funkcji falowej $\psi$ na część radialną i kątową (podobieństwo do zagadnienia atomu wodoru w mechanice kwantowej)

  $\Rightarrow$ rozwiązanie – funkcje Bessela typu $J_{l+1/2}$

### 12. Porównać właściwości heterostruktur, drutów i kropek kwantowych.
