from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load model
with open('Match_prediction.pkl', 'rb') as f:
    model = pickle.load(f)

# Load match data for dropdown values and mapping
df = pd.read_csv('matches.csv')
team_names = sorted(df['team1'].dropna().unique().tolist())
city_names = sorted(df['city'].dropna().unique().tolist())
venue_names = sorted(df['venue'].dropna().unique().tolist())

# Mappings for label encoding
team_mapping = {team: i for i, team in enumerate(team_names)}
city_mapping = {city: i for i, city in enumerate(city_names)}
venue_mapping = {venue: i for i, venue in enumerate(venue_names)}

@app.route('/')
def home():
    return render_template('index.html', team_names=team_names, city_names=city_names, venue_names=venue_names)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        team1 = request.form['team1']
        team2 = request.form['team2']
        venue = request.form['venue']
        city = request.form['city']
        toss_winner = request.form['toss-winner']
        toss_decision = request.form['toss-decision']
        target_runs = int(request.form['target-runs'])
        target_overs = int(request.form['target-overs'])
        home_adv1 = 1 if 'home-advantage-team1' in request.form else 0
        home_adv2 = 1 if 'home-advantage-team2' in request.form else 0

        # Map "team1"/"team2" from toss winner to actual team name
        toss_winner = team1 if toss_winner == 'team1' else team2

        # Prepare input for model
        input_features = np.array([[
            city_mapping[city],
            venue_mapping[venue],
            team_mapping[team1],
            team_mapping[team2],
            team_mapping[toss_winner],
            0 if toss_decision.lower() == 'bat' else 1,
            target_runs,
            target_overs,
            home_adv1,
            home_adv2
        ]])
        # Predict using model
        prediction_encoded = model.predict(input_features)[0]

        # Decode the predicted class back to team name
        inv_team_mapping = {v: k for k, v in team_mapping.items()}
        predicted_team = inv_team_mapping[prediction_encoded]

        return render_template('result.html', prediction=predicted_team)

    except Exception as e:
        return f"Something went wrong: {e}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

