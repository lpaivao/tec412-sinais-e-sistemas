# Gera um HTML 480x480 por cartão da colinha para o mostrador "Fotos" do relógio.
# Conteúdo fica dentro do círculo e acima da faixa do relógio (y > ~330 fica livre).
import os, sys

OUT = sys.argv[1]

def s(x):  # sobrescrito
    return f"<sup>{x}</sup>"

def b(x):  # subscrito
    return f"<sub>{x}</sub>"

CARDS = [
    ("Definição", [
        f"y[n] = Σ{b('k')} x[k]·h[n−k]",
        "y(t) = ∫ x(τ)·h(t−τ) dτ",
        "<i>n e t ficam constantes na conta</i>",
    ]),
    ("Janela", [
        "h ≠ 0 em [a, b] ⇒",
        "n−b ≤ k ≤ n−a",
        "cauda = n−b",
        "frente = n−a",
    ]),
    ("Eventos e limites", [
        "frente = p ⇒ n = p + a",
        "cauda = p ⇒ n = p + b",
        "N eventos ⇒ N+1 intervalos",
        "inf = max(cauda, início)",
        "sup = min(frente, fim)",
    ]),
    ("Contagem e trapézio", [
        "discreto: B − A + 1 termos",
        "contínuo: B − A",
        "pulso ∗ pulso = trapézio",
        f"patamar A{b('1')}A{b('2')}·min(L{b('1')}, L{b('2')})",
        "início/fim = soma dos inícios/fins",
    ]),
    ("Impulso: 3 operações", [
        f"x(t)·δ(t−t{b('0')}) = x(t{b('0')})·δ(t−t{b('0')})",
        f"∫ x(t)·δ(t−t{b('0')}) dt = x(t{b('0')})",
        f"x(t) ∗ δ(t−t{b('0')}) = x(t−t{b('0')})",
        "<i>amostra · número · desloca</i>",
    ]),
    ("Impulso: cuidados", [
        "δ(t−2) atrasa: x(t−2)",
        f"c·δ(t−t{b('0')}) ⇒ c·x(t−t{b('0')})",
        "δ(at) = δ(t)/|a|",
        "pulso + impulso: distributiva",
    ]),
    ("Pares contínuos (1)", [
        "u(t) ∗ u(t) = t·u(t)",
        "u(t−a) ∗ u(t−b)",
        "= (t−a−b)·u(t−a−b)",
        f"e{s('−at')}u(t) ∗ u(t) = (1−e{s('−at')})/a · u(t)",
    ]),
    ("Pares contínuos (2)", [
        f"e{s('−at')}u(t) ∗ e{s('−bt')}u(t)",
        f"= (e{s('−at')} − e{s('−bt')})/(b − a) · u(t)",
        f"a = b: t·e{s('−at')}·u(t)",
        f"x ∗ u = ∫{b('−∞')}{s('t')} x(τ) dτ",
    ]),
    ("Pares discretos (1)", [
        "u[n] ∗ u[n] = (n+1)·u[n]",
        "u[n−a] ∗ u[n−b]",
        "= (n−a−b+1)·u[n−a−b]",
        f"a{s('n')}u[n] ∗ u[n] = (1−a{s('n+1')})/(1−a)·u[n]",
    ]),
    ("Pares discretos (2)", [
        f"a{s('n')}u[n] ∗ b{s('n')}u[n]",
        f"= (a{s('n+1')} − b{s('n+1')})/(a − b) · u[n]",
        f"a = b: (n+1)·a{s('n')}·u[n]",
        f"x ∗ u = Σ{b('k≤n')} x[k]",
    ]),
    ("Propriedades", [
        "x ∗ h = h ∗ x",
        f"paralelo: h{b('1')} + h{b('2')}",
        f"cascata: h{b('1')} ∗ h{b('2')}",
        f"x(t−t{b('1')}) ∗ h(t−t{b('2')}) = y(t−t{b('1')}−t{b('2')})",
        "y′ = x′ ∗ h",
    ]),
    ("Prova real", [
        "∫y = (∫x)(∫h) · Σy = (Σx)(Σh)",
        "início = soma dos inícios",
        f"duração: L{b('x')}+L{b('h')}−1 | L{b('x')}+L{b('h')}",
        "contínuo s/ impulso: y contínua",
    ]),
    ("PG finita", [
        f"Σ{b('k=A')}{s('B')} r{s('k')} = (r{s('A')} − r{s('B+1')})/(1 − r)",
        f"r = 1: Σ{b('A')}{s('B')} 1 = B − A + 1",
        "<i>sempre escreva r, A e B</i>",
    ]),
    ("PG infinita", [
        f"|r|&lt;1: Σ{b('k=A')}{s('∞')} r{s('k')} = r{s('A')}/(1−r)",
        f"|r|&gt;1: Σ{b('−∞')}{s('B')} r{s('k')} = r{s('B+1')}/(r−1)",
        f"Σ{b('k=0')}{s('∞')} k·r{s('k')} = r/(1−r){s('2')}",
        f"diverge: S{b('N')} fechada, N → ∞",
    ]),
    ("Integrais", [
        f"∫ e{s('aτ')} dτ = e{s('aτ')}/a",
        f"∫ τe{s('aτ')} dτ = e{s('aτ')}(τ/a − 1/a{s('2')})",
        "∫ sen(ωτ) dτ = −cos(ωτ)/ω",
        "∫ cos(ωτ) dτ = sen(ωτ)/ω",
    ]),
    ("Macetes (1)", [
        "u[n] − u[n−1] = δ[n]",
        "δ[n] + u[n−1] = u[n]",
        "sen(πn) = 0 · cos(πn) = (−1)" + s("n"),
        "cos(θ − π) = −cos θ",
    ]),
    ("Macetes (2)", [
        "u(1−t) liga em t ≤ 1",
        f"e{s('−β(t−τ)')} = e{s('−βt')}·e{s('βτ')}",
        "α = β: caso à parte",
        f"3{s('k')}(¼){s('n−k')} = (¼){s('n')}·12{s('k')}",
    ]),
    ("Sistema por h", [
        "sem memória: h = c·δ",
        "causal: h = 0 p/ n &lt; 0",
        "estável: Σ|h| &lt; ∞",
        f"r{s('n')}u[n]: |r|&lt;1 · r{s('n')}u[−n]: |r|&gt;1",
        f"e{s('at')}u(t): a&lt;0 · e{s('at')}u(−t): a&gt;0",
    ]),
    ("Roteiro de prova", [
        "1. atalho? (δ, tabela, distrib.)",
        "2. fixa o de mais pedaços",
        "3. janela + tabela de eventos",
        "4. desenho de cada intervalo",
        "5. conta até o número + prova",
    ]),
]

