class Config:
    MONGODB_SETTINGS = {
        'db': 'MY_DB',
        'host': 'localhost',
        'port': 27017,
        'username': '',  # Add your MongoDB username if applicable
        'password': '',  # Add your MongoDB password if applicable
        'connect': False,  # Avoid connecting to MongoDB at the application startup
    }