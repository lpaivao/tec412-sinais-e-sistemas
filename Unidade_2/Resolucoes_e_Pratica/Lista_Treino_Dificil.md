# Lista de Treino — Nível Difícil / Prova (15 Questões) — Unidade 2
**Disciplina:** Sinais e Sistemas (TEC 412)  
**Tópicos da 2ª Prova:** Convoluções Complexas com Múltiplos Intervalos, Sistemas em Cascata com Equações de Diferenças, Deconvolução, Resolução Completa de EDOs/EDs (Natural + Forçada) e Variáveis de Estado.  
**Referências:** Oppenheim & Willsky (2ª Ed.), Haykin & Van Veen (Bookman), Apostila do Prof. Edgar Silva Júnior.

---

## Tópico 1: Convoluções de Nível Prova (Tempo Discreto e Contínuo)

**Questão 1 (Ref: Oppenheim Prob. 2.5):** Sejam $x[n] = u[n] - u[n-10]$ ($0 \le n \le 9$) e $h[n] = u[n] - u[n - (N+1)]$ ($0 \le n \le N$), onde $N \le 9$ é um inteiro. Determine o valor de $N$ sabendo que $y[n] = x[n] * h[n]$ satisfaz $y[4] = 5$ e $y[14] = 0$.
> **Resolução Passo a Passo:**
> A convolução de dois pulsos iniciados em $n=0$ de comprimentos $10$ (de $0$ a $9$) e $N+1$ (de $0$ a $N$) começa em $n = 0$ e termina em $n_{fim} = 9 + N$ (sendo nula para $n \ge 10 + N$).
> Como $y[14] = 0$, devemos ter $9 + N < 14 \implies N \le 4$.
> Além disso, para $n = 4$, a soma é $\sum_{k=\max(0, 4-N)}^{4} 1$. Para que $y[4] = 5$, todos os 5 termos ($k = 0, 1, 2, 3, 4$) precisam estar ativos, o que exige $4 - N \le 0 \implies N \ge 4$.
> Combinando $N \le 4$ e $N \ge 4$, concluímos que $N = 4$!
> **Gabarito:** $N = 4$ *(Confirmado pág. 554 do Oppenheim)*.

**Questão 2 (Ref: Oppenheim Prob. 2.10):** Suponha que $x(t) = u(t) - u(t-1)$ e $h(t) = x(t/\alpha)$, onde $0 < \alpha \le 1$.
(a) Determine $y(t) = x(t) * h(t)$.
(b) Se $dy(t)/dt$ contém somente **três** descontinuidades, qual é o valor de $\alpha$?
> **Resolução Passo a Passo:**
> (a) $x(t)$ é um pulso de largura $1$ ($0 \le t \le 1$) e $h(t)$ é um pulso de largura $\alpha \le 1$ ($0 \le t \le \alpha$). A convolução é um trapézio:
> $$y(t) = \begin{cases} t, & 0 \le t \le \alpha \\ \alpha, & \alpha \le t \le 1 \\ 1 + \alpha - t, & 1 \le t \le 1 + \alpha \\ 0, & \text{caso contrário} \end{cases}$$
> (b) A derivada $dy(t)/dt$ salta nas quinas do trapézio: $t = 0, \, \alpha, \, 1, \, 1+\alpha$ (4 descontinuidades se $\alpha < 1$). Para que existam apenas **3** descontinuidades, as quinas $t = \alpha$ e $t = 1$ devem coincidir (formando um triângulo!), logo $\alpha = 1$.
> **Gabarito:** (a) Expressão acima; (b) $\alpha = 1$ *(Confirmado pág. 554 do Oppenheim)*.

