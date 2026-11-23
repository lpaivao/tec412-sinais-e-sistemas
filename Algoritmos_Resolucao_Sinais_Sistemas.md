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


---

## PARTE 3: UNIDADE 2 — SISTEMAS LTI (SLITs), CONVOLUÇÃO E DIAGRAMAS EM BLOCOS

### 8. Algoritmo Mestre da Convolução (Tempo Discreto **e** Tempo Contínuo)

O roteiro é **o mesmo** nos dois mundos. Muda apenas o "dicionário":

| | **Tempo Discreto** | **Tempo Contínuo** |
|:---|:---:|:---:|
| Fórmula | $y[n] = \displaystyle\sum_{k=-\infty}^{\infty} x[k]\,h[n-k]$ | $y(t) = \displaystyle\int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$ |
| Variável muda (a que "corre") | $k$ (inteiro) | $\tau$ (real) |
| Variável **constante** durante a conta | $n$ | $t$ |
| Tamanho do trecho $[A, B]$ | $B - A + 1$ amostras | $B - A$ |
| Soma/integral de uma constante $c$ | $c\,(B - A + 1)$ | $c\,(B - A)$ |
| Fronteiras dos intervalos | inteiros: cada intervalo começa num $n$ exato | reais: usar $<$ ou $\le$ tanto faz (sem impulsos, $y$ é contínua) |
| Duração da saída (sinais finitos) | $L_x + L_h - 1$ amostras | $L_x + L_h$ |

---

#### **PASSO 0 — Triagem: existe atalho? (faça SEMPRE antes de deslizar qualquer coisa)**

Responda às 5 perguntas, nesta ordem:

1. **Algum dos sinais tem impulso?** Use a propriedade do deslocamento:
   $$x(t) * \delta(t - t_0) = x(t - t_0) \qquad\qquad x[n] * \delta[n - n_0] = x[n - n_0]$$
   **De onde vem (escreva estas 2 linhas na prova):** o impulso $\delta(t - \tau - t_0)$ só é não nulo quando $t - \tau - t_0 = 0 \iff \tau = t - t_0$, e tem área $1$. Pela propriedade da amostragem, $\int f(\tau)\,\delta(\tau - \tau_0)\,d\tau = f(\tau_0)$:
   $$x(t) * \delta(t - t_0) = \int_{-\infty}^{\infty} x(\tau)\,\delta(t - \tau - t_0)\,d\tau = x(\tau)\Big|_{\tau = t - t_0} = x(t - t_0)$$
   Se $h$ for "pedaço normal + impulso", separe pela distributiva: a parcela do impulso sai **sem deslizar janela e sem dividir em intervalos**. É só deslocar o sinal e multiplicar pelo peso do impulso. A justificativa de 2 linhas acima continua obrigatória.
   - Impulso em $t = +t_0$ **atrasa** o sinal: $\delta(t - 2)$ gera $x(t - 2)$, e não $x(t + 2)$.
   - O peso multiplica: $c\,\delta(t - t_0)$ gera $c\,x(t - t_0)$.

   *Ex.: Oppenheim 2.22(d):*
   $$h(t) = \underbrace{\tfrac{4}{3}[u(t) - u(t-1)]}_{h_a(t)} \underbrace{-\ \tfrac{1}{3}\delta(t-2)}_{h_b(t)} \implies y(t) = x(t) * h_a(t) + x(t) * h_b(t)$$
   Só a parcela $x \ast h_a$ exige integral (pulso de $0$ a $1$). A outra parcela é direta:
   $$x \ast h_b = -\frac{1}{3}\,x(t-2) = -\frac{1}{3}\big[a(t-2) + b\big]$$

2. **Os dois sinais são "de tabela" (degrau, exponencial causal), talvez deslocados?** Use a tabela abaixo e some os deslocamentos:
   $$x = x_0(\cdot - t_1),\ \ h = h_0(\cdot - t_2) \implies y = (x_0 * h_0)(\cdot - t_1 - t_2)$$

