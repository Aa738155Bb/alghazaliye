from datetime import datetime
from app import db

class TicketBase(db.Model):
    """النموذج الأساسي للتذاكر"""
    __abstract__ = True  # هذا الصنف مجرد للوراثة ولن يُنشئ جدولًا
    
    id = db.Column(db.Integer, primary_key=True)
    ticket_number = db.Column(db.String(50), nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    price = db.Column(db.Numeric(15, 2), nullable=True)
    currency = db.Column(db.String(3), default='YER')
    status = db.Column(db.String(20), default='pending')  # pending, issued, cancelled, refunded
    notes = db.Column(db.Text, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class AirlineTicket(TicketBase):
    """نموذج تذاكر الطيران"""
    __tablename__ = 'airline_tickets'
    
    airline = db.Column(db.String(100), nullable=False)
    flight_number = db.Column(db.String(20), nullable=True)
    departure_city = db.Column(db.String(100), nullable=False)
    arrival_city = db.Column(db.String(100), nullable=False)
    departure_date = db.Column(db.DateTime, nullable=False)
    arrival_date = db.Column(db.DateTime, nullable=True)
    booking_reference = db.Column(db.String(50), nullable=True)
    passenger_name = db.Column(db.String(120), nullable=False)
    passenger_passport = db.Column(db.String(30), nullable=True)
    seat_class = db.Column(db.String(20), nullable=True)  # اقتصادية، رجال أعمال، أولى
    is_round_trip = db.Column(db.Boolean, default=False)
    return_flight_number = db.Column(db.String(20), nullable=True)
    return_departure_date = db.Column(db.DateTime, nullable=True)
    return_arrival_date = db.Column(db.DateTime, nullable=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=True)
    
    def __repr__(self):
        return f'<AirlineTicket {self.ticket_number}>'


class BusTicket(TicketBase):
    """نموذج تذاكر الباصات"""
    __tablename__ = 'bus_tickets'
    
    bus_company = db.Column(db.String(100), nullable=False)
    trip_number = db.Column(db.String(20), nullable=True)
    departure_city = db.Column(db.String(100), nullable=False)
    arrival_city = db.Column(db.String(100), nullable=False)
    departure_date = db.Column(db.DateTime, nullable=False)
    departure_time = db.Column(db.Time, nullable=True)
    arrival_date = db.Column(db.DateTime, nullable=True)
    seat_number = db.Column(db.String(10), nullable=True)
    passenger_name = db.Column(db.String(120), nullable=False)
    passenger_id = db.Column(db.String(30), nullable=True)
    is_round_trip = db.Column(db.Boolean, default=False)
    return_trip_number = db.Column(db.String(20), nullable=True)
    return_departure_date = db.Column(db.DateTime, nullable=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=True)
    
    def __repr__(self):
        return f'<BusTicket {self.ticket_number}>'