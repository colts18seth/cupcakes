"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, render_template, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET"

connect_db(app) 

def serialize(cupcake):
    """ Serialize cupcake obj to dict. """
    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }

@app.route("/api/cupcakes")
def list_cupcakes():
    """ list all cupcakes """
    cupcakes = Cupcake.query.all()
    serialized = [serialize(cupcake) for cupcake in cupcakes]

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

    data = request.json

    cupcake = Cupcake(
            flavor=data['flavor'],
            rating=data['rating'],
            size=data['size'],
            image=data['image'] or None)

    db.session.add(cupcake)
    db.session.commit()

    serialized = serialize(cupcake)

    return (jsonify(cupcake=serialized), 201)

@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcake(id):
    """ update cupcake with id """ 
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.image = request.json.get("image", cupcake.image)

    db.session.commit()

    serialized = serialize(cupcake)

    return jsonify(cupcake=serialized)


@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    """ delete cupcake with id """ 
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message= "deleted")