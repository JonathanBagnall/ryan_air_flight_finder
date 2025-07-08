#app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
from forms import searchForm
from datetime import date
from flights import search_flights
from airport_lookup import get_iata_code


app = Flask(__name__)
app.config['SECRET_KEY'] = 'THIS_IS_MY_SECRET_KEY'


print(get_iata_code("Rio de Janeiro"))
print(get_iata_code("rio de janeiro"))
print(get_iata_code("RIO DE JANEIRO"))
print(get_iata_code("   rio   de   janeiro  "))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = searchForm(request.form)
    if request.method == 'POST' and form.validate():
        city = form.city.data
        travel_date = form.date.data

        # if travel_date < date.today():
        #     flash("Please select a date that is not in the past.", "error")
        #     return render_template('index.html', searchForm=form)

        return redirect(url_for('results', city=city))

    return render_template('index.html', searchForm=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    form = searchForm(request.form)

    if request.method == 'POST' and form.validate():
        city = form.city.data
        return redirect(url_for('results', city=city))

    # Otherwise handle GET
    city = request.args.get('city', '')
    flights = []

    if city:
        from airport_lookup import get_iata_code
        iata_code = get_iata_code(city)
        if iata_code:
            flights = search_flights(iata_code)
        else:
            flash("City not recognised.", "error")

    return render_template(
        'results.html',
        searchForm=form,
        city=city,
        flights=flights
    )


if __name__ == '__main__':
    app.run(debug=True)
