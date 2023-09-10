from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .common import DATASET, QSET
from .models import Quiz, db

from random import sample

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    # Serves the daskboard/index page
    q = current_user.quizes  # History current user's quiz
    return render_template("index.html", dataset=DATASET, name=current_user.name, quizes=len(q) > 0, q_iter=reversed(q))

@main.route('/quizzer/<topic>')
@login_required
def quizzer(topic):
    return render_template("quizzer.html", topic=topic, data=DATASET[topic], qset=QSET, qs=sample(DATASET[topic]["qs"], 10))

@main.errorhandler(404)
def not_found(e):
    # Rendering custom 404 page
    return render_template("404.html")

@main.route('/results', methods=["POST"])
@login_required
def results():
    # retrieving topic
    topic = request.form.get("topic")
    correct = 0

    for k, v in request.form.items():
        if k == "topic":
            continue

        # Evaluating answers
        if QSET[k]["a"] == v:
            correct += 1

    data = DATASET[topic]

    # Adding to quiz history
    q = Quiz(marks=correct, subject=data["name"], user=current_user)
    db.session.add(q)
    db.session.commit()

    return render_template("results.html", data=data, marks=correct)