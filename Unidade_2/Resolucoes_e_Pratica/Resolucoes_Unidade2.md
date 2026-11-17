# Resoluções da 2ª Lista de Exercícios — TEC 412 (Sinais e Sistemas)

*Material elaborado rigorosamente segundo os critérios da disciplina (Prof. Edgar Silva Júnior), com desenvolvimento algébrico passo a passo (linha a linha, em nível de prova), categorizado por blocos temáticos cronológicos e conferido com os gabaritos oficiais dos livros de referência (**Oppenheim & Willsky, 2ª Ed.** e **Haykin & Van Veen, Bookman**).*

---

# 📚 BLOCO 1: Convolução em Tempo Discreto — Soma de Convolução e Superposição

> **💡 Lembrete Fundamental para a Prova (Soma de Convolução):**
> A saída $y[n]$ de um Sistema Linear Invariante no Tempo (SLIT / LTI) de tempo discreto com resposta ao impulso $h[n]$ para uma entrada $x[n]$ é dada por:
> $$y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$$
> **Como os degraus $u[\cdot]$ cortam o somatório:**
> - Um termo $u[k - k_0]$ na entrada $x[k]$ só vale $1$ quando $k - k_0 \ge 0 \implies k \ge k_0$ (define o **limite inferior** de $k$).
> - Um termo $u[n - k - m_0]$ no sinal refletido $h[n-k]$ só vale $1$ quando $n - k - m_0 \ge 0 \implies k \le n - m_0$ (define o **limite superior** de $k$).
> - **Fórmula da Soma de Progressão Geométrica (PG) Finita** (de $k = A$ até $k = B$, com $B \ge A$):
>   $$\sum_{k=A}^{B} r^k = \begin{cases} \dfrac{r^A - r^{B+1}}{1 - r}, & \text{se } r \neq 1 \\[0.8em] B - A + 1, & \text{se } r = 1 \end{cases}$$

---

## Questão 1.1 — [Exercício 1.1 em Sala de Aula — Apostila, pág. 14]
**Sejam os sinais $x[n] = -u[n] + 2u[n-3] - u[n-6]$ e $h[n] = u[n+1] - u[n-10]$ a entrada e o sistema, respectivamente. Encontre a saída deste sistema $y[n] = x[n] * h[n]$.**

### **Resolução Passo a Passo:**

#### **Passo 1: Interpretar e destrinchar as funções na variável auxiliar $k$**
1. **Sinal de entrada $x[k] = -u[k] + 2u[k-3] - u[k-6]$:**
   Vamos avaliar o valor de $x[k]$ em cada trecho do eixo $k$:
   - Para $k < 0$: todos os degraus estão desligados $\implies x[k] = 0$.
   - Para $0 \le k \le 2$ ($k = 0, 1, 2$): apenas $u[k]$ ligou $\implies x[k] = -1$.
   - Para $3 \le k \le 5$ ($k = 3, 4, 5$): $u[k-3]$ também ligou $\implies x[k] = -1 + 2 = +1$.
   - Para $k \ge 6$: $u[k-6]$ ligou $\implies x[k] = -1 + 2 - 1 = 0$.

   Logo, $x[k]$ é um sinal de duração finita (6 amostras ao todo):
   $$x[k] = \begin{cases} -1, & 0 \le k \le 2 \\ +1, & 3 \le k \le 5 \\ 0, & \text{caso contrário} \end{cases}$$

2. **Resposta ao impulso refletida e deslocada $h[n-k]$:**
   Temos $h[k] = u[k+1] - u[k-10]$, que é um pulso retangular de amplitude $1$ existente para $-1 \le k \le 9$ (total de $9 - (-1) + 1 = 11$ amostras).
   Substituindo $k$ por $n-k$, obtemos:
   $$h[n-k] = u[n-k+1] - u[n-k-10]$$
   O pulso $h[n-k]$ vale $1$ quando:
   $$-1 \le n - k \le 9 \iff -9 \le k - n \le 1 \iff n - 9 \le k \le n + 1$$
   Ou seja, $h[n-k]$ é uma "janela deslizante" de altura $1$ que começa na **cauda esquerda** $k = n-9$ e termina na **frente direita** $k = n+1$.

---

#### **Passo 2: Montar o método — pedaços de $x[k]$, bordas da janela e eventos**

**2.1 — Pedaços de $x[k]$.** Um *pedaço* é um trecho de $k$ onde $x[k]$ segue **uma única fórmula** (aqui, uma constante):
- **Pedaço A:** $x[k] = -1$ para $k = 0, 1, 2$;
- **Pedaço B:** $x[k] = +1$ para $k = 3, 4, 5$.

Os **pontos de quebra** (onde a fórmula de $x[k]$ muda) são $k = 0$ (A começa), $k = 3$ (B começa) e $k = 6$ (primeiro $k$ após o fim do sinal). Fora de $[0, 5]$ temos $x[k] = 0$, que não contribui para a soma.

**2.2 — Bordas da janela $h[n-k]$.** Pelo Passo 1, a janela vale $1$ de $k = n-9$ (**cauda**, borda esquerda) até $k = n+1$ (**frente**, borda direita), e ambas andam para a direita à medida que $n$ cresce.

**2.3 — Eventos.** A fórmula de $y[n]$ só muda quando uma borda da janela **cruza um ponto de quebra** de $x[k]$. Igualando cada borda a cada quebra e resolvendo para $n$ (o valor obtido é o **primeiro** $n$ da nova situação):

| Borda | Encontra a quebra | Equação | $n$ | O que acontece |
|:---:|:---:|:---:|:---:|:---|
| frente | $k=0$ | $n+1 = 0$ | $-1$ | a janela começa a tocar $x[k]$ |
| frente | $k=3$ | $n+1 = 3$ | $2$ | a frente entra no pedaço B ($+1$) |
| frente | $k=6$ | $n+1 = 6$ | $5$ | a frente passa do fim de $x[k]$ (sinal todo dentro da janela) |
| cauda | $k=0$ | $n-9 = 0$ | $9$ | a cauda começa a "soltar" o pedaço A |
| cauda | $k=3$ | $n-9 = 3$ | $12$ | a cauda chega ao pedaço B (A saiu todo) |
| cauda | $k=6$ | $n-9 = 6$ | $15$ | a cauda passa do fim de $x[k]$ (fim da sobreposição) |

Os 6 eventos cortam o eixo $n$ em **7 intervalos**:

```
   I1   │  I2   │  I3   │   I4    │  I5   │  I6   │  I7
────────┼───────┼───────┼─────────┼───────┼───────┼──────► n
       −1       2       5         9      12      15
```

> **Por que todos os eventos da frente vêm antes dos da cauda?** Porque a janela (11 amostras) é **mais larga** que $x[k]$ (6 amostras): a frente atravessa o sinal inteiro (até $n = 5$) antes de a cauda chegar ($n = 9$). Por isso a etapa do meio é "$x[k]$ inteiro dentro da janela". Se a janela fosse mais estreita que $x[k]$, a etapa do meio seria "janela inteira dentro de $x[k]$".

**2.4 — Regras de conta usadas em todos os intervalos.**

1. **Limites de cada pedaço** (interseção entre a janela e o pedaço):
   - limite inferior $= \max(\text{cauda},\ \text{início do pedaço})$;
   - limite superior $= \min(\text{frente},\ \text{fim do pedaço})$;
   - se o limite inferior for **maior** que o superior, o pedaço não entra (soma vazia $= 0$).
2. **Soma de uma constante $c$** de $k = A$ até $k = B$:
   $$\sum_{k=A}^{B} c = c\cdot(B - A + 1)$$
   ⚠️ O "$+1$" conta o próprio ponto inicial: de $0$ até $2$ são **3** termos ($0, 1, 2$), e não 2.

---

#### **Passo 3: Avaliar a soma de convolução em cada um dos 7 intervalos**

Em todos os intervalos, o roteiro é o mesmo: **(a)** situação; **(b)** faixa de $n$; **(c)** posição da outra borda; **(d)** limites de cada pedaço; **(e)** soma montada; **(f)** conta; **(g)** prova real.

---

##### **Intervalo 1: $n \le -2$ (sem sobreposição à esquerda)**

**(a) Situação:** a janela está inteira à esquerda de $x[k]$; ainda não tocou nada.

**(b) Faixa de $n$:** não há sobreposição enquanto a frente estiver antes de $k = 0$:
$$n + 1 < 0 \implies n < -1 \implies n \le -2$$

**(c) Outra borda:** a cauda ($n-9$) está ainda mais à esquerda que a frente, logo também está fora.

**(d) Limites:**
- Pedaço A: inferior $= \max(n-9,\ 0) = 0$ (pois $n - 9 \le -11 < 0$); superior $= \min(n+1,\ 2) = n+1$ (pois $n+1 \le -1$). Como $0 > n+1$, a soma é **vazia**.
- Pedaço B: inferior $= \max(n-9,\ 3) = 3$; superior $= \min(n+1,\ 5) = n+1 \le -1$. Como $3 > n+1$, a soma é **vazia**.

**(e)/(f) Resultado:**
$$y[n] = 0 + 0 = 0, \quad \text{para } n \le -2$$

**(g) Prova real ($n = -2$):** a janela cobre $k = -11, \dots, -1$; nesses $k$, $x[k] = 0$ $\implies y[-2] = 0$. ✓

---

##### **Intervalo 2: $-1 \le n \le 1$ (a frente entra no pedaço A)**

**(a) Situação:** a frente entrou no pedaço A ($-1$) e ainda não chegou ao pedaço B.

**(b) Faixa de $n$:** a frente está dentro de $[0, 2]$:
$$0 \le n + 1 \le 2$$
Subtraindo $1$ dos três lados:
$$-1 \le n \le 1$$
- $n = -1$ é o primeiro instante (a frente chega em $k = 0$);
- $n = 1$ é o último (a frente está em $k = 2$); em $n = 2$ ela pisa em $k = 3$ e começa o Intervalo 3.

**(c) Outra borda:** como $n \le 1$:
$$n - 9 \le 1 - 9 = -8 < 0$$
A cauda está à esquerda de $x[k]$ e não corta nada; quem limita a soma pela esquerda é o próprio $x[k]$ (que começa em $k = 0$).

**(d) Limites:**
- Pedaço A: inferior $= \max(n-9,\ 0) = 0$ ($n-9$ é negativo); superior $= \min(n+1,\ 2) = n+1$ (pois $n+1 \le 2$) $\implies k$ de $0$ até $n+1$.
- Pedaço B: inferior $= \max(n-9,\ 3) = 3$; superior $= \min(n+1,\ 5) = n+1 \le 2$. Como $3 > n+1$, **não entra**.

**(e) Soma montada:**
$$y[n] = \sum_{k=0}^{n+1} \underbrace{x[k]}_{-1}\cdot\underbrace{h[n-k]}_{1} = \sum_{k=0}^{n+1} (-1)$$

**(f) Conta:**
$$\text{nº de termos} = (n+1) - 0 + 1 = n + 2$$
$$y[n] = (-1)\cdot(n+2)$$
$$y[n] = -n - 2, \quad \text{para } -1 \le n \le 1$$

**(g) Prova real:**

| $n$ | Janela ($k$) | $k$ com $x[k] \ne 0$ | Soma direta | $-n-2$ |
|:---:|:---:|:---:|:---:|:---:|
| $-1$ | $-10 \dots 0$ | $0$ | $-1$ | $-1$ ✓ |
| $0$ | $-9 \dots 1$ | $0, 1$ | $-1-1 = -2$ | $-2$ ✓ |
| $1$ | $-8 \dots 2$ | $0, 1, 2$ | $-1-1-1 = -3$ | $-3$ ✓ |

Detalhe do caso $n = 0$:
```
k        : -9 ... -1   0   1   2   3   4   5
x[k]     :  0 ...  0  -1  -1  -1  +1  +1  +1
h[0-k]   :  1 ...  1   1   1   0   0   0   0
produto  :  0 ...  0  -1  -1   0   0   0   0     →  soma = −2
```

---

##### **Intervalo 3: $2 \le n \le 4$ (a frente entra no pedaço B)**

**(a) Situação:** a frente passou do pedaço A e entrou no pedaço B. O pedaço A está **inteiro** dentro da janela; o pedaço B, só em parte.

**(b) Faixa de $n$:** a frente está dentro de $[3, 5]$:
$$3 \le n + 1 \le 5$$
Subtraindo $1$:
$$2 \le n \le 4$$

**(c) Outra borda:**
$$n - 9 \le 4 - 9 = -5 < 0$$
A cauda continua à esquerda de $x[k]$.

**(d) Limites:**
- Pedaço A: inferior $= \max(n-9,\ 0) = 0$; superior $= \min(n+1,\ 2) = 2$ (pois $n+1 \ge 3 > 2$) $\implies k$ de $0$ até $2$ (pedaço A inteiro).
- Pedaço B: inferior $= \max(n-9,\ 3) = 3$; superior $= \min(n+1,\ 5) = n+1$ (pois $n+1 \le 5$) $\implies k$ de $3$ até $n+1$.

**(e) Soma montada** (agora com duas parcelas):
$$y[n] = \sum_{k=0}^{2} (-1)\cdot(1) + \sum_{k=3}^{n+1} (+1)\cdot(1)$$

**(f) Conta**, uma parcela de cada vez:
- Parcela A: $\text{nº de termos} = 2 - 0 + 1 = 3 \implies (-1)\cdot 3 = -3$
- Parcela B: $\text{nº de termos} = (n+1) - 3 + 1 = n - 1 \implies (+1)\cdot(n-1) = n - 1$

$$y[n] = -3 + (n - 1)$$
$$y[n] = n - 4, \quad \text{para } 2 \le n \le 4$$

**(g) Prova real:**

