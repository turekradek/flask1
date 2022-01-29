import os
from flask import Flask, render_template, url_for, request, redirect
import csv
# render_template jest potrzebne abyprzesłać template html
app = Flask(__name__)


# w przegladarce nakoncu adresu dodaje imie wiec sie wyswietla
@app.route('/')  # jako string page_name
def my_home():
    return render_template('index.html')
# return render_template ( plik jest szukany w folderze templates )

# w przegladarce nakoncu adresu dodaje imie wiec sie wyswietla


@app.route('/<string:page_name>')  # jako string page_name
def html_page(page_name):
    return render_template(page_name)
# return render_template ( plik jest szukany w folderze templates )


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


def write_to_csv_pasowanie(data):
    with open('pasowanie.csv', mode='a', newline='', encoding='utf8') as pasowanie:
        nazwisko = data['nazwisko'].upper()
        imie = data['imie'].upper()
        pasy = data['pasy'].upper()
        belki = data['belki']
        data = data['data']
        # trener = data['trener'].upper()

        csv_writer = csv.writer(pasowanie, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([nazwisko, imie, pasy, belki, data])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():  # reszta do naszego cwiczenia nie potrzebna
    # error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/contact_thanks.html')
        except:
            return 'did not save to database'
    else:
        return 'coś nie halo wez jeszcze raz'


@app.route('/submit_form2', methods=['POST', 'GET'])
def submit_form2():  # reszta do naszego cwiczenia nie potrzebna
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv_pasowanie(data)
            return redirect('/pasowanie_thanks.html')
        except:
            return 'did not save to database submit form 2 '
    else:
        return 'coś nie halo wez jeszcze raz submit form 2 '
