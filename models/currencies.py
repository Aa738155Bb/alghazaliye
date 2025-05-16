from datetime import datetime
from app import db

class Currency(db.Model):
    """نموذج العملات في النظام"""
    __tablename__ = 'currencies'
    
    code = db.Column(db.String(3), primary_key=True)  # رمز العملة مثل USD, SAR, YER
    name = db.Column(db.String(50), nullable=False)  # اسم العملة
    symbol = db.Column(db.String(10), nullable=False)  # رمز العملة مثل $, ر.س، ر.ي
    rate = db.Column(db.Numeric(15, 6), nullable=False)  # سعر الصرف مقابل العملة الأساسية
    is_default = db.Column(db.Boolean, default=False)  # هل هي العملة الافتراضية
    is_active = db.Column(db.Boolean, default=True)  # هل العملة نشطة
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Currency {self.code}>'