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

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = -2
            cauda = n-9 = -11
                                                    frente = n+1 = -1
            ▼                                       ▼
h[n-k]      1   1   1   1   1   1   1   1   1   1   1   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
x[k]        ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·  -1  -1  -1  +1  +1  +1   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
sobrep.
         ───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼─► k
k         -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
limites: A: max(-11, 0) = 0 > min(-1, 2) = -1  →  vazio  |  B: max(-11, 3) = 3 > min(-1, 5) = -1  →  vazio
```

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

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 0
                    cauda = n-9 = -9
                                                            frente = n+1 = 1
                    ▼                                       ▼
h[n-k]      ·   ·   1   1   1   1   1   1   1   1   1   1   1   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
x[k]        ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·  -1  -1  -1  +1  +1  +1   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
sobrep.                                               ▓▓▓ ▓▓▓
         ───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼─► k
k         -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
limites: A: k = 0 … 1  (1 - (0) + 1 = 2 termos)  |  B: max(-9, 3) = 3 > min(1, 5) = 1  →  vazio
```

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

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 3
                                cauda = n-9 = -6
                                                                        frente = n+1 = 4
                                ▼                                       ▼
h[n-k]      ·   ·   ·   ·   ·   1   1   1   1   1   1   1   1   1   1   1   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
x[k]        ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·  -1  -1  -1  +1  +1  +1   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
sobrep.                                               ▓▓▓ ▓▓▓ ▓▓▓ ▓▓▓ ▓▓▓
         ───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼─► k
k         -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
limites: A: k = 0 … 2  (2 - (0) + 1 = 3 termos)  |  B: k = 3 … 4  (4 - (3) + 1 = 2 termos)
```

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

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 6
                                            cauda = n-9 = -3
                                                                                    frente = n+1 = 7
                                            ▼                                       ▼
h[n-k]      ·   ·   ·   ·   ·   ·   ·   ·   1   1   1   1   1   1   1   1   1   1   1   ·   ·   ·   ·   ·   ·   ·   ·   ·
x[k]        ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·  -1  -1  -1  +1  +1  +1   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
sobrep.                                               ▓▓▓ ▓▓▓ ▓▓▓ ▓▓▓ ▓▓▓ ▓▓▓
         ───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼─► k
k         -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
limites: A: k = 0 … 2  (2 - (0) + 1 = 3 termos)  |  B: k = 3 … 5  (5 - (3) + 1 = 3 termos)
```

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

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 10
                                                            cauda = n-9 = 1
                                                                                                    frente = n+1 = 11
                                                            ▼                                       ▼
h[n-k]      ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   1   1   1   1   1   1   1   1   1   1   1   ·   ·   ·   ·   ·
x[k]        ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·  -1  -1  -1  +1  +1  +1   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
sobrep.                                                   ▓▓▓ ▓▓▓ ▓▓▓ ▓▓▓ ▓▓▓
         ───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼─► k
k         -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
limites: A: k = 1 … 2  (2 - (1) + 1 = 2 termos)  |  B: k = 3 … 5  (5 - (3) + 1 = 3 termos)
```

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

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 13
                                                                        cauda = n-9 = 4
                                                                                                                frente = n+1 = 14
                                                                        ▼                                       ▼
h[n-k]      ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   1   1   1   1   1   1   1   1   1   1   1   ·   ·
x[k]        ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·  -1  -1  -1  +1  +1  +1   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
sobrep.                                                               ▓▓▓ ▓▓▓
         ───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼─► k
k         -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
limites: A: max(4, 0) = 4 > min(14, 2) = 2  →  vazio  |  B: k = 4 … 5  (5 - (4) + 1 = 2 termos)
```

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

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 15
                                                                                cauda = n-9 = 6
                                                                                                                        frente = n+1 = 16
                                                                                ▼                                       ▼
h[n-k]      ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   1   1   1   1   1   1   1   1   1   1   1
x[k]        ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·  -1  -1  -1  +1  +1  +1   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
sobrep.
         ───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼─► k
k         -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
limites: A: max(6, 0) = 6 > min(16, 2) = 2  →  vazio  |  B: max(6, 3) = 6 > min(16, 5) = 5  →  vazio
```

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

```
Esboço de y[n] (Questão 1.1)
      3 ┤                                                           ●
      2 ┤                                                       ●   │   ●
      1 ┤                                                   ●   │   │   │   ●
      0 ┼───●───┼───┼───┼───┼───┼───●───●───●───●───●───●───┼───┼───┼───┼───┼───●───●─►
     -1 ┤       ●   │   │   │   ●
     -2 ┤           ●   │   ●
     -3 ┤               ●
           -2  -1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16   n
```

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

Escrevendo cada fator na variável muda $k$:
- $x[k]$: trocamos $n$ por $k$ em $x[n]$:
  $$x[k] = \left(\frac{1}{2}\right)^{k-2} u[k-2]$$
- $h[n-k]$: trocamos o argumento $n$ de $h[n] = u[n+2]$ por $(n-k)$:
  $$h[n-k] = u[(n-k) + 2] = u[n - k + 2]$$

Substituindo na soma:
$$y[n] = \sum_{k=-\infty}^{\infty} \left(\frac{1}{2}\right)^{k-2} u[k-2] \cdot u[n - k + 2]$$

#### **Passo 2: Determinar os limites do somatório impostos pelos degraus**
Cada degrau vale $1$ quando seu argumento é $\ge 0$ e vale $0$ caso contrário. O produto $u[k-2]\cdot u[n-k+2]$ só vale $1$ quando **os dois** valem $1$:
- O primeiro degrau $u[k-2]$ exige:
  $$k - 2 \ge 0 \implies k \ge 2 \quad \text{(Limite inferior de } k\text{)}$$
- O segundo degrau $u[n - k + 2]$ exige:
  $$n - k + 2 \ge 0 \implies n + 2 \ge k \implies k \le n + 2 \quad \text{(Limite superior de } k\text{)}$$

Logo, os termos não nulos são os $k$ com $2 \le k \le n + 2$.

#### **Passo 3: Analisar as regiões de $n$**
A faixa $2 \le k \le n+2$ só tem algum inteiro quando o limite inferior não ultrapassa o superior, isto é, quando $2 \le n + 2$.

1. **Região 1: $n + 2 < 2 \iff n < 0$**
   O limite superior ($n+2$) é menor que o limite inferior ($2$). Por exemplo, para $n = -1$ teríamos $2 \le k \le 1$, que não contém nenhum inteiro. A soma é **vazia**:
   $$y[n] = 0, \quad \text{para } n < 0$$

   **Esboço da Região 1** (a janela $h[n-k] = u[n-k+2]$ vale $1$ para $k \le n + 2$; não tem cauda):
```
Instante representativo: n = -2
         sem cauda: a janela vai até k = -∞ (◄)
                                frente = n+2 = 0
                                ▼
h[n-k]  ◄     1     1     1     1     ·     ·     ·     ·     ·     ·     ·
x[k]          ·     ·     ·     ·     ·     1   1/2   1/4   1/8  1/16  1/32 ►
sobrep.
         ─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─► k
k            -3    -2    -1     0     1     2     3     4     5     6     7
limites: x: max(-∞, 2) = 2 > min(0, +∞) = 0  →  vazio
```

2. **Região 2: $n + 2 \ge 2 \iff n \ge 0$**
   O somatório fica ativo de $k = 2$ até $k = n + 2$ (nesse trecho, os dois degraus valem $1$).

   **Esboço da Região 2** (mesma escala; a frente $n + 2$ já passou de $k = 2$):
```
Instante representativo: n = 2
         sem cauda: a janela vai até k = -∞ (◄)
                                                        frente = n+2 = 4
                                                        ▼
h[n-k]  ◄     1     1     1     1     1     1     1     1     ·     ·     ·
x[k]          ·     ·     ·     ·     ·     1   1/2   1/4   1/8  1/16  1/32 ►
sobrep.                                 ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓
         ─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─► k
k            -3    -2    -1     0     1     2     3     4     5     6     7
limites: x: k = 2 … 4  (4 - (2) + 1 = 3 termos)
```

   Montando a soma:
   $$y[n] = \sum_{k=2}^{n+2} \left(\frac{1}{2}\right)^{k-2}$$
   Fazendo a mudança de variável $m = k - 2$:
   - Quando $k = 2 \implies m = 2 - 2 = 0$.
   - Quando $k = n + 2 \implies m = (n + 2) - 2 = n$.

   Reescrevendo o somatório em função de $m$:
   $$y[n] = \sum_{m=0}^{n} \left(\frac{1}{2}\right)^{m}$$
   **Aplicando a fórmula da PG finita**
   $$\sum_{m=A}^{B} r^m = \frac{r^A - r^{B+1}}{1 - r} \qquad (r \neq 1)$$
   com os parâmetros identificados:
   $$r = \frac{1}{2}, \qquad A = 0, \qquad B = n \qquad (\text{nº de termos} = n - 0 + 1 = n + 1)$$
   Substituindo:
   $$y[n] = \frac{\left(\frac{1}{2}\right)^{0} - \left(\frac{1}{2}\right)^{n+1}}{1 - \frac{1}{2}}$$
   Como $\left(\frac{1}{2}\right)^0 = 1$ e $1 - \frac{1}{2} = \frac{1}{2}$:
   $$y[n] = \frac{1 - \left(\frac{1}{2}\right)^{n+1}}{\frac{1}{2}}$$
   Dividir por $\frac{1}{2}$ é multiplicar por $2$:
   $$y[n] = 2\left[1 - \left(\frac{1}{2}\right)^{n+1}\right], \quad \text{para } n \ge 0$$

#### **Passo 4: Expressão fechada com degrau e valores para o gráfico**
Multiplicando por $u[n]$ para incorporar as duas regiões numa única expressão ($u[n] = 0$ para $n < 0$ reproduz a Região 1, e $u[n] = 1$ para $n \ge 0$ reproduz a Região 2):
$$y[n] = 2\left[1 - \left(\frac{1}{2}\right)^{n+1}\right] u[n]$$

**Valores principais para o esboço gráfico** *(gráfico gerado em `Visualizacao_Sinais_Unidade2.ipynb`)*:
- Para $n < 0$: $y[n] = 0$
- $n = 0 \implies y[0] = 2\left(1 - \frac{1}{2}\right) = 2 \cdot \frac{1}{2} = 1$
- $n = 1 \implies y[1] = 2\left(1 - \frac{1}{4}\right) = 2 \cdot \frac{3}{4} = 1,5$
- $n = 2 \implies y[2] = 2\left(1 - \frac{1}{8}\right) = 2 \cdot \frac{7}{8} = 1,75$
- $n = 3 \implies y[3] = 2\left(1 - \frac{1}{16}\right) = 2 \cdot \frac{15}{16} = 1,875$
- Quando $n \to \infty$: $\left(\frac{1}{2}\right)^{n+1} \to 0$, logo $y[n] \to 2(1 - 0) = 2$ (assíntota horizontal em $2$).

```
Esboço de y[n] (Questão 2.1) — cada linha = 0,25 (pirulito desenhado na linha logo abaixo do valor exato)
   2,00 ┤- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  (assíntota: nunca é atingida)
   1,75 ┤                                   ●     ●     ●     ●     ●     ●     ●
   1,50 ┤                             ●     │     │     │     │     │     │     │
   1,25 ┤                             │     │     │     │     │     │     │     │
   1,00 ┤                       ●     │     │     │     │     │     │     │     │
   0,75 ┤                       │     │     │     │     │     │     │     │     │
   0,50 ┤                       │     │     │     │     │     │     │     │     │
   0,25 ┤                       │     │     │     │     │     │     │     │     │
      0 ┼─────●─────●─────●─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─►
             -3    -2    -1     0     1     2     3     4     5     6     7     8   n
valor         0     0     0     1   1,5  1,75 1,875 1,938 1,969 1,984 1,992 1,996
```

**Prova real ($n = 2$, pela definição):** os termos ativos são $k = 2, 3, 4$ (de $2$ até $n + 2 = 4$; nº de termos $= 4 - 2 + 1 = 3$):
$$y[2] = \left(\frac{1}{2}\right)^{2-2} + \left(\frac{1}{2}\right)^{3-2} + \left(\frac{1}{2}\right)^{4-2} = 1 + \frac{1}{2} + \frac{1}{4} = \frac{7}{4} = 1,75 \quad ✓$$

> **✅ Verificação com o Gabarito Oficial (Oppenheim, pág. 554):**
> $2\left[1 - \left(\frac{1}{2}\right)^{n+1}\right]u[n]$ — **100% idêntico!**

---

## Questão 2.2 — [Oppenheim 2.4, pág. 138 (EN) / pág. 83 (PT)]
**Calcule e represente graficamente $y[n] = x[n] * h[n]$, sendo que:**
$$x[n] = \begin{cases} 1, & 3 \le n \le 8 \\ 0, & \text{caso contrário} \end{cases}, \qquad h[n] = \begin{cases} 1, & 4 \le n \le 15 \\ 0, & \text{caso contrário} \end{cases}$$

### **Resolução Passo a Passo:**

#### **Passo 1: Escolher quem fica parado e quebrar em pedaços**
Pela definição:
$$y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]$$
Fica parado $x[k]$ e desliza $h[n-k]$. O sinal $x[k]$ tem **um único pedaço**:

| Pedaço | Trecho em $k$ | Fórmula | Nº de amostras |
|:---:|:---:|:---:|:---:|
| A | $3 \le k \le 8$ | $x[k] = 1$ | $8 - 3 + 1 = 6$ |

**Pontos de quebra** (onde a fórmula de $x[k]$ muda): $k = 3$ (o pedaço A começa) e $k = 9$ (primeiro $k$ depois do fim, onde $x$ volta a ser $0$).

#### **Passo 2: Achar a janela $h[n-k]$**
$h[m] = 1$ quando $4 \le m \le 15$. Trocando $m$ por $n - k$:
$$4 \le n - k \le 15$$
Subtraindo $n$ dos três lados:
$$4 - n \le -k \le 15 - n$$
Multiplicando por $-1$ (o que **inverte** as desigualdades):
$$n - 15 \le k \le n - 4$$
Logo, $h[n-k]$ é uma janela de altura $1$ com:
- **cauda** (borda esquerda) em $k = n - 15$;
- **frente** (borda direita) em $k = n - 4$;
- largura de $(n - 4) - (n - 15) + 1 = 12$ amostras (mais larga que $x[k]$, que tem 6).

#### **Passo 3: Tabela de eventos**
Igualando cada borda a cada ponto de quebra (o valor de $n$ obtido é o **primeiro** $n$ da nova situação):

| Borda | Ponto de quebra | Equação | $n$ | O que acontece |
|:---:|:---:|:---:|:---:|:---|
| frente | $k = 3$ | $n - 4 = 3$ | $7$ | a frente toca o início de $x[k]$ (começa a sobreposição) |
| frente | $k = 9$ | $n - 4 = 9$ | $13$ | a frente passa do fim de $x[k]$ ($x$ inteiro dentro da janela) |
| cauda | $k = 3$ | $n - 15 = 3$ | $18$ | a cauda está em $k = 3$; a partir de $n = 19$ ela solta amostras |
| cauda | $k = 9$ | $n - 15 = 9$ | $24$ | a cauda passa do fim de $x[k]$ (fim da sobreposição) |

Os 4 eventos cortam o eixo $n$ em **5 intervalos**:
```
     I1     │     I2      │     I3      │     I4      │   I5
────────────┼─────────────┼─────────────┼─────────────┼──────► n
            7            13            18            24
```
*(Como a janela é mais larga que $x[k]$, os dois eventos da frente vêm antes dos da cauda, e a etapa do meio é "$x[k]$ inteiro dentro da janela".)*

**Regra dos limites** usada em todos os intervalos:
- limite inferior $= \max(\text{cauda},\ 3) = \max(n - 15,\ 3)$;
- limite superior $= \min(\text{frente},\ 8) = \min(n - 4,\ 8)$;
- se o inferior for maior que o superior, a soma é vazia ($= 0$).

#### **Passo 4: Avaliar a soma em cada intervalo**

##### **Intervalo 1: $n \le 6$ (sem sobreposição à esquerda)**
**(a) Situação:** a janela inteira está à esquerda de $x[k]$.

**(b) Faixa de $n$:** a frente ainda não chegou a $k = 3$:
$$n - 4 < 3 \implies n < 7 \implies n \le 6$$

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 6
           cauda = n-15 = -9
                                            frente = n-4 = 2
           ▼                                ▼
h[n-k]     1  1  1  1  1  1  1  1  1  1  1  1  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
x[k]       ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  1  1  1  1  1  1  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
sobrep.
         ──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼─► k
k         -9 -8 -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
limites: A: max(-9, 3) = 3 > min(2, 8) = 2  →  vazio
```

**(c) Outra borda:** a cauda $n - 15 \le 6 - 15 = -9$ está ainda mais à esquerda.

**(d) Limites:**
- inferior $= \max(n - 15,\ 3) = 3$, pois $n - 15 \le -9 < 3$;
- superior $= \min(n - 4,\ 8) = n - 4$, pois $n - 4 \le 2 < 8$.

Como $n - 4 \le 2 < 3$, o superior é menor que o inferior: soma **vazia**.

**(e)/(f) Resultado:**
$$y[n] = 0, \quad \text{para } n \le 6$$

**(g) Prova real ($n = 6$):** a janela cobre $k = -9, \dots, 2$; nesses $k$, $x[k] = 0$, logo $y[6] = 0$. ✓

---

##### **Intervalo 2: $7 \le n \le 12$ (a frente atravessa $x[k]$)**
**(a) Situação:** a frente entrou em $x[k]$ e ainda não passou do fim; a cauda está à esquerda.

**(b) Faixa de $n$:** a frente está dentro de $[3, 8]$:
$$3 \le n - 4 \le 8$$
Somando $4$ aos três lados:
$$7 \le n \le 12$$

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 9
                    cauda = n-15 = -6
                                                     frente = n-4 = 5
                    ▼                                ▼
h[n-k]     ·  ·  ·  1  1  1  1  1  1  1  1  1  1  1  1  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
x[k]       ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  1  1  1  1  1  1  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
sobrep.                                       ▓▓ ▓▓ ▓▓
         ──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼─► k
k         -9 -8 -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
limites: A: k = 3 … 5  (5 - (3) + 1 = 3 termos)
```

**(c) Outra borda:** $n - 15 \le 12 - 15 = -3 < 3$: a cauda está à esquerda de $x[k]$.

**(d) Limites:**
- inferior $= \max(n - 15,\ 3) = 3$, pois $n - 15 \le -3 < 3$;
- superior $= \min(n - 4,\ 8) = n - 4$, pois $n - 4 \le 8$.

$\implies k$ de $3$ até $n - 4$.

**(e) Soma montada:**
$$y[n] = \sum_{k=3}^{n-4} \underbrace{x[k]}_{1}\cdot\underbrace{h[n-k]}_{1} = \sum_{k=3}^{n-4} 1$$

**(f) Conta:**
$$\text{nº de termos} = (n - 4) - 3 + 1 = n - 6$$
$$y[n] = 1\cdot(n - 6)$$
$$y[n] = n - 6, \quad \text{para } 7 \le n \le 12$$

**(g) Prova real:**

| $n$ | Janela ($k$) | $k$ com $x[k] = 1$ | Soma direta | $n - 6$ |
|:---:|:---:|:---:|:---:|:---:|
| $7$ | $-8 \dots 3$ | $3$ | $1$ | $1$ ✓ |
| $9$ | $-6 \dots 5$ | $3, 4, 5$ | $3$ | $3$ ✓ |
| $12$ | $-3 \dots 8$ | $3, \dots, 8$ | $6$ | $6$ ✓ |

---

##### **Intervalo 3: $13 \le n \le 17$ ($x[k]$ inteiro dentro da janela)**
**(a) Situação:** a frente já passou do fim de $x[k]$ e a cauda ainda não passou do início.

**(b) Faixa de $n$:** duas condições simultâneas:
- frente depois do fim: $n - 4 \ge 9 \implies n \ge 13$;
- cauda no início ou antes dele: $n - 15 \le 3 \implies n \le 18$, mas $n = 18$ já é o primeiro $n$ do Intervalo 4 (tabela de eventos), então aqui $n \le 17$.

$$\implies 13 \le n \le 17$$

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 15
                                      cauda = n-15 = 0
                                                                       frente = n-4 = 11
                                      ▼                                ▼
h[n-k]     ·  ·  ·  ·  ·  ·  ·  ·  ·  1  1  1  1  1  1  1  1  1  1  1  1  ·  ·  ·  ·  ·  ·  ·  ·  ·
x[k]       ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  1  1  1  1  1  1  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
sobrep.                                       ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓
         ──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼─► k
k         -9 -8 -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
limites: A: k = 3 … 8  (8 - (3) + 1 = 6 termos)
```

**(c) Outra borda:** já conferida no item (b).

**(d) Limites:**
- inferior $= \max(n - 15,\ 3) = 3$, pois $n - 15 \le 17 - 15 = 2 < 3$;
- superior $= \min(n - 4,\ 8) = 8$, pois $n - 4 \ge 13 - 4 = 9 > 8$.

$\implies k$ de $3$ até $8$.

**(e) Soma montada:**
$$y[n] = \sum_{k=3}^{8} 1\cdot 1$$

**(f) Conta:**
$$\text{nº de termos} = 8 - 3 + 1 = 6$$
$$y[n] = 6, \quad \text{para } 13 \le n \le 17$$

**(g) Prova real ($n = 15$):** a janela cobre $k = 0, \dots, 11$ e contém todo o trecho $k = 3, \dots, 8$: $1+1+1+1+1+1 = 6$. ✓

---

##### **Intervalo 4: $18 \le n \le 23$ (a cauda atravessa $x[k]$)**
**(a) Situação:** a frente está depois do fim de $x[k]$; a cauda está dentro de $x[k]$ e vai soltando amostras.

**(b) Faixa de $n$:** a cauda está dentro de $[3, 8]$:
$$3 \le n - 15 \le 8$$
Somando $15$ aos três lados:
$$18 \le n \le 23$$

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 20
                                                     cauda = n-15 = 5
                                                                                      frente = n-4 = 16
                                                     ▼                                ▼
h[n-k]     ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  1  1  1  1  1  1  1  1  1  1  1  1  ·  ·  ·  ·
x[k]       ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  1  1  1  1  1  1  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
sobrep.                                             ▓▓ ▓▓ ▓▓ ▓▓
         ──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼─► k
k         -9 -8 -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
limites: A: k = 5 … 8  (8 - (5) + 1 = 4 termos)
```

**(c) Outra borda:** $n - 4 \ge 18 - 4 = 14 > 8$: a frente está depois do fim.

**(d) Limites:**
- inferior $= \max(n - 15,\ 3) = n - 15$, pois $n - 15 \ge 3$;
- superior $= \min(n - 4,\ 8) = 8$, pois $n - 4 \ge 14 > 8$.

$\implies k$ de $n - 15$ até $8$.

**(e) Soma montada:**
$$y[n] = \sum_{k=n-15}^{8} 1\cdot 1$$

**(f) Conta:**
$$\text{nº de termos} = 8 - (n - 15) + 1 = 8 - n + 15 + 1 = 24 - n$$
$$y[n] = 24 - n, \quad \text{para } 18 \le n \le 23$$

⚠️ **Atenção ao sinal:** $-(n - 15) = -n + 15$.

**(g) Prova real:**

| $n$ | Janela ($k$) | $k$ com $x[k] = 1$ | Soma direta | $24 - n$ |
|:---:|:---:|:---:|:---:|:---:|
| $18$ | $3 \dots 14$ | $3, \dots, 8$ | $6$ | $6$ ✓ |
| $20$ | $5 \dots 16$ | $5, 6, 7, 8$ | $4$ | $4$ ✓ |
| $23$ | $8 \dots 19$ | $8$ | $1$ | $1$ ✓ |

---

##### **Intervalo 5: $n \ge 24$ (sem sobreposição à direita)**
**(a) Situação:** a janela inteira está à direita de $x[k]$.

**(b) Faixa de $n$:** $n - 15 > 8 \implies n > 23 \implies n \ge 24$.

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 24
                                                                 cauda = n-15 = 9
                                                                                                  frente = n-4 = 20
                                                                 ▼                                ▼
h[n-k]     ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  1  1  1  1  1  1  1  1  1  1  1  1
x[k]       ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  1  1  1  1  1  1  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
sobrep.
         ──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼─► k
k         -9 -8 -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
limites: A: max(9, 3) = 9 > min(20, 8) = 8  →  vazio
```

**(c) Outra borda:** a frente $n - 4 \ge 20$ está ainda mais à direita.

**(d) Limites:**
- inferior $= \max(n - 15,\ 3) = n - 15 \ge 9$;
- superior $= \min(n - 4,\ 8) = 8$.

Como $9 > 8$, soma **vazia**.

**(e)/(f) Resultado:**
$$y[n] = 0, \quad \text{para } n \ge 24$$

**(g) Prova real ($n = 24$):** a janela cobre $k = 9, \dots, 20$; nesses $k$, $x[k] = 0$, logo $y[24] = 0$. ✓

---

#### **Passo 5: Conferir as fronteiras (por que o gabarito escreve $12 \le n \le 18$ no patamar)**
Calculando os pontos de fronteira pelas **duas** fórmulas vizinhas:
- $n = 12$: pela fórmula do Intervalo 2, $12 - 6 = 6$; pela do Intervalo 3, $6$. Iguais.
- $n = 18$: pela fórmula do Intervalo 4, $24 - 18 = 6$; pela do Intervalo 3, $6$. Iguais.

Como as fórmulas vizinhas coincidem nesses pontos, é igualmente correto escrever o patamar como $12 \le n \le 18$ (forma do gabarito) e as rampas como $7 \le n \le 11$ e $19 \le n \le 23$. **As amostras são exatamente as mesmas.**

### **Resposta Final (Questão 2.2):**
$$y[n] = \begin{cases} n - 6, & 7 \le n \le 11 \\ 6, & 12 \le n \le 18 \\ 24 - n, & 19 \le n \le 23 \\ 0, & \text{caso contrário} \end{cases}$$

**Sequência completa (amostras não nulas):**

| $n$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ | $13$ | $14$ | $15$ | $16$ | $17$ | $18$ | $19$ | $20$ | $21$ | $22$ | $23$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $y[n]$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $6$ | $6$ | $6$ | $6$ | $6$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ |

```
Esboço de y[n] (Questão 2.2) — trapézio
      6 ┤                       ●  ●  ●  ●  ●  ●  ●
      5 ┤                    ●  │  │  │  │  │  │  │  ●
      4 ┤                 ●  │  │  │  │  │  │  │  │  │  ●
      3 ┤              ●  │  │  │  │  │  │  │  │  │  │  │  ●
      2 ┤           ●  │  │  │  │  │  │  │  │  │  │  │  │  │  ●
      1 ┤        ●  │  │  │  │  │  │  │  │  │  │  │  │  │  │  │  ●
      0 ┼──●──●──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──●──●─►
           5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25   n
```

**Verificações finais (prova real):**
1. **Início:** início de $x$ + início de $h$ $= 3 + 4 = 7$ ✓.
2. **Fim:** fim de $x$ + fim de $h$ $= 8 + 15 = 23$ ✓.
3. **Duração:** $L_x + L_h - 1 = 6 + 12 - 1 = 17$ amostras, de $n = 7$ até $n = 23$ (são $23 - 7 + 1 = 17$) ✓.
4. **Soma total:** $\sum y = \left(\sum x\right)\cdot\left(\sum h\right) = 6 \cdot 12 = 72$. Conferindo pela tabela:
   $$(1 + 2 + 3 + 4 + 5) + (6 \cdot 7) + (5 + 4 + 3 + 2 + 1) = 15 + 42 + 15 = 72 \quad ✓$$
5. **Macete do trapézio:** patamar $= 1 \cdot 1 \cdot \min(6, 12) = 6$ ✓, com largura $|12 - 6| + 1 = 7$ amostras ($n = 12, \dots, 18$) ✓.

> **✅ Verificação com o Gabarito Oficial (Oppenheim, pág. 554):**
> As expressões $n-6$, $6$, $24-n$ e $0$ batem exatamente com a pág. 554. *(Nota de revisão: no gabarito impresso da pág. 554 consta o erro tipográfico `16 <= n <= 23` na 3ª linha, mas como o patamar constante $6$ vai até $n = 18$, a descida estrita ocorre em $19 \le n \le 23$).*

---

## Questão 2.3 — [Oppenheim 2.6, pág. 138 (EN) / pág. 83 (PT)]
**Calcule e represente graficamente a convolução $y[n] = x[n] * h[n]$, sendo que:**
$$x[n] = \left(\frac{1}{3}\right)^{-n} u[-n-1] \quad \text{e} \quad h[n] = u[n-1]$$

### **Resolução Passo a Passo:**

#### **Passo 1: Simplificar a potência e quebrar $x[k]$ em pedaços**
Usando a propriedade de potências $(a^{p})^{q} = a^{pq}$:
$$\left(\frac{1}{3}\right)^{-n} = \left(3^{-1}\right)^{-n} = 3^{(-1)(-n)} = 3^n$$
Assim:
$$x[n] = 3^n u[-n-1]$$
O degrau $u[-n-1]$ vale $1$ quando $-n - 1 \ge 0 \implies -n \ge 1 \implies n \le -1$. Na variável $k$:

| Pedaço | Trecho em $k$ | Fórmula |
|:---:|:---:|:---:|
| A | $k \le -1$ (infinito à esquerda) | $x[k] = 3^k$ |

**Pontos de quebra:** só $k = 0$ (primeiro $k$ depois do fim). O lado esquerdo é infinito e **não** gera ponto de quebra.

Montando a soma de convolução:
$$y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k] = \sum_{k=-\infty}^{\infty} 3^k u[-k-1] \cdot u[n - k - 1]$$

#### **Passo 2: Achar a janela $h[n-k]$**
$h[m] = u[m-1]$ vale $1$ quando $m - 1 \ge 0 \iff m \ge 1$ (de $1$ até $+\infty$). Trocando $m$ por $n - k$:
$$n - k - 1 \ge 0 \implies n - 1 \ge k \implies k \le n - 1$$
Logo, a janela vai de $k = -\infty$ até a **frente** $k = n - 1$. Ela **não tem cauda** (pois $h$ se estende até $+\infty$).

