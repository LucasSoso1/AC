import os
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as ms

app = Flask(__name__)

# Inicialização do MySQL
# Substitua as informações de conexão conforme necessário
mysql = ms.connect(
    host='172.17.0.2',
    user='root',
    password='batata123',
    database='teste'
)

# Lista temporária para armazenar os usuários registrados (vamos usar o banco de dados em vez disso)
# registered_users = []

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['inputName']
        phone = request.form['inputPhone']
        address = request.form['inputAddress']
        
        # Verifica se o telefone já está registrado no banco de dados
        cursor = mysql.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE phone = %s", (phone,))
        user = cursor.fetchone()
        cursor.close()
        
        if user:
            return "Telefone já está registrado! Use outro."
        
        # Insere o novo usuário no banco de dados
        cursor = mysql.cursor()
        cursor.execute("INSERT INTO users (name, phone, address) VALUES (%s, %s, %s)", (name, phone, address))
        mysql.commit()
        cursor.close()
        
        # Redireciona para a página de sucesso com o nome do usuário como parâmetro
        return redirect(url_for('success', name=name))
    
    return render_template('signup.html')

@app.route('/success/<name>')
def success(name):
    return f"Usuário {name} registrado com sucesso!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

