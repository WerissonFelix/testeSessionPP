# Teste Session 

from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__, template_folder='templates')
app.secret_key = 'chaveultrasecreta123'


@app.route('/')
def index():
    username = ''
    senha = ''
    if 'username' in session and 'senha' in session:
        username = session['username']
        senha = session['senha']
    return render_template('index.html', username=username, senha=senha )

@app.route('/login', methods=['GET', 'POST'])
def login(): # Precisa mudar isso quando tiver o bd pronto, fazer verificação dos dados
    if request.method == 'POST' and request.form['username'] != '':
        session['username'] = request.form['username'] # No lugar do request, vai ficar a variável do bd
        session['senha'] = request.form['senha'] # Mesma coisa aqui
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout(): # Acho que tá de boa
    session.pop('username', None)
    session.pop('senha', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)