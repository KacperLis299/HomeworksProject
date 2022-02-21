from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField


class HomeworkForm(FlaskForm):
     subject = StringField('Subject')
     date = DateField('Date', format='%Y-%m-%d')
     description = TextAreaField('Description')
     submit = SubmitField('Add homework')
