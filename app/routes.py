from app import app
from flask import render_template
from app.forms import UsernameForm

header = {"Authorization" : f"Bearer {app.config['GITHUB_PERSONAL_ACCESS_TOKEN']}"}

query = """
query='query($userName: String!){                                                                                                      user(login: $userName){
    contributionsCollection{
      contributionCalendar{
        totalContributions
        weeks{
          contributionDays{
            contributionCount
            date
            color
          }
        }
      }
    }
  }
}' 
"""

@app.route("/", methods=["GET", "POST"])
def home():
    form = UsernameForm()
    if form.validate_on_submit():
        return
    return render_template("home.html", form=form)

@app.route("/exisiting_contributions/<username>")
def existing_contributions(username):
    return