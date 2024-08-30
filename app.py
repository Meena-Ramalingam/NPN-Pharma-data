from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import os
import sys
print(sys.path)


app = Flask(__name__)

# Path to the models folder
models_folder = 'models'

# List of drugs
drugs = ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']

# Load models for weekly and daily predictions
models_weekly = {}
models_daily = {}

for drug in drugs:
    with open(os.path.join(models_folder, f'auto_arima_model_Week_{drug}.pkl'), 'rb') as file:
        models_weekly[drug] = pickle.load(file)
    with open(os.path.join(models_folder, f'auto_arima_model_{drug}.pkl'), 'rb') as file:
        models_daily[drug] = pickle.load(file)

# Routes for rendering pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/prediction')
def prediction():
    return render_template('predictions.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/no5c')
def no5c():
    return render_template('no5c.html')

@app.route('/no5b')
def no5b():
    return render_template('no5b.html')

@app.route('/mo1ab')
def mo1ab():
    return render_template('mo1ab.html')

@app.route('/mo1ae')
def mo1ae():
    return render_template('mo1ae.html')

@app.route('/no2ba')
def no2ba():
    return render_template('no2ba.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/drugs')
def drugs():
    return render_template('drugs.html')

# Route for handling date type selection and predictions
@app.route('/submit', methods=['POST'])
def submit():
    date_type = request.form.get('dateType')

    if date_type == 'daily':
        single_date = request.form.get('singleDate')
        if single_date:
            result = predict_daily_sales(single_date)
    elif date_type == 'weekly':
        start_date = request.form.get('startDate')
        end_date = request.form.get('endDate')
        if start_date and end_date:
            result = predict_weekly_sales(start_date, end_date)
    
    return jsonify(result)

# Functions to predict daily and weekly sales
def predict_daily_sales(single_date):
    start_date = '2019-11-30'  # Last date in the dataset
    date_range = pd.date_range(start=start_date, end=single_date, freq='D')

    predictions = {}
    for drug in drugs:
        predictions[drug] = models_daily[drug].predict(n_periods=len(date_range)) / 30

    predictions_df = pd.DataFrame(predictions, index=date_range)
    result = predictions_df.loc[single_date].to_dict()
    return result

def predict_weekly_sales(start_date, end_date):
    date_range = pd.date_range(start=start_date, end=end_date, freq='7D')

    predictions = {}
    for drug in drugs:
        predictions[drug] = models_weekly[drug].predict(n_periods=len(date_range))

    predictions_df = pd.DataFrame(predictions, index=date_range)
    result = predictions_df.loc[end_date].to_dict()
    return result

# Route for predicting single date (additional functionality)
@app.route('/predict_single', methods=['POST'])
def predict_single():
    single_date = request.form['single_date']
    date_range = pd.date_range(start=single_date, end=single_date, freq='D')
    
    predictions = {}
    for drug in drugs:
        predictions[drug] = models_daily[drug].predict(n_periods=1)
    
    return jsonify(predictions)

# Route for predicting a range of dates (additional functionality)
@app.route('/predict_range', methods=['POST'])
def predict_range():
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    predictions = {}
    for drug in drugs:
        predictions[drug] = models_daily[drug].predict(n_periods=len(date_range)).sum()
    
    return jsonify(predictions)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