3. **Algum sinal é uma soma de partes de natureza diferente** (ex.: uma parte à esquerda $3^n u[-n-1]$ e outra à direita $(1/3)^n u[n]$)? Use a **distributiva**, $y = x_1 * h + x_2 * h$, e resolva cada parcela separadamente (Oppenheim 2.25).

4. **A entrada é periódica?** Então a saída é periódica com o **mesmo período**: calcule só um período (Oppenheim 2.22(e)).

5. **É de fato uma convolução?** Se a relação não tem a forma $x[k]h[n-k]$ (ex.: $\sum x[k]g[n-2k]$, Oppenheim 2.7), **não** aplique o algoritmo; substitua a entrada diretamente na relação dada.

**📋 Tabela de convoluções prontas** (com deslocamento, viram atalho):

| Tempo Contínuo | Tempo Discreto |
|:---|:---|
| $u(t) * u(t) = t\,u(t)$ (rampa) | $u[n] * u[n] = (n+1)\,u[n]$ |
| $u(t-a) * u(t-b) = (t-a-b)\,u(t-a-b)$ | $u[n-a] * u[n-b] = (n-a-b+1)\,u[n-a-b]$ |
| $e^{-at}u(t) * u(t) = \dfrac{1 - e^{-at}}{a}\,u(t)$ | $a^n u[n] * u[n] = \dfrac{1 - a^{n+1}}{1 - a}\,u[n]$ |
| $e^{-at}u(t) * e^{-bt}u(t) = \dfrac{e^{-at} - e^{-bt}}{b - a}\,u(t)$, $a \neq b$ | $a^n u[n] * b^n u[n] = \dfrac{a^{n+1} - b^{n+1}}{a - b}\,u[n]$, $a \neq b$ |
| $e^{-at}u(t) * e^{-at}u(t) = t\,e^{-at}u(t)$ | $a^n u[n] * a^n u[n] = (n+1)\,a^n u[n]$ |

> **💡 Macete do Trapézio (dois pulsos retangulares):** pulso de altura $A_1$ e largura $L_1$ convoluído com pulso de altura $A_2$ e largura $L_2$ dá **sempre um trapézio** (ou triângulo, se $L_1 = L_2$):
> - começa na **soma dos inícios** e termina na **soma dos fins**;
> - patamar de altura $A_1 A_2 \cdot \min(L_1, L_2)$;
> - largura do patamar: $|L_1 - L_2|$ no contínuo, ou $|L_1 - L_2| + 1$ amostras no discreto.

> **💡 Macete das Rampas (sinais feitos só de degraus):** se $x$ e $h$ são somas de degraus deslocados, $x = \sum_i c_i\,u(t - a_i)$ e $h = \sum_j d_j\,u(t - b_j)$, então
> $$y(t) = \sum_i \sum_j c_i\,d_j\,(t - a_i - b_j)\,u(t - a_i - b_j)$$
> É uma excelente **prova real** para o método gráfico (veja o Exemplo D).

Se nenhum atalho resolver a questão por inteiro, siga os Passos 1 a 6.

---

#### **PASSO 1 — Escolher quem fica parado e quem desliza; quebrar o sinal parado em pedaços**

1. A convolução é comutativa ($x * h = h * x$), então **você escolhe**:
   - **fica parado** o sinal com **mais pedaços** (escadas, somas de degraus, seno recortado);
   - **desliza** (é refletido) o sinal **mais simples** (um único pulso, uma única exponencial com um degrau).

   No que segue, o parado se chama $x$ e o que desliza se chama $h$.

2. Escreva o sinal parado na variável muda ($x[k]$ ou $x(\tau)$) e monte a **tabela de pedaços**. Um *pedaço* é um trecho onde $x$ segue **uma única fórmula**:

   | Pedaço | Trecho | Fórmula |
   |:---:|:---:|:---:|
   | A | $[\text{início}_A, \text{fim}_A]$ | ... |
   | B | $[\text{início}_B, \text{fim}_B]$ | ... |

   *Truque para somas de degraus:* percorra o eixo da esquerda para a direita e, a cada degrau que "liga", some o seu coeficiente (Questão 1.1: $-1 \to -1 + 2 = +1 \to +1 - 1 = 0$).

