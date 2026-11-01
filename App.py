from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = "mistério-do-presente-2026"

@app.route("/fase3", methods=["GET", "POST"])
def fase3():

    etapa = session.get("fase3_etapa", 0)

    if request.method == "POST":

        resposta = (
            request.form.get("resposta") or ""
        ).strip().lower()

        tipo = request.form.get("etapa")

        if tipo == "suspeito" and etapa == 0:

            if resposta == "c":
                session["fase3_etapa"] = 1
                return redirect("/fase3")

            return render_template_string(
                ERRO,
                voltar="/fase3"
            )

        elif tipo == "senha" and etapa == 1:

            if resposta == "arquivo":
                session["fase3_concluida"] = True
                return redirect("/carta")

            return render_template_string(
                ERRO,
                voltar="/fase3"
            )

    return render_template_string(
        FASE3,
        etapa=etapa
    )


@app.route("/carta")
def carta():

    if not session.get("fase3_concluida"):
        return redirect("/fase3")

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arquivo desbloqueado</title>
    """ + FONTES + ESTILO + """
    </head>
    <body>
    <div class="container">

    <div class="gato">💌</div>

    <div class="etiqueta">ARQUIVO FINAL DESBLOQUEADO</div>

    <h1>Investigação concluída!</h1>

    <p>
    Você conseguiu encontrar todas as pistas,
    solucionar os enigmas e descobrir a senha.
    </p>

    <div class="sucesso">
    <h2>Seu presente está aqui!</h2>
    <p>
    A recompensa final aguarda você.
    </p>
    </div>

    <h2>Uma carta para você...</h2>

    <p>
    <div class="documento">
    <h2>Uma mensagem do responsável pelo caso:</h2>

    <p>
    Acho que a minha criatividade foi pro beleléu já ein...
    Mas valeu a tentativa, o joguinho foi o seu presente ☝️\n\n
    
                           
— Departamento de Presentes Questionáveis.
    </p>
</div>
    </p>

    </div>
    </body>
    </html>
    """)

# =================================
# ESTILO VISUAL
# =================================

ESTILO = """
<style>
* {
    box-sizing: border-box;
}

body {
    background: #FFF5F8;
    color: #654454;
    font-family: 'Cormorant Garamond', Georgia, serif;
    text-align: center;
    margin: 0;
    padding: 25px 18px;
    min-height: 100vh;
}

.container {
    max-width: 520px;
    margin: 35px auto;
    padding: 30px 22px;
    background: white;
    border: 1px solid #E9B9CC;
    border-radius: 20px;
    box-shadow: 0 8px 25px #E9B9CC55;
}

h1, h2 {
    color: #B96F91;
    font-family: 'Dancing Script', cursive;
}

h1 { font-size: 42px; }
h2 { font-size: 34px; }

p {
    font-size: 20px;
    line-height: 1.5;
}

.gato {
    font-size: 35px;
    margin: 12px;
}

.etiqueta {
    color: #B96F91;
    font-size: 12px;
    letter-spacing: 3px;
}

/* PAINEL DE ESCOLHAS */

.opcoes {
    margin: 25px 0;
}

.opcao input {
    display: none;
}

.opcao label {
    display: block;
    padding: 14px;
    margin: 10px 0;
    background: #FFF5F8;
    border: 2px solid #E9B9CC;
    border-radius: 12px;
    font-size: 19px;
    cursor: pointer;
    transition: 0.2s;
}

.opcao label:hover {
    background: #FCE4ED;
}

.opcao input:checked + label {
    background: #E9B9CC;
    border-color: #B96F91;
    color: #654454;
    font-weight: bold;
    transform: scale(1.02);
}

/* BOTÕES */

button {
    display: block;
    width: 100%;
    padding: 15px;
    margin: 15px 0;
    background: #FCE4ED;
    color: #654454;
    border: 1px solid #E9B9CC;
    border-radius: 12px;
    font-family: Georgia, serif;
    font-size: 18px;
    cursor: pointer;
}

button:hover {
    background: #E9B9CC;
}

/* TELA DE ERRO */

.erro {
    position: fixed;
    inset: 0;
    background: #FFF0F4;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 25px;
    z-index: 9999;
}

