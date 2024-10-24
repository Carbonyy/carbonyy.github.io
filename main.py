from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import ResumeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():

    return render_template('articles.html')

@app.route('/exchange')
def exchange():

    return render_template('exchange.html')

@app.route('/submit-resume', methods=['GET', 'POST'])
def submit_resume():
    form = ResumeForm()
    if form.validate_on_submit():
        
        return redirect(url_for('index'))
    return render_template('submit_resume.html', form=form)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/developers')
def developers():
    return render_template('developers.html')

if __name__ == '__main__':
    app.run(debug=True)