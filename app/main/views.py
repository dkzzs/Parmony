from . import main
from flask import render_template, make_response, send_file, url_for, request, current_app
from ..models import Carpark, Transaction
from datetime import datetime

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Carpark.query.order_by(Carpark.last_updated_timestamp.desc()).paginate(
        page, per_page=current_app.config['CARPARKS_PER_PAGE'], error_out=False
    )
    carparks = pagination.items
    return render_template('index.html', carparks=carparks, pagination=pagination)

@main.route('/carpark/<code>')
def carpark(code):
    carpark = Carpark.query.filter_by(code=code).first_or_404()
    volume_chart = carpark.gen_volume_chart()
    return render_template('carpark.html', carpark=carpark, volume_chart=volume_chart, filepath=url_for('static',filename='images/foo.png'))

@main.route('/transactions/<code>')
def transactions(code):
    carpark = Carpark.query.filter_by(code=code).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = carpark.transactions.order_by(Transaction.exit_timestamp.desc()).paginate(
        page, per_page=current_app.config['TRANSACTIONS_PER_PAGE'], error_out=False
    )
    transactions = pagination.items
    return render_template('transactions.html', carpark=carpark, transactions=transactions, pagination=pagination)