Combinando com o pedaço A ($k \le -1$), os termos não nulos são os $k$ com:
$$k \le -1 \quad \text{e} \quad k \le n - 1 \iff k \le \min(-1,\ n - 1)$$

#### **Passo 3: Tabela de eventos**

| Borda | Ponto de quebra | Equação | $n$ | O que acontece |
|:---:|:---:|:---:|:---:|:---|
| frente | $k = 0$ | $n - 1 = 0$ | $1$ | a frente passa do fim de $x[k]$ |

Um único evento, logo **2 intervalos**: $n \le 0$ e $n \ge 1$.

#### **Fórmula que será usada (PG infinita à esquerda)**
Para somar $\sum_{k=-\infty}^{B} 3^k$, fazemos $m = -k$ (logo $k = -m$):
- quando $k = B \implies m = -B$;
- quando $k \to -\infty \implies m \to +\infty$;
- $3^k = 3^{-m} = \left(\frac{1}{3}\right)^m$.

$$\sum_{k=-\infty}^{B} 3^k = \sum_{m=-B}^{\infty} \left(\frac{1}{3}\right)^m$$
E a PG infinita com $|r| < 1$ vale
$$\sum_{m=A}^{\infty} r^m = \frac{r^A}{1 - r} \qquad (\text{primeiro termo sobre } 1 - r)$$
Aqui $r = \frac{1}{3}$ (e $|r| = \frac{1}{3} < 1$, então a série **converge**) e $A = -B$.

#### **Passo 4: Avaliar a soma em cada intervalo**

##### **Intervalo 1: $n \le 0$ (a frente está dentro de $x[k]$)**
**(a) Situação:** a frente $n - 1$ ainda não passou do fim de $x[k]$ ($k = -1$).

**(b) Faixa de $n$:** $n - 1 \le -1 \implies n \le 0$.

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = -1
         sem cauda: a janela vai até k = -∞ (◄)
                                frente = n-1 = -2
                                ▼
h[n-k]  ◄     1     1     1     1     ·     ·     ·     ·     ·
x[k]    ◄ 1/243  1/81  1/27   1/9   1/3     ·     ·     ·     ·
sobrep.   ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓
         ─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─► k
k            -5    -4    -3    -2    -1     0     1     2     3
limites: A: k = -∞ … -2
```

**(c) Outra borda:** não existe (a janela vai até $-\infty$).

**(d) Limites:** limite superior $= \min(-1,\ n - 1) = n - 1$, pois $n - 1 \le -1$. Limite inferior: $-\infty$.

**(e) Soma montada:**
$$y[n] = \sum_{k=-\infty}^{n-1} 3^k \cdot 1$$

**(f) Conta:** com $m = -k$, temos $B = n - 1$, logo $A = -B = 1 - n$:
$$y[n] = \sum_{m=1-n}^{\infty} \left(\frac{1}{3}\right)^m$$
Aplicando a PG infinita com $r = \frac{1}{3}$ e $A = 1 - n$:
$$y[n] = \frac{\left(\frac{1}{3}\right)^{1-n}}{1 - \frac{1}{3}}$$
Simplificando o numerador, $\left(\frac{1}{3}\right)^{1-n} = 3^{-(1-n)} = 3^{n-1}$, e o denominador, $1 - \frac{1}{3} = \frac{2}{3}$:
$$y[n] = \frac{3^{n-1}}{\frac{2}{3}} = 3^{n-1}\cdot\frac{3}{2}$$
Como $3^{n-1}\cdot 3 = 3^{n}$:
$$y[n] = \frac{3^n}{2}, \quad \text{para } n \le 0$$

**(g) Prova real ($n = -1$):** os termos ativos são $k \le n - 1 = -2$:
$$y[-1] = 3^{-2} + 3^{-3} + 3^{-4} + \dots = \frac{1}{9} + \frac{1}{27} + \frac{1}{81} + \dots$$
É uma PG infinita com primeiro termo $\frac{1}{9}$ e razão $\frac{1}{3}$:
$$y[-1] = \frac{\frac{1}{9}}{1 - \frac{1}{3}} = \frac{\frac{1}{9}}{\frac{2}{3}} = \frac{1}{9}\cdot\frac{3}{2} = \frac{1}{6}$$
Pela fórmula: $\frac{3^{-1}}{2} = \frac{1}{3}\cdot\frac{1}{2} = \frac{1}{6}$ ✓.

---

##### **Intervalo 2: $n \ge 1$ (todo o $x[k]$ dentro da janela)**
**(a) Situação:** a frente $n - 1 \ge 0$ passou do fim de $x[k]$; a janela contém todo o sinal.

**(b) Faixa de $n$:** $n - 1 \ge 0 \implies n \ge 1$.

**Esboço do intervalo** (mesma escala em todos os intervalos da questão; ▓ = termos que entram na soma):
```
Instante representativo: n = 2
         sem cauda: a janela vai até k = -∞ (◄)
                                                  frente = n-1 = 1
                                                  ▼
h[n-k]  ◄     1     1     1     1     1     1     1     ·     ·
x[k]    ◄ 1/243  1/81  1/27   1/9   1/3     ·     ·     ·     ·
sobrep.   ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓
         ─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─► k
k            -5    -4    -3    -2    -1     0     1     2     3
limites: A: k = -∞ … -1
```

**(c) Outra borda:** não existe.

**(d) Limites:** limite superior $= \min(-1,\ n - 1) = -1$, pois $n - 1 \ge 0 > -1$. Limite inferior: $-\infty$.

**(e) Soma montada:**
$$y[n] = \sum_{k=-\infty}^{-1} 3^k \cdot 1$$

**(f) Conta:** com $m = -k$, temos $B = -1$, logo $A = -B = 1$:
$$y[n] = \sum_{m=1}^{\infty} \left(\frac{1}{3}\right)^m = \frac{\left(\frac{1}{3}\right)^{1}}{1 - \frac{1}{3}} = \frac{\frac{1}{3}}{\frac{2}{3}} = \frac{1}{3}\cdot\frac{3}{2}$$
$$y[n] = \frac{1}{2}, \quad \text{para } n \ge 1$$

**(g) Prova real ($n = 3$):** os termos ativos são $k \le \min(-1, 2) = -1$:
$$y[3] = 3^{-1} + 3^{-2} + 3^{-3} + \dots = \frac{1}{3} + \frac{1}{9} + \frac{1}{27} + \dots = \frac{\frac{1}{3}}{1 - \frac{1}{3}} = \frac{1}{2} \quad ✓$$

---

#### **Passo 5: Conferir a fronteira e escrever no formato do gabarito**
No ponto $n = 0$ (último $n$ do Intervalo 1), a fórmula dá:
$$y[0] = \frac{3^0}{2} = \frac{1}{2}$$
que é **exatamente** o valor constante do Intervalo 2. Portanto podemos mover o ponto $n = 0$ para o segundo ramo e escrever $n < 0$ / $n \ge 0$, como no gabarito. **As amostras são as mesmas.**

### **Resposta Final (Questão 2.3):**
$$y[n] = \begin{cases} \dfrac{3^n}{2}, & n < 0 \\[0.8em] \dfrac{1}{2}, & n \ge 0 \end{cases}$$

**Valores para o esboço:** $y[-3] = \frac{1}{54} \approx 0,019$; $y[-2] = \frac{1}{18} \approx 0,056$; $y[-1] = \frac{1}{6} \approx 0,167$; $y[n] = 0,5$ para todo $n \ge 0$ (o sinal cresce exponencialmente desde $0$ em $n \to -\infty$ e satura em $\frac{1}{2}$).

```
Esboço de y[n] (Questão 2.3) — cada linha = 0,05
   0,50 ┤                                   ●     ●     ●     ●     ●
   0,45 ┤                                   │     │     │     │     │
   0,40 ┤                                   │     │     │     │     │
   0,35 ┤                                   │     │     │     │     │
   0,30 ┤                                   │     │     │     │     │
   0,25 ┤                                   │     │     │     │     │
   0,20 ┤                                   │     │     │     │     │
   0,15 ┤                             ●     │     │     │     │     │
   0,10 ┤                             │     │     │     │     │     │
   0,05 ┤                       ●     │     │     │     │     │     │
      0 ┼─────●─────●─────●─────┼─────┼─────┼─────┼─────┼─────┼─────┼─►
             -5    -4    -3    -2    -1     0     1     2     3     4   n
valor     1/486 1/162  1/54  1/18   1/6   1/2   1/2   1/2   1/2   1/2
```

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

> **⚠️ Atenção:** a relação tem $g[n - 2k]$, e **não** $g[n - k]$. Portanto **não** é uma soma de convolução, e o algoritmo de deslizar janela **não se aplica**. O caminho é substituir a entrada diretamente na relação.

### **Resolução Passo a Passo:**

#### **Preparação: quem é $g[m]$**
$g[m] = u[m] - u[m-4]$. Avaliando trecho a trecho:
- $m < 0$: $u[m] = 0$ e $u[m-4] = 0$, logo $g[m] = 0 - 0 = 0$;
- $0 \le m \le 3$: $u[m] = 1$ e $u[m-4] = 0$ (pois $m - 4 \le -1$), logo $g[m] = 1 - 0 = 1$;
- $m \ge 4$: $u[m] = 1$ e $u[m-4] = 1$, logo $g[m] = 1 - 1 = 0$.

$$g[m] = \begin{cases} 1, & 0 \le m \le 3 \\ 0, & \text{caso contrário} \end{cases}$$

```
Esboço de g[m] = u[m] - u[m-4]
      1 ┤               ●   ●   ●   ●
      0 ┼───●───●───●───┼───┼───┼───┼───●───●───●───●─►
           -3  -2  -1   0   1   2   3   4   5   6   7   m
```

#### **Item (a): Entrada $x[n] = \delta[n-1]$**
Substituindo $x[k] = \delta[k-1]$ na relação do sistema:
$$y[n] = \sum_{k=-\infty}^{\infty} \delta[k-1]\, g[n - 2k]$$
O impulso $\delta[k-1]$ vale $1$ quando $k - 1 = 0 \iff k = 1$, e vale $0$ para todo outro $k$. Escrevendo alguns termos da soma:
$$y[n] = \dots + \underbrace{\delta[-1]}_{0}g[n] + \underbrace{\delta[0]}_{1}g[n-2] + \underbrace{\delta[1]}_{0}g[n-4] + \dots$$
(os termos correspondem a $k = 0$, $k = 1$ e $k = 2$). Só o termo $k = 1$ sobrevive:
$$y[n] = 1\cdot g[n - 2(1)] = g[n - 2]$$
Trocando $m$ por $(n - 2)$ em $g[m] = u[m] - u[m-4]$:
$$y[n] = u[n - 2] - u[(n - 2) - 4]$$
$$\mathbf{y[n] = u[n - 2] - u[n - 6]}$$
Ou seja, $y[n] = 1$ para $0 \le n - 2 \le 3 \iff 2 \le n \le 5$, e $0$ fora disso.

```
Esboço de y[n] no item (a): u[n-2] - u[n-6]
      1 ┤               ●   ●   ●   ●
      0 ┼───●───●───●───┼───┼───┼───┼───●───●───●───●─►
           -1   0   1   2   3   4   5   6   7   8   9   n
```

---

#### **Item (b): Entrada $x[n] = \delta[n-2]$**
Substituindo $x[k] = \delta[k-2]$:
$$y[n] = \sum_{k=-\infty}^{\infty} \delta[k-2]\, g[n - 2k]$$
O impulso $\delta[k-2]$ vale $1$ só em $k = 2$. Escrevendo alguns termos:
$$y[n] = \dots + \underbrace{\delta[-1]}_{0}g[n-2] + \underbrace{\delta[0]}_{1}g[n-4] + \underbrace{\delta[1]}_{0}g[n-6] + \dots$$
(os termos correspondem a $k = 1$, $k = 2$ e $k = 3$). Só o termo $k = 2$ sobrevive:
$$y[n] = g[n - 2(2)] = g[n - 4]$$
Substituindo na expressão de $g[\cdot]$:
$$y[n] = u[n - 4] - u[(n - 4) - 4]$$
$$\mathbf{y[n] = u[n - 4] - u[n - 8]}$$
Ou seja, $y[n] = 1$ para $0 \le n - 4 \le 3 \iff 4 \le n \le 7$, e $0$ fora disso.

```
Esboço de y[n] no item (b): u[n-4] - u[n-8]
      1 ┤                       ●   ●   ●   ●
      0 ┼───●───●───●───●───●───┼───┼───┼───┼───●───●─►
           -1   0   1   2   3   4   5   6   7   8   9   n
```

---

#### **Item (c): O sistema $S$ é LIT (Linear e Invariante no Tempo)?**
O enunciado já afirma que $S$ é linear. Resta testar a **invariância no tempo**: um atraso de $n_0$ amostras na entrada deve provocar exatamente o mesmo atraso de $n_0$ amostras na saída.
- No item (a), aplicamos $x_1[n] = \delta[n-1]$ e obtivemos a saída:
  $$y_1[n] = u[n-2] - u[n-6]$$
- No item (b), aplicamos a entrada $x_2[n] = \delta[n-2]$. Ela é a entrada $x_1[n]$ atrasada de $1$ amostra, pois:
  $$x_1[n-1] = \delta[(n-1)-1] = \delta[n-2] = x_2[n]$$
- Se o sistema fosse invariante no tempo, a saída para $x_2[n]$ teria de ser $y_1[n-1]$. Trocando $n$ por $n - 1$ em $y_1[n]$:
  $$y_1[n-1] = u[(n-1)-2] - u[(n-1)-6] = u[n-3] - u[n-7]$$
  que vale $1$ para $3 \le n \le 6$.
- Porém, no item (b) encontramos a saída real do sistema:
  $$y_2[n] = u[n-4] - u[n-8]$$
  que vale $1$ para $4 \le n \le 7$.
- **Comparando num ponto concreto**, $n = 3$:
  $$y_1[3 - 1] = u[0] - u[-4] = 1 - 0 = 1 \qquad \text{mas} \qquad y_2[3] = u[-1] - u[-5] = 0 - 0 = 0$$

Como $y_2[n] \neq y_1[n-1]$ (atrasar a entrada em $1$ atrasou a saída em $2$), o sistema é **variante no tempo**.
**Resposta (c): Não, $S$ não é LIT.**

---

#### **Item (d): Entrada $x[n] = u[n]$**
Substituindo $x[k] = u[k]$, que vale $1$ para $k \ge 0$ e $0$ para $k < 0$, os termos com $k < 0$ somem:
$$y[n] = \sum_{k=0}^{\infty} g[n - 2k] = g[n] + g[n-2] + g[n-4] + g[n-6] + \dots$$
(termos de $k = 0, 1, 2, 3, \dots$). Cada termo vale $1$ se o argumento $n - 2k$ está em $\{0, 1, 2, 3\}$, e $0$ caso contrário. Então **$y[n]$ é igual ao número de valores de $k \ge 0$ para os quais $0 \le n - 2k \le 3$**.

##### **Passo 1: Resolver a desigualdade para $k$**
$$0 \le n - 2k \le 3$$
Subtraindo $n$:
$$-n \le -2k \le 3 - n$$
Dividindo por $-2$ (o que **inverte** as desigualdades):
$$\frac{n - 3}{2} \le k \le \frac{n}{2}$$
Juntando com $k \ge 0$ e lembrando que $k$ é inteiro, os $k$ que contam são:
$$\max\left(0,\ \left\lceil \frac{n-3}{2} \right\rceil\right) \le k \le \left\lfloor \frac{n}{2} \right\rfloor$$
($\lceil\cdot\rceil$ arredonda para cima e $\lfloor\cdot\rfloor$ arredonda para baixo, porque $k$ precisa ser inteiro).

##### **Passo 2: Contar os termos em cada caso**

**Caso 1: $n < 0$ (ex.: $n = -1$).**
O limite superior é $\left\lfloor \frac{n}{2} \right\rfloor \le \left\lfloor -\frac{1}{2} \right\rfloor = -1$, e o inferior é pelo menos $0$. Como $-1 < 0$, **nenhum** $k$ serve. Conferindo termo a termo para $n = -1$:

| $k$ | $0$ | $1$ | $2$ | $\dots$ |
|:---:|:---:|:---:|:---:|:---:|
| $n - 2k$ | $-1$ | $-3$ | $-5$ | $\dots$ |
| $g[n-2k]$ | $0$ | $0$ | $0$ | $0$ |

$$y[n] = 0, \quad \text{para } n < 0$$

**Caso 2: $n = 0$.**
Limites: inferior $= \max\left(0, \left\lceil -\frac{3}{2} \right\rceil\right) = \max(0, -1) = 0$; superior $= \left\lfloor 0 \right\rfloor = 0$. Nº de termos $= 0 - 0 + 1 = 1$.

| $k$ | $0$ | $1$ | $2$ | $\dots$ |
|:---:|:---:|:---:|:---:|:---:|
| $n - 2k$ | $0$ | $-2$ | $-4$ | $\dots$ |
| $g[n-2k]$ | $1$ | $0$ | $0$ | $0$ |

$$y[0] = 1 + 0 + 0 + \dots = 1$$

**Caso 3: $n = 1$.**
Limites: inferior $= \max\left(0, \left\lceil -1 \right\rceil\right) = \max(0, -1) = 0$; superior $= \left\lfloor \frac{1}{2} \right\rfloor = 0$. Nº de termos $= 0 - 0 + 1 = 1$.

| $k$ | $0$ | $1$ | $2$ | $\dots$ |
|:---:|:---:|:---:|:---:|:---:|
| $n - 2k$ | $1$ | $-1$ | $-3$ | $\dots$ |
| $g[n-2k]$ | $1$ | $0$ | $0$ | $0$ |

$$y[1] = 1 + 0 + 0 + \dots = 1$$

**Caso 4: $n$ par, $n \ge 2$.** Escreva $n = 2p$ com $p \ge 1$.
- Superior: $\left\lfloor \frac{2p}{2} \right\rfloor = p$.
- Inferior: $\left\lceil \frac{2p - 3}{2} \right\rceil = \left\lceil p - 1,5 \right\rceil = p - 1$. Como $p \ge 1$, $p - 1 \ge 0$, logo $\max(0, p - 1) = p - 1$.
- Nº de termos $= p - (p - 1) + 1 = 2$, logo $y[n] = 2$.

Conferindo termo a termo para $n = 2$ e $n = 4$:

| $k$ | $0$ | $1$ | $2$ | $3$ | $\dots$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $n = 2$: $\ n - 2k$ | $2$ | $0$ | $-2$ | $-4$ | $\dots$ |
| $n = 2$: $\ g[n-2k]$ | $1$ | $1$ | $0$ | $0$ | $0$ |
| $n = 4$: $\ n - 2k$ | $4$ | $2$ | $0$ | $-2$ | $\dots$ |
| $n = 4$: $\ g[n-2k]$ | $0$ | $1$ | $1$ | $0$ | $0$ |

$$y[2] = 1 + 1 = 2, \qquad y[4] = 0 + 1 + 1 = 2$$

**Caso 5: $n$ ímpar, $n \ge 3$.** Escreva $n = 2p + 1$ com $p \ge 1$.
- Superior: $\left\lfloor \frac{2p + 1}{2} \right\rfloor = \left\lfloor p + 0,5 \right\rfloor = p$.
- Inferior: $\left\lceil \frac{2p + 1 - 3}{2} \right\rceil = \left\lceil p - 1 \right\rceil = p - 1 \ge 0$, logo $\max(0, p - 1) = p - 1$.
- Nº de termos $= p - (p - 1) + 1 = 2$, logo $y[n] = 2$.

Conferindo termo a termo para $n = 3$ e $n = 5$:

| $k$ | $0$ | $1$ | $2$ | $3$ | $\dots$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $n = 3$: $\ n - 2k$ | $3$ | $1$ | $-1$ | $-3$ | $\dots$ |
| $n = 3$: $\ g[n-2k]$ | $1$ | $1$ | $0$ | $0$ | $0$ |
| $n = 5$: $\ n - 2k$ | $5$ | $3$ | $1$ | $-1$ | $\dots$ |
| $n = 5$: $\ g[n-2k]$ | $0$ | $1$ | $1$ | $0$ | $0$ |

$$y[3] = 1 + 1 = 2, \qquad y[5] = 0 + 1 + 1 = 2$$

**Esboço dos casos $n = 4$ (par) e $n = 5$ (ímpar):** os triângulos ▲ marcam onde cada termo $g[n - 2k]$ "lê" o gráfico de $g[m]$. Os pontos andam de $2$ em $2$ para a esquerda, então **sempre** caem exatamente dois deles dentro da caixa $\{0, 1, 2, 3\}$ quando $n \ge 2$:
```
n = 4: cada termo g[n-2k] lê g[m] no ponto m = n - 2k (k = 0, 1, 2, ...)
g[m]         0    0    0    1    1    1    1    0    0    0    0
pontos            ▲         ▲         ▲         ▲
k               k=3       k=2       k=1       k=0
         ────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼─► m
m           -3   -2   -1    0    1    2    3    4    5    6    7
y[4] = g[4] + g[2] + g[0] + g[-2] + ...
     = 0 + 1 + 1 + 0 + ... = 2
```

```
n = 5: cada termo g[n-2k] lê g[m] no ponto m = n - 2k (k = 0, 1, 2, ...)
g[m]         0    0    0    1    1    1    1    0    0    0    0
pontos       ▲         ▲         ▲         ▲         ▲
k          k=4       k=3       k=2       k=1       k=0
         ────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼─► m
m           -3   -2   -1    0    1    2    3    4    5    6    7
y[5] = g[5] + g[3] + g[1] + g[-1] + g[-3] + ...
     = 0 + 1 + 1 + 0 + 0 + ... = 2
```

##### **Passo 3: Juntar os casos e escrever com degraus e impulsos**
$$y[n] = \begin{cases} 0, & n < 0 \\ 1, & n = 0 \text{ ou } n = 1 \\ 2, & n \ge 2 \end{cases}$$
Partindo de $2u[n]$ (que vale $2$ para todo $n \ge 0$), precisamos tirar $1$ unidade em $n = 0$ e em $n = 1$:
$$\mathbf{y[n] = 2u[n] - \delta[n] - \delta[n-1]}$$

```
Esboço de y[n] no item (d): 2u[n] - δ[n] - δ[n-1] = u[n] + u[n-2]
      2 ┤                   ●   ●   ●   ●   ●   ●
      1 ┤           ●   ●   │   │   │   │   │   │
      0 ┼───●───●───┼───┼───┼───┼───┼───┼───┼───┼─►
           -2  -1   0   1   2   3   4   5   6   7   n
```

**Forma equivalente $y[n] = u[n] + u[n-2]$**, conferida por substituição:

| $n$ | $2u[n] - \delta[n] - \delta[n-1]$ | $u[n] + u[n-2]$ | Valor encontrado |
|:---:|:---:|:---:|:---:|
| $-1$ | $0 - 0 - 0 = 0$ | $0 + 0 = 0$ | $0$ ✓ |
| $0$ | $2 - 1 - 0 = 1$ | $1 + 0 = 1$ | $1$ ✓ |
| $1$ | $2 - 0 - 1 = 1$ | $1 + 0 = 1$ | $1$ ✓ |
| $2$ | $2 - 0 - 0 = 2$ | $1 + 1 = 2$ | $2$ ✓ |
| $5$ | $2 - 0 - 0 = 2$ | $1 + 1 = 2$ | $2$ ✓ |

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
> - Se $h(t)$ é não nulo em $a \le t \le b$, então $h(t-\tau)$ é não nulo em $t - b \le \tau \le t - a$: **cauda** $= t - b$, **frente** $= t - a$.
> - Em cada intervalo, os limites de cada pedaço de $x$ são: inferior $= \max(\text{cauda}, \text{início do pedaço})$ e superior $= \min(\text{frente}, \text{fim do pedaço})$.
>
> **Regra de ouro desta resolução:** nenhuma integral é dada como "óbvia" ou "igual a zero" sem conta. Toda integral é feita em 4 etapas: **(1)** montar, **(2)** achar a primitiva, **(3)** substituir o limite superior e o inferior **separadamente**, **(4)** simplificar linha a linha. *(O roteiro completo está no Algoritmo Mestre, seção 8 de `Algoritmos_Resolucao_Sinais_Sistemas.md`.)*

---

## Questão 1.2 — [Exercício 1.2 em Sala de Aula — Apostila, pág. 23]
**Considere que a resposta ao impulso de um SLIT seja dada por $h(t) = u(t-1) - u(t-4)$. Encontre a saída deste sistema em resposta à entrada $x(t) = u(t) + u(t-1) - 2u(t-2)$.**

### **Resolução Passo a Passo:**

#### **Passo 1: Traçar e equacionar $x(\tau)$ (sinal parado) no eixo $\tau$**
Escolhemos deixar $x$ **parado** (ele tem 2 pedaços) e **deslizar** $h$ (um único pulso).

Sinal de entrada $x(\tau) = u(\tau) + u(\tau-1) - 2u(\tau-2)$. Percorremos o eixo $\tau$ da esquerda para a direita, somando o coeficiente de cada degrau que "liga":
- Para $\tau < 0$: nenhum degrau ligou $\implies x(\tau) = 0$.
- Para $0 \le \tau < 1$: só $u(\tau)$ ligou $\implies x(\tau) = 1$.
- Para $1 \le \tau < 2$: ligaram $u(\tau)$ e $u(\tau-1)$ $\implies x(\tau) = 1 + 1 = 2$.
- Para $\tau \ge 2$: ligou também $-2u(\tau-2)$ $\implies x(\tau) = 1 + 1 - 2 = 0$.

$$x(\tau) = \begin{cases} 1, & 0 \le \tau < 1 \quad \text{(pedaço A)} \\ 2, & 1 \le \tau < 2 \quad \text{(pedaço B)} \\ 0, & \text{caso contrário} \end{cases}$$

**Pontos de quebra** (onde a fórmula de $x$ muda): $\tau = 0$ (A começa), $\tau = 1$ (B começa) e $\tau = 2$ (fim do sinal).

#### **Passo 2: Refletir e deslocar $h$: a janela $h(t-\tau)$**
$h(\tau) = u(\tau-1) - u(\tau-4)$ vale $1$ para $1 \le \tau < 4$ (pulso de largura $3$), ou seja, $a = 1$ e $b = 4$. Substituindo o argumento por $(t-\tau)$:
$$1 \le t - \tau \le 4$$
Multiplicando por $-1$ (o que inverte as desigualdades):
$$-4 \le \tau - t \le -1$$
Somando $t$ aos três lados:
$$t - 4 \le \tau \le t - 1$$
Logo, $h(t-\tau)$ é uma janela de altura $1$ e largura $3$, com **cauda** em $\tau = t - 4$ e **frente** em $\tau = t - 1$:
$$h(t-\tau) = \begin{cases} 1, & t - 4 \le \tau \le t - 1 \\ 0, & \text{caso contrário} \end{cases}$$

#### **Passo 3: Tabela de eventos**
Cada borda da janela cruzando cada ponto de quebra muda a fórmula de $y(t)$:

| Borda | Ponto de quebra | Equação | $t$ | O que acontece |
|:---:|:---:|:---:|:---:|:---|
| frente | $\tau = 0$ | $t - 1 = 0$ | $1$ | a janela começa a tocar $x$ |
| frente | $\tau = 1$ | $t - 1 = 1$ | $2$ | a frente entra no pedaço B |
| frente | $\tau = 2$ | $t - 1 = 2$ | $3$ | a frente passa do fim de $x$ ($x$ inteiro dentro da janela) |
| cauda | $\tau = 0$ | $t - 4 = 0$ | $4$ | a cauda começa a soltar o pedaço A |
| cauda | $\tau = 1$ | $t - 4 = 1$ | $5$ | a cauda chega ao pedaço B (A saiu todo) |
| cauda | $\tau = 2$ | $t - 4 = 2$ | $6$ | a cauda passa do fim de $x$ (fim da sobreposição) |

São 6 eventos $\implies$ **7 intervalos**. Como a janela (largura 3) é **mais larga** que $x$ (largura 2), todos os eventos da frente vêm antes dos da cauda, e o intervalo do meio é "$x$ inteiro dentro da janela".

---

#### **Passo 4: Avaliar a integral de convolução nos 7 intervalos de $t$**

##### **Intervalo 1: $t < 1$ (sem sobreposição à esquerda)**

**(a) Situação:** a frente $t - 1$ ainda não chegou a $\tau = 0$.

**(b) Faixa:** $t - 1 < 0 \iff t < 1$.

```
Esboço no eixo τ para t = 0 (representante do Intervalo 1):

      x(τ) 2 │                    ████
           1 │                ████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −4  −3  −2  −1   0   1   2   3   4   5   6   7
    h(t−τ) 1 │████████████
sobreposição │
              ↑ cauda = t−4 = −4
                          ↑ frente = t−1 = −1

sem sobreposição: a frente (−1) ainda não chegou em τ = 0
y(0) = 0
```

**(c) Outra borda:** a cauda $t - 4 < -3$ está ainda mais à esquerda.

**(d) Limites:** Pedaço A: inferior $= \max(t-4, 0) = 0$; superior $= \min(t-1, 1) = t - 1 < 0$. Como $0 > t - 1$, a integral é vazia. Pedaço B: inferior $= \max(t-4, 1) = 1$; superior $= \min(t-1, 2) = t-1 < 0$. Também vazia.

**(e)/(f) Resultado:**
$$y(t) = 0, \quad \text{para } t < 1$$

##### **Intervalo 2: $1 \le t < 2$ (a frente entra no pedaço A)**

**(a) Situação:** a frente está dentro do pedaço A.

**(b) Faixa:** $0 \le t - 1 < 1$; somando $1$ aos três lados: $1 \le t < 2$.

```
Esboço no eixo τ para t = 1,5 (representante do Intervalo 2):

      x(τ) 2 │                    ████
           1 │                ████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −4  −3  −2  −1   0   1   2   3   4   5   6   7
    h(t−τ) 1 │      ████████████
sobreposição │                ▓▓
                    ↑ cauda = t−4 = −2,5
                                ↑ frente = t−1 = 0,5

