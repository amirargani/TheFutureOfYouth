import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache_data
def allgemeinbild_hochschulreife():
    # CSV laden
    allgemein_abschluss = pd.read_csv(
        rf"buesra_graphs\5_Studium\Allgemeinbildende Schulen.csv",
        delimiter=","
    )
        # Farben definieren
    farben = {
        "Allgemeine Hochschulreife": "#11741C",
    }

    # Diagramm initialisieren
    fig = go.Figure()

    # Für jedes Geschlecht einen Balken hinzufügen
    for schulabschluss in allgemein_abschluss["Schulabschluss"].unique():        
        df_g = allgemein_abschluss[allgemein_abschluss["Schulabschluss"] == schulabschluss]
        fig.add_trace(go.Bar(
            x=df_g["Zeit"],
            y=df_g["Anzahl"],
            name=schulabschluss,
            showlegend= True,
            marker_color=farben[schulabschluss],
            text=df_g["Anzahl"],
            textposition="outside"
        ))

    # Layout anpassen
    fig.update_layout(
        title="Allgemeinbildende Schulen",
        xaxis=dict(title="Schuljahr",tickangle=0, dtick=2),
        yaxis_title="Anzahl",
        #barmode="group",  # nebeneinander statt gestapelt
        yaxis=dict(tickformat=",", range=[0, 350000]),
        uniformtext_minsize=8,
        uniformtext_mode="hide"
    )

    # Anzeige in Streamlit
    st.plotly_chart(fig, use_container_width=True, key='allgemeinbildende_hochschulreife')


@st.cache_data
def berufsbild_hoehere_abschluesse():
    # CSV laden
    hoehere_abschlusse = pd.read_csv(
        rf"buesra_graphs\5_Studium\Berufsbilden Schulen.csv",
        delimiter=","
    )
        # Farben definieren
    farben = {
        "Hochschulreife": "#03420A",
        "Fachhochschulreife": "#E30620"
    }

    # Diagramm initialisieren
    fig = go.Figure()

    # Für jedes Geschlecht einen Balken hinzufügen
    for schulabschluss in hoehere_abschlusse["Abschlussart"].unique():        
        df_g = hoehere_abschlusse[hoehere_abschlusse["Abschlussart"] == schulabschluss]
        fig.add_trace(go.Bar(
            x=df_g["Zeit"],
            y=df_g["Anzahl"],
            name=schulabschluss,
            showlegend= True,
            marker_color=farben[schulabschluss],
            text=df_g["Anzahl"],
            textposition="outside"
        ))

    # Layout anpassen
    fig.update_layout(
        title="Berufsbildende Schulen",
        xaxis=dict(title="Schuljahr",tickangle=0, dtick=2),
        yaxis_title="Anzahl",
        barmode="group",  # nebeneinander statt gestapelt
        yaxis=dict(tickformat=",", range=[0, 350000]),
        uniformtext_minsize=8,
        uniformtext_mode="hide"
    )

    # Anzeige in Streamlit
    st.plotly_chart(fig, use_container_width=True, key='berufsbilden_hoehere_abschluesse')


@st.cache_data
def studium(path, title, range, key, show_fill=True):
    studium = pd.read_csv(rf"buesra_graphs\5_Studium\{path}", delimiter=",")
    
    fig = go.Figure()

    # Gewünschte Linienfarben
    line_colors = ["#C3A900", "#96B3A1", "#DE6A73"]
    # Passende dezente Füllfarben
    fill_colors = ["rgba(255,87,51,0.2)", "rgba(31,119,180,0.2)", "rgba(136,176,75,0.2)"]

    # Für jedes Geschlecht einen Trace erstellen
    geschlechter = studium["Geschlecht"].unique()
    for i, gender in enumerate(geschlechter):
        df_gender = studium[studium["Geschlecht"] == gender]
        trace_args = {
            "x": df_gender["Zeit"],
            "y": df_gender["Anzahl"],
            "mode": "lines+markers",
            "name": gender,
            "line": dict(color=line_colors[i % len(line_colors)], width=2),
            "marker": dict(size=6),
            "hovertemplate": "<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
        }
        if show_fill:
            trace_args["fill"] = "tozeroy"
            trace_args["fillcolor"] = fill_colors[i % len(fill_colors)]
        
        fig.add_trace(go.Scatter(**trace_args))

    fig.update_layout(
        title=f"{title}",
        xaxis=dict(
            title="Jahr",
            showgrid=True,
            tickmode="linear",
            gridcolor="lightgray",
            griddash="dot",
            tickangle=0,
            dtick=2
        ),
        yaxis=dict(
            title="Anzahl",
            showgrid=True,
            gridcolor="lightgray",
            griddash="dot",
            tickformat=",d",
            range=[0, range]
        ),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        # plot_bgcolor="#111111",  # dunkler Hintergrund für Streamlit
        # paper_bgcolor="#111111", 
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True, key=key)