from flask import Flask, render_template

from models import Bank

app = Flask(__name__)


@app.route('/', methods=['GET'])
def failed_banks_list():

    context = {
        'banks': Bank.select()
    }

    return render_template('list.html', **context)


@app.route('/bank/<cert_num>/', methods=['GET'])
def failed_bank_detail(cert_num):
    this_bank = Bank.select()\
        .where(Bank.cert_num == int(cert_num)).get()
    same_state_banks = Bank.select()\
        .where(Bank.state == this_bank.state)\
        .where(Bank.cert_num != int(cert_num))

    context = {
        'bank': this_bank,
        'same_state_banks': same_state_banks
    }

    return render_template('detail.html', **context)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
