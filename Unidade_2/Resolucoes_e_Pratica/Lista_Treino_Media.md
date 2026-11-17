# Lista de Treino — Nível Médio (15 Questões) — Unidade 2
**Disciplina:** Sinais e Sistemas (TEC 412)  
**Tópicos da 2ª Prova:** Convolução Discreta e Contínua por Intervalos, Propriedades da Convolução, Interconexões Mistas, Estabilidade/Causalidade com Sinais Laterais Esquerdos, EDOs/EDs e Formas Direta I e II.  
**Referências:** Oppenheim & Willsky (2ª Ed.), Haykin & Van Veen (Bookman), Hsu (Schaum).

---

## Tópico 1: Soma de Convolução com Exponenciais e Pulsos

**Questão 1 (Ref: Oppenheim Prob. 2.21a):** Calcule $y[n] = x[n] * h[n]$ para $x[n] = \alpha^n u[n]$ e $h[n] = \beta^n u[n]$, com $\alpha \neq \beta$.
> **Resolução Passo a Passo:**
> $$y[n] = \sum_{k=-\infty}^{\infty} \alpha^k u[k] \beta^{n-k} u[n-k]$$
> Os degraus exigem $0 \le k \le n$ (logo $y[n] = 0$ para $n < 0$). Para $n \ge 0$:
> $$y[n] = \beta^n \sum_{k=0}^{n} \left(\frac{\alpha}{\beta}\right)^k = \beta^n \left[\frac{1 - (\alpha/\beta)^{n+1}}{1 - \alpha/\beta}\right] = \frac{\beta^{n+1} - \alpha^{n+1}}{\beta - \alpha}u[n]$$
> **Gabarito:** $y[n] = \left(\frac{\alpha^{n+1} - \beta^{n+1}}{\alpha - \beta}\right)u[n]$.

**Questão 2 (Ref: Oppenheim Prob. 2.21b):** Calcule $y[n] = x[n] * h[n]$ quando $x[n] = h[n] = \alpha^n u[n]$.
> **Resolução Passo a Passo:**
> Para $n \ge 0$:
> $$y[n] = \sum_{k=0}^{n} \alpha^k \alpha^{n-k} = \sum_{k=0}^{n} \alpha^n = \alpha^n \sum_{k=0}^{n} 1 = (n + 1)\alpha^n u[n]$$
> **Gabarito:** $y[n] = (n + 1)\alpha^n u[n]$.

**Questão 3 (Ref: Oppenheim Prob. 2.1):** Sejam $x[n] = \delta[n] + 2\delta[n-1] - \delta[n-3]$ e $h[n] = 2\delta[n+1] + 2\delta[n-1]$. Calcule $y_1[n] = x[n] * h[n]$.
> **Resolução Passo a Passo:**
> Pela distributividade:
> $$y_1[n] = 2x[n+1] + 2x[n-1]$$
> - $2x[n+1] = 2\delta[n+1] + 4\delta[n] - 2\delta[n-2]$
> - $2x[n-1] = 2\delta[n-1] + 4\delta[n-2] - 2\delta[n-4]$
> Somando termo a termo:
> $$y_1[n] = 2\delta[n+1] + 4\delta[n] + 2\delta[n-1] + 2\delta[n-2] - 2\delta[n-4]$$
> **Gabarito:** $y_1[n] = 2\delta[n+1] + 4\delta[n] + 2\delta[n-1] + 2\delta[n-2] - 2\delta[n-4]$ *(Confirmado pág. 554 do Oppenheim)*.

---

## Tópico 2: Integral de Convolução por Intervalos

