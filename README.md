# Heart Risk Predictor

## Project Goal
Build a machine learning model predicting heart disease risk using the UCI Heart Disease dataset and deliver:
- An interactive Streamlit dashboard
- A Colab notebook with full analysis and modeling
- Business/clinical insights white paper
- Working ML Model

## Project Report
View the full white paper: [Project Report PDF](https://github.com/Vcoderprogreat/heart-risk-predictor/blob/main/Heart%20Risk%20Predictor%20Final%20Report.pdf)

## Live Demo
Try the interactive Streamlit dashboard here: [Heart Risk Predictor](https://heart-risk-predictor-vb.streamlit.app/)

## Repository Contents
- `HeartRisk_Final_EDA.ipynb` – Exploratory analysis, data cleaning, logistic regression, and random forest modeling
- `Heart Risk Predictor Final Report.pdf` – Comprehensive project report 
- `app.py` – Interactive Streamlit dashboard for predicting heart disease risk
- `best_model.pkl` – Saved Random Forest model used by the dashboard
- `heart.csv` – Sample dataset (UCI Heart Disease).
- `requirements.txt` – Python dependencies
- `README.md` – Project overview and instructions

## Tech Stack
- **Python libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `streamlit`
- **Hosting**: Streamlit Cloud
- **Version control**: GitHub

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/Vcoderprogreat/heart-risk-predictor.git
   cd heart-risk-predictor
   pip install -r requirements.txt
   streamlit run app.py
