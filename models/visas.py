from datetime import datetime
from app import db

class VisaBase(db.Model):
    """النموذج الأساسي للتأشيرات"""
    __abstract__ = True  # هذا الصنف مجرد للوراثة ولن يُنشئ جدولًا
    
    id = db.Column(db.Integer, primary_key=True)
    visa_number = db.Column(db.String(50), nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    passport_number = db.Column(db.String(30), nullable=False)
    issue_date = db.Column(db.Date, nullable=True)
    expiry_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), default='pending')  # pending, issued, rejected, expired
    price = db.Column(db.Numeric(15, 2), nullable=True)
    currency = db.Column(db.String(3), default='YER')
    notes = db.Column(db.Text, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class WorkVisa(VisaBase):
    """نموذج تأشيرة العمل"""
    __tablename__ = 'work_visas'
    
    destination_country = db.Column(db.String(50), nullable=False)
    employer = db.Column(db.String(120), nullable=True)
    job_title = db.Column(db.String(100), nullable=True)
    contract_duration = db.Column(db.Integer, nullable=True)  # بالشهور
    salary = db.Column(db.Numeric(15, 2), nullable=True)
    
    def __repr__(self):
        return f'<WorkVisa {self.visa_number}>'


class FamilyVisit(VisaBase):
    """نموذج تأشيرة الزيارة العائلية"""
    __tablename__ = 'family_visits'
    
    destination_country = db.Column(db.String(50), nullable=False)
    host_name = db.Column(db.String(120), nullable=True)
    host_relationship = db.Column(db.String(50), nullable=True)  # قريب، صديق، إلخ
    host_address = db.Column(db.String(255), nullable=True)
    host_phone = db.Column(db.String(20), nullable=True)
    visit_duration = db.Column(db.Integer, nullable=True)  # بالأيام
    
    def __repr__(self):
        return f'<FamilyVisit {self.visa_number}>'


class UmrahVisa(VisaBase):
    """نموذج تأشيرة العمرة"""
    __tablename__ = 'umrah_visas'
    
    group_number = db.Column(db.String(50), nullable=True)
    package_type = db.Column(db.String(50), nullable=True)  # اقتصادي، عادي، VIP
    hotel_makkah = db.Column(db.String(120), nullable=True)
    hotel_madinah = db.Column(db.String(120), nullable=True)
    transportation = db.Column(db.String(50), nullable=True)
    stay_duration = db.Column(db.Integer, nullable=True)  # بالأيام
    has_guarantee = db.Column(db.Boolean, default=False)  # هل لديه كفالة
    guarantee_id = db.Column(db.Integer, db.ForeignKey('umrah_guarantees.id'), nullable=True)
    
    def __repr__(self):
        return f'<UmrahVisa {self.visa_number}>'


class UmrahGuarantee(db.Model):
    """نموذج كفالة العمرة"""
    __tablename__ = 'umrah_guarantees'
    
    id = db.Column(db.Integer, primary_key=True)
    guarantor_name = db.Column(db.String(120), nullable=False)
    guarantor_id_number = db.Column(db.String(30), nullable=False)
    guarantor_address = db.Column(db.String(255), nullable=True)
    guarantor_phone = db.Column(db.String(20), nullable=True)
    relationship = db.Column(db.String(50), nullable=True)
    guarantee_amount = db.Column(db.Numeric(15, 2), nullable=True)
    currency = db.Column(db.String(3), default='SAR')
    issue_date = db.Column(db.Date, nullable=True)
    expiry_date = db.Column(db.Date, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # العلاقة مع تأشيرات العمرة
    umrah_visas = db.relationship('UmrahVisa', backref='guarantee', lazy=True)
    
    def __repr__(self):
        return f'<UmrahGuarantee {self.guarantor_name}>'