# Lista de Treino — Nível Fácil (15 Questões) — Unidade 2
**Disciplina:** Sinais e Sistemas (TEC 412)  
**Tópicos da 2ª Prova:** Soma de Convolução, Integral de Convolução, Propriedades de Sistemas LTI via $h[n]/h(t)$ (Memória, Causalidade, Estabilidade), Interconexões (Série/Paralelo) e Diagramas em Blocos (Formas Direta I e II).  
**Referências:** Oppenheim & Willsky (2ª Ed.), Haykin & Van Veen (Bookman), Hsu (Schaum).

---

## Tópico 1: Soma de Convolução Básica (Impulsos e Sequências Curtas)

**Questão 1 (Ref: Oppenheim Cap. 2):** Calcule a convolução discreta $y[n] = x[n] * h[n]$ para $x[n] = \delta[n] + 2\delta[n-1]$ e $h[n] = \delta[n] - \delta[n-1]$.
> **Resolução Passo a Passo:**
> Pela propriedade de deslocamento do impulso ($x[n] * \delta[n - k_0] = x[n - k_0]$):
> $$y[n] = x[n] * \delta[n] - x[n] * \delta[n-1] = x[n] - x[n-1]$$
> Substituindo $x[n]$ e $x[n-1] = \delta[n-1] + 2\delta[n-2]$:
> $$y[n] = \big(\delta[n] + 2\delta[n-1]\big) - \big(\delta[n-1] + 2\delta[n-2]\big)$$
> $$y[n] = \delta[n] + \delta[n-1] - 2\delta[n-2]$$
> **Gabarito:** $y[n] = \delta[n] + \delta[n-1] - 2\delta[n-2]$ (ou $\{1, 1, -2\}$ para $n = 0, 1, 2$).

**Questão 2 (Ref: Apostila Exemplo 1.1):** Um SLIT discreto possui resposta ao impulso $h[n] = 2\delta[n] + \delta[n-1]$. Determine a saída $y[n]$ para a entrada $x[n] = 3\delta[n] - \delta[n-2]$.
> **Resolução Passo a Passo:**
> Pela superposição de impulsos deslocados:
> $$y[n] = 3h[n] - h[n-2]$$
> Substituindo $h[n]$ e $h[n-2] = 2\delta[n-2] + \delta[n-3]$:
> $$y[n] = 3\big(2\delta[n] + \delta[n-1]\big) - \big(2\delta[n-2] + \delta[n-3]\big)$$
> $$y[n] = 6\delta[n] + 3\delta[n-1] - 2\delta[n-2] - \delta[n-3]$$
> **Gabarito:** $y[n] = 6\delta[n] + 3\delta[n-1] - 2\delta[n-2] - \delta[n-3]$.

**Questão 3 (Ref: Oppenheim Ex. 2.4):** Calcule a convolução de dois degraus unitários discretos: $y[n] = u[n] * u[n]$.
> **Resolução Passo a Passo:**
> $$y[n] = \sum_{k=-\infty}^{\infty} u[k]u[n-k]$$
> - $u[k] = 1 \implies k \ge 0$ (limite inferior).
> - $u[n-k] = 1 \implies k \le n$ (limite superior).
> Para $n < 0$, $y[n] = 0$. Para $n \ge 0$:
> $$y[n] = \sum_{k=0}^{n} 1 = n - 0 + 1 = n + 1$$
> **Gabarito:** $y[n] = (n + 1)u[n]$ (rampa discreta unitária).

---

## Tópico 2: Integral de Convolução Básica (Impulsos e Degraus)

**Questão 4 (Ref: Apostila Exemplo 1.6):** Calcule a saída de um SLIT contínuo com resposta ao impulso $h(t) = \delta(t - 3) + 2\delta(t + 1)$ quando excitado por $x(t) = e^{-t}u(t)$.
> **Resolução Passo a Passo:**
> Pela propriedade da replicação do impulso ($x(t) * \delta(t - t_0) = x(t - t_0)$):
> $$y(t) = x(t - 3) + 2x(t + 1)$$
> $$y(t) = e^{-(t-3)}u(t-3) + 2e^{-(t+1)}u(t+1)$$
> **Gabarito:** $y(t) = e^{-(t-3)}u(t-3) + 2e^{-(t+1)}u(t+1)$.

