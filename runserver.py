from example_apps.quickstart_app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, UserMixin

app = create_app()

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Define the User data-model.
# NB: Make sure to add flask_user UserMixin !!!
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    username = db.Column(db.String(100, collation='NOCASE'), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    email_confirmed_at = db.Column(db.DateTime())

    # User information
    first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')

# Setup Flask-User and specify the User data-model
user_manager = UserManager(app, db, User)

with app.app_context():
    # Create all database tables
    db.create_all()

app.run(host='0.0.0.0', port=5000, debug=True)

