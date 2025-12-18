# Die Zukunft der Jugend: Trends in Bildung, Beschäftigung und mentaler Gesundheit

![Die Zukunft der Jugend Header](https://github.com/amirargani/Die_Zukunft_der_Jugend/blob/main/src/Die_Zukunft_der_Jugend.png)

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-Apache_2.0-green?style=for-the-badge)](LICENSE.txt)

#### 🇺🇸 English Version: [README_EN.md](README_EN.md)

---

## 🌟 Projektübersicht

Dieses Projekt ist eine interaktive Datenanalyse-App, die die aktuellen Herausforderungen und Trends der Jugend in Deutschland beleuchtet. Wir konzentrieren uns dabei auf die Kernbereiche **Bildung**, **Arbeitsmarkt** und **psychische Gesundheit**.

📌 **Entwickelt von:** Büsra Yilmaz, Mila Böhm & Amir Argani

---

## 📊 Die Streamlit App

Unsere Anwendung bietet tiefgehende Einblicke durch interaktive Visualisierungen und Machine-Learning-Modelle.

### 🛠️ Tech Stack
- **Frontend/Backend:** [Streamlit](https://streamlit.io/)
- **Datenverarbeitung:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visualisierung:** [Plotly](https://plotly.com/python/)
- **Machine Learning:** [Scikit-learn](https://scikit-learn.org/)

---

### 🚀 Installation & Setup

1. **Repository klonen**
   ```bash
   git clone https://github.com/amirargani/Die_Zukunft_der_Jugend.git
   cd Die_Zukunft_der_Jugend
   ```

2. **Umgebung prüfen**
   Empfohlene Version: **Python 3.11.0**
   ```bash
   python --version
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

4. **Konfiguration anpassen**
   Informationen zur `config.toml` findest du hier: 📄 [readme_config.md](readme_config.md)

### ▶️ App starten
```bash
streamlit run streamlit_app.py
```

---

## � Projektstruktur & `src/` Inhalte

Der `src/` Ordner bildet das Herzstück unseres Datenmanagements.

```text
src/
├── Rohdaten/           # Unveränderte Originaldatensätze (CSV)
├── Bereinigte_Daten/   # Vorverarbeitete & gesäuberte Daten für die App
├── PowerBI/            # .pbix Dateien für Dashboards & Vergleiche
└── PSD/                # Design-Ressourcen (Photoshop Layouts)
```

### Daten-Pipeline
- **Bereinigung:** Entfernen von Outliern, Handling von Missing Values, Spalten-Mapping.
- **Analyse:** Statistische Auswertungen zu Bildungstrends.
- **Visualisierung:** Dynamische Graphen, die den Zeitverlauf verdeutlichen.

---

## 🧠 Machine Learning Fokus
Unser Projekt nutzt **Scikit-learn**, um Vorhersagen im Bereich der Jugendarbeitslosigkeit zu treffen und Zusammenhänge zwischen den verschiedenen Lebensbereichen zu analysieren.

---

## 📅 Changelog

### V.2025.10.31.0
- ✨ **Module:** Neue Deep-Dives für Bildung, Arbeitsmarkt und Gesundheit.
- 🤖 **ML:** Integration von Modellen zur Arbeitslosigkeit-Vorhersage.
- 📈 **Graphs:** Erweiterung der Plotly-Dashboards.
- 📓 **Jupyter:** Dokumentation der Indikatoren-Berechnung.

---
© 2025 – Entwickelt von: Büsra Yilmaz, Mila Böhm & Amir Argani
