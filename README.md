# Heart Risk Predictor

## Project Goal
Build a machine learning model predicting heart disease risk using the UCI Heart Disease dataset and deliver:
- An interactive Streamlit dashboard
- A Colab notebook with full analysis and modeling
- A 1-page business/clinical insights report

This project combines **Biotech (clinical biomarkers)**, **Business (cost-saving recommendations)**, and **Data Analysis (full ML pipeline)**.

## Project Report
View Full White Paper (PDF): https://github.com/Vcoderprogreat/heart-risk-predictor/blob/main/Heart%20Risk%20Predictor.pdf

## Live Demo
Try the interactive Streamlit dashboard here: [Heart Risk Predictor](https://heart-risk-predictor-vb.streamlit.app/)

## Repository Contents
- `HeartRisk_Final_EDA.ipynb` – Exploratory analysis, data cleaning, logistic regression, and random forest modeling
- `Heart Risk Predictor.pdf` – Full White Paper
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
