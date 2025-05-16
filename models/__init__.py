# ملف تهيئة مجلد النماذج
# هذا الملف يسمح باستيراد النماذج كحزمة

from app import db

# استيراد جميع النماذج هنا لضمان إنشاء الجداول
from models.users import User
from models.customers import Customer
from models.suppliers import Supplier
from models.currencies import Currency
from models.vouchers import PaymentVoucher, ReceiptVoucher, Bank, BankAccount
from models.tickets import AirlineTicket, BusTicket
from models.visas import WorkVisa, FamilyVisit, UmrahVisa, UmrahGuarantee
from models.mail import MailTracking, MailHistory