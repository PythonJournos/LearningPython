# Flask is what makes everything work. Import it.
from flask import Flask, render_template

# Import our bank model.
from models import Bank

# Flask needs to run! This gives it legs.
app = Flask(__name__)


# Routes!
@app.route('/', methods=['GET'])
def failed_banks_list():
    """
    This route is for a list of ALL banks.
    """

    # The context for this pages is just "banks", a list of all banks.
    context = {
        'banks': Bank.select()
    }

    # Render the template to list.html and with the context from above.
    return render_template('list.html', **context)


@app.route('/bank/<cert_num>/', methods=['GET'])
def failed_bank_detail(cert_num):
    """
    This route is for a single bank.
    We're going to do TWO things.
    a.) We're going to get the one bank.
    b.) We're going to get all banks EXCEPT this bank in the same state.
    """
    # a.) Get this bank.
    this_bank = Bank.select()\
        .where(Bank.cert_num == int(cert_num)).get()

    # b.) Get the other banks in this state.
    same_state_banks = Bank.select()\
        .where(Bank.state == this_bank.state)\
        .where(Bank.cert_num != int(cert_num))

    # Set up the context; include both this bank and other banks from this state.
    context = {
        'bank': this_bank,
        'same_state_banks': same_state_banks
    }

    # Render the template to detail.html and with that context.
    return render_template('detail.html', **context)

# Last bit! Just need to get flask to run when we run it.
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
