# The Future of Youth: Trends in Education, Employment and Mental Health

![The Future of Youth Header](https://github.com/amirargani/Die_Zukunft_der_Jugend/blob/main/src/Die_Zukunft_der_Jugend.png)

[![License](https://img.shields.io/badge/License-Apache_2.0-D22128?style=for-the-badge&logo=apache)](LICENSE.txt)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)

#### 🇩🇪 German Version: [README.md](README.md)

---

## 🌟 Project Overview

This project is an interactive data analysis application that highlights the current challenges and trends of youth in Germany. We focus on the core areas of **Education**, **Labor Market**, and **Mental Health**.

📌 **Developed by:** Büsra Yilmaz, Mila Böhm & Amir Argani

---

## 📊 The Streamlit App

Our application provides deep insights through interactive visualizations and machine learning models.

### 🛠️ Tech Stack
- **Frontend/Backend:** [Streamlit](https://streamlit.io/)
- **Data Processing:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visualization:** [Plotly](https://plotly.com/python/)
- **Machine Learning:** [Scikit-learn](https://scikit-learn.org/)

---

### 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/amirargani/Die_Zukunft_der_Jugend.git
   cd Die_Zukunft_der_Jugend
   ```

2. **Environment Check**
   Recommended version: **Python 3.11.0**
   ```bash
   python --version
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Adjust Configuration**
   Information regarding `config.toml` can be found here: 📄 [readme_config_en.md](readme_config_en.md)

### ▶️ Run the App
```bash
streamlit run streamlit_app.py
```

---

## 📂 Project Structure & `src/` Contents

The `src/` folder is at the heart of our data management.

```text
src/
├── Rohdaten/           # Unaltered original datasets (CSV)
├── Bereinigte_Daten/   # Preprocessed & cleaned data for the app
├── PowerBI/            # .pbix files for dashboards & comparisons
└── PSD/                # Design resources (Photoshop layouts)
```

### Data Pipeline
- **Cleaning:** Removing outliers, handling missing values, column mapping.
- **Analysis:** Statistical evaluations on education trends.
- **Visualization:** Dynamic graphs showing developments over time.

---

## 🧠 Machine Learning Focus
Our project uses **Scikit-learn** to make predictions in the area of youth unemployment and to analyze correlations between various life spheres.

---

## 📅 Changelog

### V.2025.10.31.0
- ✨ **Modules:** New deep-dives for Education, Labor Market, and Health.
- 🤖 **ML:** Integration of models for unemployment prediction.
- 📈 **Graphs:** Expansion of Plotly dashboards.
- 📓 **Jupyter:** Documentation of indicator calculations.

---
© 2025 – Developed by: Büsra Yilmaz, Mila Böhm & Amir Argani
