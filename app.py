#app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
from forms import searchForm
from datetime import date
from flights import search_flights
from airport_lookup import get_iata_code


app = Flask(__name__)
app.config['SECRET_KEY'] = 'THIS_IS_MY_SECRET_KEY'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = searchForm(request.form)
    if request.method == 'POST' and form.validate():
        city = form.city.data
        travel_date = form.date.data

        # if travel_date < date.today():
        #     flash("Please select a date that is not in the past.", "error")
        #     return render_template('index.html', searchForm=form)

        return redirect(url_for('results', city=city, travel_date=travel_date.isoformat()))

    return render_template('index.html', searchForm=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    form = searchForm(request.form)

    city = request.args.get('city', '')
    travel_date = request.args.get('travel_date', '')

    iata_code = get_iata_code(city)

    flights = []

    if iata_code:
        flights = search_flights(iata_code, travel_date)
    else:
        flash("City not recognised.", "error")
    print(city, travel_date, iata_code, flights)
    if request.method == 'POST' and form.validate():
        city = form.city.data
        new_date = form.date.data

        # if new_date < date.today():
        #     flash("Please select a date that is not in the past.", "error")
        #     return render_template('results.html', searchForm=form, city=city, travel_date=travel_date, flights=flights)

        return redirect(url_for('results', city=city, travel_date=new_date.isoformat(), flights=flights))

    return render_template('results.html', searchForm=form, city=city, travel_date=travel_date, flights=flights)


if __name__ == '__main__':
    app.run(debug=True)