limites: de τ = 0 até τ = t−1 = 0,5
y(1,5) = ∫ de 0 a 0,5 de (1)(1) dτ = 0,5
```

**(c) Outra borda:** $t - 4 < 2 - 4 = -2 < 0$, a cauda está fora, à esquerda.

**(d) Limites:**
- Pedaço A: inferior $= \max(t-4, 0) = 0$; superior $= \min(t-1, 1) = t - 1$ (pois $t - 1 < 1$).
- Pedaço B: inferior $= \max(t-4, 1) = 1$; superior $= \min(t-1, 2) = t - 1 < 1$. Vazia.

**(e) Montagem:**
$$y(t) = \int_{0}^{t-1} \underbrace{x(\tau)}_{1}\cdot\underbrace{h(t-\tau)}_{1}\,d\tau = \int_{0}^{t-1} 1\,d\tau$$

**(f) Conta:** primitiva de $1$ em $\tau$ é $\tau$:
$$y(t) = \Big[\tau\Big]_{0}^{t-1}$$
$$y(t) = (t - 1) - (0)$$
$$y(t) = t - 1, \quad \text{para } 1 \le t < 2$$

**(g) Prova real ($t = 1{,}5$):** a janela cobre $\tau \in [-2{,}5;\ 0{,}5]$; a sobreposição com $x$ é $[0;\ 0{,}5]$, onde $x = 1$: área $= 1 \cdot 0{,}5 = 0{,}5$. Fórmula: $1{,}5 - 1 = 0{,}5$ ✓.

##### **Intervalo 3: $2 \le t < 3$ (a frente entra no pedaço B)**

**(a) Situação:** a janela já cobre todo o pedaço A e a frente avança dentro do pedaço B.

**(b) Faixa:** $1 \le t - 1 < 2 \iff 2 \le t < 3$.

```
Esboço no eixo τ para t = 2,5 (representante do Intervalo 3):

      x(τ) 2 │                    ████
           1 │                ████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −4  −3  −2  −1   0   1   2   3   4   5   6   7
    h(t−τ) 1 │          ████████████
sobreposição │                ▓▓▓▓▓▓
                        ↑ cauda = t−4 = −1,5
                                    ↑ frente = t−1 = 1,5

limites: A de 0 a 1;  B de 1 até t−1 = 1,5
y(2,5) = 1 + 2·0,5 = 2
```

**(c) Outra borda:** $t - 4 < 3 - 4 = -1 < 0$, a cauda está fora, à esquerda.

**(d) Limites:**
- Pedaço A: inferior $= \max(t-4, 0) = 0$; superior $= \min(t-1, 1) = 1$ (pois $t - 1 \ge 1$).
- Pedaço B: inferior $= \max(t-4, 1) = 1$; superior $= \min(t-1, 2) = t - 1$ (pois $t - 1 < 2$).

**(e) Montagem:**
$$y(t) = \int_{0}^{1} (1)(1)\,d\tau + \int_{1}^{t-1} (2)(1)\,d\tau$$

**(f) Conta:**
- Primeira integral: $\Big[\tau\Big]_{0}^{1} = 1 - 0 = 1$.
- Segunda integral: primitiva de $2$ é $2\tau$:
$$\Big[2\tau\Big]_{1}^{t-1} = 2(t-1) - 2(1) = 2t - 2 - 2 = 2t - 4$$
- Somando:
$$y(t) = 1 + (2t - 4)$$
$$y(t) = 2t - 3, \quad \text{para } 2 \le t < 3$$

**(g) Prova real ($t = 2{,}5$):** sobreposição $[0;\ 1{,}5]$: área $= 1\cdot 1 + 2 \cdot 0{,}5 = 2$. Fórmula: $2(2{,}5) - 3 = 2$ ✓.

##### **Intervalo 4: $3 \le t < 4$ ($x$ inteiro dentro da janela)**

**(a) Situação:** a frente já passou de $\tau = 2$ e a cauda ainda não chegou a $\tau = 0$.

**(b) Faixa:** $t - 1 \ge 2$ **e** $t - 4 < 0$ $\iff 3 \le t < 4$.

```
Esboço no eixo τ para t = 3,5 (representante do Intervalo 4):

      x(τ) 2 │                    ████
           1 │                ████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −4  −3  −2  −1   0   1   2   3   4   5   6   7
    h(t−τ) 1 │              ████████████
sobreposição │                ▓▓▓▓▓▓▓▓
                            ↑ cauda = t−4 = −0,5
                                        ↑ frente = t−1 = 2,5

limites: A de 0 a 1;  B de 1 a 2  (x inteiro dentro da janela)
y(3,5) = 1 + 2 = 3
```

**(c) Outra borda:** cauda $t - 4 \in [-1, 0)$, ainda à esquerda de $x$.

**(d) Limites:**
- Pedaço A: inferior $= \max(t-4, 0) = 0$; superior $= \min(t-1, 1) = 1$.
- Pedaço B: inferior $= \max(t-4, 1) = 1$; superior $= \min(t-1, 2) = 2$.

**(e) Montagem:**
$$y(t) = \int_{0}^{1} 1\,d\tau + \int_{1}^{2} 2\,d\tau$$

**(f) Conta:**
- Primeira integral: $\Big[\tau\Big]_{0}^{1} = 1 - 0 = 1$.
- Segunda integral: $\Big[2\tau\Big]_{1}^{2} = 2(2) - 2(1) = 4 - 2 = 2$.
- Somando:
$$y(t) = 1 + 2$$
$$y(t) = 3, \quad \text{para } 3 \le t < 4$$

**(g) Prova real ($t = 3{,}5$):** janela $[-0{,}5;\ 2{,}5]$ cobre todo $x$: área total de $x$ $= 1\cdot 1 + 2\cdot 1 = 3$ ✓.

##### **Intervalo 5: $4 \le t < 5$ (a cauda atravessa o pedaço A)**

**(a) Situação:** a cauda entrou no pedaço A, "soltando" parte dele.

**(b) Faixa:** $0 \le t - 4 < 1 \iff 4 \le t < 5$.

```
Esboço no eixo τ para t = 4,5 (representante do Intervalo 5):

      x(τ) 2 │                    ████
           1 │                ████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −4  −3  −2  −1   0   1   2   3   4   5   6   7
    h(t−τ) 1 │                  ████████████
sobreposição │                  ▓▓▓▓▓▓
                                ↑ cauda = t−4 = 0,5
                                            ↑ frente = t−1 = 3,5

limites: A de t−4 = 0,5 até 1;  B de 1 a 2
y(4,5) = 0,5 + 2 = 2,5
```

**(c) Outra borda:** $t - 1 \ge 3 > 2$, a frente está fora, à direita.

**(d) Limites:**
- Pedaço A: inferior $= \max(t-4, 0) = t - 4$ (pois $t - 4 \ge 0$); superior $= \min(t-1, 1) = 1$.
- Pedaço B: inferior $= \max(t-4, 1) = 1$ (pois $t - 4 < 1$); superior $= \min(t-1, 2) = 2$.

**(e) Montagem:**
$$y(t) = \int_{t-4}^{1} 1\,d\tau + \int_{1}^{2} 2\,d\tau$$

**(f) Conta:**
- Primeira integral: $\Big[\tau\Big]_{t-4}^{1} = 1 - (t - 4) = 1 - t + 4 = 5 - t$.
- Segunda integral: $\Big[2\tau\Big]_{1}^{2} = 4 - 2 = 2$.
- Somando:
$$y(t) = (5 - t) + 2$$
$$y(t) = 7 - t, \quad \text{para } 4 \le t < 5$$

**(g) Prova real ($t = 4{,}5$):** sobreposição $[0{,}5;\ 2]$: área $= 1 \cdot 0{,}5 + 2 \cdot 1 = 2{,}5$. Fórmula: $7 - 4{,}5 = 2{,}5$ ✓.

##### **Intervalo 6: $5 \le t < 6$ (a cauda atravessa o pedaço B)**

**(a) Situação:** o pedaço A saiu inteiro; a cauda está dentro do pedaço B.

**(b) Faixa:** $1 \le t - 4 < 2 \iff 5 \le t < 6$.

```
Esboço no eixo τ para t = 5,5 (representante do Intervalo 6):

      x(τ) 2 │                    ████
           1 │                ████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −4  −3  −2  −1   0   1   2   3   4   5   6   7
    h(t−τ) 1 │                      ████████████
sobreposição │                      ▓▓
                                    ↑ cauda = t−4 = 1,5
                                                ↑ frente = t−1 = 4,5

limites: B de t−4 = 1,5 até 2  (A já saiu)
y(5,5) = 2·0,5 = 1
```

**(c) Outra borda:** $t - 1 \ge 4 > 2$, a frente está fora, à direita.

**(d) Limites:**
- Pedaço A: inferior $= \max(t-4, 0) = t - 4 \ge 1$; superior $= \min(t-1, 1) = 1$. Como $t - 4 \ge 1$, a integral é vazia (comprimento $\le 0$).
- Pedaço B: inferior $= \max(t-4, 1) = t - 4$; superior $= \min(t-1, 2) = 2$.

**(e) Montagem:**
$$y(t) = \int_{t-4}^{2} 2\,d\tau$$

**(f) Conta:**
$$y(t) = \Big[2\tau\Big]_{t-4}^{2} = 2(2) - 2(t - 4)$$
$$y(t) = 4 - 2t + 8$$
$$y(t) = 12 - 2t, \quad \text{para } 5 \le t < 6$$

**(g) Prova real ($t = 5{,}5$):** sobreposição $[1{,}5;\ 2]$: área $= 2 \cdot 0{,}5 = 1$. Fórmula: $12 - 11 = 1$ ✓.

##### **Intervalo 7: $t \ge 6$ (sem sobreposição à direita)**

**(a) Situação:** a cauda passou do fim de $x$; nada mais se sobrepõe.

**(b) Faixa:** $t - 4 \ge 2 \iff t \ge 6$.

```
Esboço no eixo τ para t = 6,5 (representante do Intervalo 7):

      x(τ) 2 │                    ████
           1 │                ████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −4  −3  −2  −1   0   1   2   3   4   5   6   7
    h(t−τ) 1 │                          ████████████
sobreposição │
                                        ↑ cauda = t−4 = 2,5
                                                    ↑ frente = t−1 = 5,5

sem sobreposição: a cauda (2,5) já passou de τ = 2
y(6,5) = 0
```

**(d) Limites:** Pedaço B: inferior $= \max(t-4, 1) = t - 4 \ge 2$; superior $= 2$. Vazia. Pedaço A também vazio.
$$y(t) = 0, \quad \text{para } t \ge 6$$

---

### **Resposta Final (Questão 1.2):**
$$y(t) = \begin{cases} 0, & t < 1 \\ t - 1, & 1 \le t < 2 \\ 2t - 3, & 2 \le t < 3 \\ 3, & 3 \le t < 4 \\ 7 - t, & 4 \le t < 5 \\ 12 - 2t, & 5 \le t < 6 \\ 0, & t \ge 6 \end{cases}$$

```
Esboço de y(t) (Questão 1.2):

           3 │           ••••••
         2,5 │          •      ••
           2 │         •         ••
         1,5 │        •            •
           1 │       •              •
         0,5 │     ••                •
           0 │•••••                   •••••
           t ─┼───┼───┼───┼───┼───┼───┼───┼►
              0   1   2   3   4   5   6   7

Valores-chave: y(1) = 0;  y(2) = 1;  y(3) = 3;  y(4) = 3;  y(5) = 2;  y(6) = 0
```

**Verificações finais (prova real):**

1. **Início e fim:** início de $x$ + início de $h$ $= 0 + 1 = 1$ ✓; fim de $x$ + fim de $h$ $= 2 + 4 = 6$ ✓.

2. **Continuidade nas fronteiras** (não há impulsos, então $y$ tem de ser contínua). Avaliando os **dois** ramos vizinhos em cada fronteira:

   | Fronteira | Ramo da esquerda | Ramo da direita | Bate? |
   |:---:|:---:|:---:|:---:|
   | $t = 1$ | $0$ | $1 - 1 = 0$ | ✓ |
   | $t = 2$ | $2 - 1 = 1$ | $2(2) - 3 = 1$ | ✓ |
   | $t = 3$ | $2(3) - 3 = 3$ | $3$ | ✓ |
   | $t = 4$ | $3$ | $7 - 4 = 3$ | ✓ |
   | $t = 5$ | $7 - 5 = 2$ | $12 - 2(5) = 2$ | ✓ |
   | $t = 6$ | $12 - 2(6) = 0$ | $0$ | ✓ |

3. **Área:** deve valer $\int y\,dt = \left(\int x\,dt\right)\left(\int h\,dt\right)$.
   - $\int x\,dt = \int_0^1 1\,d\tau + \int_1^2 2\,d\tau = [\tau]_0^1 + [2\tau]_1^2 = 1 + (4 - 2) = 3$.
   - $\int h\,dt = \int_1^4 1\,dt = [t]_1^4 = 4 - 1 = 3$.
   - Esperado: $3 \cdot 3 = 9$. Calculando $\int y\,dt$ trecho a trecho:
     - $\int_1^2 (t - 1)\,dt = \left[\frac{(t-1)^2}{2}\right]_1^2 = \frac{1}{2} - 0 = 0{,}5$
     - $\int_2^3 (2t - 3)\,dt = \Big[t^2 - 3t\Big]_2^3 = (9 - 9) - (4 - 6) = 0 + 2 = 2$
     - $\int_3^4 3\,dt = \Big[3t\Big]_3^4 = 12 - 9 = 3$
     - $\int_4^5 (7 - t)\,dt = \left[7t - \frac{t^2}{2}\right]_4^5 = (35 - 12{,}5) - (28 - 8) = 22{,}5 - 20 = 2{,}5$
     - $\int_5^6 (12 - 2t)\,dt = \Big[12t - t^2\Big]_5^6 = (72 - 36) - (60 - 25) = 36 - 35 = 1$
     - Total: $0{,}5 + 2 + 3 + 2{,}5 + 1 = 9$ ✓

4. **Prova pelas rampas** (método independente). Primeiro, a convolução de dois degraus deslocados:
   $$u(t - a) * u(t - b) = \int_{-\infty}^{\infty} u(\tau - a)\,u(t - \tau - b)\,d\tau$$
   O primeiro degrau exige $\tau \ge a$ e o segundo exige $\tau \le t - b$. Para $t \ge a + b$:
   $$\int_{a}^{t-b} 1\,d\tau = (t - b) - a = t - a - b$$
   e para $t < a + b$ a integral é vazia. Logo $u(t-a) * u(t-b) = (t - a - b)\,u(t - a - b) = r(t - a - b)$, onde $r(t) = t\,u(t)$ é a rampa.

   Distribuindo $x * h = [u(t) + u(t-1) - 2u(t-2)] * [u(t-1) - u(t-4)]$ termo a termo (6 produtos):

   | Termo de $x$ | Termo de $h$ | Coeficiente | Resultado |
   |:---:|:---:|:---:|:---:|
   | $u(t)$ | $u(t-1)$ | $(1)(1) = 1$ | $r(t-1)$ |
   | $u(t)$ | $-u(t-4)$ | $(1)(-1) = -1$ | $-r(t-4)$ |
   | $u(t-1)$ | $u(t-1)$ | $(1)(1) = 1$ | $r(t-2)$ |
   | $u(t-1)$ | $-u(t-4)$ | $(1)(-1) = -1$ | $-r(t-5)$ |
   | $-2u(t-2)$ | $u(t-1)$ | $(-2)(1) = -2$ | $-2r(t-3)$ |
   | $-2u(t-2)$ | $-u(t-4)$ | $(-2)(-1) = 2$ | $+2r(t-6)$ |

   $$y(t) = r(t-1) + r(t-2) - 2r(t-3) - r(t-4) - r(t-5) + 2r(t-6)$$
   Conferindo cada intervalo (só as rampas já "ligadas" contam):
   - $1 \le t < 2$: $y = (t - 1)$ ✓
   - $2 \le t < 3$: $y = (t-1) + (t-2) = 2t - 3$ ✓
   - $3 \le t < 4$: $y = (t-1) + (t-2) - 2(t-3) = 2t - 3 - 2t + 6 = 3$ ✓
   - $4 \le t < 5$: $y = 3 - (t - 4) = 7 - t$ ✓
   - $5 \le t < 6$: $y = 7 - t - (t - 5) = 12 - 2t$ ✓
   - $t \ge 6$: $y = 12 - 2t + 2(t - 6) = 12 - 2t + 2t - 12 = 0$ ✓

> **✅ Verificação com o Gabarito da Apostila (pág. 23):**
> **100% idêntico em todos os 7 intervalos!**

---

## Questão 3.1 — [Oppenheim 2.22, pág. 141 (EN) / pág. 85 (PT)]
**Para cada um dos pares de funções a seguir, use a integral de convolução para encontrar a resposta $y(t)$ do sistema LIT com resposta ao impulso $h(t)$ para a entrada $x(t)$. Esboce seus resultados.**

---

### **Item (a):**
$$x(t) = e^{-\alpha t}u(t), \qquad h(t) = e^{-\beta t}u(t) \quad (\text{Calcule quando } \alpha \neq \beta \text{ e quando } \alpha = \beta)$$

#### **Resolução Passo a Passo:**
1. **Montagem da integral.** Substituímos $t$ por $\tau$ em $x$ e $t$ por $(t - \tau)$ em $h$:
   $$x(\tau) = e^{-\alpha\tau}u(\tau), \qquad h(t-\tau) = e^{-\beta(t-\tau)}u(t-\tau)$$
   $$y(t) = \int_{-\infty}^{\infty} e^{-\alpha\tau}u(\tau) \cdot e^{-\beta(t-\tau)}u(t-\tau)\,d\tau$$

2. **Cortes impostos pelos degraus (pedaço e janela):**
   - $u(\tau) = 1 \iff \tau \ge 0$: o sinal parado $x$ tem um único pedaço, $[0, \infty)$, com ponto de quebra $\tau = 0$.
   - $u(t-\tau) = 1 \iff t - \tau \ge 0 \iff \tau \le t$: a janela **não tem cauda** (vai de $-\infty$ até a frente $\tau = t$).
   - **Evento:** frente $= 0 \implies t = 0$. Um evento $\implies$ **2 intervalos**.
   - **Intervalo $t < 0$:** limite inferior $= \max(-\infty, 0) = 0$; superior $= \min(t, \infty) = t < 0$. Como $0 > t$, a integral é vazia: $y(t) = 0$.
   - **Intervalo $t \ge 0$:** limites de $\tau = 0$ até $\tau = t$:
     $$y(t) = \int_{0}^{t} e^{-\alpha\tau}\,e^{-\beta(t-\tau)}\,d\tau$$

```
Esboço qualitativo no eixo τ para um t > 0 (desenhado com t = 2):

      x(τ) 1 │        █
             │        ████
             │        ████████
           τ ─┼───┼───┼───┼───┼───┼───┼►
             −2  −1   0   1   2   3   4
    h(t−τ) 1 │               █
             │              ██
             │          ██████
sobreposição │        ▓▓▓▓▓▓▓▓
                              ↑ frente = t  (a janela vem de −∞ e cresce até 1 em τ = t)

x(τ) = e^(−ατ) começa em τ = 0 e decai;  h(t−τ) = e^(−β(t−τ)) só existe para τ ≤ t.
limites: de τ = 0 até τ = t   (se t < 0, a frente fica antes de 0 e y = 0)
```

3. **Separar o que depende só de $t$.** Pela propriedade $e^{A+B} = e^{A}e^{B}$:
   $$e^{-\beta(t-\tau)} = e^{-\beta t + \beta\tau} = e^{-\beta t}\,e^{\beta\tau}$$
   Como $e^{-\beta t}$ não depende da variável de integração $\tau$, sai da integral:
   $$y(t) = e^{-\beta t}\int_{0}^{t} e^{-\alpha\tau}\,e^{\beta\tau}\,d\tau$$
   Juntando os expoentes, $e^{-\alpha\tau}e^{\beta\tau} = e^{(\beta - \alpha)\tau}$:
   $$y(t) = e^{-\beta t} \int_{0}^{t} e^{(\beta - \alpha)\tau}\,d\tau, \quad t \ge 0$$

4. **Subcaso 1: $\alpha \neq \beta$ (logo $\beta - \alpha \neq 0$).**
   Primitiva: $\displaystyle\int e^{c\tau}d\tau = \frac{e^{c\tau}}{c}$ com $c = \beta - \alpha \neq 0$ (derivando, $\frac{d}{d\tau}\frac{e^{c\tau}}{c} = \frac{c\,e^{c\tau}}{c} = e^{c\tau}$ ✓):
   $$y(t) = e^{-\beta t} \left[ \frac{e^{(\beta - \alpha)\tau}}{\beta - \alpha} \right]_{\tau=0}^{\tau=t}$$
   - Limite superior ($\tau = t$): $\dfrac{e^{(\beta - \alpha)t}}{\beta - \alpha}$.
   - Limite inferior ($\tau = 0$): $\dfrac{e^{0}}{\beta - \alpha} = \dfrac{1}{\beta - \alpha}$.
   $$y(t) = e^{-\beta t} \left( \frac{e^{(\beta - \alpha)t} - 1}{\beta - \alpha} \right) = \frac{e^{-\beta t}\,e^{(\beta - \alpha)t} - e^{-\beta t}}{\beta - \alpha}$$
   Simplificando o primeiro termo do numerador: $e^{-\beta t}e^{\beta t - \alpha t} = e^{-\beta t + \beta t - \alpha t} = e^{-\alpha t}$:
   $$\mathbf{y(t) = \frac{e^{-\alpha t} - e^{-\beta t}}{\beta - \alpha} u(t)}, \quad (\alpha \neq \beta)$$

5. **Subcaso 2: $\alpha = \beta$ (logo $\beta - \alpha = 0$).**
   ⚠️ A fórmula do subcaso 1 **não pode** ser usada (dividiria por zero). Voltamos à integral do passo 3 com $\beta - \alpha = 0$: o integrando vira $e^{0\cdot\tau} = 1$, e $e^{-\beta t} = e^{-\alpha t}$:
   $$y(t) = e^{-\alpha t} \int_{0}^{t} 1\,d\tau = e^{-\alpha t} \Big[\tau\Big]_{0}^{t} = e^{-\alpha t}\,(t - 0)$$
   $$\mathbf{y(t) = t\, e^{-\alpha t} u(t)}, \quad (\alpha = \beta)$$

6. **Provas reais:**
   - **Continuidade em $t = 0$:** subcaso 1: $\frac{e^0 - e^0}{\beta - \alpha} = \frac{1 - 1}{\beta - \alpha} = 0$ ✓; subcaso 2: $0 \cdot e^0 = 0$ ✓ (o ramo $t < 0$ também é $0$).
   - **Área** (supondo $\alpha, \beta > 0$, para que as integrais convirjam): $\int x = \int_0^\infty e^{-\alpha t}dt = \left[\frac{e^{-\alpha t}}{-\alpha}\right]_0^\infty = 0 - \left(\frac{1}{-\alpha}\right) = \frac{1}{\alpha}$; analogamente $\int h = \frac{1}{\beta}$. Esperado: $\frac{1}{\alpha\beta}$.
     - Subcaso 1: $\int_0^\infty \frac{e^{-\alpha t} - e^{-\beta t}}{\beta - \alpha}dt = \frac{1}{\beta - \alpha}\left(\frac{1}{\alpha} - \frac{1}{\beta}\right) = \frac{1}{\beta - \alpha}\cdot\frac{\beta - \alpha}{\alpha\beta} = \frac{1}{\alpha\beta}$ ✓
     - Subcaso 2: por partes, com $f = t$, $dg = e^{-\alpha t}dt$, $g = -\frac{e^{-\alpha t}}{\alpha}$: $\int_0^\infty t e^{-\alpha t}dt = \left[-\frac{t e^{-\alpha t}}{\alpha}\right]_0^\infty + \frac{1}{\alpha}\int_0^\infty e^{-\alpha t}dt = (0 - 0) + \frac{1}{\alpha}\cdot\frac{1}{\alpha} = \frac{1}{\alpha^2}$ ✓ (é $\frac{1}{\alpha\beta}$ com $\beta = \alpha$).

```
Esboço de y(t) (desenhado com α = 1, β = 2; para α = β o formato é o mesmo):

        pico │      •••
      0,1875 │     •   ••
       0,125 │    •      ••
      0,0625 │             •••••
           0 │••••              •••••••••••
           t ─┼───┼───┼───┼───┼───┼───┼───┼►
             −1   0   1   2   3   4   5   6

y(t) = 0 para t < 0;  y(0) = 0;  sobe até um pico e decai a 0 quando t → ∞ (nunca fica negativa).
```

---

### **Item (b):**
$$x(t) = u(t) - 2u(t-2) + u(t-5), \qquad h(t) = e^{2t}u(1-t)$$

#### **Resolução Passo a Passo:**

#### **Passo 1: Sinal parado $x(\tau)$ e seus pedaços**
Percorrendo o eixo $\tau$ e somando os degraus que ligam:
- $\tau < 0$: $x = 0$.
- $0 \le \tau < 2$: só $u(\tau)$ $\implies x = 1$.
- $2 \le \tau < 5$: $u(\tau) - 2u(\tau - 2) \implies x = 1 - 2 = -1$.
- $\tau \ge 5$: $1 - 2 + 1 = 0$.

$$x(\tau) = \begin{cases} +1, & 0 \le \tau < 2 \quad \text{(pedaço A)} \\ -1, & 2 \le \tau < 5 \quad \text{(pedaço B)} \\ 0, & \text{caso contrário} \end{cases}$$
**Pontos de quebra:** $\tau = 0$, $\tau = 2$ e $\tau = 5$.

#### **Passo 2: A janela $h(t-\tau)$**
Substituímos $t$ por $(t-\tau)$ em $h(t) = e^{2t}u(1-t)$:
$$h(t-\tau) = e^{2(t-\tau)}\,u\big(1 - (t - \tau)\big) = e^{2(t-\tau)}\,u(1 - t + \tau)$$
O degrau vale $1$ quando:
$$1 - t + \tau \ge 0 \iff \tau \ge t - 1$$
Logo a janela começa na **cauda** $\tau = t - 1$ e se estende até $\tau \to +\infty$ (**não tem frente**, porque $h$ vai até $-\infty$ no seu eixo original). Dentro da janela, a fórmula é $e^{2(t-\tau)}$, que vale $e^{2(t-(t-1))} = e^{2}$ na cauda e decai conforme $\tau$ cresce.

**Primitiva que será usada em todos os intervalos** (em $\tau$, com $t$ constante):
$$\int e^{2(t-\tau)}\,d\tau = -\frac{1}{2}e^{2(t-\tau)}$$
*Conferindo pela derivada:* $\frac{d}{d\tau}\left[-\frac{1}{2}e^{2(t-\tau)}\right] = -\frac{1}{2}\cdot e^{2(t-\tau)}\cdot\frac{d}{d\tau}[2(t-\tau)] = -\frac{1}{2}\cdot e^{2(t-\tau)}\cdot(-2) = e^{2(t-\tau)}$ ✓

#### **Passo 3: Tabela de eventos**
Só a cauda existe, então só ela gera eventos:

| Borda | Ponto de quebra | Equação | $t$ | O que acontece |
|:---:|:---:|:---:|:---:|:---|
| cauda | $\tau = 0$ | $t - 1 = 0$ | $1$ | a cauda entra no pedaço A |
| cauda | $\tau = 2$ | $t - 1 = 2$ | $3$ | a cauda entra no pedaço B (A saiu todo) |
| cauda | $\tau = 5$ | $t - 1 = 5$ | $6$ | a cauda passa do fim de $x$ |

3 eventos $\implies$ **4 intervalos**.

#### **Passo 4: Os 4 intervalos**

##### **Intervalo 1: $t < 1$ (a janela cobre $x$ inteiro)**

**(a) Situação:** a cauda $t - 1$ está à esquerda de $\tau = 0$; como a janela vai até $+\infty$, ela cobre os pedaços A e B inteiros.

**(b) Faixa:** $t - 1 < 0 \iff t < 1$.

```
Esboço no eixo τ para t = 0 (representante do Intervalo 1):

     x(τ) +1 │        ████████
           0 │·········································
          −1 │                ████████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −2  −1   0   1   2   3   4   5   6   7   8
   h(t−τ) e² │    █
             │    ██
             │    ███████
sobreposição │        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                  ↑ cauda = t−1 = −1  (valor e² aqui; a janela segue até +∞ →, decaindo)

limites: A de 0 a 2;  B de 2 a 5  (a janela cobre x inteiro)
```

**(d) Limites:**
- Pedaço A: inferior $= \max(t-1, 0) = 0$; superior $= \min(+\infty, 2) = 2$.
- Pedaço B: inferior $= \max(t-1, 2) = 2$; superior $= \min(+\infty, 5) = 5$.

**(e) Montagem:**
$$y(t) = \int_{0}^{2} (+1)\,e^{2(t-\tau)}\,d\tau + \int_{2}^{5} (-1)\,e^{2(t-\tau)}\,d\tau$$

**(f) Conta:**
- Primeira integral:
  $$\left[-\frac{1}{2}e^{2(t-\tau)}\right]_{0}^{2}$$
  - Limite superior ($\tau = 2$): $-\frac{1}{2}e^{2(t-2)}$
  - Limite inferior ($\tau = 0$): $-\frac{1}{2}e^{2(t-0)} = -\frac{1}{2}e^{2t}$
  - Superior menos inferior: $-\frac{1}{2}e^{2(t-2)} - \left(-\frac{1}{2}e^{2t}\right) = \frac{1}{2}e^{2t} - \frac{1}{2}e^{2(t-2)}$
- Segunda integral (com o sinal $-1$ na frente):
  $$-\left[-\frac{1}{2}e^{2(t-\tau)}\right]_{2}^{5}$$
  - Limite superior ($\tau = 5$): $-\frac{1}{2}e^{2(t-5)}$
  - Limite inferior ($\tau = 2$): $-\frac{1}{2}e^{2(t-2)}$
  - Superior menos inferior: $-\frac{1}{2}e^{2(t-5)} + \frac{1}{2}e^{2(t-2)}$
  - Com o sinal $-1$: $\frac{1}{2}e^{2(t-5)} - \frac{1}{2}e^{2(t-2)}$
- Somando:
  $$y(t) = \frac{1}{2}e^{2t} - \frac{1}{2}e^{2(t-2)} + \frac{1}{2}e^{2(t-5)} - \frac{1}{2}e^{2(t-2)}$$
  $$y(t) = \frac{1}{2}\left(e^{2t} - 2e^{2(t-2)} + e^{2(t-5)}\right), \quad \text{para } t < 1$$

**(g) Prova real ($t = 0$):** $\frac{1}{2}(1 - 2e^{-4} + e^{-10}) \approx \frac{1}{2}(1 - 0{,}036631 + 0{,}000045) \approx 0{,}481707$. Integração numérica direta de $\int x(\tau)e^{2(0-\tau)}d\tau$: $0{,}48171$ ✓.

##### **Intervalo 2: $1 \le t < 3$ (a cauda atravessa o pedaço A)**

**(a) Situação:** a cauda está dentro do pedaço A; parte de A já ficou para trás.

**(b) Faixa:** $0 \le t - 1 < 2 \iff 1 \le t < 3$.

```
Esboço no eixo τ para t = 2 (representante do Intervalo 2):

     x(τ) +1 │        ████████
           0 │·········································
          −1 │                ████████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −2  −1   0   1   2   3   4   5   6   7   8
   h(t−τ) e² │            █
             │            ██
             │            ███████
