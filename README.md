# Ferdictor – Fertilizer Recommendation System for Coconut Cultivation

A web-based Flask application that predicts the required quantity of SSP (Single Super Phosphate), MOP (Muriate of Potash), and Urea for coconut cultivation based on available soil nutrient values using trained machine learning models.

## 🔧 Features

- Predicts optimal fertilizer quantities based on N, P, K availability  
- Uses trained ML models stored as `.pkl` files  
- Applies expert rules to avoid over-fertilization  
- Flask-powered multi-page interface  
- Session-based data handling  

## 🛠️ Technologies Used

- Python  
- Flask  
- NumPy  
- Joblib  
- HTML/CSS (Jinja2 templates)  

## 📸 Screenshots

![Screenshot 2025-07-08 151919](https://github.com/user-attachments/assets/d2788445-2cef-4802-967c-050976b52ad3)
![Screenshot 2025-07-08 160258](https://github.com/user-attachments/assets/2a43c060-4c34-4fbe-aa88-861cda0a37d0)
![Screenshot 2025-07-08 160000](https://github.com/user-attachments/assets/b77a60f5-8305-4ef4-bdbe-4ba2abf98ddd)
![Screenshot 2025-07-08 160037](https://github.com/user-attachments/assets/6ee4bede-c67c-4b59-83d6-e7ca18a979e6)

## 🚀 Getting Started

```bash
git clone https://github.com/shalomxavier/Ferdictor.git
cd Ferdictor
pip install flask joblib numpy
