# Importiere Bibliotheken
import warnings #Nicht entfernen (frag' nicht warum)
import sys #Selbe Story
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.impute import SimpleImputer

# Ignore
warnings.filterwarnings("ignore", category=UserWarning)

@st.cache_data
def load_data():
    # Daten
    return pd.read_csv(r"amir_graphs\arbeitslos\arbeitlosen_nach_altergruppen_Monaten_2010_2025_.csv", delimiter=';', encoding='utf-8-sig')

@st.cache_data
def plot_arbeitslos_total(arbeitslos):
    # Deutsch → Englisch Monatsnamen
    monat_map = {
        "Januar": "January", "Februar": "February", "März": "March", "April": "April",
        "Mai": "May", "Juni": "June", "Juli": "July", "August": "August",
        "September": "September", "Oktober": "October", "November": "November", "Dezember": "December"
    }

    arbeitslos["Monat_en"] = arbeitslos["Monat"].map(monat_map)

    # Kombiniertes Datum erzeugen
    arbeitslos["Datum"] = pd.to_datetime(
        arbeitslos["Monat_en"] + " " + arbeitslos["Jahr"].astype(str),
        format="%B %Y", errors="coerce"
    )

    # Nur gültige Zeilen ab 2023
    arbeitslos = arbeitslos[(arbeitslos["Jahr"] >= 2025) & arbeitslos["Datum"].notna() & arbeitslos["Insgesamt"].notna()]
    arbeitslos = arbeitslos.sort_values("Datum")

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=arbeitslos["Datum"],
        y=arbeitslos["Insgesamt"],
        mode="lines+markers",
        name="Insgesamt",
        line=dict(color="#E66C37", width=3),
        marker=dict(size=6),
        hovertemplate="<b>Monat:</b> %{x|%B %Y}<br><b>Wert:</b> %{y:,}<extra></extra>"
    ))

    fig.update_layout(
        title= "Arbeitslosigkeit: Originalwerte Januar-September 2025",
        xaxis=dict(
            title="Monat",
            tickmode="linear",   # oder "array"
            dtick="M2",          # alle Monate anzeigen
            tickformat="%B %Y",  # voller Monatsname + Jahr
            showgrid=True,
            gridcolor="lightgray",
            griddash="dot",
            tickangle=0
        ),
        yaxis=dict(
            title="Anzahl",
            showgrid=True,
            gridcolor="lightgray",
            griddash="dot",
            tickformat=",d",
            range=[0, 3500000],
            dtick=500000
        ),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        legend_itemclick=False,
        legend_itemdoubleclick=False
    )

    st.plotly_chart(fig, use_container_width=True, key='arbeitslos_ml_key')