TPL = """<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;padding:0;background:#000;}}
body{{width:480px;height:480px;overflow:hidden;position:relative;
 font-family:"Segoe UI",Arial,sans-serif;color:#fff;}}
.n{{position:absolute;top:34px;left:0;right:0;text-align:center;font-size:15px;color:#888;}}
.box{{position:absolute;top:58px;left:56px;right:56px;height:268px;
 display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;}}
.t{{font-size:24px;font-weight:700;color:#ff6b5a;margin-bottom:10px;}}
.l{{font-family:"Cambria Math",Cambria,"Times New Roman",serif;font-size:{fs}px;line-height:1.3;margin:2px 0;}}
.l i{{font-family:"Segoe UI",Arial,sans-serif;font-style:normal;color:#aaa;font-size:17px;}}
sup,sub{{font-size:68%;line-height:0;}}
</style></head><body>
<div class="n">{i}/{tot}</div>
<div class="box"><div class="t">{titulo}</div>{linhas}</div>
</body></html>"""

os.makedirs(OUT, exist_ok=True)
tot = len(CARDS)
for i, (titulo, linhas) in enumerate(CARDS, 1):
    fs = 26 if len(linhas) <= 4 else 23
    html = TPL.format(i=i, tot=tot, titulo=titulo, fs=fs,
                      linhas="".join(f'<div class="l">{l}</div>' for l in linhas))
    with open(os.path.join(OUT, f"card{i:02d}.html"), "w", encoding="utf-8") as f:
        f.write(html)
print(tot)