| $n$ | Janela ($k$) | Contribuições | Soma direta | $n-4$ |
|:---:|:---:|:---|:---:|:---:|
| $2$ | $-7 \dots 3$ | A: $k=0,1,2 \to -3$; B: $k=3 \to +1$ | $-2$ | $-2$ ✓ |
| $3$ | $-6 \dots 4$ | A: $-3$; B: $k=3,4 \to +2$ | $-1$ | $-1$ ✓ |
| $4$ | $-5 \dots 5$ | A: $-3$; B: $k=3,4,5 \to +3$ | $0$ | $0$ ✓ |

---

##### **Intervalo 4: $5 \le n \le 8$ ($x[k]$ inteiro dentro da janela)**

**(a) Situação:** a frente já passou do fim de $x[k]$ e a cauda ainda não chegou ao começo. O sinal inteiro está dentro da janela.

**(b) Faixa de $n$:** duas condições simultâneas:
- frente depois do fim de $x[k]$: $n + 1 \ge 6 \implies n \ge 5$;
- cauda antes do começo de $x[k]$: $n - 9 < 0 \implies n < 9 \implies n \le 8$.

$$\implies 5 \le n \le 8$$

**(c) Outra borda:** já conferida no item (b) (as duas bordas estão fora de $[0, 5]$).

**(d) Limites:**
- Pedaço A: inferior $= \max(n-9,\ 0) = 0$ ($n-9 \le -1$); superior $= \min(n+1,\ 2) = 2$ ($n+1 \ge 6$) $\implies k$ de $0$ até $2$.
- Pedaço B: inferior $= \max(n-9,\ 3) = 3$; superior $= \min(n+1,\ 5) = 5$ $\implies k$ de $3$ até $5$.

**(e) Soma montada:**
$$y[n] = \sum_{k=0}^{2} (-1)\cdot(1) + \sum_{k=3}^{5} (+1)\cdot(1)$$

**(f) Conta:**
- Parcela A: $\text{nº de termos} = 2 - 0 + 1 = 3 \implies (-1)\cdot 3 = -3$
- Parcela B: $\text{nº de termos} = 5 - 3 + 1 = 3 \implies (+1)\cdot 3 = +3$

$$y[n] = -3 + 3 = 0, \quad \text{para } 5 \le n \le 8$$

O resultado não depende de $n$: enquanto $x[k]$ estiver inteiro dentro da janela, $y[n]$ é a soma de todas as amostras de $x$, que é $-3 + 3 = 0$.

**(g) Prova real ($n = 6$):** a janela cobre $k = -3, \dots, 7$ e pega todo o sinal: $-1-1-1+1+1+1 = 0$. ✓

---

##### **Intervalo 5: $9 \le n \le 11$ (a cauda atravessa o pedaço A)**

**(a) Situação:** a cauda entrou no pedaço A e começa a "soltar" as amostras $-1$; a frente continua depois do fim do sinal.

**(b) Faixa de $n$:** a cauda está dentro de $[0, 2]$:
$$0 \le n - 9 \le 2$$
Somando $9$ aos três lados:
$$9 \le n \le 11$$

**(c) Outra borda:**
$$n + 1 \ge 9 + 1 = 10 > 5$$
A frente está depois do fim de $x[k]$.

**(d) Limites:**
- Pedaço A: inferior $= \max(n-9,\ 0) = n-9$ (pois $n-9 \ge 0$); superior $= \min(n+1,\ 2) = 2$ $\implies k$ de $n-9$ até $2$.
- Pedaço B: inferior $= \max(n-9,\ 3) = 3$ (pois $n - 9 \le 2 < 3$); superior $= \min(n+1,\ 5) = 5$ $\implies k$ de $3$ até $5$.

**(e) Soma montada:**
$$y[n] = \sum_{k=n-9}^{2} (-1)\cdot(1) + \sum_{k=3}^{5} (+1)\cdot(1)$$

**(f) Conta:**
- Parcela A:
  $$\text{nº de termos} = 2 - (n - 9) + 1 = 2 - n + 9 + 1 = 12 - n$$
  $$\text{soma} = (-1)\cdot(12 - n) = n - 12$$
- Parcela B: $\text{nº de termos} = 5 - 3 + 1 = 3 \implies (+1)\cdot 3 = 3$

$$y[n] = (n - 12) + 3$$
$$y[n] = n - 9, \quad \text{para } 9 \le n \le 11$$

⚠️ **Atenção ao sinal:** $-(n - 9) = -n + 9$. É o erro de sinal mais comum neste intervalo.

**(g) Prova real:**

| $n$ | Janela ($k$) | Contribuições | Soma direta | $n-9$ |
|:---:|:---:|:---|:---:|:---:|
| $9$ | $0 \dots 10$ | A: $k=0,1,2 \to -3$; B: $+3$ | $0$ | $0$ ✓ |
| $10$ | $1 \dots 11$ | A: $k=1,2 \to -2$; B: $+3$ | $1$ | $1$ ✓ |
| $11$ | $2 \dots 12$ | A: $k=2 \to -1$; B: $+3$ | $2$ | $2$ ✓ |

---

##### **Intervalo 6: $12 \le n \le 14$ (a cauda atravessa o pedaço B)**

**(a) Situação:** a cauda já passou do pedaço A (as amostras $-1$ saíram todas) e está dentro do pedaço B.

**(b) Faixa de $n$:** a cauda está dentro de $[3, 5]$:
$$3 \le n - 9 \le 5$$
Somando $9$:
$$12 \le n \le 14$$

**(c) Outra borda:**
$$n + 1 \ge 13 > 5$$
A frente está depois do fim de $x[k]$.

**(d) Limites:**
- Pedaço A: inferior $= \max(n-9,\ 0) = n-9 \ge 3$; superior $= \min(n+1,\ 2) = 2$. Como $n - 9 > 2$, a soma é **vazia** (não entra).
- Pedaço B: inferior $= \max(n-9,\ 3) = n-9$ (pois $n-9 \ge 3$); superior $= \min(n+1,\ 5) = 5$ $\implies k$ de $n-9$ até $5$.

**(e) Soma montada:**
$$y[n] = \sum_{k=n-9}^{5} (+1)\cdot(1)$$

**(f) Conta:**
$$\text{nº de termos} = 5 - (n - 9) + 1 = 5 - n + 9 + 1 = 15 - n$$
$$y[n] = (+1)\cdot(15 - n)$$
$$y[n] = 15 - n, \quad \text{para } 12 \le n \le 14$$

**(g) Prova real:**

| $n$ | Janela ($k$) | Contribuições | Soma direta | $15-n$ |
|:---:|:---:|:---|:---:|:---:|
| $12$ | $3 \dots 13$ | B: $k=3,4,5 \to +3$ | $3$ | $3$ ✓ |
| $13$ | $4 \dots 14$ | B: $k=4,5 \to +2$ | $2$ | $2$ ✓ |
| $14$ | $5 \dots 15$ | B: $k=5 \to +1$ | $1$ | $1$ ✓ |

---

##### **Intervalo 7: $n \ge 15$ (sem sobreposição à direita)**

**(a) Situação:** a cauda passou do fim de $x[k]$; a janela está inteira à direita do sinal.

**(b) Faixa de $n$:**
$$n - 9 > 5 \implies n > 14 \implies n \ge 15$$

**(c) Outra borda:** a frente ($n+1$) está ainda mais à direita que a cauda, logo também está fora.

**(d) Limites:**
- Pedaço A: inferior $= \max(n-9,\ 0) = n - 9 \ge 6$; superior $= 2$. Como $6 > 2$, **vazia**.
- Pedaço B: inferior $= \max(n-9,\ 3) = n - 9 \ge 6$; superior $= 5$. Como $6 > 5$, **vazia**.

**(e)/(f) Resultado:**
$$y[n] = 0, \quad \text{para } n \ge 15$$

**(g) Prova real ($n = 15$):** a janela cobre $k = 6, \dots, 16$; nesses $k$, $x[k] = 0$ $\implies y[15] = 0$. ✓

### **Resposta Final (Questão 1.1):**
$$y[n] = \begin{cases} 0, & n \le -2 \\ -n - 2, & -1 \le n \le 1 \\ n - 4, & 2 \le n \le 4 \\ 0, & 5 \le n \le 8 \\ n - 9, & 9 \le n \le 11 \\ 15 - n, & 12 \le n \le 14 \\ 0, & n \ge 15 \end{cases}$$

**Sequência completa (amostras não nulas e zeros internos):**

| $n$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ | $13$ | $14$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $y[n]$ | $-1$ | $-2$ | $-3$ | $-2$ | $-1$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $1$ | $2$ | $3$ | $2$ | $1$ |

**Verificações finais (prova real em segundos):**
1. **Início:** início de $x$ + início de $h$ $= 0 + (-1) = -1$ ✓ (primeira amostra não nula em $n = -1$).
2. **Fim:** fim de $x$ + fim de $h$ $= 5 + 9 = 14$ ✓ (última amostra não nula em $n = 14$).
3. **Duração:** $L_x + L_h - 1 = 6 + 11 - 1 = 16$ amostras, de $n = -1$ até $n = 14$ ✓.
4. **Soma total:** $\sum y = \left(\sum x\right)\cdot\left(\sum h\right) = 0 \cdot 11 = 0$; conferindo: $(-1-2-3-2-1) + (1+2+3+2+1) = -9 + 9 = 0$ ✓.
5. **Fronteiras:** valores vizinhos de intervalos diferentes são coerentes ($y[1] = -3 \to y[2] = -2$; $y[11] = 2 \to y[12] = 3$) ✓.

---

## Questão 2.1 — [Oppenheim 2.3, pág. 138 (EN) / pág. 83 (PT)]
**Considere uma entrada $x[n]$ e uma resposta ao impulso unitário $h[n]$ dadas por:**
$$x[n] = \left(\frac{1}{2}\right)^{n-2} u[n-2], \qquad h[n] = u[n+2]$$
**Determine e represente graficamente a saída $y[n] = x[n] * h[n]$.**

### **Resolução Passo a Passo:**

#### **Passo 1: Montar a soma de convolução**
Pela definição da soma de convolução:
$$y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$$
Substituindo $x[k] = \left(\frac{1}{2}\right)^{k-2} u[k-2]$ e $h[n-k] = u[(n-k) + 2] = u[n - k + 2]$:
$$y[n] = \sum_{k=-\infty}^{\infty} \left(\frac{1}{2}\right)^{k-2} u[k-2] \cdot u[n - k + 2]$$

#### **Passo 2: Determinar os limites do somatório impostos pelos degraus**
- O primeiro degrau $u[k-2]$ exige:
  $$k - 2 \ge 0 \implies k \ge 2 \quad \text{(Limite inferior de } k\text{)}$$
- O segundo degrau $u[n - k + 2]$ exige:
  $$n - k + 2 \ge 0 \implies k \le n + 2 \quad \text{(Limite superior de } k\text{)}$$

#### **Passo 3: Analisar as regiões de $n$**
1. **Para $n + 2 < 2 \iff n < 0$:**
   O limite superior ($n+2$) é menor que o limite inferior ($2$), logo os intervalos não se interceptam:
   $$y[n] = 0, \quad \text{para } n < 0$$

2. **Para $n + 2 \ge 2 \iff n \ge 0$:**
   O somatório fica ativo de $k = 2$ até $k = n + 2$:
   $$y[n] = \sum_{k=2}^{n+2} \left(\frac{1}{2}\right)^{k-2}$$
   Fazendo a mudança de variável $m = k - 2$:
   - Quando $k = 2 \implies m = 0$.
   - Quando $k = n + 2 \implies m = n$.

   Reescrevendo o somatório em função de $m$:
   $$y[n] = \sum_{m=0}^{n} \left(\frac{1}{2}\right)^{m}$$
   Aplicando a fórmula da soma da PG finita com razão $r = \frac{1}{2}$ de $m = 0$ até $m = n$:
   $$y[n] = \frac{1 - \left(\frac{1}{2}\right)^{n+1}}{1 - \frac{1}{2}}$$
   $$y[n] = \frac{1 - \left(\frac{1}{2}\right)^{n+1}}{\frac{1}{2}}$$
   $$y[n] = 2\left[1 - \left(\frac{1}{2}\right)^{n+1}\right], \quad \text{para } n \ge 0$$

#### **Passo 4: Expressão fechada com degrau e valores para o gráfico**
Multiplicando por $u[n]$ para incorporar a condição $n \ge 0$:
$$y[n] = 2\left[1 - \left(\frac{1}{2}\right)^{n+1}\right] u[n]$$

**Valores principais para o esboço gráfico** *(gráfico gerado em `Visualizacao_Sinais_Unidade2.ipynb`)*:
- Para $n < 0$: $y[n] = 0$
- $n = 0 \implies y[0] = 2(1 - 1/2) = 1$
- $n = 1 \implies y[1] = 2(1 - 1/4) = 1,5$
- $n = 2 \implies y[2] = 2(1 - 1/8) = 1,75$
- $n = 3 \implies y[3] = 2(1 - 1/16) = 1,875$
- Quando $n \to \infty \implies y[\infty] \to 2$ (assíntota horizontal em $2$).

> **✅ Verificação com o Gabarito Oficial (Oppenheim, pág. 554):**
> $2\left[1 - \left(\frac{1}{2}\right)^{n+1}\right]u[n]$ — **100% idêntico!**

---

## Questão 2.2 — [Oppenheim 2.4, pág. 138 (EN) / pág. 83 (PT)]
**Calcule e represente graficamente $y[n] = x[n] * h[n]$, sendo que:**
$$x[n] = \begin{cases} 1, & 3 \le n \le 8 \\ 0, & \text{caso contrário} \end{cases}, \qquad h[n] = \begin{cases} 1, & 4 \le n \le 15 \\ 0, & \text{caso contrário} \end{cases}$$

