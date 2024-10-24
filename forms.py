from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ResumeForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired()])
    profession = StringField('Профессия', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    gender = SelectField('Пол', choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], validators=[DataRequired()])
    stack_of_technologies = StringField('Стек технологий', validators=[DataRequired()])
    soft_skills = StringField('Soft Skills', validators=[DataRequired()])
    hard_skills = StringField('Hard Skills', validators=[DataRequired()])
    salary = StringField('Цена вашей услуги', validators=[DataRequired()])
    description_about_me = TextAreaField('О себе', validators=[DataRequired()])
    image_url = StringField('URL вашего лица', validators=[DataRequired()])
    submit = SubmitField('Отправить резюме')
