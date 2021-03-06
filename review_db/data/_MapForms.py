from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class MapForm(FlaskForm):
    country = StringField('Какую страну вы бы хотели увидеть?')
    submit = SubmitField('Найти')
    return_to_main = SubmitField('Вернуться на главную страницу')
