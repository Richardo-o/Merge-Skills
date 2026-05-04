from flask import Flask, render_template

app = Flask(__name__)

CURSOS = [
    {
        "id": 1,
        "icon": "terminal",
        "title": "Python Fundamentos",
        "description": "Aprenda os conceitos essenciais da linguagem Python.",
        "total_lessons": 2,
        "color": "#306998"
    },
    {
        "id": 2,
        "icon": "flame",
        "title": "Flask API Masterclass",
        "description": "Crie APIs RESTful profissionais com documentação automática.",
        "total_lessons": 2,
        "color": "#FF5722"
    },
]

@app.route('/')
def index():
    return render_template('index.html', cursos=CURSOS)

if __name__ == '__main__':
    app.run(debug=True, port=3000)