3. Liste os **pontos de quebra**: o início de cada pedaço e o **primeiro ponto depois do fim** do sinal (no discreto, $\text{fim} + 1$; no contínuo, o próprio fim).
   - Lado infinito (ex.: $3^k$ para $k \le -1$) **não** gera ponto de quebra.

---

#### **PASSO 2 — Refletir e deslocar o que desliza: achar a janela $h[n-k]$ / $h(t-\tau)$**

1. Ache o trecho onde $h$ é não nulo: $a \le (\text{argumento}) \le b$.
2. Troque o argumento por $n - k$ (ou $t - \tau$) e isole a variável muda:
   $$a \le n - k \le b \iff \boxed{\,n - b \le k \le n - a\,} \qquad\qquad a \le t - \tau \le b \iff \boxed{\,t - b \le \tau \le t - a\,}$$
   - **Cauda** (borda esquerda) $= n - b$ (ou $t - b$);
   - **Frente** (borda direita) $= n - a$ (ou $t - a$).
3. Escreva também **a fórmula de $h$ dentro da janela**, substituindo o argumento inteiro. Em exponenciais, separe o que depende de $t$:
   $$e^{-\beta(t - \tau)} = e^{-\beta t}\,e^{\beta\tau}$$
4. **Janelas infinitas** (o caso que mais derruba aluno):
   - $h$ vai para a **direita** até $\infty$ ($b = +\infty$, ex.: $u[n-1]$, $e^{-\beta t}u(t)$): a janela **não tem cauda**, vai de $-\infty$ até a frente;
   - $h$ vai para a **esquerda** até $-\infty$ ($a = -\infty$, ex.: $e^{2t}u(1-t)$): a janela **não tem frente**, vai da cauda até $+\infty$.

> **⚠️ Atenção ao refletir degraus:** $u(1 - (t - \tau)) = u(\tau - (t-1))$ liga para $\tau \ge t - 1$ (limite **inferior**). Já $u(t - \tau - t_0)$ liga para $\tau \le t - t_0$ (limite **superior**). Sempre isole a variável muda **com a desigualdade escrita**, nunca "de cabeça".

---

#### **PASSO 3 — Tabela de eventos: onde a fórmula de $y$ muda**

A fórmula de $y$ só muda quando **uma borda da janela cruza um ponto de quebra**. Iguale cada borda a cada ponto de quebra $p$ e resolva para $n$ (ou $t$):
$$\text{frente} = p \implies n = p + a \qquad\qquad \text{cauda} = p \implies n = p + b$$

| Borda | Ponto de quebra $p$ | Equação | $n$ (ou $t$) | O que acontece |
|:---:|:---:|:---:|:---:|:---|
| frente | ... | $n - a = p$ | ... | a frente entra num novo pedaço (ou sai do sinal) |
| cauda | ... | $n - b = p$ | ... | a cauda solta um pedaço inteiro |

- Ordene os valores obtidos. **$N$ eventos cortam o eixo em $N + 1$ intervalos.**
- O valor de cada evento é o **primeiro** $n$ da nova situação. No discreto, o intervalo vai de um evento até o **próximo evento menos 1**; no contínuo, de um evento até o próximo.
- Eventos coincidentes se fundem (dão menos intervalos).
- **Quem cruza primeiro?** Se a janela é **mais larga** que $x$, todos os eventos da frente vêm antes dos da cauda, e a etapa do meio é "$x$ inteiro dentro da janela". Se a janela é **mais estreita**, os eventos se intercalam, e a etapa do meio é "janela inteira dentro de $x$".

---

#### **PASSO 4 — Em cada intervalo: limites, montagem e conta**

Para **cada** intervalo, siga o roteiro (é o mesmo usado na Questão 1.1):

**(a) Situação:** descreva em palavras onde estão a frente e a cauda.

**(b) Faixa de $n$ (ou $t$):** escreva-a pela tabela de eventos.

**(c) Limites de cada pedaço** (interseção entre a janela e o pedaço):
$$\text{limite inferior} = \max(\text{cauda},\ \text{início do pedaço}) \qquad \text{limite superior} = \min(\text{frente},\ \text{fim do pedaço})$$
- Se o limite inferior **for maior** que o superior, o pedaço não entra (contribui com $0$).
- Para decidir o $\max$/$\min$, **substitua um valor de $n$ (ou $t$) do intervalo**.

