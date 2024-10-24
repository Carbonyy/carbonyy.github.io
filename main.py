from flask import render_template
from forms import ResumeForm
from models import Article, app, Resume, db



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
    resumes = Resume.query.all()
    return render_template('exchange.html', resumes=resumes)


@app.route('/submit-resume', methods=['GET', 'POST'])
def submit_resume():
    form = ResumeForm()
    success = None

    if form.validate_on_submit():
        new_resume = Resume(
            name=form.name.data,
            profession=form.profession.data,
            age=form.age.data,
            gender=form.gender.data,
            stack_of_technologies=form.stack_of_technologies.data,
            soft_skills=form.soft_skills.data,
            hard_skills=form.hard_skills.data,
            salary=form.salary.data,
            description_about_me=form.description_about_me.data,
            image_url=form.image_url.data
        )

        try:
            db.session.add(new_resume)
            db.session.commit()
            success = True
        except Exception as e:
            db.session.rollback()
            success = False

        return render_template('submit_resume.html', form=form, success=success)

    return render_template('submit_resume.html', form=form, success=success)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/developers')
def developers():
    resumes = Resume.query.all()
    return render_template('developers.html', resumes=resumes)

if __name__ == '__main__':
    app.run(debug=False)