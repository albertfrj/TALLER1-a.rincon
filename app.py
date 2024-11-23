from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from usuarios import usuarios
from models import User

app = Flask(__name__)
app.secret_key = 'mi_secreto'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    for user in usuarios:
        if str(user.id) == user_id:
            return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((u for u in usuarios if u.username == username), None)
        
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('welcome'))
        else:
            return "Usuario o contraseña incorrectos", 401
    return render_template('login.html')

@app.route('/welcome')
@login_required
def welcome():
    if current_user.is_admin:
        return f"Hola, {current_user.username}! Aquí está la lista de perros de la guardería: [Perro1, Perro2, Perro3]"
    else:
        return f"Hola, {current_user.username}! Bienvenido a la guardería."

# Ruta de cierre de sesión
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