**(d) Montagem:** some uma parcela por pedaço que entrou:
$$y = \sum_{\text{pedaços}} \ \sum_{k = \text{inf}}^{\text{sup}} x_{\text{pedaço}}[k]\cdot h[n - k] \qquad \text{ou} \qquad y = \sum_{\text{pedaços}} \int_{\text{inf}}^{\text{sup}} x_{\text{pedaço}}(\tau)\cdot h(t - \tau)\,d\tau$$

**(e) Conta:** tudo o que depende **só** de $n$ (ou $t$) sai da soma/integral como constante. Use o formulário abaixo.

**(f) Prova real do intervalo:** escolha um $n$ do intervalo, liste os $k$ cobertos pela janela, faça a soma "na mão" e compare.

**📐 Formulário:**

- **PG finita** ($r \neq 1$): $\displaystyle\sum_{k=A}^{B} r^k = \frac{r^A - r^{B+1}}{1 - r}$; para $r = 1$, vale $B - A + 1$.
- **PG infinita à direita** ($|r| < 1$): $\displaystyle\sum_{k=A}^{\infty} r^k = \frac{r^A}{1 - r}$ (primeiro termo sobre $1 - r$).
- **PG infinita à esquerda** ($|r| > 1$): $\displaystyle\sum_{k=-\infty}^{B} r^k = \frac{r^{B+1}}{r - 1}$; alternativamente, faça $m = -k$ e caia no caso anterior com razão $1/r$.
- **Integrais:**
  $$\int e^{a\tau}d\tau = \frac{e^{a\tau}}{a} \qquad \int \tau\,e^{a\tau}d\tau = e^{a\tau}\left(\frac{\tau}{a} - \frac{1}{a^2}\right) \qquad \int \text{sen}(\omega\tau)\,d\tau = -\frac{\cos(\omega\tau)}{\omega}$$
- **Exponencial com o expoente "anulado":** se ao juntar os termos o expoente em $\tau$ zerar (ex.: $\alpha = \beta$), a integral vira $\int 1\,d\tau$. Trate esse caso **separadamente**, porque a fórmula geral divide por zero.

---

#### **PASSO 5 — Montar a resposta final e esboçar**

1. Junte tudo numa expressão por partes, intervalo por intervalo, incluindo os intervalos com $y = 0$.
2. **Discreto:** faça a tabela $n \times y[n]$ das amostras não nulas e desenhe os "pirulitos".
3. **Contínuo:** desenhe cada trecho (reta, parábola, exponencial) ligando os valores das fronteiras.

---

#### **PASSO 6 — Prova real final (5 verificações rápidas)**

1. **Início e fim** (sinais de duração finita): o início de $y$ é $\text{início}_x + \text{início}_h$, e o fim de $y$ é $\text{fim}_x + \text{fim}_h$.
2. **Duração:** $L_x + L_h - 1$ amostras no discreto, $L_x + L_h$ no contínuo.
3. **Área/soma** (só se ambas convergirem):
   $$\sum_n y[n] = \Big(\sum_n x[n]\Big)\Big(\sum_n h[n]\Big) \qquad\qquad \int y(t)\,dt = \Big(\int x(t)\,dt\Big)\Big(\int h(t)\,dt\Big)$$
4. **Fronteiras:**
   - **Contínuo sem impulsos:** $y$ é **contínua**, então os dois intervalos vizinhos **têm** de dar o mesmo valor na fronteira. Se não derem, há erro.
   - **Discreto:** as fórmulas vizinhas costumam coincidir no ponto de fronteira. Por isso um gabarito pode escrever "$12 \le n \le 18$" onde você escreveu "$13 \le n \le 17$", e **ambos estão corretos**.
5. **Um ponto qualquer** calculado direto pela definição.

