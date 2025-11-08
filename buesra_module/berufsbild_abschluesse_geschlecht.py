import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache_data
def beruliche_absolventen(path, title, selected_groups, key): #
    berufliche_absolventen = pd.read_csv(rf"buesra_graphs\4_Berufsbildende Schulen - Schulabschlüsse (Geschlecht)\{path}", delimiter=",")

    farben = {
        "Fachhochschulreife": "#E30620",
        "Hauptschulabschluss": "#A38600",
        "Hochschulreife": "#249532",
        "Mittlerer Schulabschluss": "#118DFF"
    }

    berufliche_absolventen = berufliche_absolventen[berufliche_absolventen["Abschlussart"].isin(selected_groups)]

    fig = go.Figure()
    for abschlussart in berufliche_absolventen["Abschlussart"].unique():
        gruppe_berufliche_absolventen = berufliche_absolventen[berufliche_absolventen["Abschlussart"] == abschlussart]
        fig.add_trace(go.Scatter(
            x=gruppe_berufliche_absolventen["Zeit"],
            y=gruppe_berufliche_absolventen["Anzahl"],
            mode="lines+markers",
            name=abschlussart,
            line=dict(color=farben.get(abschlussart, "#000000"), width=2.5, shape="spline"),
            marker=dict(size=6),
            hovertemplate=(
                f"<b>Abschlussart:</b> {abschlussart}<br>"
                "<b>Zeit:</b> %{x}<br>"
                "<b>Prozent:</b> %{y:.2f}%<extra></extra>"
            )
        ))

    fig.update_layout(
        title=f"📊 {title}",
        xaxis=dict(title="Schuljahr", showgrid=True, gridcolor="lightgray",
        gridwidth=1, griddash="dot", tickangle=0, dtick=2),
        yaxis=dict(title="Anzahl", showgrid=True, gridcolor="lightgray", gridwidth=1, griddash="dot", tickformat=",d", separatethousands=True, range=[0, 80000]),
        showlegend=False, 
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        legend_title="Abschlussart"
    )

    st.plotly_chart(fig, use_container_width=True, key=key)