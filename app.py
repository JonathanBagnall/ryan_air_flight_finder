from flask import Flask, render_template, request, redirect, url_for, session, flash
from forms import searchForm
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THIS_IS_MY_SECRET_KEY'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = searchForm(request.form)
    if request.method == 'POST' and form.validate():
        city = form.city.data
        travel_date = form.date.data

        if travel_date < date.today():
            flash("Please select a date that is not in the past.", "error")
            return render_template('index.html', searchForm=form)

        return redirect(url_for('results', city=city, travel_date=travel_date.isoformat()))

    return render_template('index.html', searchForm=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
    form = searchForm(request.form)
    city = request.args.get('city', '')
    travel_date = request.args.get('travel_date', '')

    if request.method == 'POST' and form.validate():
        city = form.city.data
        new_date = form.date.data

        if new_date < date.today():
            flash("Please select a date that is not in the past.", "error")
            return render_template('results.html', searchForm=form, city=city, travel_date=travel_date)

        return redirect(url_for('results', city=city, travel_date=new_date.isoformat()))

    return render_template('results.html', searchForm=form, city=city, travel_date=travel_date)

if __name__ == '__main__':
    app.run(debug=True)