> **🚫 Erros clássicos:**
> - Esquecer o "$+1$" na contagem de termos do discreto (de $0$ até $2$ são **3** termos).
> - Refletir só o degrau e esquecer de trocar o argumento da exponencial: $h(t - \tau)$ é $e^{-\beta(t-\tau)}$, **não** $e^{-\beta\tau}$.
> - Integrar em $t$ em vez de $\tau$: dentro da integral, **$t$ é constante**.
> - Tratar $u(1 - t)$ como se ligasse para a direita (ele liga para a **esquerda**: $t \le 1$).
> - Somar PG infinita divergente: confira $|r| < 1$ (à direita) ou $|r| > 1$ (à esquerda).
> - Esquecer os intervalos de $y = 0$ na resposta final.

---

### 9. Exemplos Resolvidos com o Algoritmo Mestre (2ª Lista)

*As resoluções completas, linha a linha, estão em `Unidade_2/Resolucoes_e_Pratica/Resolucoes_Unidade2.md`. Aqui o foco é **ver o algoritmo funcionando**.*

**📌 Qual caminho usar em cada questão da lista:**

| Questão | Caminho do algoritmo |
|:---|:---|
| 1.1 (sala, discreto) | Passos 1–6 completos: 2 pedaços × 2 bordas → 6 eventos → **7 intervalos** |
| 1.2 (sala, contínuo) | Passos 1–6 completos: **7 intervalos** (Exemplo D) + prova pelas rampas |
| 2.3 (Oppenheim 2.3) | **Atalho** do Passo 0.2: tabela + deslocamento (Exemplo A) |
| 2.4 (Oppenheim 2.4) | Passos 1–6 com 4 eventos (Exemplo B) ou Macete do Trapézio |
| 2.6 (Oppenheim 2.6) | Janela infinita, sem cauda: 1 evento → 2 intervalos (Exemplo C) |
| 2.7 (Oppenheim 2.7) | **Não é convolução** (Passo 0.5): substitua a entrada direto |
| 3.1(a) (Oppenheim 2.22a) | **Atalho** da tabela (exponencial × exponencial, com o caso $\alpha = \beta$) |
| 3.1(b) (Oppenheim 2.22b) | Janela infinita, sem frente: 3 eventos → 4 intervalos (Exemplo E) |
| 3.1(c) (Oppenheim 2.22c) | Passos 1–6 com um pedaço senoidal e uma janela retangular |
| 3.1(d) (Oppenheim 2.22d) | Passo 0.1: impulso por deslocamento + pulso sobre a reta |
| 3.1(e) (Oppenheim 2.22e) | Passo 0.4: entrada periódica, calcular só um período |
| 4.1 (Oppenheim 2.25) | Passo 0.3: **distributiva** (parte esquerda + parte direita) |

---

**Exemplo A — Atalho da tabela (Oppenheim 2.3):** $x[n] = \left(\frac{1}{2}\right)^{n-2}u[n-2]$ e $h[n] = u[n+2]$.

- **Passo 0.2:** $x[n] = x_0[n-2]$ com $x_0[n] = \left(\frac{1}{2}\right)^n u[n]$, e $h[n] = h_0[n+2]$ com $h_0[n] = u[n]$.
- **Pela tabela:**
  $$x_0 * h_0 = \frac{1 - \left(\frac{1}{2}\right)^{n+1}}{1 - \frac{1}{2}}u[n] = 2\left[1 - \left(\frac{1}{2}\right)^{n+1}\right]u[n]$$
- **Deslocamento total:** $+2 - 2 = 0$, então nada muda:
  $$y[n] = 2\left[1 - \left(\frac{1}{2}\right)^{n+1}\right]u[n]$$

✓ Igual à Questão 2.1, sem montar nenhum somatório.

---

**Exemplo B — Discreto completo (Oppenheim 2.4):** $x[n] = 1$ para $3 \le n \le 8$, e $h[n] = 1$ para $4 \le n \le 15$.

