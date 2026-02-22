# 🥛 Milk Quality Prediction System

An AI-powered web application that predicts the quality of milk based on key parameters like pH, temperature, taste, odor, fat, turbidity, and color.

---

## 📌 Project Overview

This project uses **Machine Learning (Random Forest Classifier)** to classify milk quality into:

* ❌ Low Quality
* ⚠️ Medium Quality
* ✅ High Quality

It also provides an interactive **Streamlit web interface** for real-time predictions.

---

## 🎯 Objectives

* Predict milk quality using ML
* Help ensure food safety
* Provide a simple and interactive user interface
* Build an end-to-end ML project (EDA → Model → Deployment)

---

## 🧠 Tech Stack

* Python 🐍
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Streamlit

---

## 📁 Project Structure

```
food_safety/
│
├── app/
│   └── app.py                # Streamlit UI
│
├── data/
│   └── milknew.csv          # Dataset
│
├── model/
│   ├── model.py             # Training script
│   └── model.pkl            # Trained model
│
├── notebooks/
│   └── milk_quality_analysis.ipynb   # EDA + Training
│
├── results/
│   ├── confusion_matrix.png
│   ├── correlation_heatmap.png
│   ├── feature_importance.png
│   ├── metrics.txt
│   └── sample_predictions.csv
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd food_safety
```

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

---

## 🚀 How to Run

### Step 1: Train the Model

```
python model/model.py
```

### Step 2: Run the App

```
streamlit run app/app.py
```

---

## 📊 Features

* Interactive UI with sliders & inputs
* Real-time prediction
* Visual feedback (progress bar, status)
* Feature importance analysis
* Model accuracy ~99%

---

## 🎯 Target Audience

* 🐄 Dairy Farmers
* 🏭 Milk Processing Industries
* 🛒 Retailers
* 👨‍👩‍👧 Consumers

---

## 📈 Model Details

* Algorithm: Random Forest Classifier
* Accuracy: ~99.5%
* Input Features:

  * pH
  * Temperature
  * Taste
  * Odor
  * Fat
  * Turbidity
  * Colour

---


## 🔮 Future Improvements

* Mobile app integration
* IoT sensor-based automatic data input
* Real-time milk quality monitoring
* Cloud deployment

---

## 👩‍💻 Author

Keerthi Shree T S

---

## 📜 License

This project is for educational purposes (AICTE Internship).