sobreposição │            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                          ↑ cauda = t−1 = 1  (valor e² aqui; a janela segue até +∞ →, decaindo)

limites: A de t−1 = 1 até 2;  B de 2 a 5
```

**(d) Limites:**
- Pedaço A: inferior $= \max(t-1, 0) = t - 1$ (pois $t - 1 \ge 0$); superior $= 2$.
- Pedaço B: inferior $= \max(t-1, 2) = 2$ (pois $t - 1 < 2$); superior $= 5$.

**(e) Montagem:**
$$y(t) = \int_{t-1}^{2} (+1)\,e^{2(t-\tau)}\,d\tau + \int_{2}^{5} (-1)\,e^{2(t-\tau)}\,d\tau$$

**(f) Conta:**
- Primeira integral: $\left[-\frac{1}{2}e^{2(t-\tau)}\right]_{t-1}^{2}$
  - Limite superior ($\tau = 2$): $-\frac{1}{2}e^{2(t-2)}$
  - Limite inferior ($\tau = t - 1$): o expoente fica $2\big(t - (t - 1)\big) = 2(t - t + 1) = 2(1) = 2$, logo $-\frac{1}{2}e^{2}$
  - Superior menos inferior: $-\frac{1}{2}e^{2(t-2)} + \frac{1}{2}e^{2}$
- Segunda integral: **idêntica** à do Intervalo 1 (mesmos limites $2$ e $5$): $\frac{1}{2}e^{2(t-5)} - \frac{1}{2}e^{2(t-2)}$
- Somando:
  $$y(t) = \frac{1}{2}e^{2} - \frac{1}{2}e^{2(t-2)} + \frac{1}{2}e^{2(t-5)} - \frac{1}{2}e^{2(t-2)}$$
  $$y(t) = \frac{1}{2}\left(e^{2} - 2e^{2(t-2)} + e^{2(t-5)}\right), \quad \text{para } 1 \le t < 3$$

**(g) Prova real ($t = 2$):** $\frac{1}{2}(e^2 - 2e^0 + e^{-6}) = \frac{1}{2}(7{,}389056 - 2 + 0{,}002479) \approx 2{,}695768$. Numérico direto: $2{,}6958$ ✓.

##### **Intervalo 3: $3 \le t < 6$ (a cauda atravessa o pedaço B)**

**(a) Situação:** o pedaço A ficou inteiro para trás; a cauda está dentro do pedaço B.

**(b) Faixa:** $2 \le t - 1 < 5 \iff 3 \le t < 6$.

```
Esboço no eixo τ para t = 4 (representante do Intervalo 3):

     x(τ) +1 │        ████████
           0 │·········································
          −1 │                ████████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −2  −1   0   1   2   3   4   5   6   7   8
   h(t−τ) e² │                    █
             │                    ██
             │                    ███████
sobreposição │                    ▓▓▓▓▓▓▓▓
                                  ↑ cauda = t−1 = 3  (valor e² aqui; a janela segue até +∞ →, decaindo)

limites: só B, de t−1 = 3 até 5  (A ficou para trás)
```

**(d) Limites:**
- Pedaço A: inferior $= \max(t-1, 0) = t - 1 \ge 2$; superior $= 2$. Vazia (comprimento $2 - (t-1) \le 0$).
- Pedaço B: inferior $= \max(t-1, 2) = t - 1$; superior $= 5$.

**(e) Montagem:**
$$y(t) = \int_{t-1}^{5} (-1)\,e^{2(t-\tau)}\,d\tau$$

**(f) Conta:**
$$y(t) = -\left[-\frac{1}{2}e^{2(t-\tau)}\right]_{t-1}^{5}$$
- Limite superior ($\tau = 5$): $-\frac{1}{2}e^{2(t-5)}$
- Limite inferior ($\tau = t-1$): $-\frac{1}{2}e^{2}$ (mesma conta do Intervalo 2)
- Superior menos inferior: $-\frac{1}{2}e^{2(t-5)} + \frac{1}{2}e^{2}$
- Multiplicando pelo $-1$ da frente:
  $$y(t) = \frac{1}{2}e^{2(t-5)} - \frac{1}{2}e^{2}$$
  $$y(t) = \frac{1}{2}\left(e^{2(t-5)} - e^{2}\right), \quad \text{para } 3 \le t < 6$$

**(g) Prova real ($t = 4$):** $\frac{1}{2}(e^{-2} - e^{2}) = \frac{1}{2}(0{,}135335 - 7{,}389056) \approx -3{,}626860$. Numérico direto: $-3{,}6269$ ✓.

##### **Intervalo 4: $t \ge 6$ (sem sobreposição)**

**(a) Situação:** a cauda passou de $\tau = 5$; não sobra nada de $x$ dentro da janela.

**(b) Faixa:** $t - 1 \ge 5 \iff t \ge 6$.

```
Esboço no eixo τ para t = 7 (representante do Intervalo 4):

     x(τ) +1 │        ████████
           0 │·········································
          −1 │                ████████████
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −2  −1   0   1   2   3   4   5   6   7   8
   h(t−τ) e² │                                █
             │                                ██
             │                                ███████
sobreposição │
                                              ↑ cauda = t−1 = 6  (valor e² aqui; a janela segue até +∞ →, decaindo)

sem sobreposição: a cauda (6) passou de τ = 5
```

**(d) Limites:** Pedaço B: inferior $= t - 1 \ge 5$, superior $= 5$. Vazia. A também.
$$y(t) = 0, \quad \text{para } t \ge 6$$

#### **Resposta Final do Item 3.1 (b):**
$$y(t) = \begin{cases} \dfrac{1}{2}\left(e^{2t} - 2e^{2(t-2)} + e^{2(t-5)}\right), & t < 1 \\[0.8em] \dfrac{1}{2}\left(e^{2} - 2e^{2(t-2)} + e^{2(t-5)}\right), & 1 \le t < 3 \\[0.8em] \dfrac{1}{2}\left(e^{2(t-5)} - e^{2}\right), & 3 \le t < 6 \\[0.8em] 0, & t \ge 6 \end{cases}$$

```
Esboço de y(t) (item b):

        3,75 │            ••
           3 │           •  ••
        2,25 │                •
         1,5 │          •      •
        0,75 │       •••
           0 │•••••••           •             •••••
       −0,75 │                               •
        −1,5 │
       −2,25 │                   •          •
          −3 │                           •••
       −3,75 │                    •••••••
           t ─┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −2  −1   0   1   2   3   4   5   6   7

Valores-chave: y → 0 quando t → −∞;  y(1) ≈ 3,559;  y(2) ≈ 2,696;  y(3) ≈ −3,685;  y(6) = 0
```

**Verificações finais:**

1. **Continuidade nas fronteiras** (avaliando os dois ramos):
   - $t = 1$: ramo 1 $= \frac{1}{2}(e^{2} - 2e^{-2} + e^{-8})$; ramo 2 $= \frac{1}{2}(e^{2} - 2e^{2(1-2)} + e^{2(1-5)}) = \frac{1}{2}(e^{2} - 2e^{-2} + e^{-8})$. Iguais ($\approx 3{,}559361$) ✓
   - $t = 3$: ramo 2 $= \frac{1}{2}(e^2 - 2e^{2} + e^{-4}) = \frac{1}{2}(e^{-4} - e^{2})$; ramo 3 $= \frac{1}{2}(e^{2(3-5)} - e^2) = \frac{1}{2}(e^{-4} - e^{2})$. Iguais ($\approx -3{,}685370$) ✓
   - $t = 6$: ramo 3 $= \frac{1}{2}(e^{2(6-5)} - e^{2}) = \frac{1}{2}(e^{2} - e^{2}) = 0$; ramo 4 $= 0$ ✓
   - Quando $t \to -\infty$: os três termos do ramo 1 vão a $0$ ✓ (a saída começa "do nada", como deve).

2. **Área:** $\int y = \left(\int x\right)\left(\int h\right)$.
   - $\int x = \int_0^2 1\,d\tau + \int_2^5 (-1)\,d\tau = 2 + (-3) = -1$.
   - $\int h = \int_{-\infty}^{1} e^{2t}dt = \left[\frac{e^{2t}}{2}\right]_{-\infty}^{1} = \frac{e^{2}}{2} - \lim_{t\to-\infty}\frac{e^{2t}}{2} = \frac{e^2}{2} - 0 = \frac{e^2}{2}$.
   - Esperado: $(-1)\cdot\frac{e^2}{2} = -\frac{e^2}{2}$. Calculando $\int y$:
     - $\int_{-\infty}^{1}$ do ramo 1: $\frac{1}{2}\left[\frac{e^{2t}}{2} - e^{2(t-2)} + \frac{e^{2(t-5)}}{2}\right]_{-\infty}^{1} = \frac{1}{2}\left(\frac{e^{2}}{2} - e^{-2} + \frac{e^{-8}}{2}\right) = \frac{e^2}{4} - \frac{e^{-2}}{2} + \frac{e^{-8}}{4}$
     - $\int_{1}^{3}$ do ramo 2: $\frac{1}{2}\left[e^{2}t - e^{2(t-2)} + \frac{e^{2(t-5)}}{2}\right]_{1}^{3} = \frac{1}{2}\left[(3e^2 - e^{2} + \tfrac{e^{-4}}{2}) - (e^2 - e^{-2} + \tfrac{e^{-8}}{2})\right] = \frac{e^2}{2} + \frac{e^{-2}}{2} + \frac{e^{-4}}{4} - \frac{e^{-8}}{4}$
     - $\int_{3}^{6}$ do ramo 3: $\frac{1}{2}\left[\frac{e^{2(t-5)}}{2} - e^{2}t\right]_{3}^{6} = \frac{1}{2}\left[(\tfrac{e^{2}}{2} - 6e^2) - (\tfrac{e^{-4}}{2} - 3e^2)\right] = \frac{e^2}{4} - \frac{3e^2}{2} - \frac{e^{-4}}{4}$
     - Somando por tipo de termo: $e^2\left(\frac{1}{4} + \frac{1}{2} + \frac{1}{4} - \frac{3}{2}\right) = -\frac{e^2}{2}$; $e^{-2}\left(-\frac{1}{2} + \frac{1}{2}\right) = 0$; $e^{-4}\left(\frac{1}{4} - \frac{1}{4}\right) = 0$; $e^{-8}\left(\frac{1}{4} - \frac{1}{4}\right) = 0$.
     - Total: $-\frac{e^2}{2} \approx -3{,}6945$ ✓

---

### **Item (c): $x(t)$ e $h(t)$ como mostrados na Figura P2.22(a)**
Da Figura P2.22(a) do livro:
- $x(t)$ é um único ciclo de $\text{sen}(\pi t)$ entre $t = 0$ e $t = 2$:
  $$x(t) = \begin{cases} \text{sen}(\pi t), & 0 \le t \le 2 \\ 0, & \text{caso contrário} \end{cases}$$
- $h(t)$ é um pulso retangular de amplitude $2$ entre $t = 1$ e $t = 3$:
  $$h(t) = 2\big[u(t-1) - u(t-3)\big]$$

#### **Resolução Passo a Passo:**

#### **Passo 1: Sinal parado e pedaços**
$x(\tau) = \text{sen}(\pi\tau)$ em $[0, 2]$: **um único pedaço** (uma só fórmula). Pontos de quebra: $\tau = 0$ e $\tau = 2$.

#### **Passo 2: A janela $h(t - \tau)$**
$h$ é não nulo para $1 \le t \le 3$ ($a = 1$, $b = 3$). Trocando o argumento:
$$1 \le t - \tau \le 3 \iff -3 \le \tau - t \le -1 \iff t - 3 \le \tau \le t - 1$$
Janela de altura $2$ e largura $2$: **cauda** $= t - 3$, **frente** $= t - 1$.

**Primitiva usada em todos os intervalos:**
$$\int 2\,\text{sen}(\pi\tau)\,d\tau = -\frac{2}{\pi}\cos(\pi\tau)$$
*Conferindo:* $\frac{d}{d\tau}\left[-\frac{2}{\pi}\cos(\pi\tau)\right] = -\frac{2}{\pi}\cdot(-\text{sen}(\pi\tau))\cdot\pi = 2\,\text{sen}(\pi\tau)$ ✓

#### **Passo 3: Tabela de eventos**

| Borda | Ponto de quebra | Equação | $t$ | O que acontece |
|:---:|:---:|:---:|:---:|:---|
| frente | $\tau = 0$ | $t - 1 = 0$ | $1$ | começa a sobreposição |
| frente | $\tau = 2$ | $t - 1 = 2$ | $3$ | a frente passa do fim de $x$ |
| cauda | $\tau = 0$ | $t - 3 = 0$ | $3$ | a cauda começa a soltar $x$ |
| cauda | $\tau = 2$ | $t - 3 = 2$ | $5$ | fim da sobreposição |

**Por que não existe intervalo "do meio"?** A janela tem largura $2$ e $x$ também tem largura $2$. Por isso, os eventos "frente sai de $x$" e "cauda entra em $x$" **coincidem** em $t = 3$: no exato instante em que a janela cobre $x$ inteiro, ela já começa a soltá-lo. Eventos coincidentes se fundem $\implies$ 3 eventos distintos ($t = 1, 3, 5$) $\implies$ **4 intervalos**. (É o caso "triângulo" do macete do trapézio: larguras iguais, patamar de largura zero.)

#### **Passo 4: Os 4 intervalos**

##### **Intervalo 1: $t < 1$**

**(a) Situação:** a janela inteira está à esquerda de $x$.

**(b) Faixa:** $t - 1 < 0 \iff t < 1$.

```
Esboço no eixo τ para t = 0 (representante do Intervalo 1):

     x(τ) +1 │             ██
       +0,35 │            ████
           0 │·································
       −0,35 │                ████
          −1 │                 ██
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −3  −2  −1   0   1   2   3   4   5
    h(t−τ) 2 │████████
sobreposição │
              ↑ cauda = t−3 = −3
                      ↑ frente = t−1 = −1

sem sobreposição: a frente (−1) não chegou em τ = 0
```

**(d) Limites:** inferior $= \max(t-3, 0) = 0$; superior $= \min(t-1, 2) = t - 1 < 0$. Como $0 > t - 1$, a integral é vazia.
$$y(t) = 0, \quad \text{para } t < 1$$

##### **Intervalo 2: $1 \le t < 3$ (a frente atravessa $x$)**

**(a) Situação:** a frente está dentro de $[0, 2]$; a cauda está à esquerda de $0$.

**(b) Faixa:** $0 \le t - 1 < 2 \iff 1 \le t < 3$.

```
Esboço no eixo τ para t = 2 (representante do Intervalo 2):

     x(τ) +1 │             ██
       +0,35 │            ████
           0 │·································
       −0,35 │                ████
          −1 │                 ██
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −3  −2  −1   0   1   2   3   4   5
    h(t−τ) 2 │        ████████
sobreposição │            ▓▓▓▓
                      ↑ cauda = t−3 = −1
                              ↑ frente = t−1 = 1

limites: de 0 até t−1 = 1  (só o arco positivo entra)
```

**(c) Outra borda:** $t - 3 < 0$, fora à esquerda.

**(d) Limites:** inferior $= \max(t-3, 0) = 0$; superior $= \min(t-1, 2) = t - 1$.

**(e) Montagem:**
$$y(t) = \int_{0}^{t-1} \text{sen}(\pi\tau)\cdot 2\,d\tau$$

**(f) Conta:**
$$y(t) = \left[-\frac{2}{\pi}\cos(\pi\tau)\right]_{0}^{t-1}$$
- Limite superior ($\tau = t - 1$): $-\frac{2}{\pi}\cos\big(\pi(t-1)\big)$
- Limite inferior ($\tau = 0$): $-\frac{2}{\pi}\cos(0) = -\frac{2}{\pi}\cdot 1 = -\frac{2}{\pi}$
- Superior menos inferior:
$$y(t) = -\frac{2}{\pi}\cos\big(\pi(t-1)\big) + \frac{2}{\pi} = \frac{2}{\pi}\Big[1 - \cos(\pi t - \pi)\Big]$$
**Identidade** (cosseno da diferença), com $\cos\pi = -1$ e $\text{sen}\,\pi = 0$:
$$\cos(\pi t - \pi) = \cos(\pi t)\cos(\pi) + \text{sen}(\pi t)\,\text{sen}(\pi) = \cos(\pi t)\cdot(-1) + \text{sen}(\pi t)\cdot 0 = -\cos(\pi t)$$
Substituindo:
$$y(t) = \frac{2}{\pi}\Big[1 - (-\cos(\pi t))\Big]$$
$$y(t) = \frac{2}{\pi}\big[1 + \cos(\pi t)\big], \quad \text{para } 1 \le t < 3$$

**(g) Prova real ($t = 2$, integral direta):** em $t = 2$ a janela é $[-1, 1]$, que pega de $x$ só o trecho $[0, 1]$:
$$y(2) = \int_0^1 2\,\text{sen}(\pi\tau)\,d\tau = \left[-\frac{2}{\pi}\cos(\pi\tau)\right]_0^1 = -\frac{2}{\pi}\cos(\pi) - \left(-\frac{2}{\pi}\cos 0\right) = -\frac{2}{\pi}(-1) + \frac{2}{\pi}(1) = \frac{4}{\pi}$$
Pela fórmula: $\frac{2}{\pi}[1 + \cos(2\pi)] = \frac{2}{\pi}[1 + 1] = \frac{4}{\pi} \approx 1{,}2732$ ✓ (é o máximo de $y$).

##### **Intervalo 3: $3 \le t < 5$ (a cauda atravessa $x$)**

**(a) Situação:** a frente já saiu à direita de $\tau = 2$; a cauda está dentro de $[0, 2]$.

**(b) Faixa:** $0 \le t - 3 < 2 \iff 3 \le t < 5$.

```
Esboço no eixo τ para t = 4 (representante do Intervalo 3):

     x(τ) +1 │             ██
       +0,35 │            ████
           0 │·································
       −0,35 │                ████
          −1 │                 ██
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −3  −2  −1   0   1   2   3   4   5
    h(t−τ) 2 │                ████████
sobreposição │                ▓▓▓▓
                              ↑ cauda = t−3 = 1
                                      ↑ frente = t−1 = 3

limites: de t−3 = 1 até 2  (só o arco negativo entra)
```

**(c) Outra borda:** $t - 1 \ge 2$, fora à direita.

**(d) Limites:** inferior $= \max(t-3, 0) = t - 3$; superior $= \min(t-1, 2) = 2$.

**(e) Montagem:**
$$y(t) = \int_{t-3}^{2} 2\,\text{sen}(\pi\tau)\,d\tau$$

**(f) Conta:**
$$y(t) = \left[-\frac{2}{\pi}\cos(\pi\tau)\right]_{t-3}^{2}$$
- Limite superior ($\tau = 2$): $-\frac{2}{\pi}\cos(2\pi) = -\frac{2}{\pi}\cdot 1 = -\frac{2}{\pi}$
- Limite inferior ($\tau = t - 3$): $-\frac{2}{\pi}\cos\big(\pi(t - 3)\big)$
- Superior menos inferior:
$$y(t) = -\frac{2}{\pi} + \frac{2}{\pi}\cos(\pi t - 3\pi)$$
**Identidade**, com $\cos(3\pi) = -1$ e $\text{sen}(3\pi) = 0$:
$$\cos(\pi t - 3\pi) = \cos(\pi t)\cos(3\pi) + \text{sen}(\pi t)\,\text{sen}(3\pi) = \cos(\pi t)\cdot(-1) + \text{sen}(\pi t)\cdot 0 = -\cos(\pi t)$$
Substituindo:
$$y(t) = -\frac{2}{\pi} + \frac{2}{\pi}\big(-\cos(\pi t)\big) = -\frac{2}{\pi} - \frac{2}{\pi}\cos(\pi t)$$
$$y(t) = -\frac{2}{\pi}\big[1 + \cos(\pi t)\big], \quad \text{para } 3 \le t < 5$$

**(g) Prova real ($t = 4$):** janela $[1, 3]$ pega de $x$ o trecho $[1, 2]$: $\int_1^2 2\,\text{sen}(\pi\tau)d\tau = -\frac{2}{\pi}\cos(2\pi) + \frac{2}{\pi}\cos(\pi) = -\frac{2}{\pi} - \frac{2}{\pi} = -\frac{4}{\pi}$. Fórmula: $-\frac{2}{\pi}[1 + \cos 4\pi] = -\frac{2}{\pi}(2) = -\frac{4}{\pi}$ ✓.

##### **Intervalo 4: $t \ge 5$**

**(a) Situação:** a cauda passou do fim de $x$; a janela inteira está à direita.

**(b) Faixa:** $t - 3 \ge 2 \iff t \ge 5$.

```
Esboço no eixo τ para t = 5,5 (representante do Intervalo 4):

     x(τ) +1 │             ██
       +0,35 │            ████
           0 │·································
       −0,35 │                ████
          −1 │                 ██
           τ ─┼───┼───┼───┼───┼───┼───┼───┼───┼►
             −3  −2  −1   0   1   2   3   4   5
    h(t−τ) 2 │                      ████████
sobreposição │
                                    ↑ cauda = t−3 = 2,5
                                            ↑ frente = t−1 = 4,5

sem sobreposição: a cauda (2,5) passou de τ = 2
```

**(d) Limites:** inferior $= \max(t-3, 0) = t - 3 \ge 2$; superior $= \min(t-1, 2) = 2$. Como $t - 3 \ge 2$, a integral é vazia.
$$y(t) = 0, \quad \text{para } t \ge 5$$

#### **Resposta Final do Item 3.1 (c):**
$$y(t) = \begin{cases} 0, & t < 1 \\[0.5em] \dfrac{2}{\pi}\big[1 + \cos(\pi t)\big], & 1 \le t < 3 \\[0.8em] -\dfrac{2}{\pi}\big[1 + \cos(\pi t)\big], & 3 \le t < 5 \\[0.5em] 0, & t \ge 5 \end{cases}$$

```
Esboço de y(t) (item c):

         4/π │       ••
         0,9 │      •  •
         0,6 │
         0,3 │     •    •
           0 │•••••      ••      ••••••
        −0,3 │             •    •
        −0,6 │
        −0,9 │              •  •
        −4/π │               ••
           t ─┼───┼───┼───┼───┼───┼───┼►
              0   1   2   3   4   5   6

Valores-chave: y(1) = 0;  y(2) = 4/π ≈ 1,273 (máximo);  y(3) = 0;  y(4) = −4/π (mínimo);  y(5) = 0
```

**Verificações finais:**
1. **Continuidade** (os dois ramos em cada fronteira; usamos $\cos\pi = \cos 3\pi = \cos 5\pi = -1$):
   - $t = 1$: esquerda $0$; direita $\frac{2}{\pi}[1 + \cos\pi] = \frac{2}{\pi}[1 - 1] = 0$ ✓
   - $t = 3$: esquerda $\frac{2}{\pi}[1 + \cos 3\pi] = \frac{2}{\pi}\cdot 0 = 0$; direita $-\frac{2}{\pi}[1 + \cos 3\pi] = 0$ ✓
   - $t = 5$: esquerda $-\frac{2}{\pi}[1 + \cos 5\pi] = 0$; direita $0$ ✓
2. **Início e fim:** $0 + 1 = 1$ e $2 + 3 = 5$ ✓.
3. **Área** (calculada, não "deduzida"):
   - $\int x = \int_0^2 \text{sen}(\pi\tau)d\tau = \left[-\frac{\cos(\pi\tau)}{\pi}\right]_0^2 = -\frac{\cos 2\pi}{\pi} + \frac{\cos 0}{\pi} = -\frac{1}{\pi} + \frac{1}{\pi} = 0$.
   - $\int h = 2 \cdot (3 - 1) = 4$. Esperado: $\int y = 0 \cdot 4 = 0$.
   - $\int_1^3 \frac{2}{\pi}[1 + \cos(\pi t)]dt = \frac{2}{\pi}\left[t + \frac{\text{sen}(\pi t)}{\pi}\right]_1^3 = \frac{2}{\pi}\left[\left(3 + \frac{\text{sen}\,3\pi}{\pi}\right) - \left(1 + \frac{\text{sen}\,\pi}{\pi}\right)\right] = \frac{2}{\pi}[(3 + 0) - (1 + 0)] = \frac{4}{\pi}$
   - $\int_3^5 -\frac{2}{\pi}[1 + \cos(\pi t)]dt = -\frac{2}{\pi}\left[t + \frac{\text{sen}(\pi t)}{\pi}\right]_3^5 = -\frac{2}{\pi}[(5 + 0) - (3 + 0)] = -\frac{4}{\pi}$
   - Total: $\frac{4}{\pi} - \frac{4}{\pi} = 0$ ✓

---

### **Item (d): $x(t)$ e $h(t)$ como mostrados na Figura P2.22(b)**
Lendo atentamente a Figura P2.22(b) do Oppenheim (pág. 85 PT / pág. 141 EN):
- $x(t)$ é uma reta infinita com inclinação $a$ e intercepto vertical $b$:
  $$x(t) = a t + b, \quad -\infty < t < \infty$$
- $h(t)$ é composto por um pulso retangular de altura $\frac{4}{3}$ entre $t = 0$ e $t = 1$, **mais um impulso de área (peso) $-\frac{1}{3}$ localizado em $t = 2$** (indicado pela seta vertical para baixo em $t=2$ com rótulo $-\frac{1}{3}$):
  $$h(t) = \frac{4}{3}\big[u(t) - u(t-1)\big] - \frac{1}{3}\delta(t-2)$$

#### **Resolução Passo a Passo:**

#### **Passo 1: Escolher quem desliza**
Aqui $x(t)$ existe em **todo** o eixo (não tem pedaços nem pontos de quebra), enquanto $h$ é curto. Pela comutatividade, deixamos $h$ **parado** e deslizamos $x$:
$$y(t) = \int_{-\infty}^{\infty} h(\tau)\,x(t-\tau)\,d\tau$$
Substituindo o argumento de $x$ por $(t - \tau)$:
$$x(t - \tau) = a(t - \tau) + b = at + b - a\tau$$
Como $x$ não tem bordas, **não há eventos**: uma única fórmula vale para todo $t$.

```
Esboço de h(τ) (sinal parado) — pulso de altura 4/3 em [0, 1) e impulso de peso −1/3 em τ = 2:

    h(τ) 4/3 │            ██████
           0 │·····································
        −1/3 │                        ↓  impulso −(1/3)δ(τ−2)
           τ ─┼─────┼─────┼─────┼─────┼─────┼─────┼►
             −2    −1     0     1     2     3     4

Esboço de x(t) = at + b (desenhado com a = 1/2 e b = 1; reta infinita, sem bordas):

           3 │                                 ••••
         2,5 │                           ••••••
           2 │                     ••••••
         1,5 │               ••••••
       b = 1 │         ••••••
         0,5 │   ••••••
           0 │•••
           t ─┼─────┼─────┼─────┼─────┼─────┼─────┼►
             −2    −1     0     1     2     3     4

Como x(t−τ) não tem bordas, não há eventos: uma única conta vale para todo t.
I1 usa o pulso (τ de 0 a 1); I2 usa só o valor de x(t−τ) em τ = 2.
```

#### **Passo 2: Separar pela distributiva (pulso + impulso)**
$$y(t) = \underbrace{\int_{-\infty}^{\infty} \frac{4}{3}\big[u(\tau) - u(\tau-1)\big]\,x(t-\tau)\,d\tau}_{I_1} + \underbrace{\int_{-\infty}^{\infty} \left(-\frac{1}{3}\right)\delta(\tau-2)\,x(t-\tau)\,d\tau}_{I_2}$$

#### **Passo 3: Primeira parcela $I_1$ (pulso de $0$ a $1$)**
O pulso $u(\tau) - u(\tau - 1)$ vale $1$ só para $0 \le \tau < 1$, então os limites ficam $0$ e $1$:
$$I_1 = \frac{4}{3}\int_{0}^{1} (at + b - a\tau)\,d\tau$$
Primitiva em $\tau$ (lembrando que $at + b$ é **constante** em relação a $\tau$):
$$\int (at + b - a\tau)\,d\tau = (at + b)\,\tau - a\,\frac{\tau^2}{2}$$
- Limite superior ($\tau = 1$): $(at + b)(1) - a\,\frac{1^2}{2} = at + b - \frac{a}{2}$
- Limite inferior ($\tau = 0$): $(at + b)(0) - a\,\frac{0^2}{2} = 0$
- Superior menos inferior: $at + b - \frac{a}{2}$

Multiplicando por $\frac{4}{3}$, termo a termo:
$$I_1 = \frac{4}{3}at + \frac{4}{3}b - \frac{4}{3}\cdot\frac{a}{2} = \frac{4}{3}at + \frac{4}{3}b - \frac{2}{3}a$$

#### **Passo 4: Segunda parcela $I_2$ (impulso em $\tau = 2$)**
**Propriedade da amostragem (peneiramento) do impulso:** para qualquer função $f$ contínua em $\tau_0$,
$$\int_{-\infty}^{\infty} f(\tau)\,\delta(\tau - \tau_0)\,d\tau = f(\tau_0)$$
pois $\delta(\tau - \tau_0)$ é nulo para $\tau \neq \tau_0$ (então $f(\tau)\delta(\tau - \tau_0) = f(\tau_0)\delta(\tau - \tau_0)$) e tem área $1$:
$$\int_{-\infty}^{\infty} f(\tau_0)\,\delta(\tau - \tau_0)\,d\tau = f(\tau_0)\underbrace{\int_{-\infty}^{\infty}\delta(\tau - \tau_0)\,d\tau}_{=\,1} = f(\tau_0)$$
Aplicando com $f(\tau) = x(t - \tau) = at + b - a\tau$ e $\tau_0 = 2$:
$$I_2 = -\frac{1}{3}\,f(2) = -\frac{1}{3}\big[at + b - a(2)\big] = -\frac{1}{3}\big[at + b - 2a\big]$$
Distribuindo o $-\frac{1}{3}$:
$$I_2 = -\frac{1}{3}at - \frac{1}{3}b + \frac{2}{3}a$$

#### **Passo 5: Somar $y(t) = I_1 + I_2$, agrupando termo a termo**
- Termos em $at$: $\frac{4}{3}at - \frac{1}{3}at = \frac{3}{3}at = at$
- Termos em $b$: $\frac{4}{3}b - \frac{1}{3}b = \frac{3}{3}b = b$
- Termos só em $a$: $-\frac{2}{3}a + \frac{2}{3}a = 0$

$$\mathbf{y(t) = a t + b = x(t)}, \quad \forall t \in \mathbb{R}$$

```
Esboço de y(t) (item d): a saída é a própria reta de entrada

           3 │                                 ••••
         2,5 │                           ••••••
           2 │                     ••••••
         1,5 │               ••••••
       b = 1 │         ••••••
         0,5 │   ••••••
           0 │•••
           t ─┼─────┼─────┼─────┼─────┼─────┼─────┼►
             −2    −1     0     1     2     3     4