- **Passo 1:** fica parado $x$ (6 amostras). Há um único pedaço A, com $x[k] = 1$ em $[3, 8]$. Pontos de quebra: $3$ e $9$.
- **Passo 2:** $a = 4$, $b = 15$, então a janela é $n - 15 \le k \le n - 4$ (12 amostras, mais larga que $x$).
- **Passo 3:**

  | Borda | $p$ | Equação | $n$ | Significado |
  |:---:|:---:|:---:|:---:|:---|
  | frente | 3 | $n - 4 = 3$ | 7 | começa a sobreposição |
  | frente | 9 | $n - 4 = 9$ | 13 | $x$ inteiro dentro da janela |
  | cauda | 3 | $n - 15 = 3$ | 18 | a cauda começa a soltar $x$ |
  | cauda | 9 | $n - 15 = 9$ | 24 | fim da sobreposição |

- **Passo 4:**
  - $n \le 6$: $y = 0$.
  - $7 \le n \le 12$: limites $[\max(n-15, 3),\ \min(n-4, 8)] = [3,\ n-4]$, logo $y = (n - 4) - 3 + 1 = n - 6$.
  - $13 \le n \le 17$: limites $[3,\ 8]$, logo $y = 6$.
  - $18 \le n \le 23$: limites $[n-15,\ 8]$, logo $y = 8 - (n - 15) + 1 = 24 - n$.
  - $n \ge 24$: $y = 0$.
- **Passo 6:**
  - Início $= 3 + 4 = 7$ ✓; fim $= 8 + 15 = 23$ ✓; duração $= 6 + 12 - 1 = 17$ ✓.
  - Soma: $\sum y = 6 \cdot 12 = 72$. Conferindo: $(1+2+3+4+5) + 6\cdot 7 + (5+4+3+2+1) = 15 + 42 + 15 = 72$ ✓.
  - Fronteiras: $y[12] = 12 - 6 = 6$ coincide com o patamar, e por isso o gabarito escreve o patamar como $12 \le n \le 18$. São as mesmas amostras.

---

**Exemplo C — Discreto com janela infinita (Oppenheim 2.6):** $x[n] = 3^n u[-n-1]$ e $h[n] = u[n-1]$.

- **Passo 1:** um único pedaço, $x[k] = 3^k$ para $k \le -1$ (infinito à esquerda). O único ponto de quebra é $p = 0$.
- **Passo 2:** $h$ é não nulo em $[1, \infty)$, então $a = 1$ e $b = \infty$. A janela **não tem cauda**: é $k \le n - 1$.
- **Passo 3:** frente $= 0 \implies n = 1$. Um evento, logo **2 intervalos**.
- **Passo 4:**
  - $n \le 0$: limite superior $= \min(n - 1, -1) = n - 1$, e então
    $$y = \sum_{k=-\infty}^{n-1} 3^k = \frac{3^{n}}{3 - 1} = \frac{3^n}{2}$$
  - $n \ge 1$: limite superior $= -1$, e então
    $$y = \sum_{k=-\infty}^{-1} 3^k = \frac{3^0}{2} = \frac{1}{2}$$
- **Passo 6:** em $n = 0$, $\frac{3^0}{2} = \frac{1}{2}$, que coincide com o outro ramo. Por isso o gabarito escreve "$n < 0$ / $n \ge 0$". ✓

---

**Exemplo D — Contínuo completo (Questão 1.2 da apostila):** $x(t) = u(t) + u(t-1) - 2u(t-2)$ e $h(t) = u(t-1) - u(t-4)$.

- **Passo 1:** fica parado $x$, com o pedaço A valendo $1$ em $[0, 1)$ e o pedaço B valendo $2$ em $[1, 2)$. Pontos de quebra: $0$, $1$ e $2$.
- **Passo 2:** $a = 1$, $b = 4$, então a janela é $t - 4 \le \tau \le t - 1$ (largura 3, mais larga que $x$).
- **Passo 3:** frente $= 0, 1, 2 \implies t = 1, 2, 3$; cauda $= 0, 1, 2 \implies t = 4, 5, 6$. São 6 eventos, logo **7 intervalos**.
- **Passo 4** (resultado):

  | Intervalo | $y(t)$ |
  |:---:|:---:|
  | $t < 1$ | $0$ |
  | $1 \le t < 2$ | $t - 1$ |
  | $2 \le t < 3$ | $2t - 3$ |
  | $3 \le t < 4$ | $3$ |
  | $4 \le t < 5$ | $7 - t$ |
  | $5 \le t < 6$ | $12 - 2t$ |
  | $t \ge 6$ | $0$ |

