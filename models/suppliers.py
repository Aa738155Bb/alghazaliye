from datetime import datetime
from app import db

class Supplier(db.Model):
    """نموذج الموردين في النظام"""
    __tablename__ = 'suppliers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    company_name = db.Column(db.String(150), nullable=True)
    contact_person = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    website = db.Column(db.String(255), nullable=True)
    supplier_type = db.Column(db.String(50), nullable=True)  # شركة طيران، فندق، وكالة تأشيرات، إلخ
    balance = db.Column(db.Numeric(15, 2), default=0)  # رصيد المورد
    currency = db.Column(db.String(3), default='YER')  # عملة الرصيد
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # العلاقات مع الجداول الأخرى
    # transactions = db.relationship('SupplierTransaction', backref='supplier', lazy=True)
    # payments = db.relationship('PaymentVoucher', backref='supplier', lazy=True)
    
    def __repr__(self):
        return f'<Supplier {self.name}>'