### **Resolução Passo a Passo:**

#### **Passo 1: Escrever $x[k]$ e $h[n-k]$ como janelas em $k$**
- $x[k] = 1$ no intervalo fixo:
  $$3 \le k \le 8 \quad \text{(largura de } 8 - 3 + 1 = 6 \text{ amostras)}$$
- $h[n-k] = 1$ quando o argumento $(n-k)$ está entre $4$ e $15$:
  $$4 \le n - k \le 15 \iff -15 \le k - n \le -4 \iff n - 15 \le k \le n - 4$$
  Esta é uma janela móvel de largura $12$ amostras, com **cauda esquerda** em $k = n - 15$ e **frente direita** em $k = n - 4$.

#### **Passo 2: Deslizar a janela $[n-15, n-4]$ sobre $[3, 8]$**

1. **Intervalo 1 — Antes da sobreposição ($n - 4 < 3 \implies n < 7$):**
   A frente direita $n-4$ está à esquerda de $k=3$.
   $$y[n] = 0, \quad \text{para } n < 7$$

2. **Intervalo 2 — Entrada parcial ($3 \le n - 4 \le 8 \text{ e } n - 15 < 3 \implies 7 \le n \le 11$):**
   A sobreposição vai de $k = 3$ até $k = n - 4$:
   $$y[n] = \sum_{k=3}^{n-4} (1)\cdot(1) = (n - 4) - 3 + 1$$
   $$y[n] = n - 6, \quad \text{para } 7 \le n \le 11$$
   *(Rampa crescente: $y[7]=1, y[8]=2, y[9]=3, y[10]=4, y[11]=5$).*

3. **Intervalo 3 — Sobreposição total ($n - 4 \ge 8 \text{ e } n - 15 \le 3 \implies 12 \le n \le 18$):**
   Como $h[n-k]$ (12 amostras) é mais largo que $x[k]$ (6 amostras), a janela cobre todo o intervalo $3 \le k \le 8$:
   $$y[n] = \sum_{k=3}^{8} 1 = 8 - 3 + 1$$
   $$y[n] = 6, \quad \text{para } 12 \le n \le 18$$
   *(Patamar constante de altura $6$ de $n=12$ até $n=18$).*

4. **Intervalo 4 — Saída parcial ($3 < n - 15 \le 8 \implies 19 \le n \le 23$):**
   A frente $n-4 > 8$ já saiu à direita, e a cauda $n-15$ está dentro de $[3, 8]$. A sobreposição vai de $k = n-15$ até $k = 8$:
   $$y[n] = \sum_{k=n-15}^{8} 1 = 8 - (n - 15) + 1$$
   $$y[n] = 24 - n, \quad \text{para } 19 \le n \le 23$$
   *(Rampa decrescente: $y[19]=5, y[20]=4, y[21]=3, y[22]=2, y[23]=1$; note que em $n=18$, $24-18=6$, conectando-se continuamente ao patamar).*

5. **Intervalo 5 — Fim da sobreposição ($n - 15 > 8 \implies n \ge 24$):**
   $$y[n] = 0, \quad \text{para } n \ge 24$$

### **Resposta Final (Questão 2.2):**
$$y[n] = \begin{cases} n - 6, & 7 \le n \le 11 \\ 6, & 12 \le n \le 18 \\ 24 - n, & 19 \le n \le 23 \\ 0, & \text{caso contrário} \end{cases}$$

> **✅ Verificação com o Gabarito Oficial (Oppenheim, pág. 554):**
> As expressões $n-6$, $6$, $24-n$ e $0$ batem exatamente com a pág. 554. *(Nota de revisão: no gabarito impresso da pág. 554 consta o erro tipográfico `16 <= n <= 23` na 3ª linha, mas como o patamar constante $6$ vai até $n = 18$, a descida estrita ocorre em $19 \le n \le 23$).*

---

## Questão 2.3 — [Oppenheim 2.6, pág. 138 (EN) / pág. 83 (PT)]
**Calcule e represente graficamente a convolução $y[n] = x[n] * h[n]$, sendo que:**
$$x[n] = \left(\frac{1}{3}\right)^{-n} u[-n-1] \quad \text{e} \quad h[n] = u[n-1]$$

### **Resolução Passo a Passo:**

#### **Passo 1: Simplificar a potência e montar o somatório**
Note que $\left(\frac{1}{3}\right)^{-n} = \left(3^{-1}\right)^{-n} = 3^n$. Assim:
$$x[n] = 3^n u[-n-1]$$
Montando a soma de convolução:
$$y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k] = \sum_{k=-\infty}^{\infty} 3^k u[-k-1] \cdot u[n - k - 1]$$

#### **Passo 2: Analisar as restrições dos dois degraus**
- O degrau $u[-k-1]$ exige:
  $$-k - 1 \ge 0 \implies k \le -1$$
- O degrau $u[n - k - 1]$ exige:
  $$n - k - 1 \ge 0 \implies k \le n - 1$$

Como **ambos** os degraus impõem limites superiores sobre $k$ ($k \le -1$ **e** $k \le n-1$), o índice $k$ varia de $-\infty$ até o **menor** dos dois limites superiores:
$$k \le \min(-1, \, n - 1)$$

#### **Passo 3: Dividir nos dois casos de $n$**

1. **Caso 1: $n - 1 < -1 \iff n < 0$**
   Quando $n < 0$, o menor limite superior é $n - 1$. Portanto, o somatório vai de $k = -\infty$ até $k = n - 1$:
   $$y[n] = \sum_{k=-\infty}^{n-1} 3^k$$
   Para calcular esta soma infinita à esquerda, façamos a substituição $m = -k$ (logo $k = -m$):
   - Quando $k = n - 1 \implies m = 1 - n$.
   - Quando $k \to -\infty \implies m \to +\infty$.

   Assim:
   $$y[n] = \sum_{m=1-n}^{\infty} 3^{-m} = \sum_{m=1-n}^{\infty} \left(\frac{1}{3}\right)^m$$
   Pela soma da PG infinita convergente ($\frac{\text{primeiro termo}}{1 - r}$):
   $$y[n] = \frac{\left(\frac{1}{3}\right)^{1-n}}{1 - \frac{1}{3}}$$
   $$y[n] = \frac{3^{n-1}}{\frac{2}{3}} = \frac{3^n \cdot 3^{-1}}{2 \cdot 3^{-1}}$$
   $$y[n] = \frac{3^n}{2}, \quad \text{para } n < 0$$

2. **Caso 2: $n - 1 \ge -1 \iff n \ge 0$**
   Quando $n \ge 0$, o menor limite superior trava em $k = -1$:
   $$y[n] = \sum_{k=-\infty}^{-1} 3^k$$
   Fazendo novamente $m = -k$ (de $m = 1$ até $\infty$):
   $$y[n] = \sum_{m=1}^{\infty} \left(\frac{1}{3}\right)^m = \frac{\frac{1}{3}}{1 - \frac{1}{3}} = \frac{\frac{1}{3}}{\frac{2}{3}}$$
   $$y[n] = \frac{1}{2}, \quad \text{para } n \ge 0$$

### **Resposta Final (Questão 2.3):**
$$y[n] = \begin{cases} \dfrac{3^n}{2}, & n < 0 \\[0.8em] \dfrac{1}{2}, & n \ge 0 \end{cases}$$

> **✅ Verificação com o Gabarito Oficial (Oppenheim, pág. 554):**
> $y[n] = \frac{3^n}{2}$ para $n < 0$ e $\frac{1}{2}$ para $n \ge 0$ — **100% idêntico!**

---

## Questão 2.4 — [Oppenheim 2.7, págs. 138–139 (EN) / págs. 83–84 (PT)]
**Um sistema linear $S$ tem a relação:**
$$y[n] = \sum_{k=-\infty}^{\infty} x[k]g[n - 2k]$$
**entre sua entrada $x[n]$ e sua saída $y[n]$, sendo $g[n] = u[n] - u[n-4]$.**
**(a) Determine $y[n]$ quando $x[n] = \delta[n-1]$.**
**(b) Determine $y[n]$ quando $x[n] = \delta[n-2]$.**
**(c) $S$ é LIT?**
**(d) Determine $y[n]$ quando $x[n] = u[n]$.**

### **Resolução Passo a Passo:**

#### **Item (a): Entrada $x[n] = \delta[n-1]$**
Substituindo $x[k] = \delta[k-1]$ na relação do sistema:
$$y[n] = \sum_{k=-\infty}^{\infty} \delta[k-1] g[n - 2k]$$
Pela propriedade da amostragem (filtragem) do impulso discreto, $\delta[k-1]$ só é não nulo (igual a $1$) quando $k - 1 = 0 \implies k = 1$. Portanto, todo o somatório colapsa apenas no termo $k = 1$:
$$y[n] = g[n - 2(1)] = g[n - 2]$$
Como $g[n] = u[n] - u[n-4]$, trocamos o argumento $n$ por $(n-2)$:
$$y[n] = u[n - 2] - u[(n - 2) - 4]$$
$$\mathbf{y[n] = u[n - 2] - u[n - 6]}$$

---

#### **Item (b): Entrada $x[n] = \delta[n-2]$**
Substituindo $x[k] = \delta[k-2]$ na relação do sistema:
$$y[n] = \sum_{k=-\infty}^{\infty} \delta[k-2] g[n - 2k]$$
O impulso $\delta[k-2]$ seleciona exclusivamente o índice $k = 2$:
$$y[n] = g[n - 2(2)] = g[n - 4]$$
Substituindo na expressão de $g[\cdot]$:
$$y[n] = u[n - 4] - u[(n - 4) - 4]$$
$$\mathbf{y[n] = u[n - 4] - u[n - 8]}$$

---

#### **Item (c): O sistema $S$ é LIT (Linear e Invariante no Tempo)?**
Para que o sistema linear $S$ seja Invariante no Tempo (LIT), um atraso de $n_0$ amostras na entrada deve provocar exatamente o mesmo atraso de $n_0$ amostras na saída.
- No item (a), aplicamos $x_1[n] = \delta[n-1]$ e obtivemos a saída:
  $$y_1[n] = u[n-2] - u[n-6]$$
- No item (b), aplicamos a entrada $x_2[n] = \delta[n-2]$, que é exatamente a entrada $x_1[n]$ atrasada de $1$ amostra ($x_2[n] = x_1[n-1]$).
- Se o sistema fosse invariante no tempo, a saída para $x_2[n]$ teria de ser $y_1[n-1]$:
  $$y_1[n-1] = u[(n-1)-2] - u[(n-1)-6] = u[n-3] - u[n-7]$$
- Porém, no item (b) encontramos a saída real do sistema:
  $$y_2[n] = u[n-4] - u[n-8] \neq y_1[n-1]$$

Como $y_2[n] \neq y_1[n-1]$, o sistema é **variante no tempo**.
**Resposta (c): Não, $S$ não é LIT.**

---

#### **Item (d): Entrada $x[n] = u[n]$**
Substituindo $x[k] = u[k]$ (que vale $1$ para $k \ge 0$ e $0$ para $k < 0$):
$$y[n] = \sum_{k=0}^{\infty} g[n - 2k]$$
Observe que $g[m] = u[m] - u[m-4]$ vale $1$ **somente** para os quatro inteiros $m \in \{0, 1, 2, 3\}$, e vale $0$ fora desse conjunto:
$$g[m] = \begin{cases} 1, & m \in \{0, 1, 2, 3\} \\ 0, & \text{caso contrário} \end{cases}$$
Para cada valor de $n$, o argumento $m = n - 2k$ (com $k = 0, 1, 2, 3, \dots$) percorre a sequência decrescente de passo 2:
$$m \in \{n, \, n-2, \, n-4, \, n-6, \, \dots\}$$
Vamos contar quantos termos dessa sequência caem dentro da caixa $\{0, 1, 2, 3\}$:
1. **Para $n < 0$:** Todos os valores de $n - 2k$ são negativos ($\le -1$), logo nenhum cai em $\{0, 1, 2, 3\}$:
   $$y[n] = 0, \quad \text{para } n < 0$$
2. **Para $n = 0$:** A sequência é $\{0, -2, -4, \dots\}$. Apenas $k=0$ ($m=0$) cai em $\{0, 1, 2, 3\}$:
   $$y[0] = g[0] = 1$$
3. **Para $n = 1$:** A sequência é $\{1, -1, -3, \dots\}$. Apenas $k=0$ ($m=1$) cai em $\{0, 1, 2, 3\}$:
   $$y[1] = g[1] = 1$$
4. **Para $n \ge 2$:**
   - Se $n$ é **par** ($n \ge 2$), a sequência $\{n, n-2, \dots\}$ passa por todos os números pares $\le n$, logo passa exatamente pelos **dois** pares do conjunto $\{0, 1, 2, 3\}$, que são $m = 2$ e $m = 0$:
     $$y[n] = g[2] + g[0] = 1 + 1 = 2$$
   - Se $n$ é **ímpar** ($n \ge 3$), a sequência $\{n, n-2, \dots\}$ passa por todos os números ímpares $\le n$, logo passa exatamente pelos **dois** ímpares do conjunto $\{0, 1, 2, 3\}$, que são $m = 3$ e $m = 1$:
     $$y[n] = g[3] + g[1] = 1 + 1 = 2$$

Assim, $y[n]$ vale $0$ para $n < 0$, vale $1$ em $n=0$ e $n=1$, e vale $2$ para todo $n \ge 2$. Escrevendo em termos do degrau $2u[n]$ e descontando $1$ unidade em $n=0$ e $n=1$:
$$\mathbf{y[n] = 2u[n] - \delta[n] - \delta[n-1]} \quad \text{(ou equivalentemente } y[n] = u[n] + u[n-2]\text{)}$$

