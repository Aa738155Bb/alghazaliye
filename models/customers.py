from datetime import datetime
from app import db

class Customer(db.Model):
    """نموذج العملاء في النظام"""
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    passport_number = db.Column(db.String(30), nullable=True)
    id_number = db.Column(db.String(30), nullable=True)
    id_type = db.Column(db.String(30), nullable=True)  # جواز سفر، بطاقة شخصية، إقامة
    nationality = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    birthdate = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(10), nullable=True)  # ذكر، أنثى
    notes = db.Column(db.Text, nullable=True)
    balance = db.Column(db.Numeric(15, 2), default=0)  # رصيد العميل
    currency = db.Column(db.String(3), default='YER')  # عملة الرصيد
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # العلاقات مع الجداول الأخرى
    # airline_tickets = db.relationship('AirlineTicket', backref='customer', lazy=True)
    # bus_tickets = db.relationship('BusTicket', backref='customer', lazy=True)
    # visas = db.relationship('Visa', backref='customer', lazy=True)
    # payments = db.relationship('Payment', backref='customer', lazy=True)
    # receipts = db.relationship('Receipt', backref='customer', lazy=True)
    
    def __repr__(self):
        return f'<Customer {self.full_name}>'