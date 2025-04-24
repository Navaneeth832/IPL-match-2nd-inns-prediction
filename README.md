# IPL Win Prediction

This project uses an XGBoost model to predict the winner of an IPL match based on various features (city, venue, teams, toss decision, target runs, etc.). The prediction is served via a Flask web app with an interactive HTML form, allowing users to input match details and view the prediction result.


## Features

- **Interactive Web Interface:** 
  - HTML form to input match details.
  - Dropdowns for selecting city, venue, and team names.
  - Numeric inputs for target runs and overs.
  - Checkboxes for home advantage.

- **Model Prediction:**
  - Trained XGBoost model is loaded from the pickle file.
  - Input data is preprocessed based on mappings generated from a CSV file.
  - The app predicts the match winner and displays the result on a separate result page.

## Installation and Setup

1. **Clone or Download the Repository:**

   ```bash
   git clone https://your-repository-link.git
   cd your-repository-directory
Create a Virtual Environment (optional but recommended):

python -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate
Install Required Dependencies:
pip install -r requirements.txt
If you don't have a requirements file, you can install the essentials manually:

pip install flask pandas numpy scikit-learn xgboost
Place Model and Data Files:

Ensure Match_prediction.pkl is in the same directory as app.py.

Ensure matches.csv is also present (used to populate dropdown options in the form).

##Running the Application
Start the Flask Application:

python app.py
Access the Web App:

Open your browser and visit http://127.0.0.1:5000.
Fill in the match details and click "Predict" to see the prediction result.

##How It Works
app.py:

Loads the trained XGBoost model from Match_prediction.pkl.

Reads matches.csv to extract unique values for teams, cities, and venues.

Sets up label mappings to convert string inputs into encoded values that the model understands.

Routes:

/: Renders the index.html form.

/predict: Handles the POST request from the form, preprocesses input data, makes a prediction, and returns the result rendered in result.html.

index.html:

Contains the HTML form for inputting match details.

Uses proper name attributes for form elements so Flask can retrieve the data.

Sends a POST request to the /predict route.

result.html:

Displays the predicted match winner in a user-friendly format.

Provides a link to go back and try another prediction.

##Contributing
Feel free to contribute by opening issues or pull requests if you have suggestions or improvements.

##License
This project is licensed under the MIT License. See the LICENSE file for details.

##Acknowledgments
XGBoost: For the machine learning model.

Flask: For serving the web application.

IPL Fans Worldwide: For inspiring the idea behind the match outcome predictor!