y(t) = at + b = x(t) para todo t (desenhado com a = 1/2, b = 1).
```

**Prova real numérica** ($a = 1{,}7$, $b = -0{,}4$, $t = 3$): $I_1 = \frac{4}{3}\int_0^1 (1{,}7(3 - \tau) - 0{,}4)\,d\tau = \frac{4}{3}(4{,}7 - 0{,}85) = \frac{4}{3}(3{,}85) \approx 5{,}1333$; $I_2 = -\frac{1}{3}(1{,}7 \cdot 1 - 0{,}4) = -\frac{1{,}3}{3} \approx -0{,}4333$. Soma $= 4{,}7 = x(3) = 1{,}7\cdot 3 - 0{,}4$ ✓.

> **💡 Interpretação Física:**
> A área líquida de $h(t)$ é $\int h(\tau)d\tau = \frac{4}{3}(1 - 0) - \frac{1}{3}(1) = 1$ e o primeiro momento temporal é $\int \tau h(\tau)d\tau = \frac{4}{3}\left[\frac{\tau^2}{2}\right]_0^1 - \frac{1}{3}(2) = \frac{4}{3}\cdot\frac{1}{2} - \frac{2}{3} = \frac{2}{3} - \frac{2}{3} = 0$. Por isso este sistema LIT reproduz qualquer reta $x(t) = at + b$ exatamente, sem atraso e sem distorção. Esse é só um comentário: a resposta já foi **provada pela conta** acima.

---

### **Item (e): $x(t)$ e $h(t)$ como mostrados na Figura P2.22(c)**
Da Figura P2.22(c):
- $x(t)$ é uma onda quadrada periódica de período fundamental $T_0 = 2$ e amplitude $\pm 1$, simétrica (par), onde os rótulos $\dots, -3, -2, -1, 0, 1, 2, 3, \dots$ estão posicionados no centro de cada semi-ciclo (ou seja, $x(t) = +1$ para $2k - \frac{1}{2} \le t < 2k + \frac{1}{2}$ e $x(t) = -1$ para $2k + \frac{1}{2} \le t < 2k + \frac{3}{2}$, com $k$ inteiro).
- $h(t)$ é o pulso triangular decrescente de duração $1$:
  $$h(t) = \begin{cases} 1 - t, & 0 \le t \le 1 \\ 0, & \text{caso contrário} \end{cases}$$

#### **Resolução Passo a Passo:**

#### **Passo 1: Montar a integral e mudar de variável**
Como $h$ é curto (só existe em $[0, 1]$), começamos pela forma $y(t) = \int h(\tau)\,x(t - \tau)\,d\tau$:
$$y(t) = \int_{0}^{1} (1 - \tau)\,x(t - \tau)\,d\tau$$
Para ter $x$ "parado", fazemos a substituição $\sigma = t - \tau$ (com $t$ constante):
- $\tau = t - \sigma$ e $d\tau = -d\sigma$;
- $\tau = 0 \implies \sigma = t$; $\tau = 1 \implies \sigma = t - 1$;
- $1 - \tau = 1 - (t - \sigma) = 1 - t + \sigma$.

$$y(t) = \int_{\sigma = t}^{\sigma = t-1} (1 - t + \sigma)\,x(\sigma)\,(-d\sigma) = \int_{t-1}^{t} (1 - t + \sigma)\,x(\sigma)\,d\sigma$$
(o sinal $-$ foi usado para inverter a ordem dos limites). Ou seja, a janela vai da **cauda** $\sigma = t - 1$ até a **frente** $\sigma = t$ (largura $1$), e dentro dela o peso é $1 - t + \sigma$, que vale $0$ na cauda e $1$ na frente.

#### **Passo 2: Provar que $y(t)$ é periódica de período 2 (não basta afirmar)**

**(i) $x$ tem período 2.** Se $2k - \frac{1}{2} \le t < 2k + \frac{1}{2}$, então somando $2$:
$$2(k+1) - \tfrac{1}{2} \le t + 2 < 2(k+1) + \tfrac{1}{2}$$
ou seja, $t + 2$ cai num trecho de $x = +1$ (com $k+1$ no lugar de $k$). Logo $x(t + 2) = +1 = x(t)$. O mesmo raciocínio vale para os trechos de $x = -1$. Portanto $x(s + 2) = x(s)$ para **todo** $s$.

**(ii) $y$ herda o período.** Calculando $y(t + 2)$ pela definição:
$$y(t + 2) = \int_{0}^{1} (1 - \tau)\,x\big((t + 2) - \tau\big)\,d\tau = \int_{0}^{1} (1 - \tau)\,x\big((t - \tau) + 2\big)\,d\tau$$
Usando (i) com $s = t - \tau$: $x\big((t - \tau) + 2\big) = x(t - \tau)$. Logo:
$$y(t + 2) = \int_{0}^{1} (1 - \tau)\,x(t - \tau)\,d\tau = y(t) \quad \checkmark$$
Assim, basta calcular $y(t)$ num período completo, por exemplo $-\frac{1}{2} \le t < \frac{3}{2}$.

#### **Passo 3: Pedaços de $x$ e eventos dentro do período**
No trecho relevante, $x(\sigma) = -1$ em $[-\frac{3}{2}, -\frac{1}{2})$, $+1$ em $[-\frac{1}{2}, \frac{1}{2})$ e $-1$ em $[\frac{1}{2}, \frac{3}{2})$. Pontos de quebra: $\sigma = -\frac{1}{2}$ e $\sigma = \frac{1}{2}$ (e os demais, repetidos a cada 2).

Como a janela tem largura $1$ (igual à largura de cada semiciclo), em cada instante ela contém **exatamente um** ponto de quebra. A frente cruza $\sigma = -\frac{1}{2}$ em $t = -\frac{1}{2}$ e $\sigma = \frac{1}{2}$ em $t = \frac{1}{2}$. Isso dá **2 trechos** por período.

**Primitiva usada nos dois trechos** (em $\sigma$, com $t$ constante): substituindo $w = 1 - t + \sigma$ (então $dw = d\sigma$),
$$\int (1 - t + \sigma)\,d\sigma = \frac{(1 - t + \sigma)^2}{2}$$
*Conferindo:* $\frac{d}{d\sigma}\frac{(1 - t + \sigma)^2}{2} = \frac{2(1 - t + \sigma)}{2}\cdot 1 = 1 - t + \sigma$ ✓

**Valores da primitiva $F(\sigma) = \frac{(1 - t + \sigma)^2}{2}$ que vão aparecer:**
- Na cauda $\sigma = t - 1$: $F = \frac{(1 - t + t - 1)^2}{2} = \frac{0^2}{2} = 0$.
- Na frente $\sigma = t$: $F = \frac{(1 - t + t)^2}{2} = \frac{1^2}{2} = \frac{1}{2}$.
- Em $\sigma = -\frac{1}{2}$: $F = \frac{(1 - t - \frac{1}{2})^2}{2} = \frac{(\frac{1}{2} - t)^2}{2}$.
- Em $\sigma = \frac{1}{2}$: $F = \frac{(1 - t + \frac{1}{2})^2}{2} = \frac{(\frac{3}{2} - t)^2}{2}$.

#### **Passo 4: Trecho 1: $-\frac{1}{2} \le t < \frac{1}{2}$**

**(a) Situação:** a cauda $t - 1 \in [-\frac{3}{2}, -\frac{1}{2})$ está num semiciclo negativo e a frente $t \in [-\frac{1}{2}, \frac{1}{2})$ está no semiciclo positivo; a troca de sinal ocorre em $\sigma = -\frac{1}{2}$.

```
Esboço no eixo σ para t = 0 (representante do Trecho 1):

     x(σ) +1 │██████████          ██████████          ██████████
           0 │···················································
          −1 │          ██████████          ██████████          █
           σ ─┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼►
             −2,5 −2   −1,5 −1   −0,5  0    0,5  1    1,5  2    2,5
      peso 1 │                      ███
             │                  ███████
           0 │               ██████████
sobreposição │               ▓▓▓▓▓▓▓▓▓▓
                             ↑ cauda = t−1 = −1  (peso 0)
                                       ↑ frente = t = 0  (peso 1)

peso = 1 − t + σ  (rampa: 0 na cauda, 1 na frente)
limites: parte −1 de t−1 = −1 até −1/2;  parte +1 de −1/2 até t = 0
```

**(d) Limites:** pedaço negativo de $t - 1$ até $-\frac{1}{2}$; pedaço positivo de $-\frac{1}{2}$ até $t$.

**(e) Montagem:**
$$y(t) = \int_{t-1}^{-1/2} (-1)(1 - t + \sigma)\,d\sigma + \int_{-1/2}^{t} (+1)(1 - t + \sigma)\,d\sigma$$

**(f) Conta:**
- Primeira integral: $-\Big[F(\sigma)\Big]_{t-1}^{-1/2} = -\left[\frac{(\frac{1}{2} - t)^2}{2} - 0\right] = -\frac{(\frac{1}{2} - t)^2}{2}$
- Segunda integral: $\Big[F(\sigma)\Big]_{-1/2}^{t} = \frac{1}{2} - \frac{(\frac{1}{2} - t)^2}{2}$
- Somando:
$$y(t) = -\frac{(\frac{1}{2} - t)^2}{2} + \frac{1}{2} - \frac{(\frac{1}{2} - t)^2}{2} = \frac{1}{2} - 2\cdot\frac{(\frac{1}{2} - t)^2}{2} = \frac{1}{2} - \left(\frac{1}{2} - t\right)^2$$
Como $\left(\frac{1}{2} - t\right)^2 = \left(t - \frac{1}{2}\right)^2$:
$$y(t) = \frac{1}{2} - \left(t - \frac{1}{2}\right)^2, \quad \text{para } -\frac{1}{2} \le t < \frac{1}{2}$$

**(g) Prova real ($t = 0$):** $y(0) = \int_0^1 (1 - \tau)\,x(-\tau)\,d\tau$. Para $0 \le \tau < \frac{1}{2}$, $x(-\tau) = +1$; para $\frac{1}{2} < \tau \le 1$, $x(-\tau) = -1$:
$$y(0) = \int_0^{1/2}(1 - \tau)\,d\tau - \int_{1/2}^{1}(1 - \tau)\,d\tau = \left[\tau - \frac{\tau^2}{2}\right]_0^{1/2} - \left[\tau - \frac{\tau^2}{2}\right]_{1/2}^{1} = \left(\frac{1}{2} - \frac{1}{8}\right) - \left[\left(1 - \frac{1}{2}\right) - \left(\frac{1}{2} - \frac{1}{8}\right)\right] = \frac{3}{8} - \frac{1}{8} = \frac{1}{4}$$
Fórmula: $\frac{1}{2} - \left(-\frac{1}{2}\right)^2 = \frac{1}{2} - \frac{1}{4} = \frac{1}{4}$ ✓

#### **Passo 5: Trecho 2: $\frac{1}{2} \le t < \frac{3}{2}$**

**(a) Situação:** a cauda $t - 1 \in [-\frac{1}{2}, \frac{1}{2})$ está no semiciclo positivo e a frente $t \in [\frac{1}{2}, \frac{3}{2})$ está no negativo; a troca ocorre em $\sigma = \frac{1}{2}$.

```
Esboço no eixo σ para t = 1 (representante do Trecho 2):

     x(σ) +1 │██████████          ██████████          ██████████
           0 │···················································
          −1 │          ██████████          ██████████          █
           σ ─┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼►
             −2,5 −2   −1,5 −1   −0,5  0    0,5  1    1,5  2    2,5
      peso 1 │                                ███
             │                            ███████
           0 │                         ██████████
sobreposição │                         ▓▓▓▓▓▓▓▓▓▓
                                       ↑ cauda = t−1 = 0  (peso 0)
                                                 ↑ frente = t = 1  (peso 1)

peso = 1 − t + σ  (rampa: 0 na cauda, 1 na frente)
limites: parte +1 de t−1 = 0 até 1/2;  parte −1 de 1/2 até t = 1
```

**(d) Limites:** pedaço positivo de $t - 1$ até $\frac{1}{2}$; pedaço negativo de $\frac{1}{2}$ até $t$.

**(e) Montagem:**
$$y(t) = \int_{t-1}^{1/2} (+1)(1 - t + \sigma)\,d\sigma + \int_{1/2}^{t} (-1)(1 - t + \sigma)\,d\sigma$$

**(f) Conta:**
- Primeira integral: $\Big[F(\sigma)\Big]_{t-1}^{1/2} = \frac{(\frac{3}{2} - t)^2}{2} - 0 = \frac{(\frac{3}{2} - t)^2}{2}$
- Segunda integral: $-\Big[F(\sigma)\Big]_{1/2}^{t} = -\left[\frac{1}{2} - \frac{(\frac{3}{2} - t)^2}{2}\right] = -\frac{1}{2} + \frac{(\frac{3}{2} - t)^2}{2}$
- Somando:
$$y(t) = \frac{(\frac{3}{2} - t)^2}{2} - \frac{1}{2} + \frac{(\frac{3}{2} - t)^2}{2} = \left(\frac{3}{2} - t\right)^2 - \frac{1}{2}$$
$$y(t) = \left(t - \frac{3}{2}\right)^2 - \frac{1}{2}, \quad \text{para } \frac{1}{2} \le t < \frac{3}{2}$$

**(g) Prova real ($t = 1$):** $y(1) = \int_0^1 (1 - \tau)\,x(1 - \tau)\,d\tau$. Para $0 \le \tau < \frac{1}{2}$, $1 - \tau \in (\frac{1}{2}, 1]$ e $x = -1$; para $\frac{1}{2} < \tau \le 1$, $1 - \tau \in [0, \frac{1}{2})$ e $x = +1$. Pelas mesmas integrais do trecho 1 com sinais trocados: $y(1) = -\frac{3}{8} + \frac{1}{8} = -\frac{1}{4}$. Fórmula: $\left(-\frac{1}{2}\right)^2 - \frac{1}{2} = \frac{1}{4} - \frac{1}{2} = -\frac{1}{4}$ ✓

#### **Resposta Final do Item 3.1 (e):**
Sinal periódico de período $T_0 = 2$ ($y(t + 2k) = y(t)$, provado no Passo 2). A saída $y(t)$ é contínua e assume valores no intervalo $\left[-\frac{1}{2}, +\frac{1}{2}\right]$, com máximo $+\frac{1}{2}$ em $t = \frac{1}{2} + 2k$ e mínimo $-\frac{1}{2}$ em $t = -\frac{1}{2} + 2k$:
$$y(t) = \begin{cases} \dfrac{1}{2} - \left(t - \dfrac{1}{2}\right)^2, & -\dfrac{1}{2} \le t < \dfrac{1}{2} \\[0.8em] \left(t - \dfrac{3}{2}\right)^2 - \dfrac{1}{2}, & \dfrac{1}{2} \le t < \dfrac{3}{2} \end{cases} \qquad \text{(repetido a cada 2 unidades)}$$

```
Esboço de y(t) (item e): arcos de parábola, período 2

         0,5 │•               •••••               •••••
        0,25 │ •            ••     •            ••
           0 │  ••        ••        ••        ••
       −0,25 │    ••     •            ••     •
        −0,5 │      •••••               •••••
           t ─┼────┼────┼────┼────┼────┼────┼────┼────┼►
             −1,5 −1   −0,5  0    0,5  1    1,5  2    2,5

Valores-chave: y(−1/2) = −1/2 (mínimo);  y(0) = 1/4;  y(1/2) = 1/2 (máximo);  y(1) = −1/4;  y(3/2) = −1/2
```

**Verificações finais:**
1. **Continuidade em $t = \frac{1}{2}$:** trecho 1: $\frac{1}{2} - \left(\frac{1}{2} - \frac{1}{2}\right)^2 = \frac{1}{2} - 0 = \frac{1}{2}$; trecho 2: $\left(\frac{1}{2} - \frac{3}{2}\right)^2 - \frac{1}{2} = (-1)^2 - \frac{1}{2} = \frac{1}{2}$ ✓
2. **Periodicidade (emenda entre períodos):** $y\left(-\frac{1}{2}\right)$ pelo trecho 1: $\frac{1}{2} - \left(-\frac{1}{2} - \frac{1}{2}\right)^2 = \frac{1}{2} - 1 = -\frac{1}{2}$. Limite de $y$ quando $t \to \frac{3}{2}$ pelo trecho 2: $\left(\frac{3}{2} - \frac{3}{2}\right)^2 - \frac{1}{2} = -\frac{1}{2}$. Iguais ✓ (o fim de um período emenda com o início do seguinte).
3. **Máximo e mínimo:** no trecho 1, $y = \frac{1}{2} - (t - \frac{1}{2})^2$ é uma parábola com vértice (máximo) em $t = \frac{1}{2}$, valor $\frac{1}{2}$; no trecho 2, $y = (t - \frac{3}{2})^2 - \frac{1}{2}$ é uma parábola com vértice (mínimo) em $t = \frac{3}{2}$, valor $-\frac{1}{2}$ ✓.
4. **Média num período** (calculada): a média de $x$ num período é $\frac{1}{2}\left[\int_{-1/2}^{1/2} 1\,dt + \int_{1/2}^{3/2}(-1)\,dt\right] = \frac{1}{2}[1 - 1] = 0$, então a média de $y$ também deve ser $0$:
   - $\int_{-1/2}^{1/2}\left[\frac{1}{2} - (t - \frac{1}{2})^2\right]dt = \left[\frac{t}{2} - \frac{(t - \frac{1}{2})^3}{3}\right]_{-1/2}^{1/2} = \left(\frac{1}{4} - 0\right) - \left(-\frac{1}{4} - \frac{(-1)^3}{3}\right) = \frac{1}{4} - \left(-\frac{1}{4} + \frac{1}{3}\right) = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$
   - $\int_{1/2}^{3/2}\left[(t - \frac{3}{2})^2 - \frac{1}{2}\right]dt = \left[\frac{(t - \frac{3}{2})^3}{3} - \frac{t}{2}\right]_{1/2}^{3/2} = \left(0 - \frac{3}{4}\right) - \left(\frac{(-1)^3}{3} - \frac{1}{4}\right) = -\frac{3}{4} + \frac{1}{3} + \frac{1}{4} = -\frac{1}{6}$
   - Total no período: $\frac{1}{6} - \frac{1}{6} = 0$ ✓

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
>    - **Na prova:** para provar que **não** é causal, exiba **um valor concreto** $h[n_0] \neq 0$ com $n_0 < 0$ (ou $h(t_0) \neq 0$ com $t_0 < 0$), com a conta feita.
> 4. **Estabilidade BIBO (Absolutamente Somável / Integrável):**
>    - **Discreto:** $\sum_{n=-\infty}^{\infty} |h[n]| < \infty$.
>    - **Contínuo:** $\int_{-\infty}^{\infty} |h(t)|\,dt < \infty$.
>    - **Na prova:** **sempre calcule** a soma (ou integral) até o número final. Para mostrar que diverge, calcule a soma parcial $S_N$ (ou a integral até $T$) em forma fechada e tome o limite $N \to \infty$ (ou $T \to \infty$) explicitamente. Frases como "a exponencial domina" ou "cresce, logo diverge" **sozinhas não valem nota**.
>
> **📐 Fórmulas de PG usadas neste bloco** (razão $r$, primeiro termo $r^A$):
> $$\sum_{k=A}^{B} r^k = \frac{r^A - r^{B+1}}{1 - r}\ (r \neq 1) \qquad \sum_{k=A}^{\infty} r^k = \frac{r^A}{1 - r}\ (|r| < 1) \qquad \sum_{k=-\infty}^{B} r^k = \frac{r^{B+1}}{r - 1}\ (|r| > 1)$$
> *A terceira sai da segunda fazendo $m = -k$: $\sum_{k=-\infty}^{B} r^k = \sum_{m=-B}^{\infty} \left(\frac{1}{r}\right)^m = \frac{(1/r)^{-B}}{1 - 1/r} = \frac{r^B \cdot r}{r - 1} = \frac{r^{B+1}}{r-1}$.*

---

## Questão 4.1 — [Oppenheim 2.25, pág. 144 (EN) / pág. 86 (PT)]
**Seja o sinal $y[n] = x[n] * h[n]$, em que:**
$$x[n] = 3^n u[-n-1] + \left(\frac{1}{3}\right)^n u[n] \quad \text{e} \quad h[n] = \left(\frac{1}{4}\right)^n u[n+3]$$
**(a) Determine $y[n]$ *sem* usar a propriedade distributiva da convolução.**
**(b) Determine $y[n]$ *usando* a propriedade distributiva da convolução.**

### **Resolução Passo a Passo:**

#### **Item (a): Cálculo direto sem usar a propriedade distributiva**

**Passo 1 — Escrever $x[k]$ por partes.**
- O termo $3^k u[-k-1]$ só é não nulo quando $-k - 1 \ge 0 \iff k \le -1$.
- O termo $\left(\frac{1}{3}\right)^k u[k]$ só é não nulo quando $k \ge 0$.
- As duas regiões não se sobrepõem e cobrem todos os inteiros. Logo:
$$x[k] = \begin{cases} 3^k, & k \le -1 \quad \text{(pedaço A, infinito à esquerda)} \\ \left(\frac{1}{3}\right)^k, & k \ge 0 \quad \text{(pedaço B, infinito à direita)} \end{cases}$$
Ponto de quebra: $k = 0$ (início do pedaço B).

**Passo 2 — Escrever $h[n-k]$ (a janela).**
Trocando $n$ por $n - k$ em $h[n] = \left(\frac{1}{4}\right)^n u[n+3]$:
$$h[n-k] = \left(\frac{1}{4}\right)^{n-k} u[n - k + 3]$$
O degrau exige:
$$n - k + 3 \ge 0 \iff k \le n + 3$$
A janela **não tem cauda** (vai de $k = -\infty$ até a frente $k = n + 3$). Portanto:
$$y[n] = \sum_{k=-\infty}^{n+3} x[k]\left(\frac{1}{4}\right)^{n-k}$$

**Passo 3 — Evento.** A frente cruza o ponto de quebra quando $n + 3 = 0 \iff n = -3$. Isso divide o eixo em **2 regiões**: $n \le -4$ (a frente ainda está no pedaço A) e $n \ge -3$ (a frente já entrou no pedaço B).

**Passo 4 — Simplificar o produto dentro da soma (vale nas duas regiões).**
Como $\left(\frac{1}{4}\right)^{n-k} = \left(\frac{1}{4}\right)^n \cdot \left(\frac{1}{4}\right)^{-k} = \left(\frac{1}{4}\right)^n \cdot 4^k$, e $\left(\frac{1}{4}\right)^n$ não depende de $k$ (sai da soma):
- No pedaço A: $3^k \cdot \left(\frac{1}{4}\right)^n 4^k = \left(\frac{1}{4}\right)^n (3 \cdot 4)^k = \left(\frac{1}{4}\right)^n 12^k$.
- No pedaço B: $\left(\frac{1}{3}\right)^k \cdot \left(\frac{1}{4}\right)^n 4^k = \left(\frac{1}{4}\right)^n \left(\frac{4}{3}\right)^k$.

---

**Região 1: $n + 3 \le -1 \iff n \le -4$**

*Esboço no eixo $k$ (representante da região: $n = -6$). A janela $h[n-k]$ ocupa todo $k \le n+3$; a sobreposição (▓) é onde $x[k] \neq 0$ **e** a janela está ligada:*
```
x[k]  1                                ●
    1/3                            ●   │   ●
    1/9                        ●   │   │   │   ●
   <1/9    ·   ·   ·   ·   ·                       ·   ·   ·
       ────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►k
          −7  −6  −5  −4  −3  −2  −1   0   1   2   3   4   5
h[n−k] ◄━━━━━━━━━━━━━━━━━━━┫  frente: k = n+3 = −3  (n = −6)
sobrep ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ◄── a janela h[n−k] continua até k = −∞ (não tem cauda)
        soma: k de −∞ até n+3 (só o pedaço A, onde x[k] = 3^k)
```

Todos os $k \le n + 3$ satisfazem $k \le -1$, ou seja, a janela só enxerga o pedaço A:
$$y[n] = \sum_{k=-\infty}^{n+3} 3^k \left(\frac{1}{4}\right)^{n-k} = \left(\frac{1}{4}\right)^n \sum_{k=-\infty}^{n+3} 12^k$$

Mudança de variável $m = -k$ (ou seja, $k = -m$):
- quando $k = n + 3$, temos $m = -n - 3$;
- quando $k \to -\infty$, temos $m \to +\infty$;
- $12^k = 12^{-m} = \left(\frac{1}{12}\right)^m$.

$$\sum_{k=-\infty}^{n+3} 12^k = \sum_{m=-n-3}^{\infty} \left(\frac{1}{12}\right)^m$$

É uma PG infinita com razão $r = \frac{1}{12}$ (convergente, pois $|r| < 1$) e primeiro termo $\left(\frac{1}{12}\right)^{-n-3} = 12^{n+3}$:
$$\sum_{m=-n-3}^{\infty} \left(\frac{1}{12}\right)^m = \frac{12^{n+3}}{1 - \frac{1}{12}} = \frac{12^{n+3}}{\frac{11}{12}} = \frac{12^{n+3}\cdot 12}{11} = \frac{12^{n+4}}{11}$$

Voltando:
$$y[n] = \left(\frac{1}{4}\right)^n \cdot \frac{12^{n+4}}{11} = \frac{12^{n+4}}{11 \cdot 4^n}$$

Abrindo $12^{n+4} = (4 \cdot 3)^{n+4} = 4^{n+4}\cdot 3^{n+4} = 4^n \cdot 4^4 \cdot 3^{n+4} = 4^n \cdot 256 \cdot 3^{n+4}$:
$$y[n] = \frac{4^n \cdot 256 \cdot 3^{n+4}}{11 \cdot 4^n} = \frac{256}{11}\,3^{n+4}$$

Se quiser em função de $3^n$: $3^{n+4} = 81 \cdot 3^n$ e $256 \cdot 81 = 20736$:
$$\boxed{y[n] = \frac{256}{11}\,3^{n+4} = \frac{20736}{11}\,3^n, \quad \text{para } n \le -4}$$

---

**Região 2: $n + 3 \ge 0 \iff n \ge -3$**

*Esboço no eixo $k$ (representante da região: $n = 1$). Agora a frente passou de $k = 0$ e a sobreposição cobre os dois pedaços:*
```
x[k]  1                                ●
    1/3                            ●   │   ●
    1/9                        ●   │   │   │   ●
   <1/9    ·   ·   ·   ·   ·                       ·   ·   ·
       ────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►k
          −7  −6  −5  −4  −3  −2  −1   0   1   2   3   4   5
h[n−k] ◄━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  frente: k = n+3 = 4  (n = 1)
sobrep ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ◄── a janela h[n−k] continua até k = −∞ (não tem cauda)
        S1: k de −∞ até −1 (pedaço A, 3^k)  ┃  S2: k de 0 até n+3 (pedaço B, (1/3)^k)
