from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'primeiro livro',
        'autor': 'alctor1'
    },
    {
        'id': 2,
        'titulo': 'segundo livro',
        'autor': 'segundoc ara'
    },
    {
        'id': 3,
        'titulo': 'terceiro livro',
        'autor': 'terceiro'
    },
    {
        'id': 4,
        'titulo': 'quarto livro',
        'autor': 'alctorsr1'
    },
]

@app.route('/livros')
def obter_livro():
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)