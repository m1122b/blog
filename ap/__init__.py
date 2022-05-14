
# ap/__init__.py


from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "nininini"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from ap import routes, models


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Post": models.Post
    }