**Questão 4 (Ref: Oppenheim Prob. 2.11a):** Sejam $x(t) = u(t-3) - u(t-5)$ e $h(t) = e^{-3t}u(t)$. Calcule $y(t) = x(t) * h(t)$.
> **Resolução Passo a Passo:**
> - $x(\tau) = 1$ para $3 \le \tau \le 5$, e $0$ fora disso.
> - $h(t-\tau) = e^{-3(t-\tau)}u(t-\tau)$ vale $e^{-3(t-\tau)}$ para $\tau \le t$.
> 1. **Para $t < 3$:** $\tau \le t$ não alcança $[3, 5] \implies y(t) = 0$.
> 2. **Para $3 \le t \le 5$:**
>    $$y(t) = \int_{3}^{t} e^{-3(t-\tau)}\,d\tau = e^{-3t}\left[\frac{e^{3\tau}}{3}\right]_{3}^{t} = \frac{1 - e^{-3(t-3)}}{3}$$
> 3. **Para $t > 5$:**
>    $$y(t) = \int_{3}^{5} e^{-3(t-\tau)}\,d\tau = e^{-3t}\left(\frac{e^{15} - e^{9}}{3}\right) = \frac{(1 - e^{-6})e^{-3(t-5)}}{3}$$
> **Gabarito:** $y(t) = 0$ ($t < 3$), $\frac{1 - e^{-3(t-3)}}{3}$ ($3 \le t \le 5$) e $\frac{(1 - e^{-6})e^{-3(t-5)}}{3}$ ($t > 5$) *(Confirmado pág. 554 do Oppenheim)*.

**Questão 5 (Ref: Oppenheim Prob. 2.8):** Determine a convolução $y(t) = x(t) * h(t)$ para $h(t) = \delta(t+2) + 2\delta(t+1)$ e:
$$x(t) = \begin{cases} t+1, & 0 \le t \le 1 \\ 2-t, & 1 < t \le 2 \\ 0, & \text{c.c.} \end{cases}$$
> **Resolução Passo a Passo:**
> Pela propriedade da replicação do impulso:
> $$y(t) = x(t+2) + 2x(t+1)$$
> - $x(t+2)$ existe em $-2 \le t \le 0$: vale $(t+2)+1 = t+3$ em $[-2, -1]$ e $2-(t+2) = -t$ em $[-1, 0]$.
> - $2x(t+1)$ existe em $-1 \le t \le 1$: vale $2(t+2) = 2t+4$ em $[-1, 0]$ e $2(1-t) = 2-2t$ em $[0, 1]$.
> Somando em cada subintervalo:
> - Em $-2 < t \le -1$: $y(t) = t + 3$.
> - Em $-1 < t \le 0$: $y(t) = -t + (2t + 4) = t + 4$.
> - Em $0 < t \le 1$: $y(t) = 2 - 2t$.
> **Gabarito:** $y(t) = t+3$ ($-2 < t \le -1$), $t+4$ ($-1 < t \le 0$), $2-2t$ ($0 < t \le 1$) e $0$ c.c. *(Confirmado pág. 554 do Oppenheim)*.

**Questão 6 (Ref: Haykin Prob. 2.39a):** Calcule $y(t) = \big(u(t) - u(t-2)\big) * u(t)$.
> **Resolução Passo a Passo:**
> Usando $u(t) * u(t) = t\,u(t)$ e a invariância no tempo:
> $$y(t) = u(t)*u(t) - u(t-2)*u(t) = t\,u(t) - (t-2)u(t-2)$$
> Abrindo por intervalos:
> - $t < 0$: $y(t) = 0$
> - $0 \le t < 2$: $y(t) = t$
> - $t \ge 2$: $y(t) = t - (t-2) = 2$
> **Gabarito:** $y(t) = t\,u(t) - (t-2)u(t-2)$.

---

## Tópico 3: Causalidade, Estabilidade e Sistema Inverso

**Questão 7 (Ref: Oppenheim Prob. 2.13):** Considere um sistema LTI $S_1$ com resposta ao impulso $h[n] = \left(\frac{1}{5}\right)^n u[n]$.
(a) Encontre a constante $A$ tal que $h[n] - A h[n-1] = \delta[n]$.
(b) Determine a resposta ao impulso $g[n]$ do sistema inverso $S_2$.
> **Resolução Passo a Passo:**
> (a) Observando que $\frac{1}{5}h[n-1] = \frac{1}{5}\left(\frac{1}{5}\right)^{n-1}u[n-1] = \left(\frac{1}{5}\right)^n u[n-1]$, subtraímos de $h[n] = \left(\frac{1}{5}\right)^n u[n]$:
> $$h[n] - \frac{1}{5}h[n-1] = \left(\frac{1}{5}\right)^n \big(u[n] - u[n-1]\big) = \left(\frac{1}{5}\right)^n \delta[n] = \left(\frac{1}{5}\right)^0 \delta[n] = \delta[n] \implies A = \frac{1}{5}$$
> (b) Como $h[n] * \big(\delta[n] - \frac{1}{5}\delta[n-1]\big) = \delta[n]$, a resposta ao impulso do sistema inverso é:
> $$g[n] = \delta[n] - \frac{1}{5}\delta[n-1]$$
> **Gabarito:** (a) $A = \frac{1}{5}$; (b) $g[n] = \delta[n] - \frac{1}{5}\delta[n-1]$ *(Confirmado pág. 554 do Oppenheim)*.

