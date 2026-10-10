# Lista de Treino - Nível Médio (15 Questões)
**Disciplina:** Sinais e Sistemas (TEC 412)
**Tópicos:** Aplicações Algébricas, Sinais Discretos e Manipulação de Tempo.

---

## Tópico 1: Sinais Pares e Ímpares

**Questão 1:** Determine a parte par do sinal $x(t) = e^{j2t} + \cos(3t)$.
> **Resolução:**
> Expandindo $e^{j2t} = \cos(2t) + j\sin(2t)$.
> Então $x(t) = \cos(2t) + j\sin(2t) + \cos(3t)$.
> Invertendo: $x(-t) = \cos(-2t) + j\sin(-2t) + \cos(-3t) = \cos(2t) - j\sin(2t) + \cos(3t)$.
> Parte Par: $x_p(t) = \frac{x(t) + x(-t)}{2}$.
> Ao somar, os senos imaginários se anulam.
> $x_p(t) = \frac{2\cos(2t) + 2\cos(3t)}{2} = \cos(2t) + \cos(3t)$.

**Questão 2:** O pulso discreto $x[n] = u[n] - u[n-4]$ não é par. Determine sua parte par $x_p[n]$.
> **Resolução:**
> O pulso vale 1 para $n \in \{0, 1, 2, 3\}$.
> $x[-n] = u[-n] - u[-n-4]$, que vale 1 para $n \in \{-3, -2, -1, 0\}$.
> Parte Par: $x_p[n] = \frac{x[n] + x[-n]}{2}$.
> Para $n=0$: $x_p[0] = (1+1)/2 = 1$.
> Para $n \in \{1, 2, 3\}$ e $n \in \{-1, -2, -3\}$: apenas uma das parcelas vale 1, logo $x_p[n] = 0.5$.
> Para $n \ge 4$ ou $n \le -4$: ambas zeram, $x_p[n]=0$.

---

## Tópico 2: Energia e Potência

**Questão 3:** Calcule a energia do sinal $x(t) = e^{-3t}u(t)$.
> **Resolução:**
> $E = \int_{0}^{\infty} (e^{-3t})^2 dt = \int_{0}^{\infty} e^{-6t} dt$
> $E = \left[ \frac{e^{-6t}}{-6} \right]_0^\infty = 0 - \left( \frac{1}{-6} \right) = \frac{1}{6} \text{ J}$.
> **Gabarito: Sinal de Energia (1/6 Joules).**

**Questão 4:** Calcule a energia total do sinal discreto $x[n] = (\frac{1}{2})^n u[n]$.
> **Resolução:**
> Em tempo discreto, Energia é a soma infinita dos quadrados.
> $E = \sum_{n=-\infty}^{\infty} |x[n]|^2 = \sum_{n=0}^{\infty} \left( \frac{1}{2} \right)^{2n} = \sum_{n=0}^{\infty} \left( \frac{1}{4} \right)^n$.
> Essa é uma progressão geométrica de razão $r = 1/4$.
> Soma PG infinita: $S = \frac{1}{1 - r} = \frac{1}{1 - 1/4} = \frac{1}{3/4} = \frac{4}{3}$.
> **Gabarito: Energia = 4/3.**

---

## Tópico 3: Memória

**Questão 5:** O integrador genérico $y(t) = \int_{-\infty}^{t} x(\tau) d\tau$ possui memória?
> **Resolução:**
> A integral computa a área da entrada desde $-\infty$ até o instante presente $t$. Isso exige o acúmulo e armazenamento de todos os infinitos valores passados.
> **Gabarito: Com Memória.**

**Questão 6:** O filtro extrator de pico $y[n] = \max(x[n], x[n-1])$ é sem memória?
> **Resolução:**
> O sistema precisa comparar o valor atual da entrada ($x[n]$) com o valor imediatamente anterior ($x[n-1]$). Como requer a leitura de $n-1$ (passado), o sistema exige registro de armazenamento da última amostra.
> **Gabarito: Com Memória.**

---

## Tópico 4: Causalidade

**Questão 7:** O sistema $y(t) = x(t/3)$ é causal?
> **Resolução:**
> Testando um tempo positivo, digamos $t=6$.
> $y(6) = x(6/3) = x(2)$. Ele precisa do passado. Parece causal.
> Testando um tempo negativo, digamos $t=-6$.
> $y(-6) = x(-6/3) = x(-2)$.
> Para calcular o que ocorre hoje no instante $-6$, eu preciso de uma informação do instante $-2$. Como $-2$ é MAIOR que $-6$, $-2$ está no futuro relativo!
> **Gabarito: NÃO-Causal.**