> **✅ Verificação com o Gabarito Oficial (Oppenheim, pág. 554):**
> (a) $u[n-2] - u[n-6]$; (b) $u[n-4] - u[n-8]$; (c) Não; (d) $y[n] = 2u[n] - \delta[n] - \delta[n-1]$ — **100% idêntico!**

---

# 📚 BLOCO 2: Convolução em Tempo Contínuo — Integral de Convolução e Método Gráfico

> **💡 Lembrete Fundamental para a Prova (Integral de Convolução):**
> Para sistemas LIT de tempo contínuo, a saída $y(t)$ é dada pela integral de convolução:
> $$y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau)h(t - \tau)\,d\tau = \int_{-\infty}^{\infty} h(\tau)x(t - \tau)\,d\tau$$
> **Como não errar os limites de integração:**
> - Transforme $t \to \tau$ em $x(\tau)$ e $(t - \tau)$ em $h(t - \tau)$.
> - Em $h(t - \tau)$, um degrau $u(t - \tau - t_0)$ liga quando $t - \tau - t_0 \ge 0 \implies \tau \le t - t_0$ (limite **superior** em $\tau$).
> - Já um degrau reverso $u(\tau - t + t_0)$ liga quando $\tau \ge t - t_0$ (limite **inferior** em $\tau$).

---

## Questão 1.2 — [Exercício 1.2 em Sala de Aula — Apostila, pág. 23]
**Considere que a resposta ao impulso de um SLIT seja dada por $h(t) = u(t-1) - u(t-4)$. Encontre a saída deste sistema em resposta à entrada $x(t) = u(t) + u(t-1) - 2u(t-2)$.**

### **Resolução Passo a Passo:**

#### **Passo 1: Traçar e equacionar $x(\tau)$ e $h(t-\tau)$ no eixo $\tau$**
1. **Sinal de entrada $x(\tau) = u(\tau) + u(\tau-1) - 2u(\tau-2)$:**
   - Para $\tau < 0$: $x(\tau) = 0$.
   - Para $0 \le \tau < 1$: apenas $u(\tau) = 1 \implies x(\tau) = 1$.
   - Para $1 \le \tau < 2$: $u(\tau)$ e $u(\tau-1)$ estão ligados $\implies x(\tau) = 1 + 1 = 2$.
   - Para $\tau \ge 2$: $-2u(\tau-2)$ liga $\implies x(\tau) = 1 + 1 - 2 = 0$.

   Portanto, $x(\tau)$ é uma "escada" de dois degraus:
   $$x(\tau) = \begin{cases} 1, & 0 \le \tau < 1 \\ 2, & 1 \le \tau < 2 \\ 0, & \text{caso contrário} \end{cases}$$

2. **Resposta ao impulso refletida e deslocada $h(t-\tau)$:**
   Como $h(\tau) = u(\tau-1) - u(\tau-4)$ vale $1$ para $1 \le \tau \le 4$, substituindo $\tau$ por $(t-\tau)$ temos:
   $$1 \le t - \tau \le 4 \iff -4 \le \tau - t \le -1 \iff t - 4 \le \tau \le t - 1$$
   Logo, $h(t-\tau)$ é um pulso retangular de altura $1$ e largura $3$, com **cauda esquerda** em $\tau = t - 4$ e **frente direita** em $\tau = t - 1$:
   $$h(t-\tau) = \begin{cases} 1, & t - 4 \le \tau \le t - 1 \\ 0, & \text{caso contrário} \end{cases}$$

---

#### **Passo 2: Avaliar a integral de convolução nos 7 intervalos de $t$**

- **Intervalo 1 ($t - 1 < 0 \implies t < 1$):**
  A frente direita $t-1$ está antes de $\tau = 0$. Não há sobreposição:
  $$y(t) = 0, \quad \text{para } t < 1$$

- **Intervalo 2 ($0 \le t - 1 < 1 \implies 1 \le t < 2$):**
  A frente $t-1$ entra no primeiro degrau $[0, 1]$ de $x(\tau)$ (onde $x(\tau)=1$), enquanto a cauda $t-4 < -2 < 0$ está fora à esquerda:
  $$y(t) = \int_{0}^{t-1} (1)\cdot(1)\,d\tau = \Big[\tau\Big]_{0}^{t-1}$$
  $$y(t) = t - 1, \quad \text{para } 1 \le t < 2$$

- **Intervalo 3 ($1 \le t - 1 < 2 \implies 2 \le t < 3$):**
  A frente $t-1$ avança sobre o segundo degrau $[1, 2]$ (onde $x(\tau)=2$), e a cauda $t-4 < -1 < 0$ continua fora à esquerda. O pulso cobre todo $[0, 1]$ e vai de $1$ até $t-1$:
  $$y(t) = \int_{0}^{1} (1)\cdot(1)\,d\tau + \int_{1}^{t-1} (2)\cdot(1)\,d\tau$$
  $$y(t) = \Big[\tau\Big]_{0}^{1} + \Big[2\tau\Big]_{1}^{t-1}$$
  $$y(t) = 1 + 2(t - 1 - 1) = 1 + 2t - 4$$
  $$y(t) = 2t - 3, \quad \text{para } 2 \le t < 3$$

- **Intervalo 4 ($t - 1 \ge 2 \text{ e } t - 4 < 0 \implies 3 \le t < 4$):**
  Como o pulso $h(t-\tau)$ tem largura $3$ e $x(\tau)$ tem largura total $2$ ($[0, 2]$), neste intervalo $h(t-\tau)$ engloba **inteiramente** $x(\tau)$:
  $$y(t) = \int_{0}^{1} 1\,d\tau + \int_{1}^{2} 2\,d\tau = 1 + 2$$
  $$y(t) = 3, \quad \text{para } 3 \le t < 4$$

- **Intervalo 5 ($0 \le t - 4 < 1 \implies 4 \le t < 5$):**
  A frente $t-1 \ge 3 > 2$ já saiu à direita, e a cauda $t-4$ atravessa o primeiro degrau $[0, 1]$. A interseção cobre $[t-4, 1]$ (altura $1$) e todo $[1, 2]$ (altura $2$):
  $$y(t) = \int_{t-4}^{1} 1\,d\tau + \int_{1}^{2} 2\,d\tau$$
  $$y(t) = \big(1 - (t - 4)\big) + 2 = (5 - t) + 2$$
  $$y(t) = 7 - t, \quad \text{para } 4 \le t < 5$$

- **Intervalo 6 ($1 \le t - 4 < 2 \implies 5 \le t < 6$):**
  A cauda $t-4$ atravessa o segundo degrau $[1, 2]$ (altura $2$), indo de $\tau = t-4$ até $\tau = 2$:
  $$y(t) = \int_{t-4}^{2} 2\,d\tau = 2\big(2 - (t - 4)\big) = 2(6 - t)$$
  $$y(t) = 12 - 2t, \quad \text{para } 5 \le t < 6$$

- **Intervalo 7 ($t - 4 \ge 2 \implies t \ge 6$):**
  A cauda $t-4$ saiu completamente de $[0, 2]$. Não há mais sobreposição:
  $$y(t) = 0, \quad \text{para } t \ge 6$$

### **Resposta Final (Questão 1.2):**
$$y(t) = \begin{cases} 0, & t < 1 \\ t - 1, & 1 \le t < 2 \\ 2t - 3, & 2 \le t < 3 \\ 3, & 3 \le t < 4 \\ 7 - t, & 4 \le t < 5 \\ 12 - 2t, & 5 \le t < 6 \\ 0, & t \ge 6 \end{cases}$$

> **✅ Verificação com o Gabarito da Apostila (pág. 23):**
> **100% idêntico em todos os 7 intervalos!**

---

## Questão 3.1 — [Oppenheim 2.22, pág. 141 (EN) / pág. 85 (PT)]
**Para cada um dos pares de funções a seguir, use a integral de convolução para encontrar a resposta $y(t)$ do sistema LIT com resposta ao impulso $h(t)$ para a entrada $x(t)$. Esboce seus resultados.**

---

### **Item (a):**
$$x(t) = e^{-\alpha t}u(t), \qquad h(t) = e^{-\beta t}u(t) \quad (\text{Calcule quando } \alpha \neq \beta \text{ e quando } \alpha = \beta)$$

#### **Resolução Passo a Passo:**
1. **Montagem da integral:**
   $$y(t) = \int_{-\infty}^{\infty} x(\tau)h(t-\tau)\,d\tau = \int_{-\infty}^{\infty} e^{-\alpha\tau}u(\tau) \cdot e^{-\beta(t-\tau)}u(t-\tau)\,d\tau$$
2. **Cortes impostos pelos degraus:**
   - $u(\tau) = 1 \iff \tau \ge 0$ (limite inferior).
   - $u(t-\tau) = 1 \iff t - \tau \ge 0 \iff \tau \le t$ (limite superior).
   - Se $t < 0$, o limite superior é menor que $0 \implies y(t) = 0$.
   - Se $t \ge 0$, os limites vão de $\tau = 0$ até $\tau = t$:
     $$y(t) = \int_{0}^{t} e^{-\alpha\tau} e^{-\beta t} e^{\beta\tau}\,d\tau$$
     Como $e^{-\beta t}$ não depende da variável de integração $\tau$, sai da integral:
     $$y(t) = e^{-\beta t} \int_{0}^{t} e^{(\beta - \alpha)\tau}\,d\tau, \quad t \ge 0$$

3. **Subcaso 1 — Quando $\alpha \neq \beta$ ($\beta - \alpha \neq 0$):**
   $$y(t) = e^{-\beta t} \left[ \frac{e^{(\beta - \alpha)\tau}}{\beta - \alpha} \right]_{\tau=0}^{\tau=t}$$
   $$y(t) = e^{-\beta t} \left( \frac{e^{(\beta - \alpha)t} - 1}{\beta - \alpha} \right)$$
   Distribuindo $e^{-\beta t}$ no numerador ($e^{-\beta t}\cdot e^{\beta t - \alpha t} = e^{-\alpha t}$):
   $$\mathbf{y(t) = \frac{e^{-\alpha t} - e^{-\beta t}}{\beta - \alpha} u(t)}, \quad (\alpha \neq \beta)$$

4. **Subcaso 2 — Quando $\alpha = \beta$ ($\beta - \alpha = 0$):**
   O integrando torna-se $e^{0\cdot\tau} = 1$:
   $$y(t) = e^{-\alpha t} \int_{0}^{t} 1\,d\tau = e^{-\alpha t} \Big[\tau\Big]_{0}^{t} = t e^{-\alpha t}$$
   $$\mathbf{y(t) = t e^{-\alpha t} u(t)}, \quad (\alpha = \beta)$$

---

### **Item (b):**
$$x(t) = u(t) - 2u(t-2) + u(t-5), \qquad h(t) = e^{2t}u(1-t)$$

#### **Resolução Passo a Passo:**
1. **Destrinchando $x(\tau)$ e $h(t-\tau)$:**
   - $x(\tau)$:
     $$x(\tau) = \begin{cases} +1, & 0 \le \tau < 2 \\ -1, & 2 \le \tau < 5 \\ 0, & \text{caso contrário} \end{cases}$$
   - $h(t-\tau)$: substituímos $t$ por $(t-\tau)$ em $h(t) = e^{2t}u(1-t)$:
     $$h(t-\tau) = e^{2(t-\tau)} u\big(1 - (t - \tau)\big) = e^{2(t-\tau)} u\big(\tau - (t - 1)\big)$$
     O degrau $u(\tau - (t-1))$ vale $1$ quando:
     $$\tau - (t - 1) \ge 0 \iff \tau \ge t - 1$$
     Ou seja, em função de $\tau$, $h(t-\tau)$ começa em $\tau = t - 1$ (onde vale $e^2$) e estende-se para $\tau \to +\infty$ decaindo como $e^{-2\tau}$.

2. **Análise dos 4 intervalos conforme o início $\tau = t - 1$ desliza:**

   - **Intervalo 1 ($t - 1 < 0 \iff t < 1$):**
     Como $\tau \ge t - 1$ começa antes de $\tau = 0$, a região ativa de $h(t-\tau)$ cobre **ambos** os blocos de $x(\tau)$ ($[0, 2]$ e $[2, 5]$):
     $$y(t) = \int_{0}^{2} (+1)e^{2(t-\tau)}\,d\tau + \int_{2}^{5} (-1)e^{2(t-\tau)}\,d\tau$$
     Como $\int e^{2(t-\tau)}d\tau = -\frac{1}{2}e^{2(t-\tau)}$:
     $$y(t) = \left[-\frac{1}{2}e^{2(t-\tau)}\right]_{0}^{2} - \left[-\frac{1}{2}e^{2(t-\tau)}\right]_{2}^{5}$$
     $$y(t) = \frac{1}{2}\left(e^{2t} - e^{2(t-2)}\right) - \frac{1}{2}\left(e^{2(t-2)} - e^{2(t-5)}\right)$$
     $$y(t) = \frac{1}{2}\left(e^{2t} - 2e^{2(t-2)} + e^{2(t-5)}\right), \quad \text{para } t < 1$$

   - **Intervalo 2 ($0 \le t - 1 < 2 \iff 1 \le t < 3$):**
     O ponto inicial $\tau = t - 1$ está dentro do bloco positivo $[0, 2]$. Logo, a primeira integral começa em $\tau = t - 1$ (e não mais em $0$):
     $$y(t) = \int_{t-1}^{2} (+1)e^{2(t-\tau)}\,d\tau + \int_{2}^{5} (-1)e^{2(t-\tau)}\,d\tau$$
     $$y(t) = \left[-\frac{1}{2}e^{2(t-\tau)}\right]_{t-1}^{2} - \left[-\frac{1}{2}e^{2(t-\tau)}\right]_{2}^{5}$$
     Note que no limite inferior $\tau = t - 1$, temos $2(t - (t-1)) = 2$:
     $$y(t) = \frac{1}{2}\left(e^{2} - e^{2(t-2)}\right) - \frac{1}{2}\left(e^{2(t-2)} - e^{2(t-5)}\right)$$
     $$y(t) = \frac{1}{2}\left(e^{2} - 2e^{2(t-2)} + e^{2(t-5)}\right), \quad \text{para } 1 \le t < 3$$

   - **Intervalo 3 ($2 \le t - 1 < 5 \iff 3 \le t < 6$):**
     O ponto inicial $\tau = t - 1$ já passou do bloco $[0, 2]$ e agora está dentro do bloco negativo $[2, 5]$:
     $$y(t) = \int_{t-1}^{5} (-1)e^{2(t-\tau)}\,d\tau = \left[\frac{1}{2}e^{2(t-\tau)}\right]_{t-1}^{5}$$
     $$y(t) = \frac{1}{2}\left(e^{2(t-5)} - e^{2}\right), \quad \text{para } 3 \le t < 6$$

   - **Intervalo 4 ($t - 1 \ge 5 \iff t \ge 6$):**
     O início $\tau = t - 1$ ultrapassou $\tau = 5$. Não há mais interseção:
     $$y(t) = 0, \quad \text{para } t \ge 6$$

