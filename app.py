from flask import Flask, request, render_template
import requests

app = Flask(__name__);

access_key = '455ac5b6cd12f364ec463587c7f38224';
base_url = f'http://api.exchangerate.host/live?access_key={access_key}';

# https://api.exchangerate.host/live
#     ? access_key = 455ac5b6cd12f364ec463587c7f38224

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        from_currency = request.form['fromCurrency']
        to_currency =  request.form['toCurrency']
        amount = float(request.form['amount'])

        response = requests.get(base_url)
        data = response.json()
        rates = data['quotes'];

        rates['USDUSD'] = 1

        try:
             converted_amount = format(amount * (rates['USD' + to_currency] / rates['USD' + from_currency]),'.2f')      
        except KeyError:
            return render_template('index.html', error='Invalid currency!')

        converted_amount = format(amount * (rates['USD' + to_currency] / rates['USD' + from_currency]),'.2f')

        return render_template('index.html', result=converted_amount)
    
    return render_template('index.html')

if __name__ == '__name__':
    app.run(debug=True)