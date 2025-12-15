# Die Zukunft der Jugend: Trends in Bildung, Beschäftigung und mentaler Gesundheit

![Die Zukunft der Jugend](https://github.com/amirargani/Die_Zukunft_der_Jugend/blob/main/src/Die_Zukunft_der_Jugend.png)

#### 🇬🇧 English: [README_EN.md](README_EN.md)

📌 **Entwickelt von Büsra Yilmaz, Mila Böhm und Amir Argani**

## 📊 Streamlit Data App

Ein interaktives Datenanalyse-Tool mit **Streamlit**, **Pandas**, **NumPy**, **Plotly** und **Scikit-learn**.

### 🚀 Installation

1. **Repository klonen**  
   ```bash
   git clone https://github.com/amirargani/Die_Zukunft_der_Jugend.git
   ```

2. **Python-Version prüfen**  
   Dieses Projekt wurde mit **Python 3.11.0** entwickelt.  
   ```bash
   python --version
   ```

3. **Abhängigkeiten installieren**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Python-Pakete**
   ```markdown
   | Paketname      | Version   |
   |----------------|-----------|
   | streamlit      | 1.50.0    |
   | pandas         | 2.3.3     |
   | numpy          | 2.3.4     |
   | plotly         | 6.3.1     |
   | scikit-learn   | 1.7.2     |
   ```

5. **Version prüfen**
   ```bash
   pip show streamlit
   pip show pandas
   pip show numpy
   pip show plotly
   pip show scikit-learn
   ```

### 🧪 Anforderungen (`requirements.txt`)

```txt
streamlit==1.50.0
pandas==2.3.3
numpy==2.3.4
plotly==6.3.1
scikit-learn==1.7.2
```

### ▶️ Anwendung starten

```bash
streamlit run streamlit_app.py
```

### 🛠️ Features

- 📈 Interaktive Visualisierungen mit Plotly  
- 📊 Datenanalyse mit Pandas & NumPy  
- 🧠 ML-Modelle mit Scikit-learn  
- 🌐 Web-App mit Streamlit  

### 🛠️ `config.toml`: [`readme_config.md`](readme_config.md)

---

## 📁 `src/` – Projektstruktur & Inhalte

Der Ordner **`src/`** enthält alle projektbezogenen Ressourcen wie Rohdaten, aufbereitete Daten, Design-Dateien und Visualisierungen, die für Analyse, Modellierung und Präsentation verwendet werden.

### 📂 Ordnerübersicht

```text
src/
├── Bereinigte_Daten/
├── Rohdaten/
├── PowerBI/
└── PSD/
```

### 📄 Detailbeschreibung der Inhalte

#### 📂 **Rohdaten/**

* Enthält **unveränderte Originaldatensätze** (z. B. CSV-Dateien)

---

#### 📂 **Bereinigte_Daten/**

* Enthält **vorverarbeitete und bereinigte Datensätze**
* Schritte umfassen z. B.:

  * Entfernen fehlender oder fehlerhafter Werte
  * Umbenennung von Spalten
  * Typkonvertierungen

---

#### 📂 **PowerBI/**

* Beinhaltet **PowerBI-Dateien (.pbix)**
* Dienen zur:

  * Explorativen Datenanalyse
  * Erstellung von Dashboards
  * Vergleich mit Streamlit-Visualisierungen

---

#### 📂 **PSD/**

* Enthält **Design- und Layout-Dateien** (z. B. Photoshop `.psd`)
* Verwendung für:

  * Projektgrafiken
 
---

## 📅 Changelog  
### V.2025.10.31.0 (31. Oktober 2025)

- **Module**
  - Bildung
  - Arbeitsmarkt
  - Psychische Gesundheit
- **ML**
  - Arbeitslosigkeit
- **CSV**
  - Graphen
    - Jupyter für Indikatoren