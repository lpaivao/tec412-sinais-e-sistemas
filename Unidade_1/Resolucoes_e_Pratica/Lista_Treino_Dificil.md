# Lista de Treino - Nível Difícil (15 Questões)
**Disciplina:** Sinais e Sistemas (TEC 412)
**Tópicos:** Análise Abstrata, Propriedades Complexas e Pegadinhas de Prova.

---

## Tópico 1: Sinais Pares e Ímpares

**Questão 1:** Prove que o sinal $x(t) = t \sin(t) + \cos^2(t)$ é puramente par.
> **Resolução:**
> Aplicando o teste de reversão $t \to -t$:
> $x(-t) = (-t) \sin(-t) + (\cos(-t))^2$
> Sabendo que $\sin(-t) = -\sin(t)$ e $\cos(-t) = \cos(t)$:
> $x(-t) = (-t)(-\sin(t)) + (\cos(t))^2$
> $x(-t) = t \sin(t) + \cos^2(t) = x(t)$.
> O sinal é inteiramente par, logo sua componente ímpar é obrigatoriamente nula para todo $t$.
> **Gabarito: Sinal 100% Par.**

**Questão 2:** A parte par de um sinal real é $x_p(t) = |t|$. Sabendo que o sinal original $x(t) = 0$ estritamente para $t < 0$, recupere o sinal completo $x(t)$.
> **Resolução:**
> Sabemos que a parte par é $x_p(t) = \frac{x(t) + x(-t)}{2} = |t|$.
> Para $t > 0$, o sinal revertido $x(-t)$ cai no território negativo. Como $x(t)$ é zero para tempos negativos, $x(-t) = 0$ para todo $t>0$.
> Assim, para $t > 0$: $\frac{x(t) + 0}{2} = |t| \implies \frac{x(t)}{2} = t \implies x(t) = 2t$.
> Como ele é $0$ para $t < 0$, o sinal completo recriado é:
> **Gabarito: $x(t) = 2t \cdot u(t)$.**

---

## Tópico 2: Energia e Potência

**Questão 3:** Encontre a potência do sinal da onda quadrada $x(t) = \sum_{k=-\infty}^{\infty} rect\left(\frac{t - 2k}{1}\right)$.
> **Resolução:**
> Trata-se de um trem de pulsos retangulares. A largura do pulso é 1, e eles estão espaçados a cada 2 unidades de tempo. Logo, o período é $T_0 = 2$.
> A potência de sinais periódicos se calcula em um único período:
> $P = \frac{1}{2} \int_{-1}^{1} |x(t)|^2 dt$.
> Dentro do intervalo de um período completo ($t \in [-1, 1]$), a onda retangular "liga" (vale 1) na faixa $[-0.5, 0.5]$ e fica zero no resto.
> $P = \frac{1}{2} \int_{-0.5}^{0.5} (1)^2 dt = \frac{1}{2} \left[ \tau \right]_{-0.5}^{0.5} = \frac{1}{2} \cdot 1 = 0.5 \text{ Watts}$.
> **Gabarito: Potência de 0.5 W (Energia é $\infty$).**

**Questão 4:** O sinal $x(t) = \cos(t) \cdot u(t)$ é de energia ou de potência?
> **Resolução:**
> Apesar de começar no tempo zero devido ao degrau e ser nulo à esquerda, ele oscila até o infinito positivo com amplitude constante.
> Sua energia diverge (área infinta). Indo pra potência calculada como o limite até $T \to \infty$:
> $P = \lim_{T \to \infty} \frac{1}{2T} \int_{0}^{T} \cos^2(t) dt$.
> Resolvendo e dividindo pelos $2T$ infinitos, o valor da potência se assenta em exatamente metade da potência de uma senoide bidirecional total.
> **Gabarito: Sinal de Potência ($P = 0.25 W$).**

---

## Tópico 3: Memória

**Questão 5:** O sistema $y(t) = x(2-t)$ possui memória?
> **Resolução:**
> Testando o instante presente $t=0$: $y(0) = x(2-0) = x(2)$.
> O sistema, posicionado no instante $0$, requisitou o valor que ocorrerá no instante $2$. Diferiu do instante de leitura, obriga armazenamento de estado (ou antecipação de buffer).
> **Gabarito: Com Memória.**

**Questão 6:** O filtro não-linear de mediana local $y[n] = \text{mediana}(x[n], x[n-1], x[n-2])$ exige memória?
> **Resolução:**
> O ato mecânico de extrair a mediana requer ordenar 3 amostras, sendo uma presente ($n$) e duas passadas ($n-1, n-2$). A leitura de instantes passados decreta a existência de registradores de atraso.
> **Gabarito: Com Memória.**

---

## Tópico 4: Causalidade

**Questão 7:** O filtro de suavização avançada $y(t) = \int_{t-1}^{t+1} x(\tau) d\tau$ é causal?
> **Resolução:**
> Avalie o limite superior da integral. Para determinar a saída no instante hoje $t$, eu preciso integrar a área do sinal até o limite de amanhã ($t+1$). Como usa o conhecimento futuro do sinal...
> **Gabarito: NÃO-Causal.**