**Questão 3 (Ref: Oppenheim Prob. 2.12):** Seja $y(t) = e^{-t}u(t) * \sum_{k=-\infty}^{\infty} \delta(t - 3k)$. Mostre que $y(t) = A e^{-t}$ para $0 \le t < 3$ e determine o valor de $A$.
> **Resolução Passo a Passo:**
> Pela propriedade distributiva e deslocamento do impulso:
> $$y(t) = \sum_{k=-\infty}^{\infty} e^{-(t-3k)}u(t - 3k)$$
> Para $0 \le t < 3$, o degrau $u(t - 3k)$ vale $1$ se e somente se $3k \le t \implies k \le 0$ ($k = 0, -1, -2, \dots$):
> $$y(t) = \sum_{k=-\infty}^{0} e^{-(t-3k)} = e^{-t} \sum_{k=-\infty}^{0} e^{3k} = e^{-t} \sum_{m=0}^{\infty} \left(e^{-3}\right)^m = e^{-t} \frac{1}{1 - e^{-3}}$$
> **Gabarito:** $A = \frac{1}{1 - e^{-3}}$ *(Confirmado pág. 554 do Oppenheim)*.

**Questão 4 (Ref: Apostila Exemplo 1.5):** Calcule a convolução contínua entre $x(t) = u(t-1) - u(t-3)$ e $h(t) = u(t+1) - 2u(t-1) + u(t-3)$.
> **Resolução Passo a Passo:**
> - $x(\tau) = 1$ para $1 < \tau < 3$.
> - $h(t-\tau)$ vale $+1$ para $t-1 < \tau < t+1$ e $-1$ para $t-3 < \tau < t-1$.
> Avaliando cada intervalo de sobreposição:
> - $t < 0$: $y(t) = 0$
> - $0 \le t < 2$: $y(t) = \int_1^{t+1} 1\,d\tau = t$
> - $2 \le t < 4$: $y(t) = \int_{t-1}^3 1\,d\tau - \int_1^{t-1} 1\,d\tau = (4 - t) - (t - 2) = -2t + 6$
> - $4 \le t < 6$: $y(t) = -\int_{t-3}^3 1\,d\tau = t - 6$
> - $t \ge 6$: $y(t) = 0$.
> **Gabarito:** $y(t) = t$ ($0\le t<2$), $-2t+6$ ($2\le t<4$), $t-6$ ($4\le t<6$), e $0$ fora.

**Questão 5 (Ref: Oppenheim Prob. 2.11 b, c):** Para os sinais da Questão 4 da Lista Média ($x(t) = u(t-3) - u(t-5)$ e $h(t) = e^{-3t}u(t)$), calcule $g(t) = \left(\frac{dx(t)}{dt}\right) * h(t)$ e explique como $g(t)$ se relaciona com $y(t) = x(t) * h(t)$.
> **Resolução Passo a Passo:**
> A derivada de $x(t) = u(t-3) - u(t-5)$ no sentido das distribuições é:
> $$\frac{dx(t)}{dt} = \delta(t-3) - \delta(t-5)$$
> Convoluindo com $h(t)$:
> $$g(t) = \big(\delta(t-3) - \delta(t-5)\big) * h(t) = h(t-3) - h(t-5) = e^{-3(t-3)}u(t-3) - e^{-3(t-5)}u(t-5)$$
> Pela propriedade da diferenciação na convolução, $g(t) = \frac{dy(t)}{dt}$.
> **Gabarito:** $g(t) = e^{-3(t-3)}u(t-3) - e^{-3(t-5)}u(t-5) = \frac{dy(t)}{dt}$ *(Confirmado pág. 554 do Oppenheim)*.

---

## Tópico 2: Cascata de Sistemas com Equações de Diferenças e Deconvolução

