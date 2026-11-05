# Zadania z Markdowna

## Zadanie z podtytułem.

## Zadanie z tekstem pochylonym, pogrubionym i przekreślonym.

Oto i one: *tekst pochylony*, **tekst pogrubiony**, ~~tekst przekreślony~~.

## Lista numerowana:

1. Punkt pierwszy:
   1. podpunkt 1,
   2. podpunkt 2.
2. Punkt drugi:
   1. podpunkt 3,
   2. podpunkt 4.
3. Punkt trzeci.

## Lista punktowa:
   Owa lista:
   - punkt 1,
   - punkt 2,
   - punkt 3,
   - punkt 4.

## Checklista

 - [ ] punkt 1,
 - [ ] punkt 2,
 - [ ]  punkt 3,
 - [x] punkt 4 z zaznaczeniem.

## Tabela

|  AAA | BBBB | CCCCCC |
|:----:| :---:|:------:|
| 123  | 1234 | 321    |
| 32123|343412|22222   |

## Link

 http://colab.research.google.com

## Wzory matematyczne w tekście

Tutaj np. wzór na zmianę entropii gazu doskonałego: $\Delta S=nC_v\ln\left(\frac{T_2}{T_1}\right) + nr\ln\left(\frac{V_2}{V_1}\right)$, a tu z kolei na rozpad promieniotwórczy: $N(t)=N_0e^{-\lambda t}$, a tu równanie interferencji na dwóch szczelinach: $I(\theta)=I_{\max}\cos^2\left(\frac{\pi d\sin(\theta)}{\lambda}\right)$.

## Wzory matematyczne jako osobny wycentrowany blok:

Równanie Shrödingera:

$$
i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r},{t})=\left[-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf {r},{t})\right]\Psi( \mathbf{r},{t})
$$

Funkcja falowa cząstki w nieskończonej studni potencjału:

$$
\psi_n(x)=\sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right), n=1,2,3,...
$$

Zasada nieoznaczoności Heisenberga:

$$
\Delta x \Delta p_x \geq\frac{\hbar}{2}
$$

## Obrazek z wykresem:
![Wykres](wykres.png)

## Kod Pythona

```python
import math
promien = 5
pole = math.pi * promien**2
print("Pole koła =", pole)
```