**Questão 8:** O subamostrador contínuo da forma $y(t) = x(t) \cdot \delta(t-3)$ é causal?
> **Resolução:**
> Cuidado: o "3" está na resposta impulsiva/função do sistema, mas o sinal na entrada exigido é APENAS o próprio instante de tempo presente: $x(t)$. Em nenhum momento a função pediu para ler um $x$ diferente.
> **Gabarito: Causal.**

---

## Tópico 5: Linearidade

**Questão 9:** O sistema $y(t) = x^2(t) + x(t)$ é linear?
> **Resolução:**
> Falha grotescamente na homogeneidade.
> Seja $x(t) \to y(t)$. 
> Aplique um ganho $A$: entrada $A \cdot x(t)$. A saída gerada será $(Ax)^2 + Ax = A^2x^2 + Ax$.
> Para ser linear, a saída deveria ser estritamente $A \cdot y(t) = A(x^2 + x) = Ax^2 + Ax$.
> Como $A^2x^2 \neq Ax^2$ para $A \neq 1$, a regra quebra.
> **Gabarito: NÃO-Linear.**

**Questão 10:** O filtro de Volterra quadrático de 1ª ordem $y[n] = x[n] \cdot x[n-1]$ preserva a superposição?
> **Resolução:**
> Seja entrada $x_3[n] = x_1[n] + x_2[n]$ (omitindo ganhos pra ficar fácil).
> $y_3[n] = (x_1[n] + x_2[n]) \cdot (x_1[n-1] + x_2[n-1])$
> Ao fazer a distributiva, surgem termos cruzados (cross-talk):
> $x_1[n]x_1[n-1] + x_2[n]x_2[n-1] + x_1[n]x_2[n-1] + x_2[n]x_1[n-1]$.
> Os dois primeiros termos são $y_1[n] + y_2[n]$. Mas a equação gerou lixo extra e não linear cruzado entre os dois sinais de entrada.
> **Gabarito: NÃO-Linear.**

---

## Tópico 6: Invariância no Tempo

**Questão 11:** O reversor puro de tempo (fita de cassete rodando ao contrário) $y(t) = x(-t)$ altera o formato se aplicar um atraso?
> **Resolução:**
> 1) Atrase apenas a entrada criando $x_a(t) = x(t-t_0)$. A saída processando $x_a$ emite $x_a(-t) = x(-t - t_0)$.
> 2) Atrase todo o sistema original global: Vá na fórmula $y(t) = x(-t)$ e substitua a letra "t" por "$(t-t_0)$".
> $y_2(t) = x(-(t-t_0)) = x(-t + t_0)$.
> Observando a álgebra de sinais: $x(-t - t_0) \neq x(-t + t_0)$. As direções de translação viraram opostas.
> **Gabarito: Variante no Tempo.**

**Questão 12:** O integrador comprimido $y(t) = \int_{-\infty}^{2t} x(\tau) d\tau$ é invariante?
> **Resolução:**
> Atrasando a entrada geramos um sinal deslocado $\tau-t_0$ dentro da integral. Mas quando aplicamos o atraso global no tempo, substituímos o limite superior para $2(t-t_0) = 2t - 2t_0$. Como as escalas de atraso ficam diferentes (uma atrasa de $t_0$, o limite de integração escorrega $2t_0$), os resultados divergem.
> **Gabarito: Variante no Tempo.**

---

## Tópico 7: Estabilidade BIBO

**Questão 13:** O sistema derivador ideal $y(t) = \frac{dx(t)}{dt}$ garante estabilidade?
> **Resolução:**
> Para estabilidade BIBO, qualquer sinal limitado deve gerar saída limitada.
> Imagine uma entrada $x(t) = u(t)$ (a famosa função degrau, que é eternamente limitada, valor 0 e 1).
> A derivada do degrau unitário é a função impulso de Dirac: $\delta(t)$. O impulso tende à amplitude de $+\infty$ no exato instante $t=0$.
> Entrou sinal limitado $\to$ Produziu infinito.
> **Gabarito: INSTÁVEL.**

**Questão 14:** O filtro integrador atenuado por exponencial ("Filtro Leaky") descrito por $y(t) = \int_{-\infty}^{t} x(\tau) e^{-(t-\tau)} d\tau$ é estável?
> **Resolução:**
> Diferente do integrador puro que varre infinitamente constante 1, a função de atenuação decresce à medida que mergulhamos no passado. Assumindo que $|x(\tau)| \le B$:
> $|y(t)| \le B \int_{-\infty}^{t} e^{-(t-\tau)} d\tau$. Resolvendo a integral da parte exponencial atenuadora resulta em exatamente $1$. A saída máxima fica aprisionada em $|y(t)| \le B \cdot 1 = B$.
> Como nunca cresce, **Gabarito: É Estável.**

---

## Tópico 8: Mistura Total

**Questão 15:** Dada a equação diferencial $y(t) = \frac{dx(t)}{dt} + t \cdot x(t)$. Classifique.
> **Resolução e Gabarito:**
> 1. Memória: Derivada requer saber instantes de tempo minúsculamente próximos (delta). **Com Memória**.
> 2. Causalidade: A derivada causal retroativa só lê o instante anterior e o presente. **Causal**.
> 3. Linearidade: A derivada da soma é a soma das derivadas, e o produto distribui. **Linear**.
> 4. Invariância no Tempo: O multiplicador genérico livre '$t$' muda as regras da física do sistema no relógio. **Variante**.
