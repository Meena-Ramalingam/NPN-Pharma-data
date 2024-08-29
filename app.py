from flask import Flask, render_template, request, jsonify
import pickle
import pmdarima
import pandas as pd

app = Flask(__name__)



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


drugs = ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']
models = {}
for drug in drugs:
    with open(f'models/auto_arima_model_{drug}.pkl', 'rb') as file:
        models[drug] = pickle.load(file)

@app.route('/predict_single', methods=['POST'])
def predict_single():
    single_date = request.form['single_date']
    date_range = pd.date_range(start=single_date, end=single_date, freq='D')
    
    predictions = {}
    for drug in drugs:
        predictions[drug] = models[drug].predict(n_periods=1)
    
    return jsonify(predictions)

@app.route('/predict_range', methods=['POST'])
def predict_range():
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    predictions = {}
    for drug in drugs:
        predictions[drug] = models[drug].predict(n_periods=len(date_range)).sum()
    
    return jsonify(predictions)



if __name__ == "__main__":
    app.run(debug=True,port=5001)