**Questão 5 (Ref: Hsu / Schaum Cap. 2):** Calcule a convolução contínua $y(t) = u(t) * u(t)$.
> **Resolução Passo a Passo:**
> $$y(t) = \int_{-\infty}^{\infty} u(\tau)u(t-\tau)\,d\tau$$
> Como $u(\tau)$ exige $\tau \ge 0$ e $u(t-\tau)$ exige $\tau \le t$, para $t < 0$ temos $y(t) = 0$, e para $t \ge 0$:
> $$y(t) = \int_{0}^{t} 1\,d\tau = \Big[\tau\Big]_{0}^{t} = t$$
> **Gabarito:** $y(t) = t\,u(t)$ (rampa contínua unitária).

**Questão 6 (Ref: Apostila Exemplo 1.8):** Encontre a resposta ao degrau $s(t) = h(t) * u(t)$ para o sistema com resposta ao impulso $h(t) = e^{-3t}u(t)$.
> **Resolução Passo a Passo:**
> A resposta ao degrau é a integral acumulada da resposta ao impulso:
> $$s(t) = \int_{-\infty}^{t} h(\tau)\,d\tau = \int_{0}^{t} e^{-3\tau}\,d\tau \cdot u(t)$$
> $$s(t) = \left[\frac{e^{-3\tau}}{-3}\right]_{0}^{t} u(t) = \frac{1 - e^{-3t}}{3}u(t)$$
> **Gabarito:** $s(t) = \frac{1}{3}\left(1 - e^{-3t}\right)u(t)$.

---

## Tópico 3: Memória, Causalidade e Estabilidade via $h[n]$ e $h(t)$

**Questão 7 (Ref: Haykin Prob. 2.12):** Classifique o sistema LTI com resposta ao impulso $h[n] = 5\delta[n]$ quanto a: (i) sem memória, (ii) causal e (iii) estável.
> **Resolução Passo a Passo:**
> - (i) Como $h[n] = 0$ para todo $n \neq 0$ ($h[n] = c\delta[n]$), a saída é $y[n] = 5x[n]$, logo é **Sem Memória**.
> - (ii) Como $h[n] = 0$ para $n < 0$, é **Causal**.
> - (iii) Como $\sum |h[n]| = 5 < \infty$, é **Estável**.
> **Gabarito:** Sem memória, Causal e Estável.

**Questão 8 (Ref: Oppenheim Prob. 2.28):** O sistema LTI com resposta ao impulso $h[n] = \left(\frac{1}{3}\right)^n u[n]$ é causal e estável?
> **Resolução Passo a Passo:**
> - **Causalidade:** Como $u[n] = 0$ para $n < 0$, temos $h[n] = 0$ para todo $n < 0 \implies$ **Causal**.
> - **Estabilidade:** $\sum_{n=0}^{\infty} \left(\frac{1}{3}\right)^n = \frac{1}{1 - 1/3} = \frac{3}{2} < \infty \implies$ **Estável**.
> **Gabarito:** Causal e Estável.

**Questão 9 (Ref: Oppenheim Prob. 2.29):** O sistema LTI contínuo com $h(t) = e^{-5t}u(t+2)$ é causal? É estável?
> **Resolução Passo a Passo:**
> - **Causalidade:** O degrau $u(t+2)$ liga em $t = -2 < 0$. Logo, $h(t) \neq 0$ em $-2 \le t < 0 \implies$ **Não-Causal**.
> - **Estabilidade:** $\int_{-2}^{\infty} e^{-5t}\,dt = \left[\frac{e^{-5t}}{-5}\right]_{-2}^{\infty} = \frac{e^{10}}{5} < \infty \implies$ **Estável**.
> **Gabarito:** Não-Causal e Estável.

**Questão 10 (Ref: Haykin Prob. 2.12):** O sistema LTI discreto com $h[n] = 4\delta[n-2]$ é sem memória? É causal? É estável?
> **Resolução Passo a Passo:**
> - A saída é $y[n] = 4x[n-2]$ (depende de $n-2 \neq n$), logo tem **Memória** ($h[2] = 4 \neq 0$).
> - Como o impulso está em $n = 2 \ge 0$ ($h[n] = 0$ para $n < 0$), é **Causal**.
> - Como $\sum |h[n]| = 4 < \infty$, é **Estável**.
> **Gabarito:** Com memória, Causal e Estável.

