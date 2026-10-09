# Guia Algorítmico, Macetes e Exemplos Clássicos: Sinais e Sistemas

Este guia apresenta passos estruturados, heurísticas visuais e **exemplos extraídos diretamente da literatura clássica (Oppenheim, Lathi e Haykin)**, classificados por nível de dificuldade. 

*As resoluções foram abertas linha a linha, simulando a escrita à mão no papel.*

---

## PARTE 1: PROPRIEDADES DOS SINAIS

### 1. Sinal Par e Ímpar
**Algoritmo:** Calcule $x(-t)$. Se $x(-t) = x(t)$ (Par). Se $x(-t) = -x(t)$ (Ímpar).
> **💡 Macete:** Par $\times$ Par = Par, Ímpar $\times$ Ímpar = Par, Par $\times$ Ímpar = Ímpar. 

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** $x(t) = \cos(t)$.
    Substituindo o tempo:
    $$x(-t) = \cos(-t)$$
    Sendo o cosseno uma função par:
    $$x(-t) = \cos(t) = x(t)$$
    Logo, é **Par**.

*   **Médio:** $x(t) = t \cdot \sin(t)$.
    Calculando a reflexão no tempo:
    $$x(-t) = (-t) \cdot \sin(-t)$$
    Sabendo que o seno é ímpar, ou seja, $\sin(-t) = -\sin(t)$:
    $$x(-t) = (-t) \cdot (-\sin(t))$$
    $$x(-t) = t \cdot \sin(t)$$
    $$x(-t) = x(t)$$
    Logo, é **Par**.

*   **Difícil:** O Degrau Unitário $u(t)$. 
    A função original $u(t)$ não é nem par nem ímpar. O *Oppenheim* pede a decomposição.
    Parte Par:
    $$x_p(t) = \frac{u(t) + u(-t)}{2} = \frac{1}{2}$$
    Parte Ímpar:
    $$x_i(t) = \frac{u(t) - u(-t)}{2} = \frac{1}{2}\text{sgn}(t)$$

### 2. Sinal de Energia ou de Potência
**Algoritmo:** Calcule a energia total. Se convergir, é Energia. Se explodir pra infinito, calcule a potência média.
> **💡 Macete:** Sinais que "morrem" em infinito são de Energia. Sinais que duram para sempre oscilando ou constantes são de Potência.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** Pulso retangular $x(t) = 1$ para $0 \le t \le 2$, e $0$ para os demais.
    Calculando Energia:
    $$E = \int_{0}^{2} (1)^2 dt$$
    $$E = [t]_{0}^{2} = 2 \text{ Joules}$$
    Sendo $E$ finito, é um **Sinal de Energia** (Potência = 0).

*   **Médio:** Exponencial decrescente $x(t) = e^{-at}u(t)$, com $a > 0$. 
    Energia:
    $$E = \int_{0}^{\infty} (e^{-at})^2 dt$$
    $$E = \int_{0}^{\infty} e^{-2at} dt$$
    $$E = \left[ \frac{e^{-2at}}{-2a} \right]_{0}^{\infty}$$
    $$E = 0 - \left( \frac{1}{-2a} \right) = \frac{1}{2a}$$
    Como 'a' é positivo, o valor é finito. Sinal de **Energia**.

*   **Difícil:** Senóide genérica $x(t) = A\cos(\omega_0 t)$.
    A integral de energia vai dar $\infty$. Indo pra Potência num período $T$:
    $$P = \frac{1}{T} \int_{-T/2}^{T/2} A^2 \cos^2(\omega_0 t) dt$$
    $$P = \frac{A^2}{T} \int_{-T/2}^{T/2} \left( \frac{1 + \cos(2\omega_0 t)}{2} \right) dt$$
    A integral do cosseno de $2\omega_0 t$ em um período zera:
    $$P = \frac{A^2}{T} \left[ \frac{t}{2} \right]_{-T/2}^{T/2} = \frac{A^2}{2}$$
    Como convergiu, Sinal de **Potência**.

---

## PARTE 2: PROPRIEDADES DOS SISTEMAS
Um sistema mapeia uma entrada $x(t)$ para uma saída $y(t)$.

### 3. Memória (Estáticos vs Dinâmicos)
**Algoritmo:** Se $y(t_0)$ precisa de $x(t)$ em instante diferente de $t_0$, tem memória.
> **💡 Macete:** Integrais, derivadas e modificadores de tempo (como $t-1$) exigem memória.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** $y(t) = 5 \cdot x(t)$.
    Para saber a saída em $t=2$:
    $$y(2) = 5 \cdot x(2)$$
    Só precisou do presente. **Sem Memória**.

*   **Médio:** O atraso ideal $y(t) = x(t-2)$.
    Para saber a saída em $t=0$:
    $$y(0) = x(0-2) = x(-2)$$
    Precisou de informação armazenada 2 segundos atrás. **Com Memória**.

*   **Difícil:** O sistema reverso $y(t) = x(-t)$. 
    Vamos testar $t = 4$:
    $$y(4) = x(-4) \quad \text{(Precisou do passado)}$$
    Vamos testar $t = -4$:
    $$y(-4) = x(-(-4)) = x(4) \quad \text{(Precisou do futuro)}$$
    Como precisa de tempos distintos, tem **Memória**.

### 4. Causalidade
**Algoritmo:** Se o sistema precisa do futuro para dar uma resposta hoje, é Não-Causal.
> **💡 Macete:** Operadores $+t$ dentro do 'x', ou "compressões" temporais costumam ser não-causais.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** $y[n] = x[n] + x[n-1]$.
    Para a amostra atual:
    $$y[1] = x[1] + x[0]$$
    Usa presente e passado. **Causal**.