**Questão 6 (Ref: Oppenheim Prob. 2.19):** Considere a cascata de dois sistemas LIT causais $S_1$ e $S_2$:
- $S_1$: $w[n] = \frac{1}{2}w[n-1] + x[n]$
- $S_2$: $y[n] = \alpha y[n-1] + \beta w[n]$
Sabendo que a equação global que relaciona $x[n]$ e $y[n]$ é $y[n] = -\frac{1}{8}y[n-2] + \frac{3}{4}y[n-1] + x[n]$:
(a) Determine $\alpha$ e $\beta$.
(b) Encontre a resposta ao impulso global da cascata.
> **Resolução Passo a Passo:**
> (a) Da equação de $S_2$, isolamos $w[n] = \frac{1}{\beta}\big(y[n] - \alpha y[n-1]\big)$. Substituindo na equação de $S_1$ ($w[n] - \frac{1}{2}w[n-1] = x[n]$):
> $$\frac{1}{\beta}\left(y[n] - \alpha y[n-1] - \frac{1}{2}y[n-1] + \frac{\alpha}{2}y[n-2]\right) = x[n]$$
> $$y[n] = \left(\alpha + \frac{1}{2}\right)y[n-1] - \frac{\alpha}{2}y[n-2] + \beta x[n]$$
> Comparando com $y[n] = \frac{3}{4}y[n-1] - \frac{1}{8}y[n-2] + x[n]$:
> $$\beta = 1, \qquad \alpha + \frac{1}{2} = \frac{3}{4} \implies \alpha = \frac{1}{4}$$
> (b) Como $h_1[n] = \left(\frac{1}{2}\right)^n u[n]$ e $h_2[n] = \left(\frac{1}{4}\right)^n u[n]$, a convolução $h[n] = h_1[n] * h_2[n]$ dá:
> $$h[n] = \frac{(1/2)^{n+1} - (1/4)^{n+1}}{1/2 - 1/4}u[n] = \left[2\left(\frac{1}{2}\right)^n - \left(\frac{1}{4}\right)^n\right]u[n]$$
> **Gabarito:** (a) $\alpha = \frac{1}{4}, \beta = 1$; (b) $h[n] = \left[2\left(\frac{1}{2}\right)^n - \left(\frac{1}{4}\right)^n\right]u[n]$ *(Confirmado pág. 554 do Oppenheim)*.

**Questão 7 (Ref: Oppenheim Prob. 2.24):** Três sistemas LIT estão em cascata: $h_1[n] * h_2[n] * h_2[n] = h[n]$, onde $h_2[n] = u[n] - u[n-2] = \delta[n] + \delta[n-1]$ e a resposta global $h[n]$ tem valores $\{1, 5, 10, 11, 8, 4, 1\}$ para $n = 0, 1, 2, 3, 4, 5, 6$ (e $0$ fora disso).
(a) Encontre $h_1[n]$.
(b) Encontre a saída global para $x[n] = \delta[n] - \delta[n-1]$.
> **Resolução Passo a Passo:**
> (a) Primeiro calculamos $h_{22}[n] = h_2[n] * h_2[n] = (\delta[n] + \delta[n-1]) * (\delta[n] + \delta[n-1]) = \delta[n] + 2\delta[n-1] + \delta[n-2]$ (coeficientes $\{1, 2, 1\}$).
> Como $h[n] = h_1[n] * h_{22}[n] = h_1[n] + 2h_1[n-1] + h_1[n-2]$, resolvemos recursivamente:
> - $n=0$: $h_1[0] = h[0] = 1$
> - $n=1$: $h_1[1] + 2(1) = 5 \implies h_1[1] = 3$
> - $n=2$: $h_1[2] + 2(3) + 1 = 10 \implies h_1[2] = 3$
> - $n=3$: $h_1[3] + 2(3) + 3 = 11 \implies h_1[3] = 2$
> - $n=4$: $h_1[4] + 2(2) + 3 = 8 \implies h_1[4] = 1$
> - $n \ge 5$: $h_1[n] = 0$ (pois $2(1)+2=4=h[5]$ e $1=h[6]$).
> Logo, $h_1[n] = \delta[n] + 3\delta[n-1] + 3\delta[n-2] + 2\delta[n-3] + \delta[n-4]$.
> (b) Como $y[n] = x[n] * h[n]$ e $x[n] = \delta[n] - \delta[n-1]$, pela propriedade do deslocamento do impulso temos diretamente:
> $$y[n] = h[n] - h[n-1] = \delta[n] + 4\delta[n-1] + 5\delta[n-2] + \delta[n-3] - 3\delta[n-4] - 4\delta[n-5] - 3\delta[n-6] - \delta[n-7]$$