#### **Resposta Final do Item 3.1 (b):**
$$y(t) = \begin{cases} \dfrac{1}{2}\left(e^{2t} - 2e^{2(t-2)} + e^{2(t-5)}\right), & t < 1 \\[0.8em] \dfrac{1}{2}\left(e^{2} - 2e^{2(t-2)} + e^{2(t-5)}\right), & 1 \le t < 3 \\[0.8em] \dfrac{1}{2}\left(e^{2(t-5)} - e^{2}\right), & 3 \le t < 6 \\[0.8em] 0, & t \ge 6 \end{cases}$$

---

### **Item (c): $x(t)$ e $h(t)$ como mostrados na Figura P2.22(a)**
Da Figura P2.22(a) do livro:
- $x(t)$ é um único ciclo de $\text{sen}(\pi t)$ entre $t = 0$ e $t = 2$:
  $$x(t) = \begin{cases} \text{sen}(\pi t), & 0 \le t \le 2 \\ 0, & \text{caso contrário} \end{cases}$$
- $h(t)$ é um pulso retangular de amplitude $2$ entre $t = 1$ e $t = 3$:
  $$h(t) = 2\big[u(t-1) - u(t-3)\big]$$

#### **Resolução Passo a Passo:**
1. **Formar $h(t-\tau)$:**
   $h(t-\tau) = 2$ quando $1 \le t - \tau \le 3 \iff t - 3 \le \tau \le t - 1$ (janela de altura $2$ e largura $2$).
2. **Avaliar os intervalos de sobreposição entre $[t-3, t-1]$ e $[0, 2]$:**
   - **Intervalo 1 ($t - 1 < 0 \iff t < 1$):** Sem sobreposição $\implies y(t) = 0$.
   - **Intervalo 2 ($0 \le t - 1 < 2 \iff 1 \le t < 3$):**
     A frente $t-1$ está dentro de $[0, 2]$ e a cauda $t-3 < 0$ está fora à esquerda. A interseção vai de $\tau = 0$ até $\tau = t - 1$:
     $$y(t) = \int_{0}^{t-1} 2\text{sen}(\pi\tau)\,d\tau = \left[-\frac{2}{\pi}\cos(\pi\tau)\right]_{0}^{t-1}$$
     $$y(t) = \frac{2}{\pi}\Big[1 - \cos\big(\pi(t-1)\big)\Big]$$
     Como $\cos(\pi t - \pi) = -\cos(\pi t)$:
     $$y(t) = \frac{2}{\pi}\big[1 + \cos(\pi t)\big], \quad \text{para } 1 \le t < 3$$
   - **Intervalo 3 ($0 \le t - 3 < 2 \iff 3 \le t < 5$):**
     A frente $t-1 \ge 2$ já saiu à direita, e a cauda $t-3$ percorre $[0, 2]$. A interseção vai de $\tau = t - 3$ até $\tau = 2$:
     $$y(t) = \int_{t-3}^{2} 2\text{sen}(\pi\tau)\,d\tau = \left[-\frac{2}{\pi}\cos(\pi\tau)\right]_{t-3}^{2}$$
     $$y(t) = \frac{2}{\pi}\Big[\cos\big(\pi(t-3)\big) - \cos(2\pi)\Big]$$
     Como $\cos(2\pi) = 1$ e $\cos(\pi t - 3\pi) = -\cos(\pi t)$:
     $$y(t) = -\frac{2}{\pi}\big[1 + \cos(\pi t)\big], \quad \text{para } 3 \le t < 5$$
   - **Intervalo 4 ($t - 3 \ge 2 \iff t \ge 5$):** Sem sobreposição $\implies y(t) = 0$.

#### **Resposta Final do Item 3.1 (c):**
$$y(t) = \begin{cases} 0, & t < 1 \\[0.5em] \dfrac{2}{\pi}\big[1 + \cos(\pi t)\big], & 1 \le t < 3 \\[0.8em] -\dfrac{2}{\pi}\big[1 + \cos(\pi t)\big], & 3 \le t < 5 \\[0.5em] 0, & t \ge 5 \end{cases}$$

---

### **Item (d): $x(t)$ e $h(t)$ como mostrados na Figura P2.22(b)**
Lendo atentamente a Figura P2.22(b) do Oppenheim (pág. 85 PT / pág. 141 EN):
- $x(t)$ é uma reta infinita com inclinação $a$ e intercepto vertical $b$:
  $$x(t) = a t + b, \quad -\infty < t < \infty$$
- $h(t)$ é composto por um pulso retangular de altura $\frac{4}{3}$ entre $t = 0$ e $t = 1$, **mais um impulso de área (peso) $-\frac{1}{3}$ localizado em $t = 2$** (indicado pela seta vertical para baixo em $t=2$ com rótulo $-\frac{1}{3}$):
  $$h(t) = \frac{4}{3}\big[u(t) - u(t-1)\big] - \frac{1}{3}\delta(t-2)$$

#### **Resolução Passo a Passo:**
Como $x(t)$ está definido para todo $t \in \mathbb{R}$, usamos a propriedade comutativa da convolução ($y(t) = h(t) * x(t)$):
$$y(t) = \int_{-\infty}^{\infty} h(\tau)x(t-\tau)\,d\tau$$
Substituindo $x(t-\tau) = a(t-\tau) + b$ e $h(\tau)$:
$$y(t) = \int_{0}^{1} \frac{4}{3}\big[a(t-\tau) + b\big]\,d\tau + \int_{-\infty}^{\infty} \left(-\frac{1}{3}\delta(\tau-2)\right)\big[a(t-\tau) + b\big]\,d\tau$$

1. **Primeira parcela (integral no pulso de $0$ a $1$):**
   $$I_1 = \frac{4}{3}\int_{0}^{1} (at + b - a\tau)\,d\tau = \frac{4}{3}\left[(at + b)\tau - a\frac{\tau^2}{2}\right]_{0}^{1}$$
   $$I_1 = \frac{4}{3}\left(at + b - \frac{a}{2}\right) = \frac{4}{3}at + \frac{4}{3}b - \frac{2}{3}a$$

2. **Segunda parcela (propriedade da filtragem do impulso $\delta(\tau-2)$ em $\tau = 2$):**
   $$I_2 = -\frac{1}{3}\big[a(t - 2) + b\big] = -\frac{1}{3}at + \frac{2}{3}a - \frac{1}{3}b$$

3. **Somando $y(t) = I_1 + I_2$:**
   $$y(t) = \left(\frac{4}{3} - \frac{1}{3}\right)at + \left(\frac{4}{3} - \frac{1}{3}\right)b + \left(-\frac{2}{3} + \frac{2}{3}\right)a$$
   $$\mathbf{y(t) = a t + b = x(t)}, \quad \forall t \in \mathbb{R}$$

> **💡 Interpretação Física Brilhante:**
> Como a área líquida de $h(t)$ é $\int h(\tau)d\tau = \frac{4}{3} - \frac{1}{3} = 1$ e o primeiro momento temporal é $\int \tau h(\tau)d\tau = \frac{4}{3}(\frac{1}{2}) - \frac{1}{3}(2) = 0$, este sistema LIT reproduz qualquer rampa linear $x(t) = at + b$ exatamente sem atraso e sem distorção!

---

### **Item (e): $x(t)$ e $h(t)$ como mostrados na Figura P2.22(c)**
Da Figura P2.22(c):
- $x(t)$ é uma onda quadrada periódica de período fundamental $T_0 = 2$ e amplitude $\pm 1$, simétrica (par), onde os rótulos $\dots, -3, -2, -1, 0, 1, 2, 3, \dots$ estão posicionados no centro de cada semi-ciclo (ou seja, $x(t) = +1$ para $2k - \frac{1}{2} \le t < 2k + \frac{1}{2}$ e $x(t) = -1$ para $2k + \frac{1}{2} \le t < 2k + \frac{3}{2}$).
- $h(t)$ é o pulso triangular decrescente de duração $1$:
  $$h(t) = \begin{cases} 1 - t, & 0 \le t \le 1 \\ 0, & \text{caso contrário} \end{cases}$$

#### **Resolução Passo a Passo:**
1. Como $x(t)$ é periódico com período $T_0 = 2$, a saída $y(t) = \int_{0}^{1} (1-\tau)x(t-\tau)\,d\tau = \int_{t-1}^{t} (1 - t + \tau)x(\tau)\,d\tau$ também é **periódica com período $T_0 = 2$** ($y(t + 2k) = y(t)$). Basta, portanto, calcular $y(t)$ em um período completo $-\frac{1}{2} \le t < \frac{3}{2}$:

2. **Trecho 1: $-\frac{1}{2} \le t < \frac{1}{2}$**
   A janela $[t-1, t]$ de comprimento $1$ começa em $t - 1 \in [-\frac{3}{2}, -\frac{1}{2})$ (onde $x(\tau) = -1$) e termina em $t \in [-\frac{1}{2}, \frac{1}{2})$ (onde $x(\tau) = +1$), mudando de sinal em $\tau = -\frac{1}{2}$:
   $$y(t) = \int_{t-1}^{-1/2} (-1)(1 - t + \tau)\,d\tau + \int_{-1/2}^{t} (+1)(1 - t + \tau)\,d\tau$$
   Como $\int (1 - t + \tau)\,d\tau = \frac{(1 - t + \tau)^2}{2}$:
   $$y(t) = -\left[\frac{(1 - t + \tau)^2}{2}\right]_{t-1}^{-1/2} + \left[\frac{(1 - t + \tau)^2}{2}\right]_{-1/2}^{t}$$
   $$y(t) = -\frac{\left(\frac{1}{2} - t\right)^2 - 0}{2} + \frac{1^2 - \left(\frac{1}{2} - t\right)^2}{2}$$
   $$y(t) = \frac{1}{2} - \left(t - \frac{1}{2}\right)^2, \quad \text{para } -\frac{1}{2} \le t < \frac{1}{2}$$

3. **Trecho 2: $\frac{1}{2} \le t < \frac{3}{2}$**
   A janela $[t-1, t]$ começa em $t - 1 \in [-\frac{1}{2}, \frac{1}{2})$ (onde $x(\tau) = +1$) e termina em $t \in [\frac{1}{2}, \frac{3}{2})$ (onde $x(\tau) = -1$), mudando de sinal em $\tau = \frac{1}{2}$:
   $$y(t) = \int_{t-1}^{1/2} (+1)(1 - t + \tau)\,d\tau + \int_{1/2}^{t} (-1)(1 - t + \tau)\,d\tau$$
   $$y(t) = \left[\frac{(1 - t + \tau)^2}{2}\right]_{t-1}^{1/2} - \left[\frac{(1 - t + \tau)^2}{2}\right]_{1/2}^{t}$$
   $$y(t) = \frac{\left(\frac{3}{2} - t\right)^2 - 0}{2} - \frac{1^2 - \left(\frac{3}{2} - t\right)^2}{2}$$
   $$y(t) = \left(t - \frac{3}{2}\right)^2 - \frac{1}{2}, \quad \text{para } \frac{1}{2} \le t < \frac{3}{2}$$

#### **Resposta Final do Item 3.1 (e):**
Sinal periódico de período $T_0 = 2$ ($y(t + 2k) = y(t)$). A saída $y(t)$ é contínua, assumindo valores no intervalo $\left[-\frac{1}{2}, +\frac{1}{2}\right]$, com máximo $+\frac{1}{2}$ em $t = \frac{1}{2} + 2k$ e mínimo $-\frac{1}{2}$ em $t = -\frac{1}{2} + 2k$:
$$y(t) = \begin{cases} \dfrac{1}{2} - \left(t - \dfrac{1}{2}\right)^2, & -\dfrac{1}{2} \le t < \dfrac{1}{2} \\[0.8em] \left(t - \dfrac{3}{2}\right)^2 - \dfrac{1}{2}, & \dfrac{1}{2} \le t < \dfrac{3}{2} \end{cases}$$


---

# 📚 BLOCO 3: Propriedades da Convolução, Interconexões de SLITs e Caracterização pela Resposta ao Impulso ($h[n]$ e $h(t)$)

