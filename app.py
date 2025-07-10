from flask import Flask, render_template, request, redirect, url_for, flash
from forms import searchForm
from airport_lookup import get_iata_codes
from flights import search_flights

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THIS_IS_MY_SECRET_KEY'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = searchForm(request.form)
    if request.method == 'POST' and form.validate():
        city = form.city.data
        return redirect(url_for('results', city=city))
    return render_template('index.html', searchForm=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
    form = searchForm(request.form)

    if request.method == 'POST' and form.validate():
        city = form.city.data
        return redirect(url_for('results', city=city))

    city = request.args.get('city', '')
    selected_airport = request.args.get('airport', None)

    iata_codes = get_iata_codes(city)
    flights = []

    if city and selected_airport:
        flights = search_flights(selected_airport)
    elif city and iata_codes:
        # Default to the first airport if none selected
        flights = search_flights(iata_codes[0])

    return render_template(
        'results.html',
        searchForm=form,
        city=city,
        iata_codes=iata_codes,
        selected_airport=selected_airport or (iata_codes[0] if iata_codes else None),
        flights=flights
    )

if __name__ == '__main__':
    app.run(debug=True)
