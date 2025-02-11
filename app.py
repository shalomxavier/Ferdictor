from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Load the trained models with absolute paths
ssp_model = joblib.load(os.path.join(os.path.dirname(__file__), 'ssp_model.pkl'))
mop_model = joblib.load(os.path.join(os.path.dirname(__file__), 'mop_model.pkl'))
urea_model = joblib.load(os.path.join(os.path.dirname(__file__), 'urea_model.pkl'))

# Function to calculate SSP, Muriate of Potash, and Urea values using the models
def calculate_values(available_p, available_k, available_n):
    # Calculate initial values using the models
    ssp_value = ssp_model.predict([[available_p]])[0]
    mop_value = mop_model.predict([[available_k]])[0]
    urea_value = urea_model.predict([[available_n]])[0]
    
    # Apply conditions
    if available_n > 0.25:
        urea_value = 0
    if available_p > 34.5:
        ssp_value = 0
    if available_k > 395:
        mop_value = 0

    return ssp_value, mop_value, urea_value

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        crop = request.form['crop']
        soil_type = request.form['soil_type']
        if crop == 'coconut' and soil_type == 'loamy/clayey':
            return redirect(url_for('calculate'))
    return render_template('index.html')

# Route for the calculation page
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        available_p = float(request.form['available_p'])
        available_k = float(request.form['available_k'])
        available_n = float(request.form['available_n'])
        ssp_value, mop_value, urea_value = calculate_values(available_p, available_k, available_n)
        
        # Store values in session
        session['ssp'] = ssp_value
        session['mop'] = mop_value
        session['urea'] = urea_value
        
        return render_template('result.html', ssp=ssp_value, mop=mop_value, urea=urea_value)
    return render_template('calculate.html')

@app.route('/schedule')
def schedule():
    # Retrieve values from session
    ssp = session.get('ssp', None)
    mop = session.get('mop', None)
    urea = session.get('urea', None)

    # Debugging: Check if values are retrieved correctly
    if ssp is None or mop is None or urea is None:
        print("Session values are not set correctly.")
        print(f"ssp: {ssp}, mop: {mop}, urea: {urea}")

    return render_template('schedule.html', ssp=ssp, mop=mop, urea=urea)

if __name__ == '__main__':
    app.run(debug=True)
