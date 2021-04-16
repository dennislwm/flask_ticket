import os

db_host = os.getenv('DB_HOST', default='10.0.1.204')
db_name = os.getenv('DB_NAME', default='dashboard')
db_password = os.getenv('DB_PASSWORD', default='secure_password')
db_port = os.getenv('DB_PORT', default='5432')
db_user = os.getenv('D_USERNAME', default='dashboard')

SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