**Questão 8 (Ref: Oppenheim Prob. 2.14):** Verifique se as respostas ao impulso abaixo correspondem a sistemas LIT contínuos estáveis:
(a) $h_1(t) = e^{-(1 - 2j)t}u(t)$; (b) $h_2(t) = e^{-t}\cos(2t)u(t)$.
> **Resolução Passo a Passo:**
> (a) Como $|e^{-(1-2j)t}| = |e^{-t}|\cdot|e^{j2t}| = e^{-t} \cdot 1 = e^{-t}$:
> $$\int_{0}^{\infty} |h_1(t)|\,dt = \int_{0}^{\infty} e^{-t}\,dt = 1 < \infty \implies \textbf{Estável!}$$
> (b) Como $|\cos(2t)| \le 1$:
> $$\int_{0}^{\infty} |e^{-t}\cos(2t)|\,dt \le \int_{0}^{\infty} e^{-t}\,dt = 1 < \infty \implies \textbf{Estável!}$$
> **Gabarito:** Ambos $h_1(t)$ e $h_2(t)$ são estáveis *(Confirmado pág. 554 do Oppenheim)*.

**Questão 9 (Ref: Oppenheim Prob. 2.15):** Verifique qual das respostas ao impulso discretas corresponde a um sistema LIT estável:
(a) $h_1[n] = n\cos\left(\frac{\pi}{4}n\right)u[n]$; (b) $h_2[n] = 3^n u[-n+10]$.
> **Resolução Passo a Passo:**
> (a) Os termos de $h_1[n]$ crescem linearmente com $n$ (por exemplo, para $n = 8k$, $h_1[8k] = 8k \to \infty$), logo $\sum |h_1[n]| = \infty \implies$ **Instável**.
> (b) Para $h_2[n]$, o suporte é $n \le 10$ (lateral esquerdo). Quando $n \to -\infty$, $3^n \to 0$ geometricamente:
> $$\sum_{n=-\infty}^{10} 3^n = \frac{3^{10}}{1 - 1/3} = \frac{3^{11}}{2} < \infty \implies \textbf{Estável!}$$
> **Gabarito:** Apenas $h_2[n]$ é estável *(Confirmado pág. 554 do Oppenheim)*.

---

## Tópico 4: Interconexões e Propriedades Algébricas

**Questão 10 (Ref: Oppenheim Prob. 2.27):** Definimos a área sob um sinal contínuo como $A_v = \int_{-\infty}^{\infty} v(t)\,dt$. Demonstre que se $y(t) = x(t) * h(t)$, então $A_y = A_x \cdot A_h$.
> **Resolução Passo a Passo:**
> Integrando $y(t)$ de $-\infty$ a $+\infty$ (assumindo $x$ e $h$ absolutamente integráveis para aplicar o Teorema de Fubini):
> $$A_y = \int_{-\infty}^{\infty} \left[\int_{-\infty}^{\infty} x(\tau)h(t-\tau)\,d\tau\right] dt$$
> Trocando a ordem de integração:
> $$A_y = \int_{-\infty}^{\infty} x(\tau) \left[\int_{-\infty}^{\infty} h(t-\tau)\,dt\right] d\tau$$
> Fazendo a mudança de variável $\lambda = t - \tau$ ($d\lambda = dt$) na integral interna, temos $\int_{-\infty}^{\infty} h(\lambda)\,d\lambda = A_h$:
> $$A_y = \int_{-\infty}^{\infty} x(\tau) \cdot A_h\,d\tau = A_h \int_{-\infty}^{\infty} x(\tau)\,d\tau = A_x \cdot A_h \quad \blacksquare$$

