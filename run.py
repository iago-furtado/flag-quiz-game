from app import create_app
from flask_sqlalchemy import SQLAlchemy
from config import Config  
from app.database import db

app = create_app()
app.config.from_object(Config)      

if __name__ == "__main__":
    app.run(debug=True)