- **Passo 6:**
  - **Continuidade:** em $t = 2$, os dois ramos dão $1 = 1$; em $t = 3$, $3 = 3$; em $t = 4$, $3 = 3$; em $t = 5$, $2 = 2$ ✓.
  - **Área:** $\int x = 1 + 2 = 3$ e $\int h = 3$, logo $\int y$ deve ser $9$. Conferindo: $0{,}5 + 2 + 3 + 2{,}5 + 1 = 9$ ✓.
  - **Prova pelas rampas** (Passo 0): com $r(t) = t\,u(t)$,
    $$y(t) = r(t-1) + r(t-2) - 2r(t-3) - r(t-4) - r(t-5) + 2r(t-6)$$
    Em $t = 3{,}5$: $2{,}5 + 1{,}5 - 2(0{,}5) = 3$ ✓.

---

**Exemplo E — Contínuo com janela infinita (Oppenheim 2.22(b)):** $x(t) = u(t) - 2u(t-2) + u(t-5)$ e $h(t) = e^{2t}u(1-t)$.

- **Passo 1:** fica parado $x$, com o pedaço A valendo $+1$ em $[0, 2)$ e o pedaço B valendo $-1$ em $[2, 5)$. Pontos de quebra: $0$, $2$ e $5$.
- **Passo 2:** $h$ é não nulo em $(-\infty, 1]$, então $a = -\infty$ e $b = 1$. A janela **não tem frente**: é $\tau \ge t - 1$. Dentro dela, $h(t - \tau) = e^{2(t - \tau)}$.
- **Passo 3:** cauda $= 0, 2, 5 \implies t = 1, 3, 6$. Três eventos, logo **4 intervalos**.
- **Passo 4:**
  - $t < 1$: entram os pedaços A e B inteiros.
  - $1 \le t < 3$: A entra de $t - 1$ até $2$; B entra inteiro.
  - $3 \le t < 6$: só B, de $t - 1$ até $5$.
  - $t \ge 6$: $y = 0$.

  Os resultados de cada intervalo estão na Questão 3.1(b).
- **Passo 6:**
  - **Continuidade em $t = 3$:** os dois ramos dão $\frac{1}{2}(e^{-4} - e^{2})$ ✓.
  - **Área:** $\int x = 2 - 3 = -1$ e $\int h = \int_{-\infty}^{1} e^{2t}\,dt = \frac{e^2}{2}$, logo $\int y = -\frac{e^2}{2} \approx -3{,}695$ ✓ (conferido numericamente).

---

### 10. Memória, Causalidade e Estabilidade BIBO pela Resposta ao Impulso ($h[n]$ ou $h(t)$)

**Algoritmo de Resolução Direta (Sem precisar usar a entrada $x$):**
1. **Sem Memória:**
   - Só é **SEM MEMÓRIA** se $h[n] = c\delta[n]$ (ou $h(t) = c\delta(t)$). Se existir qualquer valor não nulo fora da origem ($n \neq 0$ ou $t \neq 0$), tem **MEMÓRIA**.
   - *Pegadinhas clássicas (Haykin 2.12):*
     - $h[n] = 2u[n] - 2u[n-1] = 2\delta[n] \implies$ **Sem Memória!**
     - $h[n] = \delta[n] + \text{sen}(\pi n) = \delta[n]$ (pois $\text{sen}(\pi n) = 0, \forall n \in \mathbb{Z}$) $\implies$ **Sem Memória!**
2. **Causalidade:**
   - Olhe apenas para o semieixo negativo ($n < 0$ ou $t < 0$).
   - Se $h[n] = 0$ para todo $n < 0$ (ou $h(t) = 0$ para todo $t < 0$), é **CAUSAL**.
   - Se houver qualquer amostra ou trecho não nulo antes de zero (como $u[n+2]$, $u[-n]$, $u(t+1)$, $e^{-2|t|}$), é **NÃO-CAUSAL**.