**Questão 11 (Ref: Apostila Exemplo 1.7):** Considere um sistema com $h_1[n] = u[n]$ e $h_2[n] = u[n+2] - u[n]$ em paralelo, seguidos em série por $h_3[n] = \delta[n-2]$. Calcule a resposta ao impulso equivalente $h_{123}[n]$.
> **Resolução Passo a Passo:**
> 1. Paralelo: $h_{12}[n] = h_1[n] + h_2[n] = u[n] + u[n+2] - u[n] = u[n+2]$.
> 2. Série com $h_3[n]$: $h_{123}[n] = u[n+2] * \delta[n-2] = u[(n-2)+2] = u[n]$.
> **Gabarito:** $h_{123}[n] = u[n]$.

**Questão 12 (Ref: Haykin Prob. 2.14a):** Avalie a resposta ao degrau $s[n] = h[n] * u[n]$ para o sistema LTI com $h[n] = \left(\frac{1}{2}\right)^n u[n]$.
> **Resolução Passo a Passo:**
> $$s[n] = \sum_{k=-\infty}^{n} h[k] = \sum_{k=0}^{n} \left(\frac{1}{2}\right)^k u[n] = 2\left[1 - \left(\frac{1}{2}\right)^{n+1}\right]u[n]$$
> **Gabarito:** $s[n] = 2\left[1 - \left(\frac{1}{2}\right)^{n+1}\right]u[n]$.

---

## Tópico 5: EDOs, EDs e Formas Direta I e II

**Questão 13 (Ref: Oppenheim Prob. 2.18):** Considere um sistema LIT causal descrito por $y[n] = \frac{1}{4}y[n-1] + x[n]$. Determine $y[n]$ quando $x[n] = \delta[n-1]$.
> **Resolução Passo a Passo:**
> Para $x[n] = \delta[n]$ (impulso na origem), a resposta ao impulso causal de $y[n] - \frac{1}{4}y[n-1] = x[n]$ é $h[n] = \left(\frac{1}{4}\right)^n u[n]$.
> Pela invariância no tempo, para $x[n] = \delta[n-1]$, a saída é $h[n-1]$:
> $$y[n] = \left(\frac{1}{4}\right)^{n-1} u[n-1]$$
> **Gabarito:** $y[n] = \left(\frac{1}{4}\right)^{n-1} u[n-1]$ *(Confirmado pág. 554 do Oppenheim)*.

**Questão 14 (Ref: Apostila Exemplo 1.14):** Encontre as raízes características e a forma geral da resposta natural para a ED de 2ª ordem $y[n] - \frac{3}{4}y[n-1] + \frac{1}{8}y[n-2] = 2x[n]$.
> **Resolução Passo a Passo:**
> Equação característica:
> $$r^2 - \frac{3}{4}r + \frac{1}{8} = 0 \implies \left(r - \frac{1}{2}\right)\left(r - \frac{1}{4}\right) = 0 \implies r_1 = \frac{1}{4}, \; r_2 = \frac{1}{2}$$
> **Gabarito:** $y^{(n)}[n] = \left[c_1\left(\frac{1}{4}\right)^n + c_2\left(\frac{1}{2}\right)^n\right]u[n]$.

**Questão 15 (Ref: Apostila Seção 1.4):** Escreva as equações da Forma Direta I e da Forma Direta II para a EDO de 2ª ordem $\frac{d^2}{dt^2}y(t) + 5\frac{d}{dt}y(t) + 6y(t) = \frac{d^2}{dt^2}x(t) + 4x(t)$.
> **Resolução Passo a Passo:**
> Integrando duas vezes ($N = 2$):
> $$y(t) + 5y^{(1)}(t) + 6y^{(2)}(t) = x(t) + 4x^{(2)}(t)$$
> - **Forma Direta I:**
>   $$w(t) = x(t) + 4x^{(2)}(t), \qquad y(t) = w(t) - 5y^{(1)}(t) - 6y^{(2)}(t)$$
> - **Forma Direta II:**
>   $$f(t) = x(t) - 5f^{(1)}(t) - 6f^{(2)}(t), \qquad y(t) = f(t) + 4f^{(2)}(t)$$
> **Gabarito:** Equações acima (com 2 integradores no ramo central na Forma Direta II).
