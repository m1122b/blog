
# __init__.py


from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "nininini"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#from app import routes, models

if __name__ == "__main__":
    
    app.run(debug=True)

