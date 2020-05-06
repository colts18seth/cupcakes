"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, render_template, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET"

connect_db(app)
db.create_all()

def serialize(cupcake):
    """ Serialize cupcake obj to dict. """
    return {
        "id": cupcake.id,
        "flavor": cupcake.id,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }

@app.route("/api/cupcakes")
def list_cupcakes():
    """ list all cupcakes """
    cupcakes = Cupcake.query.all()
    serialized = [serialize(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes/<int:id>")
def show_cupcake(id):
    """ show cupcake with id """ 
    cupcake = Cupcake.query.get_or_404(id)
    serialized = serialize(cupcake)

    return jsonify(cupcake=serialized)

@app.route("/api/cupcakes", methods=["POST"])
def add_cupcake():
    """ add new cupcake """
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize(new_cupcake)

    return (jsonify(cupcake=serialized), 201)