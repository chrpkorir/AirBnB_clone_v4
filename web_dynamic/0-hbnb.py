#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from flask import Flask, render_template
import uuid

#flask setup
app = Flask(__name__)


#begin flask page rendering
@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = storage.all('State').values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all('Amenity').values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all('Place').values()
    places = sorted(places, key=lambda k: k.name)
    cache_id = uuid.uuid4()
    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Flask App """
    app.run(host='0.0.0.0', port=5000)
