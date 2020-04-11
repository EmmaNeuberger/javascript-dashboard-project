import csv, json

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
Base = declarative_base()
import pandas as pd
import psycopg2


from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine(f"postgresql://postgres:1000@localhost:5432/covid-19")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# Save references to all three tables
us_states = Base.classes.us_states
us_counties = Base.classes.us_counties
fips = Base.classes.fips

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/us_states<br/>"
        f"/api/v1.0/us_counties<br>"
        f"/api/v1.0/fips<br>"
    )


# @app.route("/api/v1.0/us_states")
# def usStates():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all state data"""
#     # Query all states
#     results = session.query(us_states.date, us_states.state, us_states.fips, us_states.cases, us_states.deaths).all()

#     session.close()

#     # Create a dictionary
#     all_states = []
#     for date, state, fips, cases, deaths in results:
#         states_dict = {}
#         states_dict["date"] = date
#         states_dict["state"] = state
#         states_dict["fips"] = fips
#         states_dict["cases"] = cases
#         states_dict["deaths"] = deaths
#         all_states.append(states_dict)

#     return jsonify(all_states)


# @app.route("/api/v1.0/us_counties")
# def usCounties():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all county data"""
#     # Query all counties

#     results = session.query(us_counties.date, us_counties.county, us_counties.state, us_counties.fips, us_counties.cases, us_counties.deaths).all()

#     session.close()

#     # Create a dictionary
#     all_counties = []
#     for date, county, state, fips, cases, deaths in results:
#         counties_dict = {}
#         counties_dict["date"] = date
#         counties_dict["county"] = county
#         counties_dict["state"] = state
#         counties_dict["fips"] = fips
#         counties_dict["cases"] = cases
#         counties_dict["deaths"] = deaths
#         all_counties.append(counties_dict)

#     return jsonify(all_counties)

@app.route("/api/v1.0/fips")
def fipsAPI():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all county data"""
    # Query all counties
    results = session.query(fips.lat, fips.lon, fips.fips).all()

    session.close()

    # Create a dictionary
    all_fips = []
    for lat, lon, fips in results:
        fips_dict = {}
        fips_dict["lat"] = lat
        fips_dict["lon"] = lon
        fips_dict["fips"] = fips
        all_fips.append(fips_dict)

    return jsonify(all_fips)    


if __name__ == '__main__':
    app.run(debug=True)
