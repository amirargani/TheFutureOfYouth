import warnings #Nicht entfernen (frag' nicht warum)
import sys #Selbe Story
# symptome_plot.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache_data
def plot_symptome(path, title, range, selected_groups, key):
    symptome = pd.read_csv(rf"mila_graphs\{path}", delimiter=",")
    symptome["Average of Prozent"] = symptome["Average of Prozent"].str.replace(",", ".").astype(float)
    symptome["Zeit"] = symptome["Jahr"].astype(str) + " " + symptome["Quartal"]

    farben = {
        "18-29": "#FF5733",
        "30-44": "#33C1FF",
        "45-64": "#9D33FF",
        "65+": "#33FF8A"
    }
    # st.write(selected_groups)
    symptome = symptome[symptome["Altersgruppe"].isin(selected_groups)]

    fig = go.Figure()
    for altersgruppe in symptome["Altersgruppe"].unique():
        gruppe_symptome = symptome[symptome["Altersgruppe"] == altersgruppe]
        fig.add_trace(go.Scatter(
            x=gruppe_symptome["Zeit"],
            y=gruppe_symptome["Average of Prozent"],
            mode="lines+markers",
            name=altersgruppe,
            line=dict(color=farben.get(altersgruppe, "#000000"), width=2.5, shape="spline"),
            marker=dict(size=6),
            hovertemplate=(
                f"<b>Altersgruppe:</b> {altersgruppe}<br>"
                "<b>Zeit:</b> %{x}<br>"
                "<b>Prozent:</b> %{y:.2f}%<extra></extra>"
            )
        ))

    fig.update_layout(
        title=f"📊 {title}",
        xaxis=dict(title="Zeitspanne", showgrid=True, gridcolor="lightgray", gridwidth=1, griddash="dot", tickangle=45, dtick=2),
        yaxis=dict(title="Durchschnittlicher Prozentsatz", showgrid=True, gridcolor="lightgray", gridwidth=1, griddash="dot", tickformat=".2f", range=[0, range]),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        legend_title="Altersgruppe",
        legend_itemclick=False,
        legend_itemdoubleclick=False
    )

    st.plotly_chart(fig, use_container_width=True, key=key)

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

@st.cache_data
def plot_symptome_18_29():
    """
    Erstellt ein interaktives Liniendiagramm mit Plotly aus der CSV-Datei
    'psychische_gesundheit_18_29.csv' für die Altersgruppe 18–29.
    """

    selected_group = "18-29"

    # CSV einlesen
    symptome = pd.read_csv(r"mila_graphs\psychische_gesundheit_18_29.csv", delimiter=",")
    symptome.columns = symptome.columns.str.strip()  # Spaltennamen bereinigen

    # Prozentwerte konvertieren (Komma zu Punkt)
    symptome["Average of Prozent"] = symptome["Average of Prozent"].str.replace(",", ".").astype(float)

    # Quartal in numerische Form bringen
    symptome["Quartal_Nummer"] = symptome["Quartal"].str.extract(r"(\d)").astype(int)

    # Zeitachse als numerischen Wert berechnen (z. B. 2021.0, 2021.25, …)
    symptome["Zeit_num"] = symptome["Jahr"].astype(int) + (symptome["Quartal_Nummer"] - 1) / 4

    # Daten auf Altersgruppe 18–29 filtern
    symptome = symptome[symptome["Altersgruppe"] == selected_group]

    # Farbschema für Quellen
    farben_quellen = {
        "Selbsteinschätzung": "#FF5733",  # Orange
        "Angst": "#33C1FF",               # Hellblau
        "Depression": "#9D33FF"           # Dunkelrot
    }

    # Plot erstellen
    fig = go.Figure()
    for quelle in symptome["Quelle"].unique():
        daten_quelle = symptome[symptome["Quelle"] == quelle].sort_values("Zeit_num")
        fig.add_trace(go.Scatter(
            x=daten_quelle["Zeit_num"],
            y=daten_quelle["Average of Prozent"],
            mode="lines+markers",
            name=quelle,
            line=dict(color=farben_quellen.get(quelle, "#000000")),
            marker=dict(size=6),
            hovertemplate=(
                f"<b>Indikatoren:</b> {quelle}<br>"
                "<b>Jahr/Quartal:</b> %{x:.2f}<br>"
                "<b>Prozent:</b> "
                + ("<span style='color:#800000'><b>%{y:.2f}%</b></span><extra></extra>"
                   if quelle == "Depression"
                   else "%{y:.2f}%<extra></extra>")
            )
        ))

    # Y-Achse dynamisch skalieren mit Puffer
    y_max = symptome["Average of Prozent"].max() * 1.1

    # Layout-Anpassungen
    fig.update_layout(
        title="Psychische Gesundheit (18–29 Jahre)",
        xaxis=dict(
            title="Zeitspanne",
            showgrid=True,
            gridcolor="lightgray",
            gridwidth=1,
            griddash="dot",
            tickangle=0,
            dtick=2,
        ),
        yaxis=dict(
            title="Durchschnittlicher Prozentsatz",
            showgrid=True,
            gridcolor="lightgray",
            gridwidth=1,
            griddash="dot",
            tickformat=".2f",
            range=[0, y_max]
        ),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        legend_title="Indikatoren"
    )

    st.plotly_chart(fig, use_container_width=True, key='psychische_gesundheit_18_29_key')