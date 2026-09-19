from flask import Flask, render_template, request, redirect, flash
import secrets
from pathfinderdatabase import db, Learners, Programmes

chatBot = Flask(__name__)

# Generate a secret key
sec = secrets.token_hex(32)

# Give the secret key to Flask
chatBot.config["SECRET_KEY"] = sec

chatBot.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pathfinderdatabase.db"
chatBot.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(chatBot)

with chatBot.app_context():
    db.create_all()


@chatBot.route("/")
def dashboard():
    return render_template("add_programme.html")


@chatBot.route("/add_programme", methods=["POST"])
def add_programme():

    if "POST":
        name_of_prog = request.form["name_of_prog"].lower().strip()
        mathematics = request.form["mathematics"]
        physx = request.form["physx"]
        english = request.form["english"]
        req_points = request.form["req_points"]

        if not name_of_prog and not mathematics and not physx and not english and not req_points:
            flash("your input are empty", "danger")
            return redirect("/")
        
        try:
            int(req_points)
        except:
            flash("Enter an integer value", "danger")
            return redirect("/")

        exist=Programmes.query.filter_by(name_of_prog=name_of_prog).first()
        if exist:
            flash("This programme already exist in a database", "danger")
            return redirect("/")
        
        new_prog = Programmes(
            name_of_prog=name_of_prog,
            mathematics=mathematics,
            physx=physx,
            english=english,
            req_points=req_points
        )

        if new_prog:
            db.session.add(new_prog)
            db.session.commit()

            flash("Successfully submitted", "success")
            
            return redirect("/")
        else:
            KeyError("data was not submittedto the database")
            flash("Not successful", "danger")
            return redirect("/")
        

        

        
    


if __name__ == "__main__":
    chatBot.run(debug=True)