---

## Tópico 4: Interconexão de Sistemas LTI (Série e Paralelo)

**Questão 11 (Ref: Apostila Seção 1.2.3):** Dois sistemas LTI com respostas ao impulso $h_1(t) = e^{-2t}u(t)$ e $h_2(t) = 3e^{-2t}u(t)$ são ligados em **paralelo**. Qual é a resposta ao impulso global $h(t)$?
> **Resolução Passo a Passo:**
> Em paralelo, as respostas ao impulso são somadas (propriedade distributiva):
> $$h(t) = h_1(t) + h_2(t) = e^{-2t}u(t) + 3e^{-2t}u(t) = 4e^{-2t}u(t)$$
> **Gabarito:** $h(t) = 4e^{-2t}u(t)$.

**Questão 12 (Ref: Oppenheim Cap. 2):** Dois sistemas LTI de atraso puro, $h_1[n] = \delta[n-2]$ e $h_2[n] = \delta[n-5]$, são conectados em **cascata (série)**. Qual é a resposta ao impulso equivalente $h[n]$?
> **Resolução Passo a Passo:**
> Em cascata, convoluímos as respostas ao impulso:
> $$h[n] = h_1[n] * h_2[n] = \delta[n-2] * \delta[n-5] = \delta[n - (2 + 5)] = \delta[n-7]$$
> **Gabarito:** $h[n] = \delta[n-7]$.

**Questão 13 (Ref: Apostila Seção 1.2.3):** Dada a resposta ao degrau de um SLIT contínuo como $s(t) = \left(1 - e^{-4t}\right)u(t)$, encontre sua resposta ao impulso $h(t)$.
> **Resolução Passo a Passo:**
> Como $h(t) = \frac{d}{dt}s(t)$:
> $$h(t) = \frac{d}{dt}\left[\left(1 - e^{-4t}\right)u(t)\right] = 4e^{-4t}u(t) + \underbrace{(1 - e^{0})}_{=0}\delta(t) = 4e^{-4t}u(t)$$
> **Gabarito:** $h(t) = 4e^{-4t}u(t)$.

---

## Tópico 5: Equações de Diferenças e Diagramas em Blocos (1ª Ordem)

**Questão 14 (Ref: Apostila Seção 1.3):** Qual é a ordem e a equação característica da equação de diferenças $y[n] - \frac{1}{2}y[n-1] = 3x[n]$? Encontre sua resposta natural homogênea $y_{nat}[n]$ (denotada por $y^{(n)}[n]$ na Seção 1.3.1 da apostila) para $n \ge 0$, sabendo que para entrada nula temos $y_{nat}[0] = 4$.
> **Resolução Passo a Passo:**
> - Ordem: **1ª ordem** ($N = 1$).
> - Equação característica: $r - \frac{1}{2} = 0 \implies r_1 = \frac{1}{2}$.
> - Solução natural geral: $y_{nat}[n] = c_1 \left(\frac{1}{2}\right)^n u[n]$.
> - Usando a condição de entrada nula $y_{nat}[0] = 4 \implies c_1 = 4$.
> **Gabarito:** $y_{nat}[n] = 4\left(\frac{1}{2}\right)^n u[n]$.

**Questão 15 (Ref: Apostila Seção 1.4):** Escreva as equações da **Forma Direta II** para o sistema de 1ª ordem $y[n] + \frac{1}{4}y[n-1] = x[n] + 3x[n-1]$. Quantos blocos de atraso $S$ são necessários?
> **Resolução Passo a Passo:**
> Isolando $y[n] = -\frac{1}{4}y[n-1] + x[n] + 3x[n-1]$, introduzimos o estado intermediário $f[n]$:
> $$\begin{aligned}
> f[n] &= x[n] - \frac{1}{4}f[n-1] \\
> y[n] &= f[n] + 3f[n-1]
> \end{aligned}$$
> Como o sistema é de 1ª ordem ($N = 1$), a Forma Direta II utiliza apenas **1 bloco de atraso $S$**.
> **Gabarito:** $f[n] = x[n] - \frac{1}{4}f[n-1]$ e $y[n] = f[n] + 3f[n-1]$ (1 bloco de atraso $S$).
