from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired

class searchForm(Form):
    city = StringField('City selection', validators=[DataRequired()], render_kw={"placeholder": "Start typing a city..."})
    submit = SubmitField('Search')
