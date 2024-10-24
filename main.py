from flask import render_template, redirect, url_for
from forms import ResumeForm
from models import Article, app



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():
    articles = Article.query.all()
    return render_template('articles.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', article=article)

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
    app.run(debug=False)