```

Agora a frente $k = n + 3 \ge 0$ já passou de $k = -1$: a janela enxerga **todo** o pedaço A ($k \le -1$) e o pedaço B de $k = 0$ até $k = n + 3$:
$$y[n] = \underbrace{\sum_{k=-\infty}^{-1} 3^k \left(\frac{1}{4}\right)^{n-k}}_{S_1} + \underbrace{\sum_{k=0}^{n+3} \left(\frac{1}{3}\right)^k \left(\frac{1}{4}\right)^{n-k}}_{S_2}$$

**Primeira soma $S_1$:**
$$S_1 = \left(\frac{1}{4}\right)^n \sum_{k=-\infty}^{-1} 12^k$$
Com $m = -k$: $k = -1 \Rightarrow m = 1$; $k \to -\infty \Rightarrow m \to \infty$:
$$\sum_{k=-\infty}^{-1} 12^k = \sum_{m=1}^{\infty} \left(\frac{1}{12}\right)^m$$
PG infinita com $r = \frac{1}{12}$ e primeiro termo $\left(\frac{1}{12}\right)^1 = \frac{1}{12}$:
$$\sum_{m=1}^{\infty} \left(\frac{1}{12}\right)^m = \frac{\frac{1}{12}}{1 - \frac{1}{12}} = \frac{\frac{1}{12}}{\frac{11}{12}} = \frac{1}{12}\cdot\frac{12}{11} = \frac{1}{11}$$
$$S_1 = \frac{1}{11}\left(\frac{1}{4}\right)^n$$

**Segunda soma $S_2$:**
$$S_2 = \left(\frac{1}{4}\right)^n \sum_{k=0}^{n+3} \left(\frac{4}{3}\right)^k$$
PG finita com $r = \frac{4}{3}$, $A = 0$, $B = n + 3$ (logo $B + 1 = n + 4$):
$$\sum_{k=0}^{n+3} \left(\frac{4}{3}\right)^k = \frac{\left(\frac{4}{3}\right)^0 - \left(\frac{4}{3}\right)^{n+4}}{1 - \frac{4}{3}} = \frac{1 - \left(\frac{4}{3}\right)^{n+4}}{-\frac{1}{3}} = -3\left[1 - \left(\frac{4}{3}\right)^{n+4}\right] = 3\left(\frac{4}{3}\right)^{n+4} - 3$$
Multiplicando por $\left(\frac{1}{4}\right)^n$:
$$S_2 = 3\left(\frac{1}{4}\right)^n\left(\frac{4}{3}\right)^{n+4} - 3\left(\frac{1}{4}\right)^n$$
Simplificando o primeiro termo, potência por potência:
$$3\left(\frac{1}{4}\right)^n\left(\frac{4}{3}\right)^{n+4} = 3 \cdot \frac{1}{4^n} \cdot \frac{4^{n+4}}{3^{n+4}} = 3 \cdot \frac{4^n \cdot 4^4}{4^n} \cdot \frac{1}{3^{n+4}} = \frac{3 \cdot 256}{3^{n}\cdot 3^4} = \frac{768}{81}\cdot\frac{1}{3^n} = \frac{256}{27}\left(\frac{1}{3}\right)^n$$
*(Simplificação: $\frac{768}{81}$, dividindo numerador e denominador por $3$, dá $\frac{256}{27}$.)*
$$S_2 = \frac{256}{27}\left(\frac{1}{3}\right)^n - 3\left(\frac{1}{4}\right)^n$$

**Somando $y[n] = S_1 + S_2$** e agrupando os termos em $\left(\frac{1}{4}\right)^n$:
$$y[n] = \frac{1}{11}\left(\frac{1}{4}\right)^n - 3\left(\frac{1}{4}\right)^n + \frac{256}{27}\left(\frac{1}{3}\right)^n = \left(\frac{1}{11} - 3\right)\left(\frac{1}{4}\right)^n + \frac{256}{27}\left(\frac{1}{3}\right)^n$$
Como $\frac{1}{11} - 3 = \frac{1}{11} - \frac{33}{11} = -\frac{32}{11}$:
$$\boxed{y[n] = -\frac{32}{11}\left(\frac{1}{4}\right)^n + \frac{256}{27}\left(\frac{1}{3}\right)^n, \quad \text{para } n \ge -3}$$

---

**Resposta Final do item (a):**
$$y[n] = \begin{cases} \dfrac{256}{11}\,3^{n+4}, & n \le -4 \\[1.0em] -\dfrac{32}{11}\left(\dfrac{1}{4}\right)^n + \dfrac{256}{27}\left(\dfrac{1}{3}\right)^n, & n \ge -3 \end{cases}$$
ou, de forma compacta:
$$y[n] = \frac{256}{11}\,3^{n+4}\,u[-n-4] + \left[-\frac{32}{11}\left(\frac{1}{4}\right)^n + \frac{256}{27}\left(\frac{1}{3}\right)^n\right]u[n+3]$$

---

#### **Item (b): Cálculo usando a propriedade distributiva da convolução**
Pela propriedade distributiva, decompomos $x[n] = x_1[n] + x_2[n]$, onde:
$$x_1[n] = 3^n u[-n-1] \quad \text{e} \quad x_2[n] = \left(\frac{1}{3}\right)^n u[n]$$
Então:
$$y[n] = \big(x_1[n] + x_2[n]\big) * h[n] = \underbrace{\big(x_1[n] * h[n]\big)}_{y_1[n]} + \underbrace{\big(x_2[n] * h[n]\big)}_{y_2[n]}$$

**1. Cálculo de $y_1[n] = x_1[n] * h[n]$:**
$$y_1[n] = \sum_{k=-\infty}^{\infty} 3^k u[-k-1] \left(\frac{1}{4}\right)^{n-k} u[n-k+3] = \left(\frac{1}{4}\right)^n \sum_{k} 12^k\, u[-k-1]\,u[n-k+3]$$
Os dois degraus impõem $k \le -1$ (de $u[-k-1]$) e $k \le n + 3$ (de $u[n-k+3]$). Os dois são limites **superiores**, então vale o menor deles: $k \le \min(-1,\ n+3)$.

- **Se $n \le -4$** (então $n + 3 \le -1$ e o mínimo é $n + 3$):

  ```
  x1[k] 1
      1/3                            ●
      1/9                        ●   │
     <1/9    ·   ·   ·   ·   ·
         ────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►k
            −7  −6  −5  −4  −3  −2  −1   0   1   2   3   4   5
  h[n−k] ◄━━━━━━━━━━━━━━━━━━━┫  frente: k = n+3 = −3  (n = −6)
  sobrep ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
          ◄── a janela h[n−k] continua até k = −∞ (não tem cauda)
          soma: k de −∞ até n+3 (o limite é a frente da janela)
  ```

  $$y_1[n] = \left(\frac{1}{4}\right)^n \sum_{k=-\infty}^{n+3} 12^k$$
  Pela fórmula da PG infinita à esquerda com $r = 12$ e $B = n + 3$:
  $$\sum_{k=-\infty}^{n+3} 12^k = \frac{12^{(n+3)+1}}{12 - 1} = \frac{12^{n+4}}{11}$$
  $$y_1[n] = \frac{12^{n+4}}{11\cdot 4^n} = \frac{4^n\cdot 256 \cdot 3^{n+4}}{11 \cdot 4^n} = \frac{256}{11}\,3^{n+4}$$
  *(Mesma conta da Região 1 do item (a).)*

- **Se $n \ge -3$** (então $n + 3 \ge 0 > -1$ e o mínimo é $-1$):

  ```
  x1[k] 1
      1/3                            ●
      1/9                        ●   │
     <1/9    ·   ·   ·   ·   ·
         ────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►k
            −7  −6  −5  −4  −3  −2  −1   0   1   2   3   4   5
  h[n−k] ◄━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  frente: k = n+3 = 4  (n = 1)
  sobrep ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
          ◄── a janela h[n−k] continua até k = −∞ (não tem cauda)
          soma: k de −∞ até −1 (o limite é o fim de x1, não a frente)
  ```

  $$y_1[n] = \left(\frac{1}{4}\right)^n \sum_{k=-\infty}^{-1} 12^k = \left(\frac{1}{4}\right)^n \cdot \frac{12^{-1+1}}{12 - 1} = \left(\frac{1}{4}\right)^n\cdot\frac{1}{11} = \frac{1}{11}\left(\frac{1}{4}\right)^n$$

**2. Cálculo de $y_2[n] = x_2[n] * h[n]$:**
$$y_2[n] = \sum_{k=-\infty}^{\infty} \left(\frac{1}{3}\right)^k u[k] \left(\frac{1}{4}\right)^{n-k} u[n-k+3] = \left(\frac{1}{4}\right)^n \sum_{k} \left(\frac{4}{3}\right)^k u[k]\,u[n-k+3]$$
Os degraus impõem $k \ge 0$ (limite inferior) e $k \le n + 3$ (limite superior).

- **Se $n \le -4$:** o limite superior $n + 3 \le -1$ é menor que o inferior $0$. A soma é vazia:

  ```
  x2[k] 1                                ●
      1/3                                │   ●
      1/9                                │   │   ●
     <1/9                                            ·   ·   ·
         ────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►k
            −7  −6  −5  −4  −3  −2  −1   0   1   2   3   4   5
  h[n−k] ◄━━━━━━━━━━━━━━━━━━━┫  frente: k = n+3 = −3  (n = −6)
  sobrep  (vazia: nenhum k tem x2[k] ≠ 0 e k ≤ n+3)
          ◄── a janela h[n−k] continua até k = −∞ (não tem cauda)
          a frente (k = n+3 ≤ −1) não alcança k = 0  ⇒  y2[n] = 0
  ```

  $$y_2[n] = 0$$
- **Se $n \ge -3$:** $k$ vai de $0$ até $n + 3$. Pela PG finita com $r = \frac{4}{3}$:

  ```
  x2[k] 1                                ●
      1/3                                │   ●
      1/9                                │   │   ●
     <1/9                                            ·   ·   ·
         ────┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼►k
            −7  −6  −5  −4  −3  −2  −1   0   1   2   3   4   5
  h[n−k] ◄━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫  frente: k = n+3 = 4  (n = 1)
  sobrep                              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
          ◄── a janela h[n−k] continua até k = −∞ (não tem cauda)
          soma: k de 0 (início de x2) até n+3 (frente)
  ```

  $$\sum_{k=0}^{n+3}\left(\frac{4}{3}\right)^k = \frac{1 - \left(\frac{4}{3}\right)^{n+4}}{1 - \frac{4}{3}} = 3\left(\frac{4}{3}\right)^{n+4} - 3$$
  $$y_2[n] = 3\left(\frac{1}{4}\right)^n\left(\frac{4}{3}\right)^{n+4} - 3\left(\frac{1}{4}\right)^n = \frac{256}{27}\left(\frac{1}{3}\right)^n - 3\left(\frac{1}{4}\right)^n$$
  *(Simplificação idêntica à de $S_2$ no item (a).)*

**3. Somando $y[n] = y_1[n] + y_2[n]$:**
- Para $n \le -4$: $y[n] = \frac{256}{11}3^{n+4} + 0 = \frac{256}{11}3^{n+4}$.
- Para $n \ge -3$: $y[n] = \frac{1}{11}\left(\frac{1}{4}\right)^n + \frac{256}{27}\left(\frac{1}{3}\right)^n - 3\left(\frac{1}{4}\right)^n = -\frac{32}{11}\left(\frac{1}{4}\right)^n + \frac{256}{27}\left(\frac{1}{3}\right)^n$.

$$y[n] = \begin{cases} \dfrac{256}{11}\,3^{n+4}, & n \le -4 \\[1.0em] -\dfrac{32}{11}\left(\dfrac{1}{4}\right)^n + \dfrac{256}{27}\left(\dfrac{1}{3}\right)^n, & n \ge -3 \end{cases}$$
**Idêntico ao item (a)**, como tinha de ser.

**Esboço de $y[n]$** (altura das hastes em escala aproximada; valores exatos embaixo). A sequência cresce como $3^n$ pela esquerda, atinge o pico $y[-3] = \frac{768}{11} \approx 69{,}8$ e depois decai como combinação de $\left(\frac{1}{4}\right)^n$ e $\left(\frac{1}{3}\right)^n$:
```
  70                                    ●
                                        │
                                        │
  40                                    │     ●
                                        │     │
                                  ●     │     │     ●
  10      ●     ●     ●     ●     │     │     │     │     ●     ●     ●     ●
     ─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─►n
         −8    −7    −6    −5    −4    −3    −2    −1     0     1     2     3
         0,3   0,9   2,6   7,8  23,3  69,8  38,8  16,8   6,6   2,4   0,9   0,3   ← y[n]
```

> **✅ Prova Real (valores calculados por soma direta e pela fórmula):**
> - **$y[-3]$ por soma direta:** com $n = -3$, a janela vai até $k = n + 3 = 0$.
>   - Parte A: $\sum_{k=-\infty}^{-1} 3^k\left(\frac{1}{4}\right)^{-3-k} = \left(\frac{1}{4}\right)^{-3}\sum_{k=-\infty}^{-1}12^k = 64 \cdot \frac{1}{11} = \frac{64}{11}$.
>   - Parte B: só $k = 0$, então $\left(\frac{1}{3}\right)^0\left(\frac{1}{4}\right)^{-3} = 1 \cdot 64 = 64$.
>   - Total: $y[-3] = \frac{64}{11} + 64 = \frac{64 + 704}{11} = \frac{768}{11} \approx 69{,}818$.
>   - **Pela fórmula** ($n \ge -3$): $-\frac{32}{11}\cdot 4^3 + \frac{256}{27}\cdot 3^3 = -\frac{2048}{11} + 256 = \frac{-2048 + 2816}{11} = \frac{768}{11}$ ✓.
> - **$y[-5]$ por soma direta:** a janela vai até $k = -2$. Os termos são $3^k\cdot 4^{5+k}$:
>   - $k = -2$: $\frac{1}{9}\cdot 4^3 = \frac{64}{9}$;
>   - $k = -3$: $\frac{1}{27}\cdot 4^2 = \frac{16}{27}$;
>   - cada termo seguinte é o anterior vezes $\frac{1}{12}$ (por exemplo, $\frac{64}{9}\cdot\frac{1}{12} = \frac{16}{27}$ ✓).
>   - Soma da PG: $\frac{64/9}{1 - 1/12} = \frac{64}{9}\cdot\frac{12}{11} = \frac{768}{99} = \frac{256}{33} \approx 7{,}758$.
>   - **Pela fórmula** ($n \le -4$): $\frac{256}{11}\cdot 3^{-1} = \frac{256}{33}$ ✓.
> - **$y[0]$:** $-\frac{32}{11} + \frac{256}{27} = \frac{-32\cdot 27 + 256 \cdot 11}{297} = \frac{-864 + 2816}{297} = \frac{1952}{297} \approx 6{,}572$. A soma direta (feita numericamente) dá $6{,}5724$ ✓.
> - **$y[2]$:** $-\frac{32}{11}\cdot\frac{1}{16} + \frac{256}{27}\cdot\frac{1}{9} = -\frac{2}{11} + \frac{256}{243} = \frac{-486 + 2816}{2673} = \frac{2330}{2673} \approx 0{,}8717$. A soma direta (feita numericamente) dá $0{,}8717$ ✓.
> - **Fronteira:** as duas fórmulas coincidem em $n = -4$ (as duas dão $\frac{256}{11}$; na segunda, $-\frac{32}{11}\cdot 256 + \frac{256}{27}\cdot 81 = -\frac{8192}{11} + 768 = \frac{256}{11}$) e em $n = -3$ (as duas dão $\frac{768}{11}$, pois $\frac{256}{11}\cdot 3^1 = \frac{768}{11}$). A transição é suave.
> - **Sinal:** como $x[n] > 0$ e $h[n] \ge 0$ para todo $n$, $y[n]$ tem de ser positiva em todo $n$. Todos os valores acima são positivos ✓.

---

## Questão 4.2 — [Oppenheim 2.28, pág. 144 (EN) / pág. 86 (PT)]
**A seguir, temos respostas ao impulso de sistemas LIT de tempo discreto. Determine se cada um dos sistemas é causal e/ou estável. Justifique suas respostas.**

### **Resolução Passo a Passo:**

> **Como ler os mini-esboços:** cada símbolo é uma amostra de $|h[n]|$; a altura do bloco (▁ a █) é proporcional ao valor, e · significa **exatamente zero**. Para a **causalidade**, olhe se há blocos à esquerda de $n = 0$. Para a **estabilidade**, olhe se a cauda some ($\to 0$) ou cresce, e depois **confirme com a conta**.

- **(a) $h[n] = \left(\frac{1}{5}\right)^n u[n]$**
  ```
       n: −4 −3 −2 −1  0  1  2  3  4  5  6
  |h[n]|:  ·  ·  ·  ·  █  ▂  ▁  ▁  ▁  ▁  ▁  → 0 (decai)
  ```
  - **Causalidade:** para todo $n < 0$, temos $u[n] = 0$, e então $h[n] = \left(\frac{1}{5}\right)^n \cdot 0 = 0$. Por exemplo, $h[-1] = 5 \cdot u[-1] = 5 \cdot 0 = 0$. Logo, é **CAUSAL**.
  - **Estabilidade:** para $n \ge 0$, $\left(\frac{1}{5}\right)^n > 0$, então $|h[n]| = \left(\frac{1}{5}\right)^n$:
    $$\sum_{n=-\infty}^{\infty} |h[n]| = \sum_{n=0}^{\infty} \left(\frac{1}{5}\right)^n$$
    PG infinita com $r = \frac{1}{5}$ ($|r| < 1$, converge) e primeiro termo $\left(\frac{1}{5}\right)^0 = 1$:
    $$\sum_{n=0}^{\infty} \left(\frac{1}{5}\right)^n = \frac{1}{1 - \frac{1}{5}} = \frac{1}{\frac{4}{5}} = \frac{5}{4} = 1{,}25 < \infty$$
    Logo, é **ESTÁVEL**.

- **(b) $h[n] = (0{,}8)^n u[n+2]$**
  ```
       n: −4 −3 −2 −1  0  1  2  3  4  5  6
  |h[n]|:  ·  ·  █  ▇  ▆  ▅  ▄  ▃  ▃  ▂  ▂  → 0 (decai)
  ```
  - **Causalidade:** $u[n+2] = 1$ quando $n + 2 \ge 0 \iff n \ge -2$. Então:
    $$h[-2] = (0{,}8)^{-2} = \frac{1}{0{,}64} = 1{,}5625 \neq 0 \qquad h[-1] = (0{,}8)^{-1} = \frac{1}{0{,}8} = 1{,}25 \neq 0$$
    Como existe $h[n] \neq 0$ para $n < 0$, o sistema é **NÃO-CAUSAL**.
  - **Estabilidade:** todos os termos são positivos, então $|h[n]| = (0{,}8)^n$ para $n \ge -2$:
    $$\sum_{n=-\infty}^{\infty} |h[n]| = \sum_{n=-2}^{\infty} (0{,}8)^n$$
    PG infinita com $r = 0{,}8$ ($|r| < 1$, converge) e primeiro termo $(0{,}8)^{-2} = 1{,}5625$:
    $$\sum_{n=-2}^{\infty} (0{,}8)^n = \frac{(0{,}8)^{-2}}{1 - 0{,}8} = \frac{1{,}5625}{0{,}2} = 7{,}8125 < \infty$$
    Logo, é **ESTÁVEL**.

- **(c) $h[n] = \left(\frac{1}{2}\right)^n u[-n]$**
  ```
       n: −4 −3 −2 −1  0  1  2  3  4  5  6
  |h[n]|:  █  ▄  ▂  ▁  ▁  ·  ·  ·  ·  ·  ·  (cresce para a esquerda: 2, 4, 8, 16, ...)
  ```
  - **Causalidade:** $u[-n] = 1$ quando $-n \ge 0 \iff n \le 0$. Então:
    $$h[-1] = \left(\frac{1}{2}\right)^{-1} = 2 \neq 0$$
    Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** todos os termos são positivos. Calculamos a **soma parcial** de $n = -N$ até $n = 0$:
    $$S_N = \sum_{n=-N}^{0} \left(\frac{1}{2}\right)^n$$
    Com $m = -n$ ($n = 0 \Rightarrow m = 0$; $n = -N \Rightarrow m = N$) e $\left(\frac{1}{2}\right)^{-m} = 2^m$:
    $$S_N = \sum_{m=0}^{N} 2^m$$
    PG finita com $r = 2$, $A = 0$, $B = N$:
    $$S_N = \frac{2^0 - 2^{N+1}}{1 - 2} = \frac{1 - 2^{N+1}}{-1} = 2^{N+1} - 1$$
    Tomando o limite:
    $$\sum_{n=-\infty}^{\infty}|h[n]| = \lim_{N\to\infty} S_N = \lim_{N\to\infty}\left(2^{N+1} - 1\right) = +\infty$$
    *(Exemplo: $S_{10} = 2^{11} - 1 = 2047$; $S_{20} = 2^{21} - 1 = 2\,097\,151$. A soma não para de crescer.)*
    Logo, o sistema é **INSTÁVEL**.

- **(d) $h[n] = 5^n u[3-n]$**
  ```
       n: −4 −3 −2 −1  0  1  2  3  4  5  6
  |h[n]|:  ▁  ▁  ▁  ▁  ▁  ▁  ▂  █  ·  ·  ·  (cresce até n = 3; à esquerda decai → 0)
  ```
  - **Causalidade:** $u[3-n] = 1$ quando $3 - n \ge 0 \iff n \le 3$, o que inclui todos os inteiros negativos. Por exemplo:
    $$h[-1] = 5^{-1} = \frac{1}{5} = 0{,}2 \neq 0$$
    Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** todos os termos são positivos, então $|h[n]| = 5^n$ para $n \le 3$:
    $$\sum_{n=-\infty}^{\infty} |h[n]| = \sum_{n=-\infty}^{3} 5^n$$
    Com $m = -n$: $n = 3 \Rightarrow m = -3$; $n \to -\infty \Rightarrow m \to +\infty$; $5^n = 5^{-m} = \left(\frac{1}{5}\right)^m$:
    $$\sum_{n=-\infty}^{3} 5^n = \sum_{m=-3}^{\infty}\left(\frac{1}{5}\right)^m$$
    PG infinita com $r = \frac{1}{5}$ (converge) e primeiro termo $\left(\frac{1}{5}\right)^{-3} = 5^3 = 125$:
    $$\sum_{m=-3}^{\infty}\left(\frac{1}{5}\right)^m = \frac{125}{1 - \frac{1}{5}} = \frac{125}{\frac{4}{5}} = 125\cdot\frac{5}{4} = \frac{625}{4} = 156{,}25 < \infty$$
    *(Conferência pela fórmula à esquerda com $r = 5$ e $B = 3$: $\frac{5^{4}}{5 - 1} = \frac{625}{4}$ ✓.)*
    Logo, o sistema é **ESTÁVEL**.

- **(e) $h[n] = \left(-\frac{1}{2}\right)^n u[n] + (1{,}01)^n u[n-1]$**
  ```
       n: −4 −3 −2 −1  0  1  2  3  4  5  6
  |h[n]|:  ·  ·  ·  ·  ▇  ▄  █  ▆  ▇  ▇  ▇  ... |h[100]| ≈ 2,7  |h[300]| ≈ 19,8 (cresce)
  ```
  - **Causalidade:** para $n < 0$, $u[n] = 0$ e $u[n-1] = 0$. Então $h[n] = 0 + 0 = 0$ para todo $n < 0$ (por exemplo, $h[-1] = (-2)\cdot 0 + \frac{1}{1{,}01}\cdot 0 = 0$). Logo, é **CAUSAL**.
  - **Estabilidade:** vamos mostrar, com conta, que a soma diverge.
    - Em $n = 0$: $h[0] = \left(-\frac{1}{2}\right)^0\cdot 1 + (1{,}01)^0\cdot u[-1] = 1 + 0 = 1$, então $|h[0]| = 1$.
    - Para $n \ge 1$: $h[n] = \left(-\frac{1}{2}\right)^n + (1{,}01)^n$. Pela desigualdade triangular reversa, $|a + b| \ge |b| - |a|$:
      $$|h[n]| \ge (1{,}01)^n - \left|\left(-\frac{1}{2}\right)^n\right| = (1{,}01)^n - \left(\frac{1}{2}\right)^n$$
    - **Soma parcial** até $N$:
      $$\sum_{n=0}^{N}|h[n]| \ge 1 + \sum_{n=1}^{N}(1{,}01)^n - \sum_{n=1}^{N}\left(\frac{1}{2}\right)^n$$
    - Primeira PG ($r = 1{,}01$, $A = 1$, $B = N$):
      $$\sum_{n=1}^{N}(1{,}01)^n = \frac{1{,}01 - (1{,}01)^{N+1}}{1 - 1{,}01} = \frac{1{,}01\left[(1{,}01)^N - 1\right]}{0{,}01} = 101\left[(1{,}01)^N - 1\right]$$
    - Segunda PG ($r = \frac{1}{2}$, $A = 1$, $B = N$):
      $$\sum_{n=1}^{N}\left(\frac{1}{2}\right)^n = \frac{\frac{1}{2} - \left(\frac{1}{2}\right)^{N+1}}{1 - \frac{1}{2}} = 1 - \left(\frac{1}{2}\right)^N$$
    - Juntando:
      $$\sum_{n=0}^{N}|h[n]| \ge 1 + 101\left[(1{,}01)^N - 1\right] - 1 + \left(\frac{1}{2}\right)^N = 101\left[(1{,}01)^N - 1\right] + \left(\frac{1}{2}\right)^N$$
    - Limite: como $1{,}01 > 1$, $(1{,}01)^N \to \infty$, enquanto $\left(\frac{1}{2}\right)^N \to 0$:
      $$\sum_{n=-\infty}^{\infty}|h[n]| \ge \lim_{N\to\infty}\left\{101\left[(1{,}01)^N - 1\right] + \left(\frac{1}{2}\right)^N\right\} = +\infty$$
      *(Exemplo numérico: para $N = 500$, a cota inferior já vale $\approx 14\,520$.)*
    Logo, o sistema é **INSTÁVEL**.

- **(f) $h[n] = \left(-\frac{1}{2}\right)^n u[n] + (1{,}01)^n u[1-n]$**
  ```
       n: −4 −3 −2 −1  0  1  2  3  4  5  6
  |h[n]|:  ▄  ▄  ▄  ▄  █  ▃  ▁  ▁  ▁  ▁  ▁  (à esquerda decai devagar, 1,01^n → 0; à direita → 0)
  ```
  - **Causalidade:** o segundo termo tem $u[1-n] = 1$ para $1 - n \ge 0 \iff n \le 1$. Em $n = -1$:
    $$h[-1] = \left(-\frac{1}{2}\right)^{-1}\underbrace{u[-1]}_{0} + (1{,}01)^{-1}\underbrace{u[2]}_{1} = 0 + \frac{1}{1{,}01} \approx 0{,}990 \neq 0$$
    Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** pela desigualdade triangular $|a + b| \le |a| + |b|$:
    $$\sum_{n=-\infty}^{\infty} |h[n]| \le \underbrace{\sum_{n=0}^{\infty} \left(\frac{1}{2}\right)^n}_{\Sigma_1} + \underbrace{\sum_{n=-\infty}^{1} (1{,}01)^n}_{\Sigma_2}$$
    - $\Sigma_1$: PG infinita, $r = \frac{1}{2}$, primeiro termo $1$:
      $$\Sigma_1 = \frac{1}{1 - \frac{1}{2}} = \frac{1}{\frac{1}{2}} = 2$$
    - $\Sigma_2$: com $m = -n$ ($n = 1 \Rightarrow m = -1$; $n \to -\infty \Rightarrow m \to \infty$), $(1{,}01)^n = \left(\frac{1}{1{,}01}\right)^m$. É uma PG infinita com $r = \frac{1}{1{,}01} < 1$ (converge) e primeiro termo $\left(\frac{1}{1{,}01}\right)^{-1} = 1{,}01$:
      $$\Sigma_2 = \frac{1{,}01}{1 - \frac{1}{1{,}01}} = \frac{1{,}01}{\frac{1{,}01 - 1}{1{,}01}} = \frac{1{,}01 \cdot 1{,}01}{0{,}01} = \frac{1{,}0201}{0{,}01} = 102{,}01$$
      *(Conferência pela fórmula à esquerda com $r = 1{,}01$ e $B = 1$: $\frac{(1{,}01)^2}{1{,}01 - 1} = \frac{1{,}0201}{0{,}01} = 102{,}01$ ✓.)*
    - Total:
      $$\sum_{n=-\infty}^{\infty} |h[n]| \le 2 + 102{,}01 = 104{,}01 < \infty$$
    Como a soma é limitada por um número finito, o sistema é **ESTÁVEL**.

- **(g) $h[n] = n\left(\frac{1}{3}\right)^n u[n-1]$**
  ```
       n: −4 −3 −2 −1  0  1  2  3  4  5  6
  |h[n]|:  ·  ·  ·  ·  ·  █  ▆  ▃  ▂  ▁  ▁  → 0 (decai)
  ```
  - **Causalidade:** $u[n-1] = 0$ para $n < 1$, logo $h[n] = 0$ para todo $n < 0$ (por exemplo, $h[-1] = (-1)\cdot 3 \cdot u[-2] = -3 \cdot 0 = 0$). Logo, é **CAUSAL**.
  - **Estabilidade:** para $n \ge 1$, todos os termos são positivos, então:
    $$\sum_{n=-\infty}^{\infty} |h[n]| = \sum_{n=1}^{\infty} n\left(\frac{1}{3}\right)^n$$
    **Dedução da fórmula $\sum_{n=1}^{\infty} n r^n$ (para $|r| < 1$), pelo método $S - rS$:**
    $$S = 1r + 2r^2 + 3r^3 + 4r^4 + \cdots$$
    $$rS = \phantom{1r + {}} 1r^2 + 2r^3 + 3r^4 + \cdots$$
    Subtraindo termo a termo (mesma potência de $r$):
    $$S - rS = r + (2-1)r^2 + (3-2)r^3 + \cdots = r + r^2 + r^3 + \cdots = \frac{r}{1 - r}$$
    $$S(1 - r) = \frac{r}{1 - r} \implies S = \frac{r}{(1 - r)^2}$$
    Aplicando com $r = \frac{1}{3}$:
    $$1 - r = 1 - \frac{1}{3} = \frac{2}{3} \qquad (1 - r)^2 = \frac{4}{9}$$
    $$\sum_{n=1}^{\infty} n\left(\frac{1}{3}\right)^n = \frac{\frac{1}{3}}{\frac{4}{9}} = \frac{1}{3}\cdot\frac{9}{4} = \frac{9}{12} = \frac{3}{4} = 0{,}75 < \infty$$
    *(Conferência pelos primeiros termos: $\frac{1}{3} + \frac{2}{9} + \frac{3}{27} + \frac{4}{81} \approx 0{,}333 + 0{,}222 + 0{,}111 + 0{,}049 = 0{,}716$, que já se aproxima de $0{,}75$ ✓.)*
    Logo, o sistema é **ESTÁVEL**.

> **✅ Gabarito (Oppenheim 2.28):** (a) causal, estável; (b) não-causal, estável; (c) não-causal, instável; (d) não-causal, estável; (e) causal, instável; (f) não-causal, estável; (g) causal, estável. Todos os valores de soma acima também foram conferidos numericamente.

---

## Questão 4.3 — [Oppenheim 2.29, pág. 144 (EN) / pág. 86 (PT)]
**A seguir, temos respostas ao impulso de sistemas LIT de tempo contínuo. Determine se cada um dos sistemas é causal e/ou estável. Justifique suas respostas.**

### **Resolução Passo a Passo:**

> **Como ler os mini-esboços:** cada símbolo é uma amostra de $|h(t)|$ a cada $0{,}5$ (no item (e), a cada $0{,}25$); a altura do bloco (▁ a █) é proporcional ao valor, e · significa **exatamente zero**. Para a **causalidade**, olhe se há blocos à esquerda de $t = 0$. Para a **estabilidade**, olhe se a cauda some ($\to 0$) ou cresce, e depois **confirme com a conta**.

- **(a) $h(t) = e^{-4t}u(t-2)$**
  ```
       t:−3  −2  −1   0   1   2   3   4   5
  |h(t)|: · · · · · · · · · · █ ▂ ▁ ▁ ▁ ▁ ▁  → 0 (decai)
  ```
  - **Causalidade:** $u(t-2) = 0$ para $t < 2$, logo $h(t) = 0$ para todo $t < 0$ (por exemplo, $h(-1) = e^{4}\cdot u(-3) = e^4 \cdot 0 = 0$). Logo, é **CAUSAL**.
  - **Estabilidade:** $e^{-4t} > 0$, então $|h(t)| = e^{-4t}$ para $t \ge 2$. Integrando até $T$ e depois tomando o limite:
    $$\int_{2}^{T} e^{-4t}\,dt = \left[\frac{e^{-4t}}{-4}\right]_{2}^{T} = \frac{e^{-4T}}{-4} - \frac{e^{-8}}{-4} = \frac{e^{-8} - e^{-4T}}{4}$$
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \lim_{T\to\infty}\frac{e^{-8} - e^{-4T}}{4} = \frac{e^{-8} - 0}{4} = \frac{e^{-8}}{4} \approx 8{,}39\times 10^{-5} < \infty$$
    *(O limite $e^{-4T} \to 0$ vale porque o expoente $-4T \to -\infty$.)*
    Logo, é **ESTÁVEL**.

- **(b) $h(t) = e^{-6t}u(3-t)$**
  ```
       t:−3  −2  −1   0   1   2   3   4   5
  |h(t)|: █ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ · · · ·  (explode para a esquerda: h(−3) = e^18)
  ```
  - **Causalidade:** $u(3-t) = 1$ para $3 - t \ge 0 \iff t \le 3$, o que inclui $t < 0$. Por exemplo:
    $$h(-1) = e^{-6(-1)}\,u(4) = e^{6}\cdot 1 \approx 403{,}4 \neq 0$$
    Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** $|h(t)| = e^{-6t}$ para $t \le 3$. Integrando de $-T$ até $3$:
    $$\int_{-T}^{3} e^{-6t}\,dt = \left[\frac{e^{-6t}}{-6}\right]_{-T}^{3} = \frac{e^{-18}}{-6} - \frac{e^{-6(-T)}}{-6} = \frac{e^{6T} - e^{-18}}{6}$$
    Tomando o limite $T \to \infty$ (o expoente $6T \to +\infty$, logo $e^{6T} \to +\infty$):
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \lim_{T\to\infty}\frac{e^{6T} - e^{-18}}{6} = +\infty$$
    *(Exemplo: com $T = 5$, a integral já vale $\frac{e^{30}}{6} \approx 1{,}78 \times 10^{12}$.)*
    Logo, é **INSTÁVEL**.

- **(c) $h(t) = e^{-2t}u(t+50)$**
  ```
       t:−3  −2  −1   0   1   2   3   4   5
  |h(t)|: █ ▃ ▂ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁  (começa em t = −50, fora do desenho; decai → 0)
  ```
  - **Causalidade:** $u(t + 50) = 1$ para $t \ge -50$. Por exemplo:
    $$h(-1) = e^{-2(-1)}\,u(49) = e^{2} \approx 7{,}39 \neq 0$$
    Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** $|h(t)| = e^{-2t}$ para $t \ge -50$. Integrando até $T$:
    $$\int_{-50}^{T} e^{-2t}\,dt = \left[\frac{e^{-2t}}{-2}\right]_{-50}^{T} = \frac{e^{-2T}}{-2} - \frac{e^{-2(-50)}}{-2} = \frac{e^{100} - e^{-2T}}{2}$$
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \lim_{T\to\infty}\frac{e^{100} - e^{-2T}}{2} = \frac{e^{100} - 0}{2} = \frac{e^{100}}{2} < \infty$$
    Embora $\frac{e^{100}}{2} \approx 1{,}34 \times 10^{43}$ seja um número enorme, ele é **finito**. Logo, o sistema é **ESTÁVEL**.

- **(d) $h(t) = e^{2t}u(-1-t)$**
  ```
       t:−5  −4  −3  −2  −1   0   1   2   3
  |h(t)|: ▁ ▁ ▁ ▁ ▁ ▁ ▂ ▃ █ · · · · · · · ·  (à esquerda decai → 0)
  ```
  - **Causalidade:** $u(-1-t) = 1$ para $-1 - t \ge 0 \iff t \le -1$. Por exemplo:
    $$h(-2) = e^{2(-2)}\,u(1) = e^{-4} \approx 0{,}0183 \neq 0$$
    Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** $|h(t)| = e^{2t}$ para $t \le -1$. Integrando de $-T$ até $-1$:
    $$\int_{-T}^{-1} e^{2t}\,dt = \left[\frac{e^{2t}}{2}\right]_{-T}^{-1} = \frac{e^{-2}}{2} - \frac{e^{-2T}}{2}$$
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \lim_{T\to\infty}\left(\frac{e^{-2}}{2} - \frac{e^{-2T}}{2}\right) = \frac{e^{-2}}{2} - 0 = \frac{e^{-2}}{2} \approx 0{,}0677 < \infty$$
    Logo, é **ESTÁVEL**.

- **(e) $h(t) = e^{-6|t|}$**
  ```
       t:−3      −2      −1       0       1       2       3
  |h(t)|: ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▂ █ ▂ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁ ▁  (dos dois lados → 0)
  ```
  - **Causalidade:** para $t < 0$, $|t| = -t$ e $h(t) = e^{6t}$. Por exemplo:
    $$h(-1) = e^{-6|-1|} = e^{-6} \approx 0{,}00248 \neq 0$$
    Logo, é **NÃO-CAUSAL**.
  - **Estabilidade:** dividimos a integral em $t < 0$ (onde $|t| = -t$) e $t \ge 0$ (onde $|t| = t$):
    $$\int_{-\infty}^{\infty} e^{-6|t|}\,dt = \int_{-\infty}^{0} e^{6t}\,dt + \int_{0}^{\infty} e^{-6t}\,dt$$
    - Primeira integral (até $-T$, depois o limite):
      $$\int_{-T}^{0} e^{6t}\,dt = \left[\frac{e^{6t}}{6}\right]_{-T}^{0} = \frac{1}{6} - \frac{e^{-6T}}{6} \xrightarrow{T\to\infty} \frac{1}{6}$$
    - Segunda integral (até $T$, depois o limite):
      $$\int_{0}^{T} e^{-6t}\,dt = \left[\frac{e^{-6t}}{-6}\right]_{0}^{T} = \frac{1 - e^{-6T}}{6} \xrightarrow{T\to\infty} \frac{1}{6}$$
    - Total:
      $$\int_{-\infty}^{\infty} |h(t)|\,dt = \frac{1}{6} + \frac{1}{6} = \frac{1}{3} < \infty$$
    Logo, é **ESTÁVEL**.

- **(f) $h(t) = t e^{-t}u(t)$**
  ```
       t:−3  −2  −1   0   1   2   3   4   5   6   7   8
  |h(t)|: · · · · · · · ▇ █ █ ▆ ▅ ▄ ▃ ▂ ▂ ▁ ▁ ▁ ▁ ▁ ▁ ▁  → 0 (decai)
  ```
  - **Causalidade:** $u(t) = 0$ para $t < 0$, logo $h(t) = 0$ para todo $t < 0$ (por exemplo, $h(-1) = (-1)e^{1}\cdot u(-1) = 0$). Logo, é **CAUSAL**.
  - **Estabilidade:** para $t \ge 0$, $t e^{-t} \ge 0$, então $|h(t)| = t e^{-t}$. Integração **por partes** até $T$, com $\int u\,dv = uv - \int v\,du$:
    - $u = t \implies du = dt$
    - $dv = e^{-t}\,dt \implies v = -e^{-t}$

    $$\int_{0}^{T} t e^{-t}\,dt = \Big[-t e^{-t}\Big]_{0}^{T} - \int_{0}^{T}\left(-e^{-t}\right)dt = \left(-T e^{-T} - 0\right) + \int_{0}^{T} e^{-t}\,dt$$
    $$\int_{0}^{T} e^{-t}\,dt = \Big[-e^{-t}\Big]_{0}^{T} = -e^{-T} + 1$$
    $$\int_{0}^{T} t e^{-t}\,dt = 1 - e^{-T} - T e^{-T}$$
    **Limite $T \to \infty$:**
    - $e^{-T} \to 0$;
    - $T e^{-T} = \frac{T}{e^{T}}$ é do tipo $\frac{\infty}{\infty}$. Por L'Hôpital, $\lim_{T\to\infty}\frac{T}{e^T} = \lim_{T\to\infty}\frac{1}{e^T} = 0$.

    $$\int_{-\infty}^{\infty} |h(t)|\,dt = 1 - 0 - 0 = 1 < \infty$$
    Logo, é **ESTÁVEL**.

- **(g) $h(t) = \left(2e^{-t} - e^{(t-100)/100}\right)u(t)$**
  ```
       t:−3  −2  −1   0   1   2   3   4   5   6   7   8
  |h(t)|: · · · · · · █ ▅ ▂ ▁ ▁ ▂ ▂ ▂ ▂ ▂ ▂ ▂ ▂ ▂ ▂ ▂ ▂  ... |h(300)| ≈ 7,4 (cresce sem limite)
  ```
  - **Causalidade:** $u(t) = 0$ para $t < 0$, logo $h(t) = 0$ para todo $t < 0$. Logo, é **CAUSAL**.
  - **Estabilidade:** reescrevendo a segunda parcela, $e^{(t-100)/100} = e^{t/100 - 1} = e^{-1}e^{t/100}$, que tem expoente **positivo** em $t$. Vamos provar a divergência **com conta**:
    - Pela desigualdade $|a - b| \ge b - a$ (válida para quaisquer reais):
      $$|h(t)| = \left|2e^{-t} - e^{(t-100)/100}\right| \ge e^{(t-100)/100} - 2e^{-t}, \quad t \ge 0$$
    - Integrando a cota inferior de $0$ até $T$:
      $$\int_{0}^{T} e^{(t-100)/100}\,dt = \Big[100\,e^{(t-100)/100}\Big]_{0}^{T} = 100\left(e^{(T-100)/100} - e^{-1}\right)$$
      $$\int_{0}^{T} 2e^{-t}\,dt = \Big[-2e^{-t}\Big]_{0}^{T} = 2\left(1 - e^{-T}\right)$$
      $$\int_{0}^{T}|h(t)|\,dt \ge 100\left(e^{(T-100)/100} - e^{-1}\right) - 2\left(1 - e^{-T}\right)$$
      *(Conferindo a primitiva: $\frac{d}{dt}\left[100\,e^{(t-100)/100}\right] = 100\cdot\frac{1}{100}e^{(t-100)/100} = e^{(t-100)/100}$ ✓.)*
    - Limite: quando $T \to \infty$, o expoente $\frac{T - 100}{100} \to +\infty$, logo $e^{(T-100)/100} \to +\infty$, enquanto $e^{-T} \to 0$:
      $$\int_{-\infty}^{\infty}|h(t)|\,dt \ge \lim_{T\to\infty}\left[100\left(e^{(T-100)/100} - e^{-1}\right) - 2\left(1 - e^{-T}\right)\right] = +\infty$$
      *(Exemplo: com $T = 300$, a cota inferior já vale $100(e^2 - e^{-1}) - 2 \approx 700{,}1$, e continua crescendo.)*
    Logo, o sistema é **INSTÁVEL**.

> **✅ Gabarito (Oppenheim 2.29):** (a) causal, estável; (b) não-causal, instável; (c) não-causal, estável; (d) não-causal, estável; (e) não-causal, estável; (f) causal, estável; (g) causal, instável. Todas as integrais acima também foram conferidas numericamente.

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

**Esboço da Figura P2.11:**
```
                         ┌───────┐
                    ┌───►│ h2[n] │─────┐
       ┌───────┐    │    └───────┘     ▼