.erro h1 {
    color: #C34F78;
    font-family: Georgia, serif;
    font-size: 35px;
}

/* SUCESSO */

.sucesso {
    background: #FFF5F8;
    border: 2px solid #E9B9CC;
    border-radius: 15px;
    padding: 20px;
    margin: 20px 0;
}
</style>
"""

FONTES = """
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Dancing+Script:wght@400;700&display=swap" rel="stylesheet">
"""


# =================================
# PÁGINA INICIAL
# =================================


INICIO = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>O Mistério do Presente</title>
""" + FONTES + ESTILO + """
</head>
<body>
<div class="container">

<div class="gato">🐈</div>

<div class="etiqueta">ACESSO RESTRITO • ARQUIVO 001</div>

<h1>O Mistério do Presente</h1>

<p>
Você foi convocado para uma investigação especial.
</p>

<p>
Um segredo foi escondido e somente um investigador
atento será capaz de encontrá-lo.
</p>

<p>
Três desafios separam você da descoberta final.
Cada resposta aproxima você da recompensa.
</p>

<div class="sucesso">
<h2>Seu objetivo</h2>
<p>
Observe as pistas, pense com cuidado e não confie
demais na sua primeira impressão.
</p>
</div>

<p><strong>A investigação começa agora.</strong></p>

<form action="/fase1">
<button type="submit">Iniciar investigação</button>
</form>

<div class="gato">🐾</div>

</div>
</body>
</html>
"""



# =================================
# FASE 1 - ESCOLHA
# =================================

FASE1 = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fase I - Primeira Pista</title>
""" + FONTES + ESTILO + """
</head>
<body>

<div class="container">

<div class="gato">🐈‍⬛</div>
<div class="etiqueta">INVESTIGAÇÃO Nº 001</div>

<h1>Quem sou eu?</h1>

<p>Primeira pergunta:</p>
<p><strong>Qual o meu apelido dado unicamente por você?</strong></p>

<form method="POST">

<div class="opcoes">

<div class="opcao">
<input type="radio" id="a1" name="resposta" value="mel" required>
<label for="a1">1) Mel</label>
</div>

<div class="opcao">
<input type="radio" id="a2" name="resposta" value="star">
<label for="a2">2) Star</label>
</div>

<div class="opcao">
<input type="radio" id="a3" name="resposta" value="corujinha">
<label for="a3">3) Corujinha</label>
</div>

<div class="opcao">
<input type="radio" id="a4" name="resposta" value="docinho">
<label for="a4">4) Docinho</label>
</div>

<div class="opcao">
<input type="radio" id="a5" name="resposta" value="estrela">
<label for="a5">5) Estrela</label>
</div>

</div>

<button type="submit">Confirmar resposta</button>

</form>

<div class="gato">🐾</div>
</div>

</body>
</html>
"""


# =================================
# TELA DE ERRO
# =================================

ERRO = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Resposta incorreta</title>
""" + FONTES + ESTILO + """
</head>
<body>

<div class="erro">

<div class="gato">🙀</div>

<h1>FALA SÉRIO.</h1>
<h1>VOCÊ ERROU.</h1>

<p>Atualize a tela e tente de novo.</p>

<div class="gato">🐾</div>

</div>

<script>
history.replaceState({}, "", "/fase1");
</script>

</body>
</html>
"""


# =================================
# TELA DE PARABÉNS
# =================================

PARABENS = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Resposta correta!</title>
""" + FONTES + ESTILO + """
</head>
<body>

<div class="container">

<div class="gato">😸</div>

<div class="etiqueta">INVESTIGAÇÃO Nº 001</div>

<h1>Parabéns!</h1>

<div class="sucesso">
<h2>Resposta correta!</h2>
<p>Você encontrou a primeira pista.</p>
<p>O investigador está começando a mostrar seu potencial...</p>
</div>

<form action="/fase2">
<button type="submit">Continuar para a próxima fase</button>
</form>

</div>

