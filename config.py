import os
from datetime import timedelta

# تكوينات مختلفة للبيئات المختلفة (تطوير، اختبار، إنتاج)
class Config:
    """تكوين أساسي مشترك"""
    SECRET_KEY = os.environ.get('SESSION_SECRET', 'default_secret_key')
    
    # إعدادات قاعدة البيانات PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@localhost/alghazaliye')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
    
    # إعدادات جلسة المستخدم
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    
    # إعدادات البريد الإلكتروني
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = bool(os.environ.get('MAIL_USE_TLS', True))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    
    # إعدادات التطبيق
    APP_NAME = 'نظام وكالة الغزالية للسفر والسياحة'
    COMPANY_NAME = 'وكالة الغزالية للسفر والسياحة'
    COMPANY_ADDRESS = 'صنعاء - شارع جمال'
    COMPANY_PHONE = '+967 123 456 789'
    COMPANY_EMAIL = 'info@alghazaliye.com'
    COMPANY_WEBSITE = 'www.alghazaliye.com'
    COMPANY_LOGO = 'static/img/logo.png'
    
    # إعدادات العملات
    DEFAULT_CURRENCY = 'YER'  # الريال اليمني
    SUPPORTED_CURRENCIES = {
        'YER': {'name': 'ريال يمني', 'symbol': 'ر.ي', 'rate': 1.0},
        'USD': {'name': 'دولار أمريكي', 'symbol': '$', 'rate': 0.004},
        'SAR': {'name': 'ريال سعودي', 'symbol': 'ر.س', 'rate': 0.015},
        'AED': {'name': 'درهم إماراتي', 'symbol': 'د.إ', 'rate': 0.015}
    }
    
    # إعدادات الملفات
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'doc', 'docx', 'xls', 'xlsx'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 ميجابايت

    # إعدادات الإشعارات
    ENABLE_EMAIL_NOTIFICATIONS = False
    ENABLE_SMS_NOTIFICATIONS = False
    
    # إعدادات Twilio للرسائل القصيرة
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
    
    # إعدادات أخرى
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """تكوين بيئة التطوير"""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    

class TestingConfig(Config):
    """تكوين بيئة الاختبار"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql://postgres:postgres@localhost/alghazaliye_test')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """تكوين بيئة الإنتاج"""
    # ضمان استخدام مفتاح سري آمن في الإنتاج
    SECRET_KEY = os.environ.get('SESSION_SECRET') or os.urandom(24)
    
    # تعطيل وضع التصحيح
    DEBUG = False


# القاموس لاختيار التكوين المناسب
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# اختيار التكوين بناءً على متغير البيئة
def get_config():
    """استرجاع كائن التكوين المناسب بناءً على متغير بيئة FLASK_ENV"""
    env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])