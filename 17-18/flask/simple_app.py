from flask import Flask, render_template

# создаем экземпляр класса Flask
# создаем переменную с приложением
app = Flask('my_app')

users = ['alisa', 'bob']

@app.route('/')
def hello():
    return render_template('main.html', my_users=users)


@app.route('/home')
def home():
    return '<h2>Домашняя страница</h2>'

app.run(debug=True)