</body>
</html>
"""


# =================================
# FASE 2
# =================================


FASE2 = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fase II - Mensagem Fragmentada</title>
""" + FONTES + ESTILO + """
<style>
.fragmentos {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin: 25px 0;
}

.fragmento {
    background: #FCE4ED;
    border: 1px solid #E9B9CC;
    border-radius: 12px;
    padding: 15px 8px;
    font-size: 18px;
}

.fragmento strong {
    color: #B96F91;
}

.desafio {
    background: #FFF5F8;
    border: 1px solid #E9B9CC;
    border-radius: 15px;
    padding: 20px;
    margin-top: 20px;
}

input[type="text"] {
    width: 100%;
    padding: 14px;
    margin: 15px 0;
    border: 1px solid #E9B9CC;
    border-radius: 10px;
    font-size: 18px;
    text-align: center;
    color: #654454;
}
</style>
</head>

<body>
<div class="container">

<div class="gato">🐈‍⬛</div>

<div class="etiqueta">INVESTIGAÇÃO Nº 002</div>

<h1>Mensagem fragmentada</h1>

<p>
Uma mensagem foi dividida em oito partes.
Resolva os pequenos enigmas para recuperar cada fragmento.
</p>

<p><strong>A ordem importa. Não perca nenhuma palavra.</strong></p>

<div class="fragmentos">
{% for palavra in fragmentos %}
    <div class="fragmento">
        <strong>{{ loop.index }}.</strong>
        {{ palavra }}
    </div>
{% endfor %}
</div>

{% if concluido %}

<div class="sucesso">
    <h2>Mensagem recuperada!</h2>
    <p>Todos os fragmentos foram encontrados.</p>
    <h2>{{ frase }}</h2>
    <p>...</p>
    <p>Era isso mesmo que você estava fazendo?</p>
</div>

<form action="/fase3">
    <button type="submit">Avançar para a terceira fase</button>
</form>

{% else %}

<div class="desafio">

<div class="etiqueta">
FRAGMENTO {{ indice + 1 }} DE 8
</div>

<h2>{{ desafio.titulo }}</h2>

<p>{{ desafio.pergunta }}</p>

<form method="POST">

<input
    type="text"
    name="resposta"
    placeholder="Digite sua resposta..."
    autocomplete="off"
    required
>

<button type="submit">Desbloquear fragmento</button>

</form>

</div>

{% endif %}

<div class="gato">🐾</div>

</div>
</body>
</html>
"""



# =================================
# ROTAS DO SITE
# =================================

@app.route("/")
def inicio():
    return render_template_string(INICIO)


@app.route("/fase1", methods=["GET", "POST"])
def fase1():

    if request.method == "POST":

        resposta = request.form.get("resposta")

        if resposta == "docinho":
            return redirect("/parabens")

        return render_template_string(ERRO), 200

    return render_template_string(FASE1)


@app.route("/parabens")
def parabens():
    return render_template_string(PARABENS)



DESAFIOS = [
    {
        "titulo": "Fragmento misterioso",
        "pergunta": "Qual pronome usamos para falar diretamente com a pessoa que está lendo esta mensagem?",
        "resposta": "você"
    },
    {
        "titulo": "Uma negação",
        "pergunta": "Qual é a palavra que representa o contrário de SIM?",
        "resposta": "não"
    },
    {
        "titulo": "Complete o ditado",
        "pergunta": "Complete: Quem ___ boca vai a Roma.",
        "resposta": "tem"
    },
    {
        "titulo": "Ausência",
        "pergunta": "Qual palavra significa coisa nenhuma?",
        "resposta": "nada"
    },
    {
        "titulo": "Comparação",
        "pergunta": "Qual é o contrário de PIOR?",
        "resposta": "melhor"
    },
    {
        "titulo": "Linguagem informal",
        "pergunta": "Como podemos escrever informalmente a palavra PARA?",
        "resposta": "pra"
    },
    {
        "titulo": "Ação",
        "pergunta": "Qual verbo significa realizar ou executar alguma coisa?",
        "resposta": "fazer"
    },
    {
        "titulo": "Último fragmento",
        "pergunta": "Qual palavra usamos para negar alguma coisa?",
        "resposta": "não"
    }
]


