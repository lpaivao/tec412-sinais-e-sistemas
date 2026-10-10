# Guia Algorítmico, Macetes e Exemplos Clássicos: Sinais e Sistemas

Este guia apresenta passos estruturados, heurísticas visuais e exemplos classificados em **Fácil**, **Médio** e **Nível de Prova**, com base nos livros clássicos e nas suas **próprias listas e provas (Prof. Edgar Silva Júnior)**.

*As resoluções foram abertas linha a linha, simulando a escrita à mão no papel.*

---

## PARTE 1: PROPRIEDADES DOS SINAIS

### 1. Sinal Par, Ímpar ou Nenhum dos dois
Um sinal é par se apresenta simetria em relação ao eixo vertical, e ímpar se apresenta anti-simetria.

**Algoritmo de Resolução:**
1. **Passo 1:** Escreva a expressão original do sinal $x(t)$ (ou $x[n]$).
2. **Passo 2:** Crie um novo sinal refletido no tempo: substitua todos os $t$ (ou $n$) da equação por $-t$ (ou $-n$). Chame esse resultado de $x(-t)$.
3. **Passo 3:** Compare $x(-t)$ com a expressão original $x(t)$. Se $x(-t) == x(t)$ para todos os valores, então o sinal é **PAR**. Fim.
4. **Passo 4:** Se forem diferentes, pegue a expressão original $x(t)$ e multiplique toda ela por $-1$, obtendo $-x(t)$.
5. **Passo 5:** Compare $x(-t)$ com $-x(t)$. Se $x(-t) == -x(t)$, então o sinal é **ÍMPAR**. Se também for diferente, não é nem par nem ímpar.

> **💡 Dica de Ouro / Macete Visual:**
> *   Par $\times$ Par = Par
> *   Ímpar $\times$ Ímpar = Par
> *   Par $\times$ Ímpar = Ímpar

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
**Algoritmo de Resolução:**
1. **Passo 1:** Calcule a energia total do sinal $E_\infty = \lim_{T \to \infty} \int_{-T}^{T} |x(t)|^2 dt$.
2. **Passo 2:** Se a integral convergir para um número finito ($0 < E_\infty < \infty$), então é um **Sinal de Energia**. A potência média será zero. Fim.
3. **Passo 3:** Se $E_\infty = \infty$, calcule a potência média: $P_\infty = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 dt$.
4. **Passo 4:** Se o limite convergir para um número finito ($0 < P_\infty < \infty$), é um **Sinal de Potência**.

> **💡 Dica de Ouro / Macete Visual:**
> Sinais que "morrem" em infinito são de Energia (ex: exponenciais decrescentes). Sinais que duram para sempre oscilando ou constantes são de Potência (ex: degraus e senoides).

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** Exponencial decrescente $x(t) = e^{-at}u(t)$, com $a > 0$. 
    Energia:
    $$E = \int_{0}^{\infty} (e^{-at})^2 dt$$
    $$E = \left[ \frac{e^{-2at}}{-2a} \right]_{0}^{\infty}$$
    $$E = \frac{1}{2a}$$
    Finito, logo é **Energia**.

*   **Médio:** Senóide genérica $x(t) = A\cos(\omega_0 t)$.
    A integral de energia vai dar $\infty$. Indo pra Potência num período $T$:
    $$P = \frac{1}{T} \int_{-T/2}^{T/2} A^2 \cos^2(\omega_0 t) dt = \frac{A^2}{2}$$
    Sinal de **Potência**.

*   **Nível Prova/Lista (Difícil):** Energia da integral de impulsos.
    *(Origem: Questão 3 da sua 1ª Avaliação / Q. 21 da Lista)*
    Seja $x(t) = \delta(t + 2) - \delta(t - 2)$. Calcule a Energia $E_\infty$ de $y(t) = \int_{-\infty}^{t} x(\tau) d\tau$.
    Passo 1 (Resolver a integral analiticamente, lembrando que integral do impulso é o degrau):
    $$y(t) = \int_{-\infty}^{t} [\delta(\tau + 2) - \delta(\tau - 2)] d\tau$$
    $$y(t) = u(t + 2) - u(t - 2)$$
    Passo 2 (Interpretação): Isso forma um pulso retangular de amplitude 1 que existe apenas de $t = -2$ até $t = 2$.
    Passo 3 (Calcular Energia):
    $$E_\infty = \int_{-2}^{2} (1)^2 dt$$
    $$E_\infty = [t]_{-2}^{2}$$
    $$E_\infty = 2 - (-2) = 4 \text{ J}$$
    Como é finito ($E=4$), é **Sinal de Energia**.

---

## PARTE 2: PROPRIEDADES DOS SISTEMAS
Um sistema mapeia uma entrada $x(t)$ para uma saída $y(t)$.

### 3. Com Memória ou Sem Memória (Estático)
Um sistema sem memória só depende do instante presente.

