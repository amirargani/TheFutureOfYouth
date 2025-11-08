import streamlit as st
import pandas as pd
import plotly.graph_objects as go


@st.cache_data
def ohne_abschluss(path, title, farbe, range, key):
    # CSV laden
    schulart = pd.read_csv(
        rf"buesra_graphs\3_Allgemeinbildende Schulen - Ohne Abschluss\{path}",
        delimiter=","
    )
    fig = go.Figure(data=[
    go.Bar(x=schulart["Zeit"], y=schulart["Anzahl"], marker_color=farbe)
])
    fig.update_layout(
        title=title,
        xaxis_title="Schuljahr",
        yaxis_title="Anzahl",
        xaxis=dict(title="Schuljahr",tickangle=0, dtick=2),
        yaxis=dict(tickformat=",", range=[0, range]), #für englische Version
        uniformtext_minsize=8,
        uniformtext_mode="hide"
    )

    # Anzeige in Streamlit
    st.plotly_chart(fig, use_container_width=True, key=key)


    