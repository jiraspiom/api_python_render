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

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livro/<int:id>', methods=['GET'])
def obter_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/')
def index():
    return jsonify({'msg': 'api criada'})

app.run(port=5000)