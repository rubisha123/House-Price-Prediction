House Price Prediction
Overview
A regression-based machine learning project to predict house prices using Jupyter Notebooks (.ipynb) for exploration/training and Python scripts (.py) for deployment.
Models Used
Linear Regression

Lasso Regression

Random Forest Regressor

Metrics
Mean Squared Error (MSE)

R² Score

Usage
1.Install dependencies:
pip install -r requirements.txt
2.Run in Jupyter Notebook
Open house_price_prediction.ipynb to explore, preprocess data, train, and evaluate models.
3.Run Streamlit app
streamlit run app.py

Project Structure

house_price_prediction/
│
├── model_development/
│   ├── house_price_prediction.ipynb  # Jupyter Notebook for model development
│   ├── house.csv                     # dataset
│   ├── app.py                        # Streamlit application
│   ├── requirements.txt              # For the Streamlit environment
│   └── model.pk1  scaler.pk1         # Saved model
│
└── README.md                         # Project documentation