x[n] ─►│ h1[n] │────●                 (+)───► y[n]
       └───────┘    │    ┌───────┐     ▲
                    └───►│ h3[n] │─────┘
                         └───────┘
```

1. **Leitura do diagrama:** a entrada $x[n]$ passa primeiro por $h_1[n]$. Chamemos de $v[n]$ a saída desse primeiro bloco:
   $$v[n] = x[n] * h_1[n]$$
2. **Ramo paralelo:** o sinal $v[n]$ é aplicado **ao mesmo tempo** aos blocos $h_2[n]$ e $h_3[n]$, e as duas saídas são **somadas** no nó $(+)$:
   $$y[n] = v[n] * h_2[n] + v[n] * h_3[n]$$
   Pela propriedade distributiva da convolução, colocamos $v[n]$ em evidência:
   $$y[n] = v[n] * \big(h_2[n] + h_3[n]\big)$$
   Logo, o bloco paralelo equivale a um único sistema com resposta ao impulso:
   $$h_{23}[n] = h_2[n] + h_3[n]$$
3. **Cascata (série):** substituindo $v[n] = x[n] * h_1[n]$ e usando a propriedade associativa:
   $$y[n] = \big(x[n] * h_1[n]\big) * h_{23}[n] = x[n] * \underbrace{\big(h_1[n] * h_{23}[n]\big)}_{h[n]}$$
   Portanto:
   $$\mathbf{h[n] = h_1[n] * \big(h_2[n] + h_3[n]\big)}$$

   **Redução do diagrama (paralelo → soma; cascata → convolução):**
   ```
   x[n] ─►│ h1[n] │───►│ h2[n] + h3[n] │───► y[n]

   x[n] ─►│ h[n] = h1[n] * (h2[n] + h3[n]) │───► y[n]
   ```

---

#### **Item (b): Avaliação explícita de $h[n]$**

**Passo 1 — Simplificar o bloco paralelo $h_2[n] + h_3[n] = \delta[n] + u[n-1]$.**

Vamos verificar amostra por amostra, separando em três casos:
- **Para $n < 0$** (ex.: $n = -1$): $\delta[-1] = 0$ e $u[-1-1] = u[-2] = 0$, logo $\delta[n] + u[n-1] = 0 + 0 = 0$.
- **Para $n = 0$:** $\delta[0] = 1$ e $u[0-1] = u[-1] = 0$, logo $\delta[0] + u[-1] = 1 + 0 = 1$.
- **Para $n \ge 1$** (ex.: $n = 1, 2, 3, \dots$): $\delta[n] = 0$ (pois $n \neq 0$) e $u[n-1] = 1$ (pois $n - 1 \ge 0$), logo $\delta[n] + u[n-1] = 0 + 1 = 1$.

Resumindo: a soma vale $0$ para $n < 0$ e $1$ para $n \ge 0$, que é exatamente a definição do degrau unitário:
$$h_2[n] + h_3[n] = u[n]$$

Portanto:
$$h[n] = h_1[n] * u[n]$$

**Passo 2 — Escrever $h_1[n] * u[n]$ como uma soma acumulada.**

Pela definição da soma de convolução:
$$h[n] = \sum_{k=-\infty}^{\infty} h_1[k]\,u[n-k]$$
O degrau $u[n-k]$ vale $1$ quando o seu argumento é não negativo:
$$n - k \ge 0 \iff k \le n$$
e vale $0$ quando $k > n$. Assim, os termos com $k > n$ são multiplicados por zero e somem, e os termos com $k \le n$ são multiplicados por $1$:
$$h[n] = \sum_{k=-\infty}^{n} h_1[k]$$
Ou seja, $h[n]$ é a **soma acumulada** (acumulador) de $h_1[k]$ até o instante $n$.

**Passo 3 — Descobrir onde $h_1[k]$ é não nulo e listar suas amostras.**

O pulso $u[k+2] - u[k-3]$:
- vale $0$ para $k < -2$ (os dois degraus desligados: $0 - 0$);
- vale $1$ para $-2 \le k \le 2$ ($u[k+2] = 1$ pois $k + 2 \ge 0$, e $u[k-3] = 0$ pois $k - 3 < 0$: $1 - 0 = 1$);
- vale $0$ para $k \ge 3$ (os dois degraus ligados: $1 - 1 = 0$).

Logo $h_1[k] = \left(\frac{1}{2}\right)^k$ somente para $k = -2, -1, 0, 1, 2$ (5 amostras):
- $h_1[-2] = \left(\frac{1}{2}\right)^{-2} = 2^2 = 4$
- $h_1[-1] = \left(\frac{1}{2}\right)^{-1} = 2^1 = 2$
- $h_1[0] = \left(\frac{1}{2}\right)^0 = 1$
- $h_1[1] = \left(\frac{1}{2}\right)^1 = \frac{1}{2}$
- $h_1[2] = \left(\frac{1}{2}\right)^2 = \frac{1}{4}$

**Passo 4 — Avaliar a soma acumulada nos três intervalos de $n$.**

- **Intervalo 1: $n < -2$ (ou seja, $n \le -3$).**
  O limite superior da soma é $k = n \le -3$, e todas as amostras $h_1[k]$ com $k \le -3$ são nulas:
  $$h[n] = \sum_{k=-\infty}^{n} 0 = 0, \quad \text{para } n \le -3$$

  **Esboço no eixo $k$ para $n = -3$** (alturas dos pirulitos fora de escala, valores escritos acima; a janela $u[n-k]$ vale $1$ de $k = -\infty$ até a frente $k = n$; ▓ = trecho efetivamente somado):
  ```
                      4
                      ●
                      │    2
                      │    ●    1
                      │    │    ●   1/2  1/4
                      │    │    │    ●    ●
  ─────•────•────•────┴────┴────┴────┴────┴────•────•────•─────────────────────► k
      -5   -4   -3   -2   -1    0    1    2    3    4    5
  ◄━━━━━━━━━━━━━━┫ frente k = n = -3
    sem sobreposição: a janela não alcança k = -2
  ```

- **Intervalo 2: $-2 \le n \le 2$.**
  As amostras não nulas acumuladas vão de $k = -2$ até $k = n$:
  $$h[n] = \sum_{k=-2}^{n} \left(\frac{1}{2}\right)^k$$
  Fórmula da PG finita: $\displaystyle\sum_{k=A}^{B} r^k = \frac{r^A - r^{B+1}}{1 - r}$, com $r = \frac{1}{2}$, $A = -2$ e $B = n$:
  $$h[n] = \frac{\left(\frac{1}{2}\right)^{-2} - \left(\frac{1}{2}\right)^{n+1}}{1 - \frac{1}{2}}$$
  Calculando o numerador e o denominador separadamente: $\left(\frac{1}{2}\right)^{-2} = 4$ e $1 - \frac{1}{2} = \frac{1}{2}$:
  $$h[n] = \frac{4 - \left(\frac{1}{2}\right)^{n+1}}{\frac{1}{2}}$$
  Dividir por $\frac{1}{2}$ é multiplicar por $2$:
  $$h[n] = 2\cdot 4 - 2\cdot\left(\frac{1}{2}\right)^{n+1}$$
  Como $2\cdot\left(\frac{1}{2}\right)^{n+1} = 2\cdot\frac{1}{2}\cdot\left(\frac{1}{2}\right)^{n} = \left(\frac{1}{2}\right)^{n}$:
  $$h[n] = 8 - \left(\frac{1}{2}\right)^n, \quad \text{para } -2 \le n \le 2$$

  **Esboço no eixo $k$ para $n = 0$** (alturas dos pirulitos fora de escala, valores escritos acima; a janela $u[n-k]$ vale $1$ de $k = -\infty$ até a frente $k = n$; ▓ = trecho efetivamente somado):
  ```
                      4
                      ●
                      │    2
                      │    ●    1
                      │    │    ●   1/2  1/4
                      │    │    │    ●    ●
  ─────•────•────•────┴────┴────┴────┴────┴────•────•────•─────────────────────► k
      -5   -4   -3   -2   -1    0    1    2    3    4    5
  ◄━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ frente k = n = 0
                      ▓▓▓▓▓▓▓▓▓▓▓
                      soma de k = -2 até k = n = 0
  ```

  **Conferência dos 5 valores (soma acumulada × fórmula):**

  | $n$ | Soma acumulada $\sum_{k=-2}^{n} h_1[k]$ | Fórmula $8 - (1/2)^n$ |
  |:---:|:---|:---|
  | $-2$ | $4$ | $8 - 4 = 4$ ✓ |
  | $-1$ | $4 + 2 = 6$ | $8 - 2 = 6$ ✓ |
  | $0$ | $6 + 1 = 7$ | $8 - 1 = 7$ ✓ |
  | $1$ | $7 + \frac{1}{2} = \frac{15}{2}$ | $8 - \frac{1}{2} = \frac{15}{2}$ ✓ |
  | $2$ | $\frac{15}{2} + \frac{1}{4} = \frac{31}{4}$ | $8 - \frac{1}{4} = \frac{31}{4}$ ✓ |

- **Intervalo 3: $n \ge 3$.**
  O limite superior $k = n \ge 3$ já ultrapassou a última amostra não nula ($k = 2$). As amostras com $3 \le k \le n$ são nulas, então a soma fica "congelada" no total das 5 amostras:
  $$h[n] = \sum_{k=-2}^{2} h_1[k] + \sum_{k=3}^{n} 0 = 4 + 2 + 1 + \frac{1}{2} + \frac{1}{4}$$
  Colocando tudo sobre o denominador $4$:
  $$h[n] = \frac{16}{4} + \frac{8}{4} + \frac{4}{4} + \frac{2}{4} + \frac{1}{4} = \frac{31}{4} = 7{,}75, \quad \text{para } n \ge 3$$

  **Esboço no eixo $k$ para $n = 4$** (alturas dos pirulitos fora de escala, valores escritos acima; a janela $u[n-k]$ vale $1$ de $k = -\infty$ até a frente $k = n$; ▓ = trecho efetivamente somado):
  ```
                      4
                      ●
                      │    2
                      │    ●    1
                      │    │    ●   1/2  1/4
                      │    │    │    ●    ●
  ─────•────•────•────┴────┴────┴────┴────┴────•────•────•─────────────────────► k
      -5   -4   -3   -2   -1    0    1    2    3    4    5
  ◄━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ frente k = n = 4
                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                      soma de k = -2 até k = 2
  ```

**Passo 5 — Conferir a passagem $n = 2 \to n = 3$ (continuidade do acumulador).**
- Pelo Intervalo 2 em $n = 2$: $h[2] = 8 - \frac{1}{4} = \frac{31}{4}$.
- Pelo Intervalo 3 em $n = 3$: $h[3] = \frac{31}{4}$.
- Como $h_1[3] = 0$, devemos ter $h[3] = h[2] + h_1[3] = \frac{31}{4} + 0 = \frac{31}{4}$ ✓.

**Expressão final de $h[n]$ (por partes e na forma compacta):**
$$h[n] = \begin{cases} 0, & n \le -3 \\[0.4em] 8 - \left(\dfrac{1}{2}\right)^n, & -2 \le n \le 2 \\[0.6em] \dfrac{31}{4}, & n \ge 3 \end{cases}$$
$$\mathbf{h[n] = \left[8 - \left(\frac{1}{2}\right)^n\right]\big(u[n+2] - u[n-3]\big) + \frac{31}{4}u[n-3]}$$

**Esboço de $h[n]$** (alturas aproximadas; valores exatos nos rótulos — sobe de $4$ até $7{,}75$ e fica constante a partir de $n = 2$):
```
                                 7,5  7,75  7,75  7,75  7,75
                            7     ●     ●     ●     ●     ●
                      6     ●     │     │     │     │     │
                      ●     │     │     │     │     │     │
                4     │     │     │     │     │     │     │
                ●     │     │     │     │     │     │     │
                │     │     │     │     │     │     │     │
                │     │     │     │     │     │     │     │
                │     │     │     │     │     │     │     │
────•─────•─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴───► n
   -4    -3    -2    -1     0     1     2     3     4     5