> **💡 Lembrete Fundamental para a Prova (Propriedades de SLITs via $h[n]$ e $h(t)$):**
> 1. **Interconexões:**
>    - **Paralelo (Propriedade Distributiva):** $h_{eq}[n] = h_1[n] + h_2[n]$
>    - **Cascata / Série (Propriedade Associativa):** $h_{eq}[n] = h_1[n] * h_2[n]$
> 2. **Sem Memória (Estático):**
>    - **Discreto:** $h[n] = c\delta[n]$ (ou seja, $h[n] = 0$ para todo $n \neq 0$).
>    - **Contínuo:** $h(t) = c\delta(t)$ (ou seja, $h(t) = 0$ para todo $t \neq 0$).
> 3. **Causalidade:**
>    - **Discreto:** $h[n] = 0$ para todo $n < 0$.
>    - **Contínuo:** $h(t) = 0$ para todo $t < 0$.
> 4. **Estabilidade BIBO (Absolutamente Somável / Integrável):**
>    - **Discreto:** $\sum_{n=-\infty}^{\infty} |h[n]| < \infty$.
>    - **Contínuo:** $\int_{-\infty}^{\infty} |h(t)|\,dt < \infty$.

---

## Questão 4.1 — [Oppenheim 2.25, pág. 144 (EN) / pág. 86 (PT)]
**Seja o sinal $y[n] = x[n] * h[n]$, em que:**
$$x[n] = 3^n u[-n-1] + \left(\frac{1}{3}\right)^n u[n] \quad \text{e} \quad h[n] = \left(\frac{1}{4}\right)^n u[n+3]$$
**(a) Determine $y[n]$ *sem* usar a propriedade distributiva da convolução.**
**(b) Determine $y[n]$ *usando* a propriedade distributiva da convolução.**

### **Resolução Passo a Passo:**

#### **Item (a): Cálculo direto sem usar a propriedade distributiva**
1. **Escrevendo $x[k]$ por partes e $h[n-k]$:**
   $$x[k] = \begin{cases} 3^k, & k \le -1 \\ \left(\frac{1}{3}\right)^k, & k \ge 0 \end{cases}$$
   E para $h[n-k]$:
   $$h[n-k] = \left(\frac{1}{4}\right)^{n-k} u[n - k + 3] = \begin{cases} \left(\frac{1}{4}\right)^{n-k}, & k \le n + 3 \\ 0, & k > n + 3 \end{cases}$$
   Portanto, o somatório vai de $k = -\infty$ até o limite superior $k = n + 3$:
   $$y[n] = \sum_{k=-\infty}^{n+3} x[k]\left(\frac{1}{4}\right)^{n-k}$$

2. **Região 1: $n + 3 \le -1 \iff n \le -4$**
   Quando $n \le -4$, todo o intervalo $k \le n + 3$ está dentro da região negativa $k \le -1$, onde $x[k] = 3^k$:
   $$y[n] = \sum_{k=-\infty}^{n+3} 3^k \left(\frac{1}{4}\right)^{n-k} = \left(\frac{1}{4}\right)^n \sum_{k=-\infty}^{n+3} 12^k$$
   Fazendo $m = -k$ (de $m = -(n+3)$ até $\infty$, razão $r = \frac{1}{12} < 1$):
   $$y[n] = \left(\frac{1}{4}\right)^n \frac{12^{n+3}}{1 - \frac{1}{12}} = \left(\frac{1}{4}\right)^n \frac{12^{n+3}}{\frac{11}{12}} = \frac{1}{11}\left(\frac{1}{4}\right)^n 12^{n+4}$$
   Como $12^{n+4} = 4^{n+4}\cdot 3^{n+4} = 4^n \cdot 4^4 \cdot 3^{n+4} = 256 \cdot 4^n \cdot 3^{n+4}$, o fator $\left(\frac{1}{4}\right)^n 4^n$ cancela:
   $$y[n] = \frac{256}{11} 3^{n+4} = \frac{20736}{11} 3^n, \quad \text{para } n \le -4$$

3. **Região 2: $n + 3 \ge 0 \iff n \ge -3$**
   Agora o limite superior $n + 3 \ge 0$ abrange **toda** a parte negativa ($k \le -1$) e avança sobre a parte não-negativa de $k = 0$ até $k = n + 3$:
   $$y[n] = \sum_{k=-\infty}^{-1} 3^k \left(\frac{1}{4}\right)^{n-k} + \sum_{k=0}^{n+3} \left(\frac{1}{3}\right)^k \left(\frac{1}{4}\right)^{n-k}$$
   - **Primeira soma ($S_1$):**
     $$S_1 = \left(\frac{1}{4}\right)^n \sum_{k=-\infty}^{-1} 12^k = \left(\frac{1}{4}\right)^n \frac{\frac{1}{12}}{1 - \frac{1}{12}} = \frac{1}{11}\left(\frac{1}{4}\right)^n$$
   - **Segunda soma ($S_2$):**
     $$S_2 = \left(\frac{1}{4}\right)^n \sum_{k=0}^{n+3} \left(\frac{4}{3}\right)^k = \left(\frac{1}{4}\right)^n \frac{\left(\frac{4}{3}\right)^{n+4} - 1}{\frac{4}{3} - 1} = 3\left(\frac{1}{4}\right)^n \left[\left(\frac{4}{3}\right)^{n+4} - 1\right]$$
     Distribuindo $\left(\frac{1}{4}\right)^n$ e simplificando $3 \cdot \left(\frac{1}{3}\right)^{n+4} = \left(\frac{1}{3}\right)^{n+3}$:
     $$S_2 = 3 \cdot 4^4 \left(\frac{1}{3}\right)^{n+4} - 3\left(\frac{1}{4}\right)^n = 4^4\left(\frac{1}{3}\right)^{n+3} - 3\left(\frac{1}{4}\right)^n = \frac{256}{27}\left(\frac{1}{3}\right)^n - 3\left(\frac{1}{4}\right)^n$$
   - **Somando $y[n] = S_1 + S_2$:**
     $$y[n] = \left(\frac{1}{11} - 3\right)\left(\frac{1}{4}\right)^n + \frac{256}{27}\left(\frac{1}{3}\right)^n$$
     $$y[n] = -\frac{32}{11}\left(\frac{1}{4}\right)^n + \frac{256}{27}\left(\frac{1}{3}\right)^n, \quad \text{para } n \ge -3$$

---

#### **Item (b): Cálculo usando a propriedade distributiva da convolução**
Pela propriedade distributiva, decompomos $x[n] = x_1[n] + x_2[n]$, onde:
$$x_1[n] = 3^n u[-n-1] \quad \text{e} \quad x_2[n] = \left(\frac{1}{3}\right)^n u[n]$$
Então:
$$y[n] = \big(x_1[n] + x_2[n]\big) * h[n] = \underbrace{\big(x_1[n] * h[n]\big)}_{y_1[n]} + \underbrace{\big(x_2[n] * h[n]\big)}_{y_2[n]}$$

1. **Cálculo de $y_1[n] = x_1[n] * h[n]$:**
   $$y_1[n] = \sum_{k=-\infty}^{\infty} 3^k u[-k-1] \left(\frac{1}{4}\right)^{n-k} u[n-k+3]$$
   Os dois degraus impõem $k \le -1$ e $k \le n + 3 \implies k \le \min(-1, \, n+3)$:
   - Se $n \le -4$ ($n + 3 \le -1$):
     $$y_1[n] = \left(\frac{1}{4}\right)^n \sum_{k=-\infty}^{n+3} 12^k = \frac{256}{11} 3^{n+4}$$
   - Se $n \ge -3$ ($n + 3 \ge 0$):
     $$y_1[n] = \left(\frac{1}{4}\right)^n \sum_{k=-\infty}^{-1} 12^k = \frac{1}{11}\left(\frac{1}{4}\right)^n$$

2. **Cálculo de $y_2[n] = x_2[n] * h[n]$:**
   $$y_2[n] = \sum_{k=-\infty}^{\infty} \left(\frac{1}{3}\right)^k u[k] \left(\frac{1}{4}\right)^{n-k} u[n-k+3]$$
   Os degraus impõem $0 \le k \le n + 3$:
   - Se $n \le -4$: $y_2[n] = 0$.
   - Se $n \ge -3$:
     $$y_2[n] = \left(\frac{1}{4}\right)^n \sum_{k=0}^{n+3} \left(\frac{4}{3}\right)^k = \frac{256}{27}\left(\frac{1}{3}\right)^n - 3\left(\frac{1}{4}\right)^n$$

3. **Somando $y[n] = y_1[n] + y_2[n]$:**
   $$y[n] = \begin{cases} \dfrac{256}{11} 3^{n+4}, & n \le -4 \\[1.0em] -\dfrac{32}{11}\left(\dfrac{1}{4}\right)^n + \dfrac{256}{27}\left(\dfrac{1}{3}\right)^n, & n \ge -3 \end{cases}$$

> **💡 Checagem de Prova (Sinal Positivo e Continuidade na Fronteira $n = -3$):**
> - Como $x[n] > 0$ para todo $n$ e $h[n] \ge 0$, a saída $y[n]$ deve ser estritamente positiva para todo $n$.
> - Avaliando em $n = -3$ pela soma direta: $y[-3] = \frac{64}{11} + 64 = \frac{768}{11} \approx 69,82 > 0$.
> - Avaliando pela expressão de $n \ge -3$ em $n = -3$: $-\frac{32}{11}(64) + \frac{256}{27}(27) = 256 - \frac{2048}{11} = \frac{768}{11}$ (e pela extensão de $\frac{256}{11}3^{n+4}$ em $n=-3$, também obtemos $\frac{256}{11}\cdot 3^1 = \frac{768}{11}$!). O resultado por ambos os métodos é **estritamente idêntico**!

---

## Questão 4.2 — [Oppenheim 2.28, pág. 144 (EN) / pág. 86 (PT)]
**A seguir, temos respostas ao impulso de sistemas LIT de tempo discreto. Determine se cada um dos sistemas é causal e/ou estável. Justifique suas respostas.**

### **Resolução Passo a Passo:**

- **(a) $h[n] = \left(\frac{1}{5}\right)^n u[n]$**
  - **Causalidade:** Como $u[n] = 0$ para todo $n < 0$, temos $h[n] = 0$ para $n < 0$. Logo, é **CAUSAL**.
  - **Estabilidade:** Calculando a soma absoluta:
    $$\sum_{n=-\infty}^{\infty} |h[n]| = \sum_{n=0}^{\infty} \left(\frac{1}{5}\right)^n = \frac{1}{1 - \frac{1}{5}} = \frac{5}{4} < \infty$$
    Como a série geométrica converge ($|r| = \frac{1}{5} < 1$), o sistema é **ESTÁVEL**.

- **(b) $h[n] = (0,8)^n u[n+2]$**
  - **Causalidade:** O degrau $u[n+2]$ liga em $n = -2$. Logo, $h[-2] = (0,8)^{-2} = 1,5625 \neq 0$ e $h[-1] = (0,8)^{-1} = 1,25 \neq 0$. Como $h[n] \neq 0$ para $n < 0$, o sistema é **NÃO-CAUSAL**.
  - **Estabilidade:** Calculando a soma absoluta a partir de $n = -2$:
    $$\sum_{n=-\infty}^{\infty} |h[n]| = \sum_{n=-2}^{\infty} (0,8)^n = \frac{(0,8)^{-2}}{1 - 0,8} = \frac{1,5625}{0,2} = 7,8125 < \infty$$
    Como a soma converge ($|r| = 0,8 < 1$), o sistema é **ESTÁVEL**.

- **(c) $h[n] = \left(\frac{1}{2}\right)^n u[-n]$**
  - **Causalidade:** O degrau $u[-n]$ vale $1$ para todo $n \le 0$ (ex.: $h[-1] = 2 \neq 0$). Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** Calculando a soma absoluta para $n \le 0$ (fazendo $m = -n$):
    $$\sum_{n=-\infty}^{0} \left(\frac{1}{2}\right)^n = \sum_{m=0}^{\infty} 2^m = 1 + 2 + 4 + 8 + \dots = \infty$$
    Como a série diverge, o sistema é **INSTÁVEL**.

- **(d) $h[n] = (5)^n u[3-n]$**
  - **Causalidade:** O degrau $u[3-n]$ vale $1$ para $3 - n \ge 0 \iff n \le 3$, o que inclui todos os inteiros negativos ($n < 0$). Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** Calculando a soma absoluta para $n \le 3$ (fazendo a mudança de variável $m = -n$, de $m = -3$ até $\infty$):
    $$\sum_{n=-\infty}^{3} 5^n = \sum_{m=-3}^{\infty} \left(\frac{1}{5}\right)^m = \frac{\left(\frac{1}{5}\right)^{-3}}{1 - \frac{1}{5}} = \frac{125}{\frac{4}{5}} = \frac{625}{4} = 156,25 < \infty$$
    Como $5^n$ decai rapidamente para zero quando $n \to -\infty$, a soma é finita e o sistema é **ESTÁVEL**.

- **(e) $h[n] = \left(-\frac{1}{2}\right)^n u[n] + (1,01)^n u[n-1]$**
  - **Causalidade:** Ambos os degraus $u[n]$ e $u[n-1]$ são nulos para $n < 0$, logo $h[n] = 0$ para todo $n < 0$. O sistema é **CAUSAL**.
  - **Estabilidade:** A segunda parcela possui base $|r| = 1,01 > 1$ para $n \ge 1$. Quando $n \to +\infty$, $(1,01)^n \to \infty$, fazendo com que:
    $$\sum_{n=-\infty}^{\infty} |h[n]| = \infty$$
    Logo, o sistema é **INSTÁVEL**.

