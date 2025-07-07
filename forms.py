from wtforms import Form, StringField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import date

class searchForm(Form):
    city = StringField('City selection', validators=[DataRequired()], render_kw={"placeholder": "Start typing a city..."})
    date = DateField('Travel date', validators=[DataRequired()], format='%Y-%m-%d', default=date.today)
    submit = SubmitField('Search')