```

> **💡 Caminho alternativo (mesma resposta):** sem simplificar o paralelo, $h[n] = h_1[n] * \delta[n] + h_1[n] * u[n-1] = h_1[n] + \sum_{k=-\infty}^{n-1} h_1[k]$. Por exemplo, em $n = 0$: $h_1[0] + (h_1[-2] + h_1[-1]) = 1 + 4 + 2 = 7$ ✓.

---

#### **Itens (c), (d) e (e): Classificação de $h_1[n]$, $h_2[n]$ e $h_3[n]$**

- **(c) Para $h_1[n] = \left(\frac{1}{2}\right)^n (u[n+2] - u[n-3])$:**
  - **(i) Estável: SIM.** Calculando a soma absoluta (só há 5 amostras não nulas, todas positivas):
    $$\sum_{n=-\infty}^{\infty} |h_1[n]| = \sum_{n=-2}^{2} \left(\frac{1}{2}\right)^n = 4 + 2 + 1 + \frac{1}{2} + \frac{1}{4} = \frac{16 + 8 + 4 + 2 + 1}{4} = \frac{31}{4} = 7{,}75 < \infty$$
  - **(ii) Causal: NÃO.** Basta exibir uma amostra não nula em $n < 0$: $h_1[-1] = \left(\frac{1}{2}\right)^{-1} = 2 \neq 0$ (e também $h_1[-2] = 4 \neq 0$).
  - **(iii) Sem memória: NÃO.** Existe amostra não nula fora de $n = 0$: $h_1[1] = \left(\frac{1}{2}\right)^{1} = \frac{1}{2} \neq 0$. Logo $h_1[n]$ não é da forma $c\,\delta[n]$.

- **(d) Para $h_2[n] = \delta[n]$:**
  - **(i) Estável: SIM.** A única amostra não nula é $\delta[0] = 1$:
    $$\sum_{n=-\infty}^{\infty} |\delta[n]| = |\delta[0]| = 1 < \infty$$
  - **(ii) Causal: SIM.** Para todo $n < 0$ (ex.: $n = -1, -2, \dots$), $\delta[n] = 0$.
  - **(iii) Sem memória: SIM.** $h_2[n] = 1\cdot\delta[n]$, isto é, $c\,\delta[n]$ com $c = 1$. De fato, $y[n] = x[n] * \delta[n] = x[n]$: a saída só depende da entrada no mesmo instante.

- **(e) Para $h_3[n] = u[n-1]$:**
  - **(i) Estável: NÃO (Instável).** As amostras não nulas são $h_3[n] = 1$ para $n \ge 1$. Calculando a soma parcial até $N$:
    $$S_N = \sum_{n=1}^{N} |u[n-1]| = \sum_{n=1}^{N} 1 = N - 1 + 1 = N$$
    Tomando o limite:
    $$\sum_{n=-\infty}^{\infty} |h_3[n]| = \lim_{N\to\infty} S_N = \lim_{N\to\infty} N = \infty$$
  - **(ii) Causal: SIM.** $u[n-1] = 0$ sempre que $n - 1 < 0$, isto é, para todo $n \le 0$; em particular, $h_3[n] = 0$ para todo $n < 0$.
  - **(iii) Sem memória: NÃO.** $h_3[1] = u[0] = 1 \neq 0$, ou seja, há amostra não nula fora de $n = 0$.

---

## Questão 5.2 — [Haykin & Van Veen 2.12, págs. 156–157 (Bookman)]
**Para cada resposta ao impulso listada abaixo, determine se o sistema correspondente é (i) sem memória, (ii) causal e (iii) estável.**

> **Critérios usados em todos os itens:**
> - **Sem memória** $\iff h = c\,\delta$ (nenhum valor não nulo fora da origem). Para negar, basta **exibir um valor não nulo** fora da origem.
> - **Causal** $\iff h = 0$ para todo instante negativo. Para negar, basta **exibir um valor não nulo** num instante negativo.
> - **Estável (BIBO)** $\iff \int_{-\infty}^{\infty}|h(t)|\,dt < \infty$ (ou $\sum_{n}|h[n]| < \infty$). Calculamos a integral/soma **até o número**; quando diverge, calculamos a integral/soma **parcial** em forma fechada e tomamos o limite.

### **Resolução Passo a Passo (Itens a até k):**

- **(a) $h(t) = e^{-2|t|}$**
  - **Esboço:** pico em $t=0$; há valores para $t<0$ (não causal); decai dos dois lados (área finita).
    ```
                       •
                     ••│••
                •••••  │  •••••
    ───•••••••••───────┼───────•••••••••──►t

      -2      -1       0       1       2
    ```
  - **(i) Sem memória: Não.** Exemplo fora da origem: $h(1) = e^{-2|1|} = e^{-2} \approx 0{,}135 \neq 0$.
  - **(ii) Causal: Não.** Exemplo em instante negativo: $h(-0{,}5) = e^{-2|-0{,}5|} = e^{-1} \approx 0{,}368 \neq 0$.
  - **(iii) Estável: Sim.** Como $e^{-2|t|} > 0$, $|h(t)| = e^{-2|t|}$. Separando em $t < 0$ (onde $|t| = -t$) e $t \ge 0$ (onde $|t| = t$):
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \int_{-\infty}^{0} e^{2t}\,dt + \int_{0}^{\infty} e^{-2t}\,dt$$
    Primeira integral (primitiva $\frac{e^{2t}}{2}$):
    $$\int_{-\infty}^{0} e^{2t}\,dt = \left[\frac{e^{2t}}{2}\right]_{-\infty}^{0} = \frac{e^{0}}{2} - \lim_{t\to-\infty}\frac{e^{2t}}{2} = \frac{1}{2} - 0 = \frac{1}{2}$$
    Segunda integral (primitiva $-\frac{e^{-2t}}{2}$):
    $$\int_{0}^{\infty} e^{-2t}\,dt = \left[-\frac{e^{-2t}}{2}\right]_{0}^{\infty} = \lim_{t\to\infty}\left(-\frac{e^{-2t}}{2}\right) - \left(-\frac{e^{0}}{2}\right) = 0 + \frac{1}{2} = \frac{1}{2}$$
    Somando:
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \frac{1}{2} + \frac{1}{2} = 1 < \infty$$

- **(b) $h(t) = e^{2t}u(t-1)$**
  - **Esboço:** nulo para $t<1$ (causal); salta para $e^2$ em $t=1$ e **cresce** sem limite (↑ = fora da escala).
    ```
               │               •↑↑↑↑
               │              •
               │            ••
               │        ••••
    ───━━━━━━━━┼━━━━━━━•──────────────►t

      -1       0       1       2
    ```
  - **(i) Sem memória: Não.** Exemplo fora da origem: $h(2) = e^{4}u(1) = e^4 \approx 54{,}6 \neq 0$.
  - **(ii) Causal: Sim.** $u(t-1) = 0$ para $t < 1$; em particular, para todo $t < 0$ temos $h(t) = e^{2t}\cdot 0 = 0$.
  - **(iii) Estável: Não (Instável).** Para $t \ge 1$, $|h(t)| = e^{2t}$. Calculando a integral até um instante finito $T > 1$:
    $$\int_{1}^{T} e^{2t}\,dt = \left[\frac{e^{2t}}{2}\right]_{1}^{T} = \frac{e^{2T}}{2} - \frac{e^{2}}{2} = \frac{e^{2T} - e^{2}}{2}$$
    Tomando o limite $T \to \infty$:
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \lim_{T\to\infty} \frac{e^{2T} - e^{2}}{2} = \infty$$
    pois $e^{2T} \to \infty$.

  *(Observação: No Problema análogo 2.49(b) da 2ª edição em inglês da Wiley, este item aparece com expoente negativo $h(t) = e^{-2t}u(t-1)$, que é estável; porém, na edição brasileira da Bookman indicada na lista, o expoente é positivo $+2t$ e o sistema é **Instável**).*

- **(c) $h(t) = u(t+1) - 2u(t-1)$**
  - **Esboço:** vale $1$ em $[-1,1)$ (inclui $t<0$: não causal) e $-1$ para sempre a partir de $t=1$ (não decai).
    ```
            ••••••••••
                 │
    ───━━━━━─────┼──────────────────────►t
                 │
                 │    ••••••••••••••••

      -2   -1    0    1    2    3    4
    ```
  - **Destrinchando $h(t)$ por trechos:**
    - $t < -1$: $u(t+1) = 0$ e $u(t-1) = 0$, logo $h(t) = 0 - 0 = 0$.
    - $-1 \le t < 1$: $u(t+1) = 1$ e $u(t-1) = 0$, logo $h(t) = 1 - 0 = 1$.
    - $t \ge 1$: $u(t+1) = 1$ e $u(t-1) = 1$, logo $h(t) = 1 - 2 = -1$.
  - **(i) Sem memória: Não.** Exemplo fora da origem: $h(0{,}5) = 1 \neq 0$.
  - **(ii) Causal: Não.** Exemplo em instante negativo: $h(-0{,}5) = u(0{,}5) - 2u(-1{,}5) = 1 - 0 = 1 \neq 0$.
  - **(iii) Estável: Não (Instável).** Calculando a integral de $|h(t)|$ de $-1$ até um instante finito $T > 1$:
    $$\int_{-1}^{T} |h(t)|\,dt = \int_{-1}^{1} |1|\,dt + \int_{1}^{T} |-1|\,dt = \Big[t\Big]_{-1}^{1} + \Big[t\Big]_{1}^{T}$$
    $$= \big(1 - (-1)\big) + (T - 1) = 2 + T - 1 = T + 1$$
    Tomando o limite:
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \lim_{T\to\infty} (T + 1) = \infty$$

- **(d) $h(t) = 3\delta(t)$**
  - **Esboço:** só um impulso de área $3$ na origem: nada fora de $t=0$.
    ```
                 ▲ (3)
                 │
                 │
    ───━━━━━━━━━━│━━━━━━━━━━──►t

      -2   -1    0    1    2
    ```
  - **(i) Sem memória: Sim.** É da forma $c\,\delta(t)$ com $c = 3$. De fato, pela propriedade de amostragem:
    $$y(t) = \int_{-\infty}^{\infty} x(\tau)\,3\delta(t-\tau)\,d\tau = 3x(t)$$
    A saída só depende da entrada no mesmo instante $t$.
  - **(ii) Causal: Sim.** $\delta(t) = 0$ para todo $t \neq 0$; em particular, $h(t) = 0$ para todo $t < 0$.
  - **(iii) Estável: Sim.** Como $|3\delta(t)| = 3\delta(t)$ e a área do impulso unitário é $1$:
    $$\int_{-\infty}^{\infty} |3\delta(t)|\,dt = 3\int_{-\infty}^{\infty} \delta(t)\,dt = 3\cdot 1 = 3 < \infty$$

- **(e) $h(t) = \cos(\pi t)u(t)$**
  - **Esboço:** nulo para $t<0$ (causal); para $t \ge 0$ **oscila** entre $\pm 1$ sem decair.
    ```
               ••             •••             ••
               │ ••         ••   ••         ••
    ───━━━━━━━━┼───━───────━───────━───────━──────►t
               │    ••   ••         ••   ••
               │      •••             •••

      -1       0       1       2       3       4
    ```
  - **(i) Sem memória: Não.** Exemplo fora da origem: $h(1) = \cos(\pi)\cdot u(1) = -1 \neq 0$.
  - **(ii) Causal: Sim.** $u(t) = 0$ para $t < 0$, logo $h(t) = \cos(\pi t)\cdot 0 = 0$ para todo $t < 0$.
  - **(iii) Estável: Não (Instável).** Precisamos calcular $\int_{0}^{\infty} |\cos(\pi t)|\,dt$. O cosseno troca de sinal em $t = \frac{1}{2}, \frac{3}{2}, \frac{5}{2}, \dots$, então dividimos o eixo nesses pontos. Primitiva: $\int \cos(\pi t)\,dt = \frac{\text{sen}(\pi t)}{\pi}$.

    **Trecho inicial $[0, \frac{1}{2}]$** (onde $\cos(\pi t) \ge 0$, logo $|\cos(\pi t)| = \cos(\pi t)$):
    $$\int_{0}^{1/2} \cos(\pi t)\,dt = \left[\frac{\text{sen}(\pi t)}{\pi}\right]_{0}^{1/2} = \frac{\text{sen}(\pi/2)}{\pi} - \frac{\text{sen}(0)}{\pi} = \frac{1}{\pi} - 0 = \frac{1}{\pi}$$

    **Cada meio período completo $[k - \frac{1}{2},\ k + \frac{1}{2}]$, com $k = 1, 2, 3, \dots$:** nesse trecho, $\cos(\pi t)$ tem o sinal de $\cos(\pi k) = (-1)^k$, logo $|\cos(\pi t)| = (-1)^k \cos(\pi t)$. Calculando:
    $$\int_{k-1/2}^{k+1/2} \cos(\pi t)\,dt = \frac{\text{sen}\big(\pi k + \frac{\pi}{2}\big) - \text{sen}\big(\pi k - \frac{\pi}{2}\big)}{\pi}$$
    Usando $\text{sen}(\pi k + \frac{\pi}{2}) = \cos(\pi k) = (-1)^k$ e $\text{sen}(\pi k - \frac{\pi}{2}) = -\cos(\pi k) = -(-1)^k$:
    $$\int_{k-1/2}^{k+1/2} \cos(\pi t)\,dt = \frac{(-1)^k - \big(-(-1)^k\big)}{\pi} = \frac{2(-1)^k}{\pi}$$
    Multiplicando por $(-1)^k$ (o sinal do módulo) e usando $(-1)^k\cdot(-1)^k = 1$:
    $$\int_{k-1/2}^{k+1/2} |\cos(\pi t)|\,dt = (-1)^k\cdot\frac{2(-1)^k}{\pi} = \frac{2}{\pi}$$
    *Exemplo ($k = 1$, trecho $[\frac{1}{2}, \frac{3}{2}]$, onde o cosseno é negativo):* $-\left[\frac{\text{sen}(\pi t)}{\pi}\right]_{1/2}^{3/2} = -\frac{\text{sen}(3\pi/2) - \text{sen}(\pi/2)}{\pi} = -\frac{-1 - 1}{\pi} = \frac{2}{\pi}$ ✓.

    **Somando o trecho inicial e $N$ meios períodos** (de $0$ até $T_N = N + \frac{1}{2}$):
    $$\int_{0}^{N + 1/2} |\cos(\pi t)|\,dt = \frac{1}{\pi} + \underbrace{\frac{2}{\pi} + \frac{2}{\pi} + \dots + \frac{2}{\pi}}_{N \text{ parcelas}} = \frac{1}{\pi} + \frac{2N}{\pi} = \frac{1 + 2N}{\pi}$$
    Tomando o limite:
    $$\int_{-\infty}^{\infty} |h(t)|\,dt = \lim_{N\to\infty} \frac{1 + 2N}{\pi} = \infty$$

- **(f) $h[n] = 2^n u[-n]$**
  - **Esboço:** só existe para $n \le 0$ (inclui $n<0$: não causal); decai para $0$ quando $n \to -\infty$.
    ```
                                ●
                                │
                            ●   │
                        ●   │   │
    ────●───●───●───●───│───│───│───•───•────►n

       -6  -5  -4  -3  -2  -1   0   1   2
    ```
  - **(i) Sem memória: Não.** Exemplo fora da origem: $h[-1] = 2^{-1}u[1] = \frac{1}{2} \neq 0$.
  - **(ii) Causal: Não.** $u[-n] = 1$ para $-n \ge 0 \iff n \le 0$; o mesmo exemplo $h[-1] = \frac{1}{2} \neq 0$ ocorre em $n < 0$.
  - **(iii) Estável: Sim.** Como $2^n > 0$, $|h[n]| = 2^n$ para $n \le 0$:
    $$\sum_{n=-\infty}^{\infty} |h[n]| = \sum_{n=-\infty}^{0} 2^n$$
    Mudança de variável $m = -n$: quando $n = 0$, $m = 0$; quando $n \to -\infty$, $m \to +\infty$; e $2^n = 2^{-m} = \left(\frac{1}{2}\right)^m$:
    $$\sum_{n=-\infty}^{0} 2^n = \sum_{m=0}^{\infty} \left(\frac{1}{2}\right)^m$$
    PG infinita com primeiro termo $\left(\frac{1}{2}\right)^0 = 1$ e razão $r = \frac{1}{2}$ ($|r| < 1$):
    $$\sum_{m=0}^{\infty} \left(\frac{1}{2}\right)^m = \frac{1}{1 - \frac{1}{2}} = \frac{1}{\frac{1}{2}} = 2 < \infty$$
    *(Conferência pelos primeiros termos: $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots \to 2$.)*

- **(g) $h[n] = e^{2n}u[n-1]$**
  - **Esboço:** nulo para $n \le 0$ (causal); $e^2 \approx 7{,}4$, $e^4 \approx 54{,}6$, $e^6 \approx 403$ (↑ = fora da escala): **cresce**.
    ```
                │       ●   ↑
                │       │   │
                │       │   │
                │       │   │
                │       │   │
                │       │   │
                │   ●   │   │
    ────•───•───•───│───│───│────►n

       -2  -1   0   1   2   3
    ```
  - **(i) Sem memória: Não.** Exemplo fora da origem: $h[1] = e^{2}u[0] = e^2 \approx 7{,}389 \neq 0$.
  - **(ii) Causal: Sim.** $u[n-1] = 0$ para $n - 1 < 0 \iff n \le 0$; em particular, $h[n] = 0$ para todo $n < 0$.
  - **(iii) Estável: Não (Instável).** Escrevendo $e^{2n} = (e^2)^n$, a razão é $r = e^2 \approx 7{,}389$. Soma parcial de $n = 1$ até $N$ pela PG finita ($A = 1$, $B = N$):
    $$S_N = \sum_{n=1}^{N} (e^2)^n = \frac{(e^2)^1 - (e^2)^{N+1}}{1 - e^2} = \frac{e^2\big(1 - e^{2N}\big)}{1 - e^2} = \frac{e^2\big(e^{2N} - 1\big)}{e^2 - 1}$$
    Tomando o limite (o denominador $e^2 - 1 \approx 6{,}389$ é uma constante positiva e $e^{2N} \to \infty$):
    $$\sum_{n=-\infty}^{\infty} |h[n]| = \lim_{N\to\infty} \frac{e^2\big(e^{2N} - 1\big)}{e^2 - 1} = \infty$$

- **(h) $h[n] = \cos\left(\frac{1}{8}\pi n\right)\big\{u[n] - u[n-10]\big\}$**
  - **Esboço:** 10 amostras ($0 \le n \le 9$), nulo fora delas: duração finita.
    ```
              ●  ●
              │  │  ●  ●
    ────•──•──│──│──│──│──•──│──│──│──│──│──•──•────►n
              │              ●  ●  │  │  │
              │                    ●  ●  ●

       -2 -1  0  1  2  3  4  5  6  7  8  9  10 11
    ```
  - **Destrinchando o pulso:** $u[n] - u[n-10]$ vale $0$ para $n < 0$ ($0 - 0$), vale $1$ para $0 \le n \le 9$ ($1 - 0$) e vale $0$ para $n \ge 10$ ($1 - 1$). Logo $h[n]$ tem no máximo 10 amostras não nulas, em $n = 0, 1, \dots, 9$.
  - **(i) Sem memória: Não.** Exemplo fora da origem: $h[1] = \cos(\pi/8) \approx 0{,}924 \neq 0$.
  - **(ii) Causal: Sim.** Para todo $n < 0$, o pulso vale $0$, logo $h[n] = 0$.
  - **(iii) Estável: Sim.** Listando as 10 amostras:

    | $n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    | $\cos(\pi n/8)$ | $1$ | $0{,}924$ | $0{,}707$ | $0{,}383$ | $0$ | $-0{,}383$ | $-0{,}707$ | $-0{,}924$ | $-1$ | $-0{,}924$ |

    Agrupando os módulos iguais ($|\cos(\pi/8)|$ aparece em $n = 1, 7, 9$; $|\cos(\pi/4)| = \frac{\sqrt{2}}{2}$ em $n = 2, 6$; $|\cos(3\pi/8)|$ em $n = 3, 5$; o valor $1$ em $n = 0, 8$; e $0$ em $n = 4$):
    $$\sum_{n=0}^{9} |h[n]| = 2\cdot 1 + 3\cos\left(\frac{\pi}{8}\right) + 2\cdot\frac{\sqrt{2}}{2} + 2\cos\left(\frac{3\pi}{8}\right) + 0$$
    $$= 2 + 3(0{,}9239) + 1{,}4142 + 2(0{,}3827) = 2 + 2{,}7716 + 1{,}4142 + 0{,}7654 \approx 6{,}95 < \infty$$
    *(Cota rápida que também prova a estabilidade: como $|\cos(\theta)| \le 1$ para todo $\theta$, cada um dos 10 termos é $\le 1$, logo a soma é $\le 10\cdot 1 = 10 < \infty$.)*

- **(i) $h[n] = 2u[n] - 2u[n-1]$** *(Atenção: Pegadinha Clássica de Prova!)*
  - **Esboço:** só uma amostra, de valor $2$, em $n=0$.
    ```
                    ●
                    │
    ────•───•───•───│───•───•───•────►n

       -3  -2  -1   0   1   2   3
    ```
  - **Simplificação algébrica prévia:** colocando o $2$ em evidência, $h[n] = 2\big(u[n] - u[n-1]\big)$. Verificando a diferença amostra por amostra:
    - $n \le -1$: $u[n] = 0$ e $u[n-1] = 0$, logo $u[n] - u[n-1] = 0 - 0 = 0$.
    - $n = 0$: $u[0] = 1$ e $u[-1] = 0$, logo $u[0] - u[-1] = 1 - 0 = 1$.
    - $n \ge 1$: $u[n] = 1$ e $u[n-1] = 1$, logo $u[n] - u[n-1] = 1 - 1 = 0$.

    A diferença vale $1$ só em $n = 0$ e $0$ em todo o resto, que é exatamente $\delta[n]$. Portanto:
    $$h[n] = 2\delta[n]$$
  - **(i) Sem memória: Sim.** $h[n] = 2\delta[n]$ é da forma $c\,\delta[n]$ com $c = 2$; logo $y[n] = x[n] * 2\delta[n] = 2x[n]$.
  - **(ii) Causal: Sim.** $h[n] = 2\delta[n] = 0$ para todo $n < 0$.
  - **(iii) Estável: Sim.** A única amostra não nula é $h[0] = 2$:
    $$\sum_{n=-\infty}^{\infty} |2\delta[n]| = |h[0]| = 2 < \infty$$

- **(j) $h[n] = \text{sen}\left(\frac{1}{2}\pi n\right)$**
  - **Esboço:** padrão $0, 1, 0, -1$ repetido para sempre, inclusive em $n<0$: **oscila** sem decair.
    ```
              ●        │  ●           ●
    ────│──•──│──•──│──•──│──•──│──•──│──•──│────►n
        ●           ●  │        ●           ●

       -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7
    ```
  - **(i) Sem memória: Não.** Exemplo fora da origem: $h[1] = \text{sen}(\pi/2) = 1 \neq 0$.
  - **(ii) Causal: Não.** Exemplo em instante negativo: $h[-1] = \text{sen}(-\pi/2) = -1 \neq 0$.
  - **(iii) Estável: Não (Instável).** Calculando as amostras de um bloco de 4 valores consecutivos ($n = 0, 1, 2, 3$):
    - $h[0] = \text{sen}(0) = 0$;
    - $h[1] = \text{sen}(\pi/2) = 1$;
    - $h[2] = \text{sen}(\pi) = 0$;
    - $h[3] = \text{sen}(3\pi/2) = -1$.

    Como $\text{sen}\left(\frac{\pi}{2}(n + 4)\right) = \text{sen}\left(\frac{\pi n}{2} + 2\pi\right) = \text{sen}\left(\frac{\pi n}{2}\right)$, a sequência se repete a cada 4 amostras ($0, 1, 0, -1, 0, 1, 0, -1, \dots$). A soma dos módulos em **cada** bloco de 4 amostras é:
    $$|0| + |1| + |0| + |-1| = 2$$
    Soma parcial com $N$ blocos (de $n = 0$ até $n = 4N - 1$):
    $$S_N = \sum_{n=0}^{4N-1} \left|\text{sen}\left(\frac{\pi n}{2}\right)\right| = \underbrace{2 + 2 + \dots + 2}_{N \text{ blocos}} = 2N$$
    Como a soma total (de $-\infty$ a $+\infty$) é maior ou igual a qualquer soma parcial de termos não negativos:
    $$\sum_{n=-\infty}^{\infty} |h[n]| \ge \lim_{N\to\infty} 2N = \infty$$

- **(k) $h[n] = \delta[n] + \text{sen}(\pi n)$** *(Atenção: Segunda Pegadinha Clássica!)*
  - **Esboço:** só uma amostra, de valor $1$, em $n=0$.
    ```
                    ●
    ────•───•───•───│───•───•───•────►n

       -3  -2  -1   0   1   2   3
    ```
  - **Simplificação algébrica prévia:** a variável discreta $n$ assume **apenas valores inteiros**. Calculando $\text{sen}(\pi n)$ amostra por amostra:
    - $n = 0$: $\text{sen}(0) = 0$;
    - $n = 1$: $\text{sen}(\pi) = 0$;
    - $n = -1$: $\text{sen}(-\pi) = 0$;
    - $n = 2$: $\text{sen}(2\pi) = 0$;
    - $n = -2$: $\text{sen}(-2\pi) = 0$.

    Em geral, $\text{sen}(\pi n) = 0$ para todo $n \in \mathbb{Z}$, pois os zeros do seno são exatamente os múltiplos inteiros de $\pi$. Portanto:
    $$h[n] = \delta[n] + 0 = \delta[n]$$
  - **(i) Sem memória: Sim.** $h[n] = 1\cdot\delta[n]$, logo $y[n] = x[n]$.
  - **(ii) Causal: Sim.** $h[n] = \delta[n] = 0$ para todo $n < 0$.
  - **(iii) Estável: Sim.** A única amostra não nula é $h[0] = 1$:
    $$\sum_{n=-\infty}^{\infty} |\delta[n]| = |h[0]| = 1 < \infty$$

**📋 Quadro-resumo da Questão 5.2:**

| Item | Sem memória | Causal | Estável |
|:---:|:---:|:---:|:---:|
| (a) | Não | Não | Sim ($= 1$) |
| (b) | Não | Sim | Não |
| (c) | Não | Não | Não |
| (d) | Sim | Sim | Sim ($= 3$) |
| (e) | Não | Sim | Não |
| (f) | Não | Não | Sim ($= 2$) |
| (g) | Não | Sim | Não |
| (h) | Não | Sim | Sim ($\approx 6{,}95$) |
| (i) | Sim | Sim | Sim ($= 2$) |
| (j) | Não | Não | Não |
| (k) | Sim | Sim | Sim ($= 1$) |

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
Partimos da equação dada:
$$y[n] + \frac{1}{2}y[n-1] - \frac{1}{3}y[n-3] = x[n] + 2x[n-2]$$
Passando os termos $\frac{1}{2}y[n-1]$ e $-\frac{1}{3}y[n-3]$ para o lado direito (trocando os sinais):
$$y[n] = -\frac{1}{2}y[n-1] + \frac{1}{3}y[n-3] + x[n] + 2x[n-2]$$
Escrevendo explicitamente os termos que faltam com coeficiente zero ($y[n-2]$ e $x[n-1]$):
$$y[n] = -\frac{1}{2}y[n-1] + 0\cdot y[n-2] + \frac{1}{3}y[n-3] + x[n] + 0\cdot x[n-1] + 2x[n-2]$$
Comparando com a forma padrão $y[n] + a_1 y[n-1] + a_2 y[n-2] + a_3 y[n-3] = b_0 x[n] + b_1 x[n-1] + b_2 x[n-2]$:
- Realimentação (saída): $a_1 = \frac{1}{2}$, $a_2 = 0$, $a_3 = -\frac{1}{3}$ $\implies$ ganhos no diagrama $-a_1 = -\frac{1}{2}$, $-a_2 = 0$, $-a_3 = +\frac{1}{3}$.
- Alimentação direta (entrada): $b_0 = 1$, $b_1 = 0$, $b_2 = 2$.
- Ordem: o maior atraso em $y$ é $3$ ($N = 3$); o maior atraso em $x$ é $2$ ($M = 2$).

#### **Passo 2: Equações e Diagrama para a Forma Direta I**
Separamos a equação em duas, usando o sinal intermediário $w[n]$ (o lado das entradas):
$$\begin{aligned}
w[n] &= x[n] + 2x[n-2] \\
y[n] &= w[n] - \frac{1}{2}y[n-1] + \frac{1}{3}y[n-3]
\end{aligned}$$
**Verificação:** substituindo a primeira equação na segunda, obtemos $y[n] = x[n] + 2x[n-2] - \frac{1}{2}y[n-1] + \frac{1}{3}y[n-3]$, que é exatamente a equação do Passo 1 ✓.

*(Na coluna da entrada precisamos de $M = 2$ atrasos $S$ para chegar em $x[n-2]$, e na coluna da saída precisamos de $N = 3$ atrasos $S$ para chegar em $y[n-3]$, totalizando $M + N = 5$ blocos $S$).*

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
Permutamos a ordem dos dois subsistemas (primeiro a realimentação, depois a combinação das entradas), através do estado intermediário central $f[n]$, que exige apenas $\max(N, M) = \max(3, 2) = 3$ blocos de atraso $S$ compartilhados:
$$\begin{aligned}
f[n] &= x[n] - \frac{1}{2}f[n-1] + \frac{1}{3}f[n-3] \\
y[n] &= f[n] + 2f[n-2]
\end{aligned}$$

**Verificação por eliminação (prova de que a Forma Direta II reproduz a equação original):**
A primeira equação, reorganizada, diz que para **qualquer** instante $m$:
$$f[m] + \frac{1}{2}f[m-1] - \frac{1}{3}f[m-3] = x[m] \qquad (\star)$$
Agora montamos o lado esquerdo da equação original usando $y[n] = f[n] + 2f[n-2]$:
- $y[n] = f[n] + 2f[n-2]$
- $y[n-1] = f[n-1] + 2f[n-3]$
- $y[n-3] = f[n-3] + 2f[n-5]$

Logo:
$$y[n] + \frac{1}{2}y[n-1] - \frac{1}{3}y[n-3] = \big(f[n] + 2f[n-2]\big) + \frac{1}{2}\big(f[n-1] + 2f[n-3]\big) - \frac{1}{3}\big(f[n-3] + 2f[n-5]\big)$$
Separando os termos "sem o fator 2" dos termos "com o fator 2":
$$= \Big[f[n] + \frac{1}{2}f[n-1] - \frac{1}{3}f[n-3]\Big] + 2\Big[f[n-2] + \frac{1}{2}f[n-3] - \frac{1}{3}f[n-5]\Big]$$
O primeiro colchete é $(\star)$ com $m = n$, ou seja, vale $x[n]$. O segundo colchete é $(\star)$ com $m = n - 2$, ou seja, vale $x[n-2]$. Portanto:
$$y[n] + \frac{1}{2}y[n-1] - \frac{1}{3}y[n-3] = x[n] + 2x[n-2] \quad ✓$$

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
A equação diferencial de 2ª ordem ($N = 2$), escrita com todos os coeficientes (inclusive os nulos) e com as derivadas de $x$ em ordem decrescente:
$$\frac{d^2}{dt^2}y(t) + 0\cdot\frac{d}{dt}y(t) + 3y(t) = 2\frac{d^2}{dt^2}x(t) + \frac{d}{dt}x(t) + 0\cdot x(t)$$
Notação: $v^{(k)}(t)$ é a $k$-ésima integral sucessiva de $v$:
$$v^{(1)}(t) = \int_{-\infty}^{t} v(\tau)\,d\tau, \qquad v^{(2)}(t) = \int_{-\infty}^{t} v^{(1)}(\tau)\,d\tau$$
Hipótese: **condições iniciais nulas** (o sistema está em repouso; todos os sinais e suas derivadas valem $0$ em $t \to -\infty$).

**1ª integração (de $-\infty$ até $t$), termo a termo:**
- $\displaystyle\int_{-\infty}^{t} \frac{d^2 y}{d\tau^2}\,d\tau = \frac{dy}{dt}(t) - \underbrace{\frac{dy}{dt}(-\infty)}_{0} = \frac{dy}{dt}(t)$
- $\displaystyle\int_{-\infty}^{t} 3y(\tau)\,d\tau = 3y^{(1)}(t)$
- $\displaystyle\int_{-\infty}^{t} 2\frac{d^2 x}{d\tau^2}\,d\tau = 2\left[\frac{dx}{dt}(t) - \underbrace{\frac{dx}{dt}(-\infty)}_{0}\right] = 2\frac{dx}{dt}(t)$
- $\displaystyle\int_{-\infty}^{t} \frac{dx}{d\tau}\,d\tau = x(t) - \underbrace{x(-\infty)}_{0} = x(t)$

Resultado após a 1ª integração:
$$\frac{dy}{dt}(t) + 3y^{(1)}(t) = 2\frac{dx}{dt}(t) + x(t)$$

**2ª integração (de $-\infty$ até $t$), termo a termo:**
- $\displaystyle\int_{-\infty}^{t} \frac{dy}{d\tau}\,d\tau = y(t) - \underbrace{y(-\infty)}_{0} = y(t)$
- $\displaystyle\int_{-\infty}^{t} 3y^{(1)}(\tau)\,d\tau = 3y^{(2)}(t)$
- $\displaystyle\int_{-\infty}^{t} 2\frac{dx}{d\tau}\,d\tau = 2\big[x(t) - \underbrace{x(-\infty)}_{0}\big] = 2x(t)$
- $\displaystyle\int_{-\infty}^{t} x(\tau)\,d\tau = x^{(1)}(t)$

Resultado após a 2ª integração:
$$y(t) + 3y^{(2)}(t) = 2x(t) + x^{(1)}(t)$$
Isolando $y(t)$:
$$y(t) = -3y^{(2)}(t) + 2x(t) + x^{(1)}(t)$$
Os coeficientes são: $a_1 = 0$, $a_0 = 3$ (logo os ganhos de realimentação são $-a_1 = 0$ e $-a_0 = -3$) e $b_2 = 2$, $b_1 = 1$, $b_0 = 0$.

#### **Passo 2: Equações e Diagrama para a Forma Direta I**
$$\begin{aligned}
w(t) &= 2x(t) + x^{(1)}(t) \\
y(t) &= w(t) - 3y^{(2)}(t)
\end{aligned}$$
**Verificação:** substituindo $w(t)$ na segunda equação, $y(t) = 2x(t) + x^{(1)}(t) - 3y^{(2)}(t)$, que é a equação integral do Passo 1 ✓.

*(Na coluna da entrada usamos 1 integrador para gerar $x^{(1)}$; como $b_0 = 0$, não é preciso gerar $x^{(2)}$. Na coluna da saída usamos 2 integradores para gerar $y^{(1)}$ e $y^{(2)}$; o ganho de $y^{(1)}$ é $-a_1 = 0$, então esse ramo não é desenhado.)*

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

**Verificação por eliminação (prova de que a Forma Direta II reproduz a equação integral):**
A primeira equação, reorganizada, diz que:
$$f(t) + 3f^{(2)}(t) = x(t) \qquad (\star\star)$$
Integrando $(\star\star)$ uma vez de $-\infty$ até $t$ (condições iniciais nulas), cada termo ganha um índice de integração:
$$f^{(1)}(t) + 3f^{(3)}(t) = x^{(1)}(t) \qquad (\star\star\star)$$
Agora montamos o lado esquerdo da equação integral usando $y = 2f + f^{(1)}$:
- $y(t) = 2f(t) + f^{(1)}(t)$
- $y^{(2)}(t) = 2f^{(2)}(t) + f^{(3)}(t)$ (integrando duas vezes cada parcela)

Logo:
$$y(t) + 3y^{(2)}(t) = 2f(t) + f^{(1)}(t) + 3\big(2f^{(2)}(t) + f^{(3)}(t)\big) = 2f(t) + f^{(1)}(t) + 6f^{(2)}(t) + 3f^{(3)}(t)$$
Reagrupando:
$$= 2\Big[f(t) + 3f^{(2)}(t)\Big] + \Big[f^{(1)}(t) + 3f^{(3)}(t)\Big]$$
Pelo $(\star\star)$, o primeiro colchete vale $x(t)$; pelo $(\star\star\star)$, o segundo colchete vale $x^{(1)}(t)$. Portanto:
$$y(t) + 3y^{(2)}(t) = 2x(t) + x^{(1)}(t) \quad ✓$$

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
