# Heart Risk Predictor

## Project Goal
Build a machine learning model predicting heart disease risk using the UCI Heart Disease dataset and deliver:
- An interactive Streamlit dashboard
- A Colab notebook with full analysis and modeling
- Business/clinical insights white paper
- Working ML Model

## Model Overview
Logistic Regression and Random Forest models were built and used to predict heart disease risk using clinical and demographic features. Data preprocessing, feature encoding, and scaling were handled in Colab, and model performance was assessed through accuracy, recall, and F1-score. A simple baseline heuristic (age > 55 OR chol > 240) was tested for comparison, but both models significantly outperformed it. The Random Forest achieved the best results with 81.5% accuracy and strong precision-recall balance, making it the chosen production model. 

## Project Report
View the full white paper: [Project Report PDF](https://github.com/Vcoderprogreat/heart-risk-predictor/blob/main/Heart%20Risk%20Predictor%20Final%20Report.pdf)

## Live Demo
Try the interactive Streamlit dashboard here: [Heart Risk Predictor](https://heart-risk-predictor-vb.streamlit.app/)

## Limitations
This project is for educational and research purposes only. Predictions are probabilistic and should not replace clinical diagnosis. The model was trained on a limited dataset of 1,026 samples, which may reduce generalizability. Dataset bias in age or gender distribution may also affect accuracy. 

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
