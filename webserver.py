from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///players.db'

#initialise the database
db = SQLAlchemy(app)

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Name:{self.name}, Date joined: {self.date_joined}"


@app.route("/delete/<int:id>")
def delete(id):
    delete = Players.query.get_or_404(id)

    if delete:
        try:
            db.session.delete(delete)
            db.session.commit()

            return redirect("/home")
        except:
            return "something went wrong while deleting player"



@app.route("/", methods=["GET"])
def index():
    title = "LOgin Page"
    return render_template("index.html", title=title)

@app.route("/home", methods=["POST", "GET"])
def home():
    title = "Gouping"
    if request.method == "POST":
        player_name = request.form.get("name")
        new_player = Players(name=player_name)

        #add players to database
        db.session.add(new_player)
        #commit players to database
        db.session.commit()
        return redirect("/home")
    else:
        players = Players.query.order_by(Players.date_joined)
        return render_template("home.html", players=players, title= title)



if __name__ == "__main__":
    app.run(debug=True)