---

## Tópico 3: Resolução Completa de EDOs e EDs (Natural + Forçada)

**Questão 8 (Ref: Oppenheim Prob. 2.17):** Considere o sistema LIT em repouso inicial descrito pela EDO $\frac{d}{dt}y(t) + 4y(t) = x(t)$.
(a) Se $x(t) = e^{(-1 + 3j)t}u(t)$, qual é $y(t)$?
(b) Usando a parte real do item (a), determine a saída para $x(t) = e^{-t}\cos(3t)u(t)$.
> **Resolução Passo a Passo:**
> (a) Para $t \ge 0$, a solução natural é $y^{(n)}(t) = c e^{-4t}$ e a solução particular para $e^{(-1+3j)t}$ é $y^{(p)}(t) = K e^{(-1+3j)t}$:
> $$(-1 + 3j + 4)K = 1 \implies K = \frac{1}{3 + 3j} = \frac{3 - 3j}{18} = \frac{1 - j}{6}$$
> Aplicando repouso inicial $y(0^+) = 0 \implies c + K = 0 \implies c = -K$:
> $$y(t) = \frac{1 - j}{6}\left[e^{(-1+3j)t} - e^{-4t}\right]u(t)$$
> (b) Tomando a parte real $\mathcal{R}e\{y(t)\}$:
> Como $\mathcal{R}e\big\{(1 - j)(\cos 3t + j\text{sen}\,3t)\big\} = \cos(3t) + \text{sen}(3t)$:
> $$y_r(t) = \frac{1}{6}\left[e^{-t}\big(\cos(3t) + \text{sen}(3t)\big) - e^{-4t}\right]u(t)$$
> **Gabarito:** Confirmado na pág. 554 do Oppenheim!

**Questão 9 (Ref: Apostila Exemplos 1.14, 1.18 e 1.20):** Para a ED $y[n] - \frac{3}{4}y[n-1] + \frac{1}{8}y[n-2] = 2x[n]$, com condições iniciais $y[-1] = 1, y[-2] = -1$ e entrada $x[n] = 2u[n]$, determine:
(a) A resposta natural $y^{(n)}[n]$; (b) A resposta forçada $y^{(f)}[n]$; (c) A resposta completa $y[n]$.
> **Resolução Passo a Passo:**
> - Raízes características: $r_1 = \frac{1}{4}, r_2 = \frac{1}{2}$.
> - Solução particular para $x[n] = 2u[n]$: $y^{(p)}[n] = c u[n] \implies c\left(1 - \frac{3}{4} + \frac{1}{8}\right) = 4 \implies \frac{3}{8}c = 4 \implies c = \frac{32}{3}$.
> - (a) Resposta natural ($x[n]=0$): $y[0] = \frac{3}{4}(1) - \frac{1}{8}(-1) = \frac{7}{8}$ e $y[1] = \frac{3}{4}(\frac{7}{8}) - \frac{1}{8}(1) = \frac{17}{32}$, dando $y^{(n)}[n] = \left[-\frac{3}{8}\left(\frac{1}{4}\right)^n + \frac{5}{4}\left(\frac{1}{2}\right)^n\right]u[n]$.
> - (b) Resposta forçada ($y[-1]=y[-2]=0$): $y[0] = 4$ e $y[1] = 7$, dando $y^{(f)}[n] = \left[\frac{4}{3}\left(\frac{1}{4}\right)^n - 8\left(\frac{1}{2}\right)^n + \frac{32}{3}\right]u[n]$.
> - (c) Resposta completa ($y^{(n)} + y^{(f)}$):
>   $$y[n] = \left[\frac{23}{24}\left(\frac{1}{4}\right)^n - \frac{27}{4}\left(\frac{1}{2}\right)^n + \frac{32}{3}\right]u[n]$$

