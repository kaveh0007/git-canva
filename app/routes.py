from app import app
from flask import redirect, render_template, url_for
from app.forms import UsernameForm
import requests
from app.utils import generate_query

@app.route("/", methods=["GET", "POST"])
def home():
    form = UsernameForm()
    if form.validate_on_submit():
        return redirect(url_for("existing_contributions", username=form.username.data))
    return render_template("home.html", form=form)

@app.route("/exisiting_contributions/<username>")
def existing_contributions(username):
    header = {"Authorization" : f"Bearer {app.config['GITHUB_PERSONAL_ACCESS_TOKEN']}"}
    payload = {
        "query" : generate_query(),
        "variables" : {"userName" : username}
    }
    response = requests.post(app.config["GITHUB_GRAPHQL_ENDPOINT"], headers=header, json=payload)
    print(response.text)
    return redirect(url_for("home"))