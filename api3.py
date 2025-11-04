from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

aluno={
    'nome':'Gabriel',
    'idade':26,
    'telefone':'12312312'
}

@app.route('/')
def home():
    
    return render_template('register.html',aluno=aluno)

app.run(debug=True)
