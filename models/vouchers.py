from datetime import datetime
from app import db

class PaymentVoucher(db.Model):
    """نموذج سندات الصرف (المدفوعات)"""
    __tablename__ = 'payment_vouchers'
    
    id = db.Column(db.Integer, primary_key=True)
    voucher_number = db.Column(db.String(20), nullable=False, unique=True)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(15, 2), nullable=False)
    currency = db.Column(db.String(3), default='YER')
    exchange_rate = db.Column(db.Numeric(15, 6), default=1.0)
    recipient_type = db.Column(db.String(20), nullable=False)  # supplier, customer, employee, other
    recipient_id = db.Column(db.Integer, nullable=True)  # سيتم ربطه بالجدول المناسب حسب recipient_type
    recipient_name = db.Column(db.String(120), nullable=False)
    payment_method = db.Column(db.String(20), default='cash')  # cash, bank_transfer, check
    check_number = db.Column(db.String(30), nullable=True)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'), nullable=True)
    account_number = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='active')  # active, cancelled, modified
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    approved_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<PaymentVoucher {self.voucher_number}>'


class ReceiptVoucher(db.Model):
    """نموذج سندات القبض (الإيرادات)"""
    __tablename__ = 'receipt_vouchers'
    
    id = db.Column(db.Integer, primary_key=True)
    voucher_number = db.Column(db.String(20), nullable=False, unique=True)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(15, 2), nullable=False)
    currency = db.Column(db.String(3), default='YER')
    exchange_rate = db.Column(db.Numeric(15, 6), default=1.0)
    payer_type = db.Column(db.String(20), nullable=False)  # customer, other
    payer_id = db.Column(db.Integer, nullable=True)  # سيتم ربطه بالجدول المناسب حسب payer_type
    payer_name = db.Column(db.String(120), nullable=False)
    payment_method = db.Column(db.String(20), default='cash')  # cash, bank_transfer, check
    check_number = db.Column(db.String(30), nullable=True)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'), nullable=True)
    account_number = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='active')  # active, cancelled, modified
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    approved_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<ReceiptVoucher {self.voucher_number}>'


class Bank(db.Model):
    """نموذج البنوك"""
    __tablename__ = 'banks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    contact_person = db.Column(db.String(100), nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # العلاقات مع الجداول الأخرى
    accounts = db.relationship('BankAccount', backref='bank', lazy=True)
    payment_vouchers = db.relationship('PaymentVoucher', backref='bank', lazy=True)
    receipt_vouchers = db.relationship('ReceiptVoucher', backref='bank', lazy=True)
    
    def __repr__(self):
        return f'<Bank {self.name}>'


class BankAccount(db.Model):
    """نموذج الحسابات البنكية"""
    __tablename__ = 'bank_accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(50), nullable=False)
    account_name = db.Column(db.String(100), nullable=False)
    account_type = db.Column(db.String(50), nullable=True)
    currency = db.Column(db.String(3), default='YER')
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'), nullable=False)
    iban = db.Column(db.String(50), nullable=True)
    swift_code = db.Column(db.String(20), nullable=True)
    balance = db.Column(db.Numeric(15, 2), default=0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<BankAccount {self.account_number}>'