**Questão 10 (Ref: Apostila Exemplos 1.13, 1.17 e 1.19):** Um circuito RL série com $R = 1\,\Omega$ e $L = 1\,\text{H}$ é descrito pela EDO $\frac{d}{dt}y(t) + y(t) = x(t)$, com corrente inicial $y(0^-) = 2\,\text{A}$ e entrada $x(t) = \cos(\pi t)u(t)$. Determine a resposta completa $y(t)$ para $t \ge 0$.
> **Resolução Passo a Passo:**
> - Solução natural: $y^{(n)}(t) = 2e^{-t}u(t)$.
> - Solução particular: $y^{(p)}(t) = \frac{1}{\pi^2+1}\cos(\pi t) + \frac{\pi}{\pi^2+1}\text{sen}(\pi t)$.
> - Solução forçada ($y^{(f)}(0) = 0$): $y^{(f)}(t) = \left[-\frac{1}{\pi^2+1}e^{-t} + \frac{1}{\pi^2+1}\cos(\pi t) + \frac{\pi}{\pi^2+1}\text{sen}(\pi t)\right]u(t)$.
> - Solução completa:
>   $$y(t) = \left[\frac{2\pi^2 + 1}{\pi^2 + 1}e^{-t} + \frac{1}{\pi^2 + 1}\cos(\pi t) + \frac{\pi}{\pi^2 + 1}\text{sen}(\pi t)\right]u(t)$$

---

## Tópico 4: Descrição por Variáveis de Estado e Resposta em Frequência

**Questão 11 (Ref: Apostila Seção 1.5, págs. 53–54):** A partir da Forma Direta II para a equação de diferenças $y[n] + a_1 y[n-1] + a_2 y[n-2] = x[n] + b_1 x[n-1] + b_2 x[n-2]$ (com $a_1 = \frac{1}{2}, a_2 = -\frac{1}{4}, b_1 = 2, b_2 = 1$), escreva as matrizes $\mathbf{A}, \mathbf{b}, \mathbf{c}, D$ da representação por variáveis de estado $\mathbf{q}[n+1] = \mathbf{A}\mathbf{q}[n] + \mathbf{b}x[n]$ e $y[n] = \mathbf{c}\mathbf{q}[n] + Dx[n]$.
> **Resolução Passo a Passo:**
> Pela formulação das págs. 53–54 da apostila, definindo $q_1[n] = f[n-1]$ e $q_2[n] = f[n-2]$:
> $$\mathbf{A} = \begin{bmatrix} -a_1 & -a_2 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} -1/2 & 1/4 \\ 1 & 0 \end{bmatrix}, \qquad \mathbf{b} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$
> $$\mathbf{c} = \begin{bmatrix} b_1 - a_1 & b_2 - a_2 \end{bmatrix} = \begin{bmatrix} 2 - 1/2 & 1 - (-1/4) \end{bmatrix} = \begin{bmatrix} 3/2 & 5/4 \end{bmatrix}, \qquad D = [1]$$

**Questão 12 (Ref: Apostila Seção 1.5, pág. 55):** Escreva a representação matricial em variáveis de estado para a EDO do Exercício 1.3(b) da apostila: $\frac{d^2}{dt^2}y(t) + 3y(t) = 2\frac{d^2}{dt^2}x(t) + \frac{d}{dt}x(t)$.
> **Resolução Passo a Passo:**
> Comparando com $\frac{d^2}{dt^2}y + a_1\frac{d}{dt}y + a_0 y = b_2\frac{d^2}{dt^2}x + b_1\frac{d}{dt}x + b_0 x$, temos $a_1 = 0, a_0 = 3, b_2 = 2, b_1 = 1, b_0 = 0$. Pela fórmula da pág. 55 da apostila:
> $$\mathbf{A} = \begin{bmatrix} -a_1 & -a_0 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -3 \\ 1 & 0 \end{bmatrix}, \qquad \mathbf{b} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$
> $$\mathbf{c} = \begin{bmatrix} b_1 - a_1 b_2 & b_0 - a_0 b_2 \end{bmatrix} = \begin{bmatrix} 1 - 0 & 0 - 3(2) \end{bmatrix} = \begin{bmatrix} 1 & -6 \end{bmatrix}, \qquad D = [b_2] = [2]$$