- **(f) $h[n] = \left(-\frac{1}{2}\right)^n u[n] + (1,01)^n u[1-n]$**
  - **Causalidade:** O segundo termo possui o degrau $u[1-n]$, que é não nulo para $1 - n \ge 0 \iff n \le 1$ (incluindo $n < 0$). Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** Pela desigualdade triangular:
    $$\sum_{n=-\infty}^{\infty} |h[n]| \le \sum_{n=0}^{\infty} \left(\frac{1}{2}\right)^n + \sum_{n=-\infty}^{1} (1,01)^n$$
    A primeira soma vale $\frac{1}{1 - 1/2} = 2 < \infty$, e a segunda soma (com $m = -n$, razão $\frac{1}{1,01} < 1$) vale $\frac{1,01}{1 - \frac{1}{1,01}} = 102,01 < \infty$. Como ambas convergem, o sistema é **ESTÁVEL**.

- **(g) $h[n] = n\left(\frac{1}{3}\right)^n u[n-1]$**
  - **Causalidade:** Como $u[n-1] = 0$ para $n < 1$ (e portanto para todo $n < 0$), o sistema é **CAUSAL**.
  - **Estabilidade:** A queda exponencial $\left(\frac{1}{3}\right)^n$ domina o crescimento linear $n$. Pela série aritmético-geométrica ($\sum_{n=1}^\infty n r^n = \frac{r}{(1-r)^2}$ para $|r| < 1$):
    $$\sum_{n=1}^{\infty} n\left(\frac{1}{3}\right)^n = \frac{\frac{1}{3}}{\left(1 - \frac{1}{3}\right)^2} = \frac{\frac{1}{3}}{\frac{4}{9}} = \frac{3}{4} < \infty$$
    Logo, o sistema é **ESTÁVEL**.

---

## Questão 4.3 — [Oppenheim 2.29, pág. 144 (EN) / pág. 86 (PT)]
**A seguir, temos respostas ao impulso de sistemas LIT de tempo contínuo. Determine se cada um dos sistemas é causal e/ou estável. Justifique suas respostas.**

### **Resolução Passo a Passo:**

- **(a) $h(t) = e^{-4t}u(t-2)$**
  - **Causalidade:** Como $u(t-2) = 0$ para $t < 2$, temos $h(t) = 0$ para todo $t < 0$. Logo, é **CAUSAL**.
  - **Estabilidade:**
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \int_{2}^{\infty} e^{-4t}\,dt = \left[\frac{e^{-4t}}{-4}\right]_{2}^{\infty} = \frac{e^{-8}}{4} < \infty$$
    Logo, é **ESTÁVEL**.

- **(b) $h(t) = e^{-6t}u(3-t)$**
  - **Causalidade:** O degrau $u(3-t)$ está ativo para $3 - t \ge 0 \iff t \le 3$, portanto existe para $t < 0$. Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:**
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \int_{-\infty}^{3} e^{-6t}\,dt$$
    Quando $t \to -\infty$, o expoente $-6t \to +\infty$ e $e^{-6t} \to +\infty$, de modo que a integral diverge ($\infty$). Logo, é **INSTÁVEL**.

- **(c) $h(t) = e^{-2t}u(t+50)$**
  - **Causalidade:** O degrau $u(t+50)$ liga em $t = -50 < 0$. Como $h(t) \neq 0$ no intervalo $-50 \le t < 0$, é **NÃO-CAUSAL**.
  - **Estabilidade:**
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \int_{-50}^{\infty} e^{-2t}\,dt = \left[\frac{e^{-2t}}{-2}\right]_{-50}^{\infty} = 0 - \left(-\frac{e^{100}}{2}\right) = \frac{e^{100}}{2} < \infty$$
    Embora $e^{100}/2$ seja um número grande, ele é estritamente finito! Logo, o sistema é **ESTÁVEL**.

- **(d) $h(t) = e^{2t}u(-1-t)$**
  - **Causalidade:** O degrau $u(-1-t)$ vale $1$ para $-1 - t \ge 0 \iff t \le -1 < 0$. Como existe exclusivamente no passado ($t \le -1$), é **NÃO-CAUSAL**.
  - **Estabilidade:**
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \int_{-\infty}^{-1} e^{2t}\,dt = \left[\frac{e^{2t}}{2}\right]_{-\infty}^{-1} = \frac{e^{-2}}{2} - 0 = \frac{e^{-2}}{2} < \infty$$
    Como a exponencial $e^{2t}$ decai para $0$ quando $t \to -\infty$, a integral converge e o sistema é **ESTÁVEL**.

- **(e) $h(t) = e^{-6|t|}$**
  - **Causalidade:** Para $t < 0$, $h(t) = e^{6t} \neq 0$. Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** Pela simetria par de $e^{-6|t|}$:
    $$\int_{-\infty}^{\infty} e^{-6|t|}\,dt = 2\int_{0}^{\infty} e^{-6t}\,dt = 2\left(\frac{1}{6}\right) = \frac{1}{3} < \infty$$
    Logo, é **ESTÁVEL**.

- **(f) $h(t) = t e^{-t}u(t)$**
  - **Causalidade:** Devido a $u(t)$, $h(t) = 0$ para todo $t < 0$. Logo, é **CAUSAL**.
  - **Estabilidade:** Integrando por partes ($\int_0^\infty t e^{-t}dt = [-te^{-t} - e^{-t}]_0^\infty = 1$):
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \int_{0}^{\infty} t e^{-t}\,dt = 1 < \infty$$
    Logo, é **ESTÁVEL**.

- **(g) $h(t) = \left(2e^{-t} - e^{(t-100)/100}\right)u(t)$**
  - **Causalidade:** Como $u(t) = 0$ para $t < 0$, temos $h(t) = 0$ para $t < 0$. Logo, é **CAUSAL**.
  - **Estabilidade:** A segunda parcela dentro do parêntese é $-e^{-1}\cdot e^{+t/100}$, que possui expoente positivo ($+t/100$) e cresce ilimitadamente quando $t \to +\infty$. Portanto:
    $$\int_{0}^{\infty} \left|2e^{-t} - e^{(t-100)/100}\right|\,dt = \infty$$
    Logo, o sistema é **INSTÁVEL**.

---

## Questão 5.1 — [Haykin & Van Veen 2.11, pág. 156 (Bookman)]
**Uma interconexão de sistemas LTI é descrita na Figura P2.11 (onde $h_1[n]$ está em série com o bloco paralelo formado por $h_2[n]$ e $h_3[n]$). As respostas ao impulso são:**
$$h_1[n] = \left(\frac{1}{2}\right)^n \big(u[n+2] - u[n-3]\big), \qquad h_2[n] = \delta[n], \qquad h_3[n] = u[n-1]$$
**Admitamos que a resposta ao impulso do sistema global de $x[n]$ até $y[n]$ seja denotada como $h[n]$.**
**(a) Expresse $h[n]$ em termos de $h_1[n]$, $h_2[n]$ e $h_3[n]$.**
**(b) Avalie $h[n]$ usando os resultados de (a).**
**Nas partes (c)–(e), determine se o sistema correspondente a cada resposta ao impulso é (i) estável, (ii) causal e (iii) sem memória:**
**(c) $h_1[n]$; (d) $h_2[n]$; (e) $h_3[n]$.**

### **Resolução Passo a Passo:**

#### **Item (a): Expressão da resposta ao impulso global $h[n]$**
1. Os subsistemas $h_2[n]$ e $h_3[n]$ estão conectados em **paralelo** (mesma entrada e saídas somadas), logo sua resposta equivalente é a soma:
   $$h_{23}[n] = h_2[n] + h_3[n]$$
2. O subsistema $h_1[n]$ está em **cascata (série)** com essa combinação paralela, logo a resposta ao impulso global é a convolução:
   $$\mathbf{h[n] = h_1[n] * \big(h_2[n] + h_3[n]\big)}$$

---

#### **Item (b): Avaliação explícita de $h[n]$**
1. **Simplificação fundamental da associação em paralelo:**
   Substituindo $h_2[n] = \delta[n]$ e $h_3[n] = u[n-1]$:
   $$h_2[n] + h_3[n] = \delta[n] + u[n-1]$$
   Lembrando que $\delta[n]$ vale $1$ em $n=0$ e $u[n-1]$ vale $1$ para $n \ge 1$ ($n = 1, 2, 3, \dots$), a soma dos dois reconstrói exatamente o **degrau unitário** $u[n]$!
   $$h_2[n] + h_3[n] = u[n]$$

2. **Convolução de $h_1[n]$ com $u[n]$ (acumulador):**
   $$h[n] = h_1[n] * u[n] = \sum_{k=-\infty}^{\infty} h_1[k]u[n-k] = \sum_{k=-\infty}^{n} h_1[k]$$
   Onde $h_1[k] = \left(\frac{1}{2}\right)^k \big(u[k+2] - u[k-3]\big)$ é não nulo apenas para $-2 \le k \le 2$ (5 amostras):
   - $h_1[-2] = (1/2)^{-2} = 4$
   - $h_1[-1] = (1/2)^{-1} = 2$
   - $h_1[0] = (1/2)^0 = 1$
   - $h_1[1] = (1/2)^1 = \frac{1}{2}$
   - $h_1[2] = (1/2)^2 = \frac{1}{4}$

3. **Avaliando a soma acumulada $\sum_{k=-\infty}^{n} h_1[k]$ por intervalos:**
   - **Para $n < -2$:** Nenhuma amostra de $h_1[k]$ foi alcançada $\implies h[n] = 0$.
   - **Para $-2 \le n \le 2$:**
     $$h[n] = \sum_{k=-2}^{n} \left(\frac{1}{2}\right)^k = \frac{\left(\frac{1}{2}\right)^{-2} - \left(\frac{1}{2}\right)^{n+1}}{1 - \frac{1}{2}} = 2\left[4 - \left(\frac{1}{2}\right)^{n+1}\right] = 8 - \left(\frac{1}{2}\right)^n$$
     *(Valores individuais: $h[-2] = 4$; $h[-1] = 6$; $h[0] = 7$; $h[1] = \frac{15}{2} = 7,5$; $h[2] = \frac{31}{4} = 7,75$).*
   - **Para $n \ge 3$:** Todas as 5 amostras de $h_1[k]$ já foram somadas:
     $$h[n] = 4 + 2 + 1 + \frac{1}{2} + \frac{1}{4} = \frac{31}{4} = 7,75$$

   **Expressão final de $h[n]$ (por partes e na forma compacta):**
   $$h[n] = \begin{cases} 0, & n < -2 \\[0.4em] 8 - \left(\dfrac{1}{2}\right)^n, & -2 \le n \le 2 \\[0.6em] \dfrac{31}{4}, & n \ge 3 \end{cases}$$
   $$\mathbf{h[n] = \left[8 - \left(\frac{1}{2}\right)^n\right]\big(u[n+2] - u[n-3]\big) + \frac{31}{4}u[n-3]}$$

---

#### **Itens (c), (d) e (e): Classificação de $h_1[n]$, $h_2[n]$ e $h_3[n]$**

- **(c) Para $h_1[n] = \left(\frac{1}{2}\right)^n (u[n+2] - u[n-3])$:**
  - **(i) Estável:** **SIM.** É um sinal de duração finita (5 amostras) com amplitudes finitas, cuja soma absoluta é $\sum_{n=-2}^2 |h_1[n]| = \frac{31}{4} < \infty$.
  - **(ii) Causal:** **NÃO.** Pois $h_1[-2] = 4 \neq 0$ e $h_1[-1] = 2 \neq 0$ ($h_1[n] \neq 0$ para $n < 0$).
  - **(iii) Sem memória:** **NÃO.** Pois $h_1[n] \neq 0$ para $n \neq 0$ (possui amostras em $n = -2, -1, 1, 2$).

- **(d) Para $h_2[n] = \delta[n]$:**
  - **(i) Estável:** **SIM.** Pois $\sum_{n=-\infty}^\infty |\delta[n]| = 1 < \infty$.
  - **(ii) Causal:** **SIM.** Pois $h_2[n] = 0$ para todo $n < 0$.
  - **(iii) Sem memória:** **SIM.** Pois tem exatamente a forma $h_2[n] = c\delta[n]$ com $c = 1$ ($h_2[n] = 0$ para todo $n \neq 0$, resultando em $y[n] = x[n]$).

- **(e) Para $h_3[n] = u[n-1]$:**
  - **(i) Estável:** **NÃO (Instável).** Pois $\sum_{n=-\infty}^\infty |u[n-1]| = \sum_{n=1}^\infty 1 = \infty$.
  - **(ii) Causal:** **SIM.** Pois $u[n-1] = 0$ para todo $n < 1$, o que garante $h_3[n] = 0$ para todo $n < 0$.
  - **(iii) Sem memória:** **NÃO.** Pois $h_3[n] = 1 \neq 0$ para todo $n \ge 1$.

---

## Questão 5.2 — [Haykin & Van Veen 2.12, págs. 156–157 (Bookman)]
**Para cada resposta ao impulso listada abaixo, determine se o sistema correspondente é (i) sem memória, (ii) causal e (iii) estável.**

### **Resolução Passo a Passo (Itens a até k):**

- **(a) $h(t) = e^{-2|t|}$**
  - **(i) Sem memória:** **Não** ($h(t) \neq 0$ para $t \neq 0$).
  - **(ii) Causal:** **Não** ($h(t) = e^{2t} \neq 0$ para $t < 0$).
  - **(iii) Estável:** **Sim**, pois $\int_{-\infty}^{\infty} e^{-2|t|}\,dt = 2\int_0^\infty e^{-2t}\,dt = 2\left(\frac{1}{2}\right) = 1 < \infty$.

