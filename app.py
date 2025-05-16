import os
import logging
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# إنشاء تطبيق Flask
app = Flask(__name__)

# تحميل الإعدادات من config.py
from config import get_config
app.config.from_object(get_config())

# تهيئة قاعدة البيانات
db = SQLAlchemy(app)

# تهيئة نظام تسجيل الدخول
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    from models.users import User
    return User.query.get(int(user_id))

# Routes
@app.route('/')
@app.route('/login')
def login():
    # Redirect directly to dashboard for now
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/airline-tickets')
def airline_tickets():
    return render_template('airline-tickets.html')

@app.route('/bus-tickets')
def bus_tickets():
    return render_template('bus-tickets.html')

@app.route('/work-visa')
def work_visa():
    return render_template('work-visa.html')

@app.route('/family-visit')
def family_visit():
    return render_template('family-visit.html')

@app.route('/umrah-visa')
def umrah_visa():
    return render_template('umrah-visa.html')

@app.route('/umrah-guarantee')
def umrah_guarantee():
    return render_template('umrah-guarantee.html')

@app.route('/mail-tracking')
def mail_tracking():
    return render_template('mail-tracking.html')

@app.route('/customers')
def customers():
    return render_template('customers.html')

@app.route('/suppliers')
def suppliers():
    return render_template('suppliers.html')

@app.route('/banks')
def banks():
    return render_template('banks.html')

@app.route('/payment-vouchers')
def payment_vouchers():
    return render_template('payment-vouchers.html')

@app.route('/receipt-vouchers')
def receipt_vouchers():
    return render_template('receipt-vouchers.html')

@app.route('/receipts')
def receipts():
    return render_template('receipts.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/currencies')
def currencies():
    return render_template('currencies.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/budget-profits')
def budget_profits():
    return render_template('budget-profits.html')

@app.route('/cash-journal')
def cash_journal():
    return render_template('cash-journal.html')

@app.route('/bank-journal')
def bank_journal():
    return render_template('bank-journal.html')

@app.route('/daily-journal')
def daily_journal():
    return render_template('daily-journal.html')

@app.route('/employees')
def employees():
    return render_template('employees.html')

@app.route('/account-statements')
def account_statements():
    return render_template('account-statements.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