**Algoritmo de Resolução:**
1. **Passo 1:** Avalie a equação de saída $y(t)$ para um instante de tempo arbitrário $t = t_0$.
2. **Passo 2:** Identifique os argumentos de tempo de todas as entradas $x(\cdot)$ que compõem a saída.
3. **Passo 3:** Se você precisa de $x(t_0 - 1)$ (passado) ou $x(2t_0)$ ou $x(t_0+1)$ (futuro), o sistema precisa armazenar valores. Logo, tem **MEMÓRIA** (dinâmico).
4. **Passo 4:** Se e somente se aparecer **apenas** $x(t_0)$, então o sistema é **SEM MEMÓRIA** (estático).

> **💡 Dica de Ouro / Macete Visual:**
> Integrais, derivadas e modificadores de tempo dentro do argumento do x (como $t-1$, $2t$, $-t$) sempre exigem memória. Para ser sem memória, a relação precisa ser puramente algébrica instantânea.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** $y(t) = 5 \cdot x(t)$.
    Para saber a saída em $t=2$, só usa $x(2)$. **Sem Memória**.

*   **Médio:** $y(t) = x(t-2)$.
    Para $y(0) = x(-2)$, precisou do passado. **Com Memória**.

*   **Difícil:** $y(t) = x(-t)$. 
    Vamos testar $t = 4$:
    $$y(4) = x(-4) \quad \text{(Precisou do passado)}$$
    Vamos testar $t = -4$:
    $$y(-4) = x(4) \quad \text{(Precisou do futuro)}$$
    Tem **Memória**.

### 4. Causalidade
Causalidade significa que o sistema não pode prever o futuro.

**Algoritmo de Resolução:**
1. **Passo 1:** Considere a saída num instante de tempo presente $t_0$.
2. **Passo 2:** Verifique o argumento da entrada $x(\cdot)$ na equação.
3. **Passo 3:** Se para qualquer valor escolhido de $t_0$, o argumento for **maior** que $t_0$, o sistema está olhando para o futuro. Logo, é **NÃO-CAUSAL**. Se o argumento for sempre $\le t_0$, ele só olha para presente/passado e é **CAUSAL**.

> **💡 Dica de Ouro / Macete Visual:**
> Operadores $+t$ dentro do 'x', ou "compressões/expansões" temporais ($x(2t)$) costumam ser não-causais. Todo sistema sem memória é causal.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** $y[n] = x[n] + x[n-1]$. Usa presente e passado. **Causal**.
*   **Médio:** $y(t) = x(t+2)$. Preciso do futuro hoje. **Não-Causal**.

*   **Nível Prova/Lista (A Pegadinha do Oppenheim):** $y(t) = t \cdot x(t)$.
    *(Origem: Questão 5 da sua 1ª Avaliação)*
    Você avalia um instante $t$: o valor da saída depende EXCLUSIVAMENTE da entrada $x$ no mesmo exato momento $t$. O coeficiente "$t$" multiplicando de fora é apenas um ganho variável, não muda o instante de leitura do sinal. Como não olha para o futuro, é **Causal** (e sem memória).

### 5. LINEAR ou NÃO-LINEAR (Superposição)
A superposição exige aditividade e homogeneidade.

**Algoritmo de Resolução:**
1. **Passo 1:** Escreva as saídas individuais para duas entradas: $y_1(t) = T\{x_1(t)\}$ e $y_2(t) = T\{x_2(t)\}$.
2. **Passo 2:** Crie uma entrada combinada linearmente: $x_3(t) = a \cdot x_1(t) + b \cdot x_2(t)$.
3. **Passo 3:** Calcule qual seria a saída do sistema **se** a entrada fosse $x_3(t)$. Troque todo $x(t)$ pela expressão inteira de $x_3(t)$. Chame de $y_3(t)$.
4. **Passo 4:** Calcule a soma linear das saídas individuais: $y_{comb}(t) = a \cdot y_1(t) + b \cdot y_2(t)$.
5. **Passo 5:** Compare $y_3(t)$ com $y_{comb}(t)$. Se $y_3(t) == y_{comb}(t)$, o sistema é **LINEAR**. Se forem diferentes, é **NÃO-LINEAR**.

> **💡 Dica de Ouro / Macete Visual:**
> Constantes somadas isoladas (ex: $+3$) ou o sinal de entrada enjaulado em funções não-lineares ($x^2$, $\sin(x)$) destroem a linearidade.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** $y(t) = x(t) + 3$.
    Entrada zero = $x(t) = 0 \implies y(t) = 3$. Um sistema linear não pode produzir saída se não há entrada. Falhou na origem. **Não-Linear**.