**Questão 8:** O sistema $y(t) = x(t) \cdot \cos(t+1)$ é causal?
> **Resolução:**
> O "+1" está dentro do cosseno, que é o ganho do sistema. Mas não está dentro do "x(t)". A entrada exigida para a saída $y(t_0)$ é APENAS $x(t_0)$. Não se lê o futuro do sinal de entrada.
> **Gabarito: Causal.**

---

## Tópico 5: Linearidade

**Questão 9:** O sistema extrator de parte real $y(t) = \text{Re}\{x(t)\}$ é linear?
> **Resolução:**
> Seja a combinação complexa genérica $a \cdot x_1(t) + b \cdot x_2(t)$, onde $a$ e $b$ podem ser coeficientes **complexos**.
> Se o sistema for linear para qualquer constante complexa, a saída será $y_3(t) = \text{Re}\{a \cdot x_1(t) + b \cdot x_2(t)\}$.
> Porém, $\text{Re}\{a \cdot x\} \neq a \cdot \text{Re}\{x\}$ se '$a$' tiver parte imaginária. (Ex: se $a=j$ e $x=1$, $\text{Re}\{j \cdot 1\} = 0$, mas $j \cdot \text{Re}\{1\} = j$).
> A linearidade morre no campo complexo.
> **Gabarito: NÃO-Linear.**

**Questão 10:** O sistema $y(t) = \int_{0}^{t} x(\tau) d\tau$ é linear?
> **Resolução:**
> Entrada combinada: $x_3(t) = ax_1(t) + bx_2(t)$.
> $y_3(t) = \int_{0}^{t} [ax_1(\tau) + bx_2(\tau)] d\tau$.
> Pela propriedade da integral da soma, abrimos em duas:
> $y_3(t) = a\int_{0}^{t} x_1(\tau) d\tau + b\int_{0}^{t} x_2(\tau) d\tau$.
> Que resulta exatamente em $a y_1(t) + b y_2(t)$.
> **Gabarito: Linear.**

---

## Tópico 6: Invariância no Tempo

**Questão 11:** O sistema modulador $y(t) = \sin(t) \cdot x(t)$ é invariante no tempo?
> **Resolução:**
> Atrasando apenas o sinal de entrada: $y_1(t) = \sin(t) \cdot x(t-t_0)$.
> Atrasando todas as variáveis temporais do sistema: $y_2(t) = \sin(t-t_0) \cdot x(t-t_0)$.
> É claro que $y_1(t) \neq y_2(t)$. O ganho oscila no tempo.
> **Gabarito: Variante no Tempo.**

**Questão 12:** O sistema dizimador $y[n] = x[2n]$ é invariante no tempo?
> **Resolução:**
> 1) Atrasa entrada: O sinal $x_1[n] = x[n-n_0]$ gerará a saída $y_1[n] = x[2n - n_0]$.
> 2) Atrasa a saída: Substitui $n$ por $n-n_0$: $y_2[n] = y[n-n_0] = x[2(n-n_0)] = x[2n - 2n_0]$.
> Como $x[2n - n_0] \neq x[2n - 2n_0]$, ele varia com a época de aplicação.
> **Gabarito: Variante no Tempo.**

---

## Tópico 7: Estabilidade BIBO

**Questão 13:** O sistema $y(t) = e^{x(t)}$ é estável?
> **Resolução:**
> Supomos entrada limitada $-B \le x(t) \le B$.
> A máxima excursão possível da saída ocorre quando a entrada é $+B$:
> $y(t)_{max} = e^B$.
> Sendo $e \approx 2.71$ e $B$ finito, $e^B$ é rigorosamente um número finito. Não há como tender ao infinito sem que a própria entrada o faça.
> **Gabarito: Estável.**

**Questão 14:** O sistema $y[n] = \log(1 + |x[n]|)$ é estável?
> **Resolução:**
> Como a entrada é restrita em $|x[n]| \le B$:
> A máxima saída será $y_{max} = \log(1 + B)$. O logaritmo cresce muito devagar, e o logaritmo de qualquer número finito positivo sempre resulta num valor finito.
> **Gabarito: Estável.**

---

## Tópico 8: Mistura de Conceitos

**Questão 15:** Classifique o sistema com atraso fixo $y(t) = x(t) + x(t-1)$ quanto aos 4 critérios base.
> **Resolução e Gabarito:**
> 1. Memória: Precisa do instante atual ($t$) e do passado ($t-1$). **Com Memória.**
> 2. Causalidade: Como o argumento $t-1$ nunca será maior que $t$, ele jamais exigirá o futuro. **Causal.**
> 3. Linearidade: A soma de sinais combina perfeitamente sem elevar a potências ou inserir constantes isoladas. **Linear.**
> 4. Invariância: Atrasar a entrada gera $x(t-t_0) + x(t-t_0-1)$. Atrasar as referências 't' na equação geral gera exatamente $x(t-t_0) + x((t-t_0)-1)$. **Invariante no Tempo.**