@app.route("/fase2", methods=["GET", "POST"])
def fase2():

    palavras = [
        "VOCÊ", "NÃO", "TEM", "NADA",
        "MELHOR", "PRA", "FAZER", "NÃO?"
    ]

    indice = session.get("fase2_indice", 0)

    if request.method == "POST":

        resposta = (
            request.form.get("resposta") or ""
        ).strip().lower()

        resposta_correta = DESAFIOS[indice]["resposta"]

        if resposta == resposta_correta:

            indice += 1
            session["fase2_indice"] = indice

            return redirect("/fase2")

        return render_template_string(
            ERRO,
            voltar="/fase2"
        )

    concluido = indice >= len(DESAFIOS)

    fragmentos = [
        palavra if i < indice else "???"
        for i, palavra in enumerate(palavras)
    ]

    desafio = None if concluido else DESAFIOS[indice]

    return render_template_string(
        FASE2,
        indice=indice,
        desafio=desafio,
        fragmentos=fragmentos,
        concluido=concluido,
        frase="Você não tem nada melhor pra fazer não?"
    )



FASE3 = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fase III - O Último Caso</title>
""" + FONTES + ESTILO + """
<style>
.suspeito {
    background: #FFF5F8;
    border: 1px solid #E9B9CC;
    border-radius: 12px;
    padding: 15px;
    margin: 12px 0;
    text-align: left;
}

.documento {
    background: #FCE4ED;
    padding: 18px;
    border-radius: 12px;
    margin: 20px 0;
}

input[type="text"] {
    width: 100%;
    padding: 14px;
    border: 1px solid #E9B9CC;
    border-radius: 10px;
    font-size: 18px;
    text-align: center;
    margin: 15px 0;
}
</style>
</head>

<body>
<div class="container">

<div class="gato">🕵️</div>

<div class="etiqueta">INVESTIGAÇÃO Nº 003</div>

<h1>O último caso</h1>

{% if etapa == 0 %}

<p>
Um envelope desapareceu às 20h.
Três pessoas foram interrogadas.
Apenas uma está mentindo.
</p>

<div class="suspeito">
<strong>Suspeito A — O Bibliotecário</strong>
<p>
"Saí da biblioteca às 20h00, no horário oficial."
</p>
</div>

<div class="suspeito">
<strong>Suspeito B — O Porteiro</strong>
<p>
"Vi o Bibliotecário sair quando o relógio da entrada marcava 20h05. O relógio estava cinco minutos adiantado."
</p>
</div>

<div class="suspeito">
<strong>Suspeito C — A Arquivista</strong>
<p>
"O relógio estava cinco minutos atrasado. Eu não saí da sala de arquivos naquela noite."
</p>
</div>

<div class="documento">
<strong>PROVA ENCONTRADA</strong>
<p>
Um registro técnico confirma que o relógio da entrada estava exatamente cinco minutos adiantado.
</p>
<p>
O horário oficial da saída do Bibliotecário foi confirmado como 20h00.
</p>
</div>

<h2>Quem está mentindo?</h2>

<form method="POST">
<input type="hidden" name="etapa" value="suspeito">

<div class="opcoes">

<div class="opcao">
<input type="radio" id="s1" name="resposta" value="A" required>
<label for="s1">A) O Bibliotecário</label>
</div>

<div class="opcao">
<input type="radio" id="s2" name="resposta" value="B">
<label for="s2">B) O Porteiro</label>
</div>

<div class="opcao">
<input type="radio" id="s3" name="resposta" value="C">
<label for="s3">C) A Arquivista</label>
</div>

</div>

<button type="submit">Apresentar conclusão</button>
</form>

{% elif etapa == 1 %}

<div class="sucesso">
<h2>Suspeito identificado!</h2>
<p>
A Arquivista foi desmascarada.
Mas o arquivo ainda está protegido por uma senha.
</p>
</div>

<div class="documento">
<strong>ÚLTIMA INSTRUÇÃO</strong>
<p>
A senha é o nome do objeto que guarda documentos importantes.
</p>
<p>
É o mesmo tipo de objeto em que esta investigação foi organizada.
</p>
</div>

<h2>Qual é a senha?</h2>

<form method="POST">
<input type="hidden" name="etapa" value="senha">

<input
type="text"
name="resposta"
placeholder="Digite a senha..."
autocomplete="off"
required
>

<button type="submit">Desbloquear arquivo</button>
</form>

{% endif %}

<div class="gato">🐾</div>

</div>
</body>
</html>
"""

# =================================
# EXECUÇÃO
# =================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
)
