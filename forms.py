from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired

class ResumeForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    profession = StringField('Профессия', validators=[DataRequired()])
    image = FileField('Изображение', validators=[DataRequired()])
    submit = SubmitField('Отправить')