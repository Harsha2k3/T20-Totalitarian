<<<<<<< HEAD
import numpy as np
from flask import Flask , request , jsonify , render_template
import pickle
import pandas as pd
import os

app=Flask(__name__)
current_directory = os.path.dirname(os.path.realpath(__file__))

model_path = os.path.join(current_directory, "model_XGB.pkl")

model = pickle.load(open(model_path, "rb"))
@app.route('/')
def home():
    teams = [
        'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa',
        'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
    ]
    cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 'Nagpur', 'Cardiff', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Christchurch', 'Trinidad']

    return render_template('index.html', teams=teams,cities=cities)



@app.route("/predict", methods=["POST"])
def predict():
    form_data = {key: value for key, value in request.form.items()}
    form_data["wickets_left"] = 10 - int(form_data["wickets"])
    form_data["balls_left"] = 120 - (int(form_data["overs"]) * 6)
    crr = float(form_data["current_score"]) / float(form_data["overs"])
    form_data["extras"] = float(form_data["extras"])
    form_data["last_five"] = float(form_data["last_five"])
    form_data["crr"] = crr
    form_data.pop("wickets")
    form_data.pop("overs")

    input_df = pd.DataFrame({
        'batting_team': [form_data["batting_team"]],
        'bowling_team': [form_data["bowling_team"]],
        'city': [form_data["city"]],
        'current_score': [form_data["current_score"]],
        'balls_left': [form_data["balls_left"]],
        'extras': [form_data["extras"]],
        'wickets_left': [form_data["wickets_left"]],
        'crr': [form_data["crr"]],
        'last_five': [form_data["last_five"]]
    })
    teams = [
        'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa',
        'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
    ]
    cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 'Nagpur', 'Cardiff', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Christchurch', 'Trinidad']
    
    if form_data["batting_team"]==form_data["bowling_team"]:
        return render_template("index.html", prediction_text="Batting Team and Bowling Team can't be Same",teams=teams,cities=cities)
    if form_data["balls_left"]==0 or form_data["wickets_left"]==0:
        output=form_data["current_score"]
    else:
        result = model.predict(input_df)
        output=str(int (result[0]))
    return render_template("index.html", prediction_text="Score: {}".format(output),teams=teams,cities=cities)


if __name__== "__main__":
    app.run(debug=True)
=======
import numpy as np
from flask import Flask , request , jsonify , render_template
import pickle
import pandas as pd
import os

app=Flask(__name__)
current_directory = os.path.dirname(os.path.realpath(__file__))

model_path = os.path.join(current_directory, "model_XGB.pkl")

model = pickle.load(open(model_path, "rb"))
@app.route('/')
def home():
    teams = [
        'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa',
        'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
    ]
    cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 'Nagpur', 'Cardiff', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Christchurch', 'Trinidad']

    return render_template('index.html', teams=teams,cities=cities)



@app.route("/predict", methods=["POST"])
def predict():
    form_data = {key: value for key, value in request.form.items()}
    form_data["wickets_left"] = 10 - int(form_data["wickets"])
    form_data["balls_left"] = 120 - (int(form_data["overs"]) * 6)
    crr = float(form_data["current_score"]) / float(form_data["overs"])
    form_data["extras"] = float(form_data["extras"])
    form_data["last_five"] = float(form_data["last_five"])
    form_data["crr"] = crr
    form_data.pop("wickets")
    form_data.pop("overs")

    input_df = pd.DataFrame({
        'batting_team': [form_data["batting_team"]],
        'bowling_team': [form_data["bowling_team"]],
        'city': [form_data["city"]],
        'current_score': [form_data["current_score"]],
        'balls_left': [form_data["balls_left"]],
        'extras': [form_data["extras"]],
        'wickets_left': [form_data["wickets_left"]],
        'crr': [form_data["crr"]],
        'last_five': [form_data["last_five"]]
    })
    teams = [
        'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa',
        'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
    ]
    cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 'Nagpur', 'Cardiff', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Christchurch', 'Trinidad']
    
    if form_data["batting_team"]==form_data["bowling_team"]:
        return render_template("index.html", prediction_text="Batting Team and Bowling Team can't be Same",teams=teams,cities=cities)
    if form_data["balls_left"]==0 or form_data["wickets_left"]==0:
        output=form_data["current_score"]
    else:
        result = model.predict(input_df)
        output=str(int (result[0]))
    return render_template("index.html", prediction_text="Score: {}".format(output),teams=teams,cities=cities)


if __name__== "__main__":
    app.run(debug=True)
>>>>>>> 18e1e38fa1b7185cf717cea7eca76a96636e2b06
