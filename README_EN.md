# The Future of Youth: Trends in Education, Employment and Mental Health

![The Future of Youth](https://github.com/amirargani/Die_Zukunft_der_Jugend/blob/main/src/Die_Zukunft_der_Jugend.png)

#### 🇩🇪 German: [README.md](README.md)

📌 **Developed by Büsra Yilmaz, Mila Böhm, and Amir Argani**

## 📊 Streamlit Data App

An interactive data analysis tool built with **Streamlit**, **Pandas**, **NumPy**, **Plotly**, and **Scikit-learn**.

---

### 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/amirargani/Die_Zukunft_der_Jugend.git
   ```

2. **Check Python version**
   This project was developed using **Python 3.11.0**.

   ```bash
   python --version
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Python packages**

   ```markdown
   | Package Name   | Version |
   |----------------|---------|
   | streamlit      | 1.50.0  |
   | pandas         | 2.3.3   |
   | numpy          | 2.3.4   |
   | plotly         | 6.3.1   |
   | scikit-learn   | 1.7.2   |
   ```

5. **Verify installed versions**

   ```bash
   pip show streamlit
   pip show pandas
   pip show numpy
   pip show plotly
   pip show scikit-learn
   ```

---

### 🧪 Requirements (`requirements.txt`)

```txt
streamlit==1.50.0
pandas==2.3.3
numpy==2.3.4
plotly==6.3.1
scikit-learn==1.7.2
```

---

### ▶️ Run the Application

```bash
streamlit run streamlit_app.py
```

---

### 🛠️ Features

* 📈 Interactive visualizations with Plotly
* 📊 Data analysis using Pandas & NumPy
* 🧠 Machine learning models with Scikit-learn
* 🌐 Web application built with Streamlit

---

### 🛠️ `config.toml`

Configuration details are documented here:
📄 [`readme_config_en.md`](readme_config_en.md)

---

## 📁 `src/` – Project Structure & Contents

The **`src/`** folder contains all project-related resources such as raw data, processed datasets, design files, and visualizations used for analysis, modeling, and presentation.

### 📂 Folder Overview

```text
src/
├── Bereinigte_Daten/
├── Rohdaten/
├── PowerBI/
└── PSD/
```

---

### 📄 Detailed Folder Description

#### 📂 **Rohdaten/** (Raw Data)

* Contains **unaltered original datasets** (e.g., CSV files)

---

#### 📂 **Bereinigte Daten/** (Cleaned Data)

* Contains **preprocessed and cleaned datasets**
* Processing steps include, for example:

  * Removing missing or invalid values
  * Renaming columns
  * Data type conversions

---

#### 📂 **PowerBI/**

* Contains **Power BI files (.pbix)**
* Used for:

  * Exploratory data analysis
  * Dashboard creation
  * Comparison with Streamlit visualizations

---

#### 📂 **PSD/**

* Contains **design and layout files** (e.g., Photoshop `.psd`)
* Used for:

  * Project graphics

---

## 📅 Changelog

### V.2025.10.31.0 (October 31, 2025)

* **Modules**

  * Education
  * Labor Market
  * Mental Health
* **Machine Learning**

  * Unemployment
* **CSV**

  * Charts

    * Jupyter notebooks for indicators