*   **Nível Prova/Lista (Médio/Difícil):** O ganho variante $y(t) = t \cdot x(t)$.
    *(Origem: Questão 5 da sua 1ª Avaliação)*
    Combinação nas entradas:
    $$x_3(t) = a \cdot x_1(t) + b \cdot x_2(t)$$
    Passando pelo sistema (multiplicando a entrada inteira por t):
    $$y_3(t) = t \cdot [a \cdot x_1(t) + b \cdot x_2(t)]$$
    Distribuindo:
    $$y_3(t) = a \cdot [t \cdot x_1(t)] + b \cdot [t \cdot x_2(t)]$$
    $$y_3(t) = a \cdot y_1(t) + b \cdot y_2(t)$$
    Como a saída resultante separou direitinho e não quebrou a superposição, é **Linear**.

### 6. Invariância no Tempo (LTI) ou Variante no Tempo
Invariância no tempo significa que um atraso na entrada causa exatamente o mesmo atraso na saída.

**Algoritmo de Resolução:**
1. **Passo 1:** Aplique uma entrada $x(t)$ para obter a saída original $y(t)$.
2. **Passo 2:** Crie um sinal de entrada atrasado artificialmente: $x_1(t) = x(t - t_0)$.
3. **Passo 3:** Passe esse sinal $x_1(t)$ pelo sistema (na equação, troque a notação $x(\cdot)$ por $x_1(\cdot)$) e chame de $y_1(t)$.
4. **Passo 4:** Pegue a expressão da saída original $y(t)$ e substitua a variável **global** $t$ por $(t - t_0)$ em **TODOS** os lugares onde $t$ aparecer. Chame de $y_2(t)$.
5. **Passo 5:** Compare $y_1(t)$ com $y_2(t)$. Se $y_1(t) == y_2(t)$, o sistema é **INVARIANTE**. Caso contrário, é **VARIANTE**.

> **💡 Dica de Ouro / Macete Visual:**
> Variáveis de tempo ($t$) "soltas" do lado de fora do sinal indicam Variância no tempo. Alterações internas de relógio como $x(2t)$ também indicam Variância.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** $y(t) = 2x(t)$. 
    Atrasando a entrada e a saída, ambas dão $2x(t-t_0)$. **Invariante**.

*   **Nível Prova/Lista (A clássica de Variância):** $y(t) = t \cdot x(t)$.
    *(Origem: Questão 5 da sua 1ª Avaliação)*
    Passo 1 (atrasa SÓ a entrada $x$):
    $$y_1(t) = t \cdot x(t-t_0)$$
    Passo 2 (atrasa a variável de tempo 't' global do sistema):
    $$y_2(t) = (t-t_0) \cdot x(t-t_0)$$
    Avaliando: $y_1(t) \neq y_2(t)$. Logo, **Variante no Tempo**.

*   **Difícil (Compressão no Tempo):** $y(t) = x(2t)$.
    Passo 1 (Atraso na entrada): 
    $$y_1(t) = x(2t - t_0)$$
    Passo 2 (trocar a variável de tempo global $t$ por $t-t_0$): 
    $$y_2(t) = x(2(t-t_0))$$
    $$y_2(t) = x(2t - 2t_0)$$
    Comparando:
    $$x(2t - t_0) \neq x(2t - 2t_0)$$
    Logo, é **Variante no tempo**.

### 7. Estabilidade BIBO
Se entra um valor limitado (finito), tem que sair um valor limitado (finito).

**Algoritmo de Resolução:**
1. **Passo 1:** Assuma, por hipótese, que a entrada é limitada. Escreva: $|x(t)| \le B_x < \infty$ para todo $t$.
2. **Passo 2:** Aplique o módulo na equação inteira da saída: $|y(t)| = |T\{x(t)\}|$.
3. **Passo 3:** Use propriedades de módulo e desigualdade triangular para isolar o termo $|x(t)|$.
4. **Passo 4:** Substitua $|x(t)|$ por $B_x$.
5. **Passo 5:** Analise a expressão. Se houver alguma entrada limitada (mesmo que seja um caso apenas) que faça a saída ir para infinito (ex: divisão por zero ou integração de constante infinita), é **INSTÁVEL**. Se o limite for sempre finito, é **ESTÁVEL**.

> **💡 Macete Visual:**
> Integradores com limites abertos ($-\infty$ até $t$) tendem a instabilizar com entradas constantes. Funções divididas por tempo ($1/t$) podem instabilizar em zero.

**📚 Exemplos Práticos:**

*   **Fácil (Trivial):** Divisor $y(t) = \frac{1}{2} x(t)$.
    $$|y(t)| = \frac{1}{2}|x(t)| \le \frac{1}{2} B_x < \infty$$. **Estável**.

*   **Nível Prova/Lista (Pegadinha do "t"):** O ganho variante $y(t) = t \cdot x(t)$.
    *(Origem: Questão 5 da sua 1ª Avaliação)*
    Assuma que aplicamos um degrau unitário $x(t) = 1$ (sinal super comportado e limitado, $B_x=1$).
    A saída será:
    $$y(t) = t \cdot (1) = t$$
    Se avaliarmos quando $t \to \infty$, a saída $y(t) \to \infty$. 
    Ou seja, entrou um sinal com limite e a saída estourou pro infinito por conta do $t$ livre! Sistema **Instável**.
