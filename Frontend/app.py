from flask import Flask, render_template, request, jsonify
from coastle_model import run_coastle_model  # this is the actual model
import random

app = Flask(__name__)

@app.route('/')
def index():
    # ADD API STUFF HERE SOMEHOW
    city_data = {
        #ADD DATA
    city_coords = [32, -32]  # give sum example stuff here

    return render_template('index.html', city_data=city_data, city_coords=city_coords)

