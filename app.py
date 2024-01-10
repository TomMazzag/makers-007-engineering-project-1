import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import *
from lib.space import *
from lib.booking_repository import BookingRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route("/spaces", methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    spaces = space_repo.all()
    return render_template("spaces.html", spaces=spaces)

@app.route("/spaces/<id>", methods=['GET'])
def get_space(id):
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    booking_repo = BookingRepository(connection)
    space = space_repo.find(id)
    bookings = booking_repo.get_by_id(id)
    return render_template("space.html", space=space, bookings=bookings)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