@st.cache_data
def ml_modelle():
    # Daten laden
    df = pd.read_csv(r"amir_graphs\arbeitslos\arbeitlosen_nach_altergruppen_Monaten_2010_2025_.csv", delimiter=';', encoding='utf-8-sig')

    # Monatsmapping
    monat_map = {
        "Januar": 1, "Februar": 2, "März": 3, "April": 4,
        "Mai": 5, "Juni": 6, "Juli": 7, "August": 8,
        "September": 9, "Oktober": 10, "November": 11, "Dezember": 12
    }

    # Zeitspalte erstellen
    df["Datum"] = pd.to_datetime(dict(year=df["Jahr"], month=df["Monat"].map(monat_map), day=1))
    df["Datum"] = pd.to_datetime(df['Datum'], errors='coerce').dt.strftime('%m.%Y')
    df["Monat_num"] = df["Monat"].map(monat_map)
    df['Zeitindex'] = range(1, len(df) + 1)

    # Interpolation
    df['Insgesamt'] = df['Insgesamt'].interpolate(method='linear')
    df['Insgesamt_lag1'] = df['Insgesamt'].shift(1)

    # Features und Ziel
    X = df[['Monat_num', 'Zeitindex', 'Insgesamt_lag1']]
    y = df[['Insgesamt']]
    imputer = SimpleImputer(strategy='mean')
    X = imputer.fit_transform(X)
    y = y.fillna(y.mean())

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # Modelle
    models = {
        "Lineare Regression": LinearRegression(),
        "Polynomiale Regression (Grad 2)": LinearRegression(),
        "Random Forest Regressor": RandomForestRegressor(n_estimators=100, random_state=42),
        "Decision Tree Regressor": DecisionTreeRegressor(random_state=42),
        "SVR": SVR()
    }

    trained_models = {}
    predictions = {}
    mse_scores = {}
    r2_scores = {}
    r2_data = []

    for name, model in models.items():
        mse_scores[name] = {}
        r2_scores[name] = {}
        trained_models[name] = {}
        predictions[name] = {}

        for target_col in y.columns:
            y_train_target = y_train[target_col].copy()
            y_test_target = y_test[target_col].copy()

            if name == "Polynomiale Regression (Grad 2)":
                poly = PolynomialFeatures(degree=2)
                X_train_poly = poly.fit_transform(X_train)
                X_test_poly = poly.transform(X_test)
                model.fit(X_train_poly, y_train_target)
                scores = cross_val_score(model, X_train_poly, y_train_target, cv=5, scoring='neg_mean_squared_error')
                trained_models[name][target_col] = (model, poly)
                y_pred = model.predict(X_test_poly)
            else:
                model.fit(X_train, y_train_target)
                scores = cross_val_score(model, X_train, y_train_target, cv=5, scoring='neg_mean_squared_error')
                trained_models[name][target_col] = model
                y_pred = model.predict(X_test)

            predictions[name][target_col] = y_pred
            mse_scores[name][target_col] = -scores.mean()
            r2_scores[name][target_col] = r2_score(y_test_target, y_pred)
            r2_percent = r2_scores[name][target_col] * 100
            r2_data.append({
                "Modell": name,
                "Zielvariable": target_col,
                "R² (%)": round(r2_percent, 2)
            })

    df_new = pd.DataFrame(r2_data)
    df_new_sorted = df_new.sort_values(by='R² (%)', ascending=False)
    df_new_sorted.drop(index=4, inplace=True)
    df_new_sorted.reset_index(drop=True, inplace=True)

    # Prognose vorbereiten
    df_copy = df.copy()
    df_copy["Datum_dt"] = pd.to_datetime(df_copy["Datum"], format="%m.%Y", errors="coerce")
    mask = (df_copy["Datum_dt"].dt.year >= 2023) & (df_copy["Datum_dt"].dt.year <= 2025)
    df_filtered = df_copy[mask].copy()

    best_model_name = min(mse_scores, key=lambda name: mse_scores[name]['Insgesamt'])

    if best_model_name == "Polynomiale Regression (Grad 2)":
        poly = trained_models[best_model_name]['Insgesamt'][1]
        model = trained_models[best_model_name]['Insgesamt'][0]
        X_filtered = imputer.transform(df_filtered[['Monat_num', 'Zeitindex', 'Insgesamt_lag1']])
        X_filtered_poly = poly.transform(X_filtered)
        y_pred_filtered = model.predict(X_filtered_poly)
        # print(np.round(y_pred_filtered, 2))

    else:
        model = trained_models[best_model_name]['Insgesamt']
        X_filtered = imputer.transform(df_filtered[['Monat_num', 'Zeitindex', 'Insgesamt_lag1']])
        y_pred_filtered = model.predict(X_filtered)

    # Prognosewerte einfügen
    df_filtered["Prognose"] = df_filtered["Insgesamt"]
    df_filtered["Datum_dt"] = pd.to_datetime(df_filtered["Datum"], format="%m.%Y", errors="coerce")
    mask_replace = (df_filtered["Datum_dt"] >= pd.Timestamp("2025-10-01")) & (df_filtered["Datum_dt"] <= pd.Timestamp("2025-12-31"))
    df_filtered.loc[mask_replace, "Prognose"] = np.round(y_pred_filtered)[mask_replace]

    # Anzeige der geänderten Werte
    # st.subheader("Werte für Oktober–Dezember 2025 / ML Modelle")
    st.markdown("<span style='font-size:15px'>Werte für Oktober–Dezember 2025 / ML Modelle</span>", unsafe_allow_html=True)
    # st.dataframe(df_filtered.loc[mask_replace][["Datum", "Insgesamt", "Prognose"]])
    st.dataframe(df_filtered.loc[mask_replace][["Datum", "Prognose"]])

    # Plot
    # plot_prognose(df_filtered)

    return df_new_sorted, df_filtered

@st.cache_data
def plot_prognose(df_filtered):
    # Stelle sicher, dass Datum korrekt ist
    df_filtered["Datum_dt"] = pd.to_datetime(df_filtered["Datum"], format="%m.%Y", errors="coerce")

    # Prognosewerte für Okt–Dez 2025 übernehmen
    mask_replace = (df_filtered["Datum_dt"] >= pd.Timestamp("2025-10-01")) & (df_filtered["Datum_dt"] <= pd.Timestamp("2025-12-31"))
    df_filtered["Wert_anzeige"] = df_filtered["Insgesamt"].copy()
    df_filtered.loc[mask_replace, "Wert_anzeige"] = df_filtered.loc[mask_replace, "Prognose"]

    # Filter für Plot: ab 2024
    df_filtered = df_filtered[(df_filtered["Jahr"] >= 2025) & df_filtered["Datum_dt"].notna() & df_filtered["Wert_anzeige"].notna()]

    fig = go.Figure()

    # Nur eine Linie mit gemischten Werten (Original + Prognose für Okt–Dez)
    fig.add_trace(go.Scatter(
        x=df_filtered["Datum_dt"],
        y=df_filtered["Wert_anzeige"],
        mode="lines+markers",
        name="Original",  # Legende bleibt "Original"
        line=dict(color="#F84E05", width=3),
        marker=dict(size=6),
        hovertemplate="<b>Monat:</b> %{x|%B %Y}<br><b>Wert:</b> %{y:,}<extra></extra>"
    ))

    fig.update_layout(
        title="Arbeitslosigkeit: Originalwerte (inkl. Prognose Okt–Dez 2025)",
        xaxis=dict(
            title="Monat",
            tickmode="linear",
            dtick="M2",
            tickformat="%B %Y",
            showgrid=True,
            gridcolor="lightgray",
            griddash="dot",
            tickangle=0
        ),
        yaxis=dict(
            title="Anzahl",
            showgrid=True,
            gridcolor="lightgray",
            griddash="dot",
            tickformat=",d",
            range=[0, 3500000],
            dtick=500000
        ),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        legend=dict(x=0.01, y=0.99)
    )

    st.plotly_chart(fig, use_container_width=True, key='plot_prognose_key')