- **(b) $h(t) = e^{2t}u(t-1)$**
  - **(i) Sem memória:** **Não** ($h(t) \neq 0$ para $t \ge 1$).
  - **(ii) Causal:** **Sim** (o degrau $u(t-1)$ garante $h(t) = 0$ para $t < 1$, logo $h(t) = 0$ para todo $t < 0$).
  - **(iii) Estável:** **Não (Instável)**, pois o expoente $+2t$ cresce ilimitadamente quando $t \to +\infty$, resultando em $\int_{1}^{\infty} e^{2t}\,dt = \infty$.
  *(Observação: No Problema análogo 2.49(b) da 2ª edição em inglês da Wiley, este item aparece com expoente negativo $h(t) = e^{-2t}u(t-1)$, que é estável; porém, na edição brasileira da Bookman indicada na lista, o expoente é positivo $+2t$ e o sistema é **Instável**).*

- **(c) $h(t) = u(t+1) - 2u(t-1)$**
  - **(i) Sem memória:** **Não** ($h(t) \neq 0$ para $t \neq 0$).
  - **(ii) Causal:** **Não**, pois no intervalo $-1 \le t < 0$ temos $h(t) = 1 \neq 0$.
  - **(iii) Estável:** **Não (Instável)**, pois para todo $t \ge 1$ temos $h(t) = 1 - 2 = -1$ constante, logo $\int_{-\infty}^{\infty} |h(t)|\,dt = \int_{-1}^{1} 1\,dt + \int_{1}^{\infty} |-1|\,dt = \infty$.

- **(d) $h(t) = 3\delta(t)$**
  - **(i) Sem memória:** **Sim**, pois é da forma $h(t) = c\delta(t)$ com $c = 3$ ($y(t) = 3x(t)$).
  - **(ii) Causal:** **Sim**, pois $h(t) = 0$ para todo $t < 0$.
  - **(iii) Estável:** **Sim**, pois $\int_{-\infty}^{\infty} |3\delta(t)|\,dt = 3 < \infty$.

- **(e) $h(t) = \cos(\pi t)u(t)$**
  - **(i) Sem memória:** **Não** ($h(t) \neq 0$ para $t > 0$).
  - **(ii) Causal:** **Sim**, pois $u(t) = 0$ para $t < 0$.
  - **(iii) Estável:** **Não (Instável)**, pois o cosseno oscila perpetuamente para $t \ge 0$ com área de $\frac{2}{\pi}$ a cada meio ciclo de duração $1$, logo $\int_{0}^{\infty} |\cos(\pi t)|\,dt = \infty$.

- **(f) $h[n] = 2^n u[-n]$**
  - **(i) Sem memória:** **Não** ($h[n] \neq 0$ para $n < 0$).
  - **(ii) Causal:** **Não**, pois $u[-n] = 1$ para todo $n \le 0$ (ex.: $h[-1] = 1/2 \neq 0$).
  - **(iii) Estável:** **Sim**, pois fazendo $m = -n$:
    $$\sum_{n=-\infty}^{0} 2^n = \sum_{m=0}^{\infty} \left(\frac{1}{2}\right)^m = \frac{1}{1 - \frac{1}{2}} = 2 < \infty$$

- **(g) $h[n] = e^{2n}u[n-1]$**
  - **(i) Sem memória:** **Não** ($h[n] \neq 0$ para $n \ge 1$).
  - **(ii) Causal:** **Sim**, pois $u[n-1] = 0$ para $n < 1$ (e, portanto, para todo $n < 0$).
  - **(iii) Estável:** **Não (Instável)**, pois $e^2 \approx 7,389 > 1$, logo $\sum_{n=1}^{\infty} (e^2)^n = \infty$.

- **(h) $h[n] = \cos\left(\frac{1}{8}\pi n\right)\big\{u[n] - u[n-10]\big\}$**
  - **(i) Sem memória:** **Não** ($h[n] \neq 0$ para $n \in \{0, 1, \dots, 9\}$, ex.: $h[1] = \cos(\pi/8) \neq 0$).
  - **(ii) Causal:** **Sim**, pois o pulso $u[n] - u[n-10]$ só existe para $0 \le n \le 9$, sendo nulo para todo $n < 0$.
  - **(iii) Estável:** **Sim**, pois é uma sequência de **duração finita** (apenas 10 amostras não nulas limitadas por $1$): $\sum_{n=0}^{9} \left|\cos\left(\frac{\pi}{8}n\right)\right| \le 10 < \infty$.

- **(i) $h[n] = 2u[n] - 2u[n-1]$** *(Atenção: Pegadinha Clássica de Prova!)*
  - **Simplificação algébrica prévia:** Colocando o $2$ em evidência:
    $$h[n] = 2\big(u[n] - u[n-1]\big) = 2\delta[n]$$
    Pois $u[n] - u[n-1]$ vale $1$ exclusivamente em $n = 0$, e $0$ para todo $n \neq 0$!
  - **(i) Sem memória:** **Sim**, pois $h[n] = 2\delta[n]$ ($h[n] = 0$ para todo $n \neq 0$, logo $y[n] = 2x[n]$).
  - **(ii) Causal:** **Sim**, pois $h[n] = 0$ para todo $n < 0$.
  - **(iii) Estável:** **Sim**, pois $\sum_{n=-\infty}^{\infty} |2\delta[n]| = 2 < \infty$.

- **(j) $h[n] = \text{sen}\left(\frac{1}{2}\pi n\right)$**
  - **(i) Sem memória:** **Não**, pois $h[1] = \text{sen}(\pi/2) = 1 \neq 0$.
  - **(ii) Causal:** **Não**, pois para $n = -1 < 0$ temos $h[-1] = \text{sen}(-\pi/2) = -1 \neq 0$.
  - **(iii) Estável:** **Não (Instável)**, pois a sequência periódica alterna indefinidamente entre $\{0, 1, 0, -1\}$, de modo que $\sum_{n=-\infty}^{\infty} \left|\text{sen}\left(\frac{\pi}{2}n\right)\right| = \infty$.

- **(k) $h[n] = \delta[n] + \text{sen}(\pi n)$** *(Atenção: Segunda Pegadinha Clássica!)*
  - **Simplificação algébrica prévia:** Como a variável discreta $n$ assume **apenas valores inteiros** ($n \in \mathbb{Z}$), temos que $\text{sen}(\pi n) = 0$ para **todo** $n \in \mathbb{Z}$! Portanto:
    $$h[n] = \delta[n] + 0 = \delta[n]$$
  - **(i) Sem memória:** **Sim**, pois $h[n] = \delta[n]$ ($y[n] = x[n]$).
  - **(ii) Causal:** **Sim**, pois $h[n] = 0$ para todo $n < 0$.
  - **(iii) Estável:** **Sim**, pois $\sum_{n=-\infty}^{\infty} |\delta[n]| = 1 < \infty$.

---

# 📚 BLOCO 4: Representação de SLITs por Diagramas em Blocos — Formas Direta I e Direta II

> **💡 Lembrete Fundamental para a Prova (Formas Direta I e Direta II):**
> - **Forma Direta I:** Implementa primeiro o lado direito da equação (combinação das entradas atrasadas/integradas, gerando $w[n]$ ou $w(t)$) em cascata com o lado esquerdo (realimentação das saídas atrasadas/integradas). Usa $M + N$ blocos de memória.
> - **Forma Direta II (Canônica):** Inverte a ordem dos dois subsistemas LTI e funde a linha de atrasos/integradores em uma única coluna central com o estado intermediário $f[n]$ (ou $f(t)$), utilizando o número **mínimo** de elementos de memória ($\max(N, M)$).

---

## Questão 1.3 — [Exercício 1.3 em Sala de Aula — Apostila, pág. 52]
**Desenhe as formas direta I e II para as seguintes equações:**
**(a) $y[n] + \frac{1}{2}y[n-1] - \frac{1}{3}y[n-3] = x[n] + 2x[n-2]$**
**(b) $\frac{d^2}{dt^2}y(t) + 3y(t) = \frac{d}{dt}x(t) + 2\frac{d^2}{dt^2}x(t)$**

---

### **Resolução Passo a Passo do Item (a): Tempo Discreto (Equação de Diferenças)**

#### **Passo 1: Isolar $y[n]$ e identificar todos os coeficientes (incluindo os nulos)**
Isolando $y[n]$ na equação dada:
$$y[n] = -\frac{1}{2}y[n-1] + 0\cdot y[n-2] + \frac{1}{3}y[n-3] + x[n] + 0\cdot x[n-1] + 2x[n-2]$$
Trata-se de um sistema de **3ª ordem ($N = 3$)**, com coeficientes:
- Realimentação (saída): $-a_1 = -\frac{1}{2}$, $-a_2 = 0$, $-a_3 = +\frac{1}{3}$.
- Alimentação direta (entrada): $b_0 = 1$, $b_1 = 0$, $b_2 = 2$, $b_3 = 0$.

#### **Passo 2: Equações e Diagrama para a Forma Direta I**
Separamos em duas equações usando o sinal intermediário $w[n]$:
$$\begin{aligned}
w[n] &= x[n] + 2x[n-2] \\
y[n] &= w[n] - \frac{1}{2}y[n-1] + \frac{1}{3}y[n-3]
\end{aligned}$$
*(Note que na coluna da entrada precisamos de 2 atrasos $S$ para chegar em $x[n-2]$, e na coluna da saída precisamos de 3 atrasos $S$ para chegar em $y[n-3]$, totalizando 5 blocos $S$).*

```
                  FORMA DIRETA I — Item (a)

 x[n] ●──────(b0=1)──────►(+)─────────────►(+)──────●─────► y[n]
      │                    ▲                ▲       │
     [S]                   │                │      [S]
      │ x[n-1]             │                │       │ y[n-1]
     [S]                   │               (+)◄──(-1/2)──●
      │ x[n-2]             │                ▲            │
      └──────(b2=2)────────┘                │           [S]
                                            │            │ y[n-2]
                                            │           [S]
                                            │            │ y[n-3]
                                            └────(+1/3)──┘
```

#### **Passo 3: Equações e Diagrama para a Forma Direta II**
Permutando os blocos através do estado intermediário central $f[n]$ (que exige apenas **3 blocos de atraso $S$** compartilhados):
$$\begin{aligned}
f[n] &= x[n] - \frac{1}{2}f[n-1] + \frac{1}{3}f[n-3] \\
y[n] &= f[n] + 2f[n-2]
\end{aligned}$$

```
                  FORMA DIRETA II — Item (a)

                       f[n]
 x[n] ─────►(+)─────────●────────(b0=1)────────►(+)─────► y[n]
             ▲          │                        ▲
             │         [S]                       │
             │          │ f[n-1]                 │
            (+)◄─(-1/2)─●                        │
             ▲          │                        │
             │         [S]                       │
             │          │ f[n-2]                 │
             │          ●────────(b2=2)──────────┘
             │          │
             │         [S]
             │          │ f[n-3]
             └──(+1/3)──┘
```

---

### **Resolução Passo a Passo do Item (b): Tempo Contínuo (Equação Diferencial)**

#### **Passo 1: Converter a EDO em Equação Integral integrando $N = 2$ vezes**
A equação diferencial de 2ª ordem ($N = 2$) é:
$$\frac{d^2}{dt^2}y(t) + 0\cdot\frac{d}{dt}y(t) + 3y(t) = 2\frac{d^2}{dt^2}x(t) + \frac{d}{dt}x(t) + 0\cdot x(t)$$
Assumindo condições iniciais nulas e aplicando o operador de integração dupla ($\int_{-\infty}^{t}$ duas vezes) em ambos os lados, onde $v^{(k)}(t)$ denota a $k$-ésima integral sucessiva de $v(t)$:
- A integral dupla de $\frac{d^2}{dt^2}v(t)$ é o próprio $v(t)$.
- A integral dupla de $\frac{d}{dt}v(t)$ é a integral simples $v^{(1)}(t) = \int_{-\infty}^t v(\tau)\,d\tau$.
- A integral dupla de $v(t)$ é $v^{(2)}(t) = \int_{-\infty}^t \int_{-\infty}^{\tau} v(\sigma)\,d\sigma\,d\tau$.

Logo, a EDO integrada duas vezes torna-se:
$$y(t) + 3y^{(2)}(t) = 2x(t) + x^{(1)}(t)$$
Isolando $y(t)$:
$$y(t) = -3y^{(2)}(t) + 2x(t) + x^{(1)}(t)$$
Os coeficientes são: $a_1 = 0, a_0 = 3$ (logo $-a_1 = 0, -a_0 = -3$) e $b_2 = 2, b_1 = 1, b_0 = 0$.

#### **Passo 2: Equações e Diagrama para a Forma Direta I**
$$\begin{aligned}
w(t) &= 2x(t) + x^{(1)}(t) \\
y(t) &= w(t) - 3y^{(2)}(t)
\end{aligned}$$

```
                  FORMA DIRETA I — Item (b)

 x(t) ●──────(b2=2)──────►(+)─────────────►(+)──────●─────► y(t)
      │                    ▲                ▲       │
     [∫]                   │                │      [∫]
      │ x^(1)(t)           │                │       │ y^(1)(t)
      └──────(b1=1)────────┘                │      [∫]
                                            │       │ y^(2)(t)
                                            └──(-3)─┘
```

#### **Passo 3: Equações e Diagrama para a Forma Direta II**
Definindo o sinal intermediário central $f(t)$ e suas integrais $f^{(1)}(t)$ e $f^{(2)}(t)$ (utilizando apenas **2 integradores $\int$** no ramo central):
$$\begin{aligned}
f(t) &= x(t) - 3f^{(2)}(t) \\
y(t) &= 2f(t) + f^{(1)}(t)
\end{aligned}$$

```
                  FORMA DIRETA II — Item (b)

                       f(t)
 x(t) ─────►(+)─────────●────────(b2=2)────────►(+)─────► y(t)
             ▲          │                        ▲
             │         [∫]                       │
             │          │ f^(1)(t)               │
             │          ●────────(b1=1)──────────┘
             │          │
             │         [∫]
             │          │ f^(2)(t)
             └───(-3)───┘
```
