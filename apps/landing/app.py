from flask import Flask, render_template

app = Flask(__name__)

CURSOS = [
    {
        "id": 1,
        "icon": "terminal",
        "title": "Python Fundamentos",
        "description": "Aprenda os conceitos essenciais da linguagem mais popular.",
        "total_lessons": 2,
        "color": "#306998",
    },
    {
        "id": 2,
        "icon": "flame",
        "title": "Flask API Masterclass",
        "description": "Crie APIs RESTful profissionais com documentacao automatica.",
        "total_lessons": 2,
        "color": "#FF5722",
    },
]

FEATURES = [
    {"icon": "book-open", "title": "Cursos Interativos", "description": "Conteudo organizado em modulos progressivos."},
    {"icon": "lightbulb", "title": "Quizzes Praticos", "description": "Perguntas reais em cada licao."},
    {"icon": "bar-chart-3", "title": "Progresso Salvo", "description": "Historico persistente no banco."},
    {"icon": "refresh-cw", "title": "Refaca Licoes", "description": "Pratique quantas vezes quiser."},
    {"icon": "smartphone", "title": "Multiplataforma", "description": "Roda no navegador, desktop e mobile."},
    {"icon": "file-text", "title": "API Documentada", "description": "Swagger gerado automaticamente."},
]

TECH_STACK = [
    {"name": "Flask", "role": "Backend & SSR", "icon": "flame"},
    {"name": "SQLAlchemy", "role": "ORM & Migrations", "icon": "database"},
    {"name": "PostgreSQL", "role": "Banco de Dados", "icon": "hard-drive"},
    {"name": "Flet", "role": "UI Multiplataforma", "icon": "smartphone"},
    {"name": "Tailwind CSS", "role": "Estilizacao", "icon": "palette"},
    {"name": "Docker", "role": "Containers", "icon": "container"},
]

@app.route('/')
def index():
    return render_template('index.html', cursos=CURSOS)

if __name__ == '__main__':
    app.run(debug=True, port=3000)