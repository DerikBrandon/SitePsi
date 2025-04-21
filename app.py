from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']
    # Aqui você pode adicionar lógica para enviar a mensagem ou armazená-la.
    print(f'Nome: {nome}, Email: {email}, Mensagem: {mensagem}')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
