import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache_data
def allgemeinbild_abschluss(path, title, key):
    # CSV laden
    allgemein_abschluss = pd.read_csv(
        rf"buesra_graphs\2_Allgemeinbildende Schulen _Abschlüsse Geschlecht\{path}",
        delimiter=","
    )
        # Farben definieren
    farben = {
        "Männlich": "#96B3A1",
        "Weiblich": "#DE6A73"
    }

    # Diagramm initialisieren
    fig = go.Figure()

    # Für jedes Geschlecht einen Balken hinzufügen
    for geschlecht in allgemein_abschluss["Geschlecht"].unique():        
        df_g = allgemein_abschluss[allgemein_abschluss["Geschlecht"] == geschlecht]
        fig.add_trace(go.Bar(
            x=df_g["Zeit"],
            y=df_g["Anzahl"],
            name=geschlecht,
            showlegend= False,
            marker_color=farben[geschlecht],
            text=df_g["Anzahl"],
            textposition="outside"
        ))

    # Layout anpassen
    fig.update_layout(
        title=title,
        xaxis_title="Schuljahr",
        yaxis_title="Anzahl",
        barmode="group",  # nebeneinander statt gestapelt
        xaxis=dict(title="Schuljahr",tickangle=0, dtick=2),
        yaxis=dict(tickformat=",", range=[0, 200000]), #für englische Version
        uniformtext_minsize=8,
        uniformtext_mode="hide"
    )

    # Anzeige in Streamlit
    st.plotly_chart(fig, use_container_width=True, key=key)