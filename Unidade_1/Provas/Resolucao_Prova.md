# Resolução da 1ª Avaliação - Sinais e Sistemas (TEC 412)
**Professor**: Dr. Edgar Silva Júnior

---

## 1) Responda aos itens abaixo:

### a) Defina e diferencie os conceitos de sinais de tempo contínuo e discreto. (1,4 pts.)
*(Origem: Questão 3 da Lista de Exercícios)*

**Sinal de Tempo Contínuo**: A variável independente assume um conjunto contínuo de valores. O sinal é definido para todo e qualquer instante de tempo em um dado intervalo. É denotado por $x(t)$, onde $t \in \mathbb{R}$.
**Sinal de Tempo Discreto**: A variável independente assume apenas valores em um conjunto discreto de instantes (frequentemente inteiros). É denotado por $x[n]$, onde $n \in \mathbb{Z}$. O sinal só existe nesses instantes espaçados.
**Diferença**: A principal diferença é o domínio da variável independente: os contínuos existem em todo instante (domínio contínuo), enquanto os discretos são definidos apenas em instantes espaçados e específicos (domínio discreto).

### b) Defina e diferencie os conceitos de sinais analógicos e digitais. (1,4 pts.)
*(Origem: Questão 6 da Lista de Exercícios)*

**Sinal Analógico**: A amplitude do sinal pode assumir qualquer valor dentro de uma faixa contínua infinita de valores (amplitude contínua).
**Sinal Digital**: A amplitude é quantizada, ou seja, restrita a um conjunto finito e pré-definido de valores discretos. Na prática, além de amplitude quantizada, ele também costuma ser discreto no tempo.
**Diferença**: A diferença recai sobre o eixo vertical (amplitude). O sinal analógico pode assumir infinitos valores de amplitude, enquanto o digital só pode assumir valores contidos em um conjunto predefinido.

---

## 2) Considere o sinal de tempo discreto $x[n] = 1 - \sum_{k=3}^{\infty} \delta[n - 1 - k]$. Determine os valores de $M$ e $n_0$ de modo que $x[n]$ possa ser expresso como $x[n] = u[Mn - n_0]$. (1,6 pts.)
*(Origem: Oppenheim 1.12 / Questão 21 da Lista de Exercícios)*

Avaliando o somatório: o impulso $\delta[n - 1 - k]$ é igual a 1 quando $n - 1 - k = 0 \implies k = n - 1$.
Como a soma é avaliada para $k \ge 3$, o somatório será 1 para qualquer $n - 1 \ge 3 \implies n \ge 4$.
Ou seja, a soma vale 1 para $n \ge 4$, e vale 0 para $n \le 3$.
Subtraindo isso de 1, temos:
- Para $n \ge 4$: $x[n] = 1 - 1 = 0$
- Para $n \le 3$: $x[n] = 1 - 0 = 1$

Essa é a definição de uma função degrau discreta que foi rebatida e deslocada no tempo, correspondendo a $u[-n + 3]$ (pois $u[-n+3] = 1$ quando $-n + 3 \ge 0 \implies n \le 3$).
Comparando a forma obtida $u[-n + 3]$ com a forma genérica dada $u[Mn - n_0]$:
Concluímos que **$M = -1$** e **$n_0 = -3$**.

---

## 3) Considere o sinal de tempo contínuo $x(t) = \delta(t + 2) - \delta(t - 2)$. Calcule o valor de $E_\infty$ (Energia sobre um intervalo infinito) para o sinal $y(t) = \int_{-\infty}^{t} x(\tau) d\tau$. (1,6 pts.)
*(Origem: Oppenheim 1.13 / Questão 21 da Lista de Exercícios)*

Primeiro, calculamos $y(t)$:
$$y(t) = \int_{-\infty}^{t} [\delta(\tau + 2) - \delta(\tau - 2)] d\tau$$
A integral da função impulso é a função degrau unitário $u(t)$. Logo, integrando termo a termo:
$$y(t) = u(t + 2) - u(t - 2)$$
Esta função define um pulso retangular de amplitude 1 que "liga" em $t = -2$ e "desliga" em $t = 2$. Fora do intervalo $[-2, 2]$, o sinal $y(t)$ é nulo.
A energia $E_\infty$ de um sinal de tempo contínuo é a integral do seu quadrado:
$$E_\infty = \int_{-\infty}^{\infty} |y(t)|^2 dt = \int_{-2}^{2} 1^2 dt = [t]_{-2}^{2} = 2 - (-2) = 4 \text{ J}$$
**Resposta**: $E_\infty = 4$.

---

## 4) Para uma forma de onda senoidal com valor de pico igual a $A$, uma frequência $f_0$ e fase $\phi$, calcule o seu valor RMS. (1,6 pts.)
*(Origem: Couch 2.1 / Questão 15 da Lista de Exercícios)*

Seja a forma de onda $x(t) = A \cos(2\pi f_0 t + \phi)$. O valor RMS (Root Mean Square) é a raiz quadrada do valor médio quadrático num período $T_0 = 1/f_0$:
$$X_{RMS} = \sqrt{ \frac{1}{T_0} \int_{0}^{T_0} x^2(t) dt }$$
Elevando ao quadrado:
$$X_{RMS}^2 = \frac{1}{T_0} \int_{0}^{T_0} A^2 \cos^2(2\pi f_0 t + \phi) dt$$
Usando a identidade trigonométrica $\cos^2(\theta) = \frac{1}{2} + \frac{1}{2}\cos(2\theta)$:
$$X_{RMS}^2 = \frac{A^2}{T_0} \int_{0}^{T_0} \left[ \frac{1}{2} + \frac{1}{2}\cos(4\pi f_0 t + 2\phi) \right] dt$$
Como estamos integrando um cosseno ($\cos(4\pi f_0 t + 2\phi)$) sobre múltiplos exatos do seu período (ele completa dois ciclos exatos em $T_0$), a integral da parte senoidal oscilante zera. Resta apenas a constante:
$$X_{RMS}^2 = \frac{A^2}{T_0} \int_{0}^{T_0} \frac{1}{2} dt = \frac{A^2}{T_0} \left( \frac{1}{2} T_0 \right) = \frac{A^2}{2}$$
Tirando a raiz quadrada, obtemos o valor RMS:
$$X_{RMS} = \frac{A}{\sqrt{2}}$$

---

## 5) Determine quais das seguintes propriedades se aplicam ao sistema contínuo no tempo $y(t) = t \cdot x(t)$. Justifique sua resposta. (0,6 pts. cada)
*(Origem: Exemplo clássico do livro do Oppenheim, Capítulo 1)*

**a) Invariância no tempo: NÃO se aplica.**
Justificativa: Um atraso de tempo $t_0$ na entrada produz $x_1(t) = x(t-t_0)$. A saída para essa nova entrada seria $y_1(t) = t \cdot x(t-t_0)$. Porém, se o sistema fosse invariante, a saída seria a própria $y(t)$ deslocada: $y(t-t_0) = (t-t_0)x(t-t_0)$. Como $t \cdot x(t-t_0) \neq (t-t_0)x(t-t_0)$, o sistema varia no tempo devido ao coeficiente $t$.

**b) Causalidade: SIM se aplica.**
Justificativa: Um sistema é causal se a saída em um instante temporal depende apenas de valores da entrada no presente ou no passado. Para qualquer instante escolhido $t$, o valor de $y(t)$ depende apenas do valor de $x$ naquele exato instante temporal $t$, multiplicado pelo escalar $t$. Como não requer conhecimento futuro da entrada, ele é causal (na verdade, é até um sistema "sem memória").

**c) Estabilidade: NÃO se aplica.**
Justificativa: O critério de estabilidade BIBO (*Bounded-Input Bounded-Output*) dita que para toda entrada limitada, a saída deve ser limitada. Se aplicarmos uma entrada constante $x(t) = 1$ (que é limitada por $B=1$), a saída será $y(t) = t$. Conforme $t \to \infty$, a saída tenderá ao infinito, tornando-se ilimitada. Logo, o sistema é instável.

**d) Linearidade: SIM se aplica.**
Justificativa: Aplicando o princípio da superposição, para uma entrada $x(t) = a \cdot x_1(t) + b \cdot x_2(t)$:
$$y(t) = t \cdot [a \cdot x_1(t) + b \cdot x_2(t)] = a \cdot t \cdot x_1(t) + b \cdot t \cdot x_2(t) = a \cdot y_1(t) + b \cdot y_2(t)$$
A equação da saída é exatamente a combinação linear das saídas individuais, portanto o sistema é linear.
