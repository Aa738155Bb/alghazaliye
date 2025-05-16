from datetime import datetime
from app import db

class MailTracking(db.Model):
    """نموذج تتبع البريد/المستندات"""
    __tablename__ = 'mail_tracking'
    
    id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String(50), nullable=False, unique=True)
    reference_number = db.Column(db.String(50), nullable=True)
    mail_type = db.Column(db.String(50), nullable=False)  # جواز سفر، تأشيرة، مستندات أخرى
    description = db.Column(db.Text, nullable=True)
    
    # معلومات المرسل
    sender_name = db.Column(db.String(120), nullable=False)
    sender_phone = db.Column(db.String(20), nullable=True)
    sender_address = db.Column(db.String(255), nullable=True)
    
    # معلومات المستلم
    recipient_name = db.Column(db.String(120), nullable=False)
    recipient_phone = db.Column(db.String(20), nullable=True)
    recipient_address = db.Column(db.String(255), nullable=True)
    
    # معلومات الإرسال والاستلام
    shipping_company = db.Column(db.String(100), nullable=True)
    shipping_date = db.Column(db.DateTime, nullable=True)
    expected_delivery_date = db.Column(db.DateTime, nullable=True)
    actual_delivery_date = db.Column(db.DateTime, nullable=True)
    delivery_status = db.Column(db.String(20), default='pending')  # pending, in_transit, delivered, returned
    
    # معلومات أخرى
    shipping_cost = db.Column(db.Numeric(15, 2), nullable=True)
    currency = db.Column(db.String(3), default='YER')
    notes = db.Column(db.Text, nullable=True)
    
    # حقول النظام
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<MailTracking {self.tracking_number}>'


class MailHistory(db.Model):
    """نموذج سجل تحديثات البريد"""
    __tablename__ = 'mail_history'
    
    id = db.Column(db.Integer, primary_key=True)
    mail_id = db.Column(db.Integer, db.ForeignKey('mail_tracking.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # العلاقة مع جدول تتبع البريد
    mail = db.relationship('MailTracking', backref='history', lazy=True)
    
    def __repr__(self):
        return f'<MailHistory {self.id}>'