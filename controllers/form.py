from flask_wtf import FlaskForm
from flask_editormd.fields import EditormdField
from wtforms.fields import SubmitField, StringField
from wtforms import StringField


class EditormdForm(FlaskForm):
    title = StringField('Title')
    subtitle = StringField('Subtitle')
    author = StringField("Author")
    body = EditormdField()
    submit = SubmitField('Submit')