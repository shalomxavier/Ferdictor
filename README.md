🌾 Fertilizer Recommendation System for Coconut Cultivation
A simple web-based application built with Flask that predicts the recommended quantity of SSP (Single Super Phosphate), MOP (Muriate of Potash), and Urea for coconut cultivation, based on the nutrient availability in soil.

🚀 Features
Predicts SSP, MOP, and Urea quantities using machine learning models (.pkl files).

Takes available soil N, P, and K values as input.

Applies domain-specific rules:

No Urea if available N > 0.25

No SSP if available P > 34.5

No MOP if available K > 395

Multi-page interface using Flask routing (index, calculate, result, and schedule).

Maintains state using Flask session.

🧠 Tech Stack
Frontend: HTML (via Jinja2 templates)

Backend: Python with Flask

Machine Learning Models: Pretrained .pkl models using joblib

Hosting: Run locally with Flask’s development server

💻 How to Run Locally
Clone the repository

bash
Copy
Edit
git clone https://github.com/shalomxavier/ferdictor.git
cd fertilizer-app
Install dependencies

Make sure you have Python 3 installed. Then:

bash
Copy
Edit
pip install flask joblib numpy
Add model files

Place the following trained model files in the root directory:

ssp_model.pkl

mop_model.pkl

urea_model.pkl

Run the Flask server

bash
Copy
Edit
python app.py
Open in browser

Navigate to http://127.0.0.1:5000 in your browser.

🔍 Example Use Case
Select Coconut as the crop and Loamy/Clayey as the soil type.

Enter the available values of:

Phosphorus (P)

Potassium (K)

Nitrogen (N)

Get fertilizer recommendations tailored for your soil!

📌 Note
This is a prototype system built for research and learning purposes.

Models are trained externally and are expected to be accurate for specific soil/crop conditions.

📜 License
MIT License