**Questão 13 (Ref: Apostila Seção 1.2.3, pág. 32):** Um SLIT contínuo possui resposta ao impulso $h(t) = e^{-2t}u(t)$. Determine sua resposta em frequência $H(j\omega)$ e a saída em regime permanente para $x(t) = e^{j3t}$.
> **Resolução Passo a Passo:**
> $$H(j\omega) = \int_{-\infty}^{\infty} h(\tau)e^{-j\omega\tau}\,d\tau = \int_{0}^{\infty} e^{-(2 + j\omega)\tau}\,d\tau = \frac{1}{2 + j\omega}$$
> Para $\omega = 3$: $H(j3) = \frac{1}{2 + j3}$, logo a saída é $y(t) = \frac{1}{2 + j3}e^{j3t}$.

**Questão 14 (Ref: Oppenheim Prob. 2.16):** Determine se cada afirmação sobre a convolução é verdadeira ou falsa:
(a) Se $x[n] = 0$ para $n < N_1$ e $h[n] = 0$ para $n < N_2$, então $x[n]*h[n] = 0$ para $n < N_1 + N_2$.
(b) Se $y[n] = x[n]*h[n]$, então $y[n-1] = x[n-1]*h[n-1]$.
(c) Se $y(t) = x(t)*h(t)$, então $y(-t) = x(-t)*h(-t)$.
(d) Se $x(t) = 0$ para $t > T_1$ e $h(t) = 0$ para $t > T_2$, então $x(t)*h(t) = 0$ para $t > T_1 + T_2$.
> **Resolução Passo a Passo:**
> - **(a) Verdadeiro:** o início da convolução é a soma dos inícios ($N_1 + N_2$).
> - **(b) Falso:** atrasar ambos os sinais de 1 amostra atrasa a convolução de **2** amostras ($x[n-1]*h[n-1] = y[n-2] \neq y[n-1]$).
> - **(c) Verdadeiro:** trocando $\tau \to -\tau$ na integral de convolução, verifica-se que $\int x(-\tau)h(-t+\tau)d\tau = y(-t)$.
> - **(d) Verdadeiro:** o término da convolução é a soma dos términos ($T_1 + T_2$).
> **Gabarito:** (a) V; (b) F; (c) V; (d) V *(Confirmado pág. 554 do Oppenheim)*.

**Questão 15 (Ref: Haykin Prob. 2.13):** Explique como demonstrar que a somabilidade absoluta $\sum_{k=-\infty}^{\infty} |h[k]| < \infty$ é também uma condição **necessária** para estabilidade BIBO (isto é, se $\sum |h[k]| = \infty$, existe uma entrada limitada $|x[n]| \le 1$ que produz saída ilimitada em $n = 0$).
> **Resolução Passo a Passo:**
> Se $\sum_{k=-\infty}^{\infty} |h[k]| = \infty$, escolhemos a entrada limitada por $1$ definida como:
> $$x[-k] = \text{sgn}(h[k]) = \begin{cases} +1, & h[k] > 0 \\ -1, & h[k] < 0 \\ 0, & h[k] = 0 \end{cases}$$
> Claramente $|x[n]| \le 1$ para todo $n$. Porém, avaliando a saída no instante $n = 0$:
> $$y[0] = \sum_{k=-\infty}^{\infty} h[k]x[-k] = \sum_{k=-\infty}^{\infty} h[k]\text{sgn}(h[k]) = \sum_{k=-\infty}^{\infty} |h[k]| = \infty$$
> Portanto, uma entrada limitada produziu saída infinita, provando que o sistema é instável! $\blacksquare$
