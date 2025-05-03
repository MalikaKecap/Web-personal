from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
USERNAME = 'MALIKAKECAP'
PASSWORD = '250601'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('success', user=username))
        else:
            error = 'Username atau password salah!'
    return render_template('login.html', error=error)

@app.route('/success/<user>')
def success(user):
    return render_template('success.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)