3. **Estabilidade BIBO:**
   - Calcule $\sum_{n=-\infty}^{\infty} |h[n]|$ (ou $\int_{-\infty}^{\infty} |h(t)|\,dt$).
   - **Todo sinal de duração finita e amplitude finita é sempre ESTÁVEL.**
   - Para exponenciais $r^n u[n]$ (direita): estável se $|r| < 1$.
   - Para exponenciais $r^n u[-n]$ (esquerda): estável se $|r| > 1$ (pois para $n \to -\infty$, $r^n \to 0$!).
   - Para exponenciais contínuas $e^{at}u(t)$ (direita): estável se $a < 0$.
   - Para exponenciais contínuas $e^{at}u(-t)$ (esquerda): estável se $a > 0$ (pois para $t \to -\infty$, $e^{at} \to 0$!).

---

### 11. Diagramas em Blocos (Formas Direta I e Direta II) e Variáveis de Estado

**Algoritmo de Resolução:**
1. **Passo 1 (Padronização):**
   - **Tempo Discreto (ED de ordem $N$):** Isole $y[n]$ (com $a_0 = 1$), identificando todos os coeficientes $a_1, \dots, a_N$ e $b_0, \dots, b_M$ (incluindo os coeficientes iguais a zero!):
     $$y[n] = -a_1 y[n-1] - \dots - a_N y[n-N] + b_0 x[n] + b_1 x[n-1] + \dots + b_M x[n-M]$$
   - **Tempo Contínuo (EDO de ordem $N$):** Com coeficiente líder $a_N = 1$ em $\frac{d^N}{dt^N}y(t)$, integre ambos os lados $N$ vezes (assumindo condições iniciais nulas), onde $v^{(k)}(t)$ denota a $k$-ésima integral sucessiva:
     $$y(t) = -a_{N-1}y^{(1)}(t) - \dots - a_0 y^{(N)}(t) + b_N x(t) + b_{N-1}x^{(1)}(t) + \dots + b_0 x^{(N)}(t)$$
2. **Passo 2 (Forma Direta I — usa $M + N$ elementos de memória):**
   - Crie o sinal intermediário $w$ somando as entradas atrasadas/integradas:
     $$w[n] = b_0 x[n] + \dots + b_M x[n-M] \qquad \text{e} \qquad y[n] = w[n] - a_1 y[n-1] - \dots - a_N y[n-N]$$
3. **Passo 3 (Forma Direta II — Canônica, usa apenas $\max(N, M)$ elementos de memória no ramo central):**
   - Crie o estado intermediário central $f$:
     $$\begin{aligned}
     f[n] &= x[n] - a_1 f[n-1] - \dots - a_N f[n-N] \\
     y[n] &= b_0 f[n] + b_1 f[n-1] + \dots + b_M f[n-M]
     \end{aligned}$$
4. **Passo 4 (Variáveis de Estado para 2ª Ordem na Forma Direta II):**
   - **Discreto ($b_0 = 1$):** $\mathbf{A} = \begin{bmatrix} -a_1 & -a_2 \\ 1 & 0 \end{bmatrix}, \; \mathbf{b} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \; \mathbf{c} = \begin{bmatrix} b_1 - a_1 & b_2 - a_2 \end{bmatrix}, \; D = [1]$.
   - **Contínuo ($a_2 = 1$):** $\mathbf{A} = \begin{bmatrix} -a_1 & -a_0 \\ 1 & 0 \end{bmatrix}, \; \mathbf{b} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \; \mathbf{c} = \begin{bmatrix} b_1 - a_1 b_2 & b_0 - a_0 b_2 \end{bmatrix}, \; D = [b_2]$.

**📚 Exemplo de Nível Prova (Exercício 1.3 da Apostila, pág. 52):**
*   **Contínuo:** $\frac{d^2}{dt^2}y(t) + 3y(t) = \frac{d}{dt}x(t) + 2\frac{d^2}{dt^2}x(t)$.
    - Integrando $N = 2$ vezes: $y(t) + 3y^{(2)}(t) = 2x(t) + x^{(1)}(t)$.
    - Forma Direta II (2 integradores): $f(t) = x(t) - 3f^{(2)}(t)$ e $y(t) = 2f(t) + f^{(1)}(t)$.
