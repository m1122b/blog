
# ap/routes.py


from flask import render_template
from ap import app


@app.route("/")
def index():
    return render_template("base.html")