*   **Médio:** Avanço temporal $y(t) = x(t+2)$. 
    Testando $t=0$:
    $$y(0) = x(0+2) = x(2)$$
    Preciso do futuro ($t=2$) hoje. **Não-Causal**.

*   **Difícil:** Expansão/Compressão $y(t) = x(2t)$.
    Teste um instante $t=2$:
    $$y(2) = x(2 \cdot 2)$$
    $$y(2) = x(4)$$
    Para calcular o hoje ($t=2$), fomos buscar um valor lá na frente ($t=4$). **Não-Causal**.

### 5. Linearidade
**Algoritmo:** Aplique $x_3(t) = ax_1(t)+bx_2(t)$ e veja se a saída resultante bate com $a y_1(t) + b y_2(t)$.
> **💡 Macete:** Constantes somadas ou o sinal de entrada enjaulado em funções ($x^2$, seno) matam a linearidade.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** $y(t) = 3 \cdot x(t)$.
    Entrada combinada:
    $$y_3(t) = 3 \cdot (ax_1(t) + bx_2(t))$$
    $$y_3(t) = a \cdot [3x_1(t)] + b \cdot [3x_2(t)]$$
    $$y_3(t) = a \cdot y_1(t) + b \cdot y_2(t)$$
    Idêntico. **Linear**.

*   **Médio:** Offset de nível DC $y(t) = x(t) + 3$.
    Regra básica: entrada zero = saída zero.
    $$x(t) = 0$$
    $$y(t) = 0 + 3 = 3$$
    A regra falhou. **Não-Linear**.

*   **Difícil:** O ganho variante $y(t) = t \cdot x(t)$.
    Combinação nas entradas:
    $$x_3(t) = a \cdot x_1(t) + b \cdot x_2(t)$$
    Passando $x_3$ pelo sistema:
    $$y_3(t) = t \cdot x_3(t)$$
    $$y_3(t) = t \cdot [a \cdot x_1(t) + b \cdot x_2(t)]$$
    Distribuindo o $t$:
    $$y_3(t) = a \cdot [t \cdot x_1(t)] + b \cdot [t \cdot x_2(t)]$$
    $$y_3(t) = a \cdot y_1(t) + b \cdot y_2(t)$$
    Não quebrou a superposição. Logo, **Linear**.

### 6. Invariância no Tempo (LTI vs Variante)
**Algoritmo:** Atrase a entrada $\to y_1$. Atrase todas as referências a $t$ na equação $\to y_2$. Compare.
> **💡 Macete:** Variáveis de tempo ($t$) "soltas" indicam Variância no tempo.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** $y(t) = 2x(t)$.
    Passo 1 (atrasa entrada):
    $$y_1(t) = 2 \cdot x(t-t_0)$$
    Passo 2 (atrasa o relógio geral):
    $$y_2(t) = 2 \cdot x(t-t_0)$$
    São iguais. **Invariante**.

*   **Médio:** $y(t) = t \cdot x(t)$. 
    Passo 1 (atrasa só a entrada $x$):
    $$y_1(t) = t \cdot x(t-t_0)$$
    Passo 2 (atrasa a variável global 't'):
    $$y_2(t) = (t-t_0) \cdot x(t-t_0)$$
    Avaliando: $y_1(t) \neq y_2(t)$. Logo, **Variante**.

*   **Difícil:** Compressão $y(t) = x(2t)$.
    Passo 1 (atrasa a entrada internamente):
    Seja $x_a(t) = x(t-t_0)$.
    $$y_1(t) = x_a(2t) = x(2t - t_0)$$
    Passo 2 (atrasa a variável de saída 't'):
    Substituímos todo "t" da fórmula original por "$(t-t_0)$":
    $$y_2(t) = y(t-t_0)$$
    $$y_2(t) = x(2 \cdot (t-t_0))$$
    $$y_2(t) = x(2t - 2t_0)$$
    Comparando as duas:
    $$x(2t - t_0) \neq x(2t - 2t_0)$$
    **Variante no tempo**.

### 7. Estabilidade BIBO
**Algoritmo:** Assuma entrada limitada $|x(t)| \le B_x$. Veja se a conta final da saída é menor que $\infty$.
> **💡 Macete:** Integradores com limites abertos tendem a instabilizar com entradas constantes.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** Divisor $y(t) = \frac{1}{2} x(t)$.
    Aplicando limite $B_x$:
    $$|y(t)| = \left| \frac{1}{2} x(t) \right|$$
    $$|y(t)| \le \frac{1}{2} B_x < \infty$$
    Sendo a saída finita, **Estável**.

*   **Médio:** Integrador $y(t) = \int_{-\infty}^{t} x(\tau) d\tau$.
    Vamos dar um contra-exemplo limitado. Escolha $x(t) = u(t)$ (Degrau unitário, limitado a $B_x = 1$).
    Para um $t > 0$:
    $$y(t) = \int_{0}^{t} (1) d\tau$$
    $$y(t) = [ \tau ]_{0}^{t} = t$$
    Se avaliarmos o sistema no limite $t \to \infty$, a saída explode pra infinito, mesmo com a entrada presa em 1.
    **Instável**.

*   **Difícil:** Sistema exponencial $y(t) = e^{x(t)}$.
    Assumimos que a entrada tem um pico máximo: $|x(t)| \le B_x$ (onde $B_x$ é finito, tipo 10, 20...).
    Calculando o limite máximo da saída:
    $$|y(t)| = |e^{x(t)}|$$
    $$|y(t)| \le e^{B_x}$$
    Uma constante ("e") elevada a um número finito ($B_x$) sempre gera um número finito, não importa o seu tamanho.
    $$e^{B_x} < \infty$$
    Como não explodiu para o infinito, é **Estável**.
