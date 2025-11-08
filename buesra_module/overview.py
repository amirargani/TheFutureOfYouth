import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache_data
def overview(path, title, farbe, key):
    overview = pd.read_csv(rf"buesra_graphs\1_Uebersicht\{path}", delimiter=",")
    
    fig = go.Figure(data=[
    go.Bar(x=overview["Zeit"], y=overview["Anzahl"], marker_color=farbe)
])
    fig.update_layout(
        #title=title,
        xaxis_title="Schuljahr",
        yaxis_title="Anzahl",
        xaxis=dict(title="Schuljahr",tickangle=0, dtick=2),
        yaxis=dict(tickformat=",", range=[0, 1000000]), #für englische Version
        uniformtext_minsize=8,
        uniformtext_mode="hide"
    )
    
    st.plotly_chart(fig, use_container_width=True, key=key)

def abgaenger_beruflich_gesamt():
    abgaenger_berufsb_gesamt = pd.read_csv(rf"buesra_graphs\1_Uebersicht\Abgänger und Absolventen an BerusbildendenSchulen.csv",delimiter=",")
    return abgaenger_berufsb_gesamt[abgaenger_berufsb_gesamt["Zeit"] == "2022/23"].iloc[0].iloc[3]

def berufsb_absolventin_fachhochschulreife():
    absolventin_fachhochschulreife = pd.read_csv(rf"buesra_graphs\4_Berufsbildende Schulen - Schulabschlüsse (Geschlecht)\Absolventinnen an beruflichen Schulen.csv",delimiter=",")
    return absolventin_fachhochschulreife[(absolventin_fachhochschulreife["Zeit"] == "2022/23") & (absolventin_fachhochschulreife['Abschlussart'] == 'Fachhochschulreife')].iloc[0].iloc[3]


def berufsb_absolvent_fachhochschulreife():
    absolvent_fachhochschulreife = pd.read_csv(rf"buesra_graphs\4_Berufsbildende Schulen - Schulabschlüsse (Geschlecht)\Absolventen an beruflichen Schulen.csv",delimiter=",")
    return absolvent_fachhochschulreife[(absolvent_fachhochschulreife["Zeit"] == "2022/23") & (absolvent_fachhochschulreife['Abschlussart'] == 'Fachhochschulreife')].iloc[0].iloc[3]


def allgemein_insgesamt():
    allgemein_insgesamt = pd.read_csv(rf"buesra_graphs\1_Uebersicht\Abgänger und Absolventen an Allgemeinbildende Schulen.csv",delimiter=",")
    return allgemein_insgesamt[allgemein_insgesamt["Zeit"] == "2022/23"].iloc[0].iloc[2]

def allg_hochschulreife_weiblich(): 
    hochschulreife_weiblich = pd.read_csv(rf"buesra_graphs\2_Allgemeinbildende Schulen _Abschlüsse Geschlecht\Allgemeine Hochschulreife.csv",delimiter=",")
    return hochschulreife_weiblich[(hochschulreife_weiblich["Zeit"] == "2022/23") & (hochschulreife_weiblich['Geschlecht'] == 'Weiblich')].iloc[0].iloc[4]

def allg_hochschulreife_man(): 
    hochschulreife_man = pd.read_csv(rf"buesra_graphs\2_Allgemeinbildende Schulen _Abschlüsse Geschlecht\Allgemeine Hochschulreife.csv",delimiter=",")
    return hochschulreife_man[(hochschulreife_man["Zeit"] == "2022/23") & (hochschulreife_man['Geschlecht'] == 'Männlich')].iloc[0].iloc[4]

def abgaenger_ohne_abschluss(): 
    ohne_abschluss = pd.read_csv(rf"buesra_graphs\2_Allgemeinbildende Schulen _Abschlüsse Geschlecht\Ohne Abschluss.csv",delimiter=",")
    return ohne_abschluss[ohne_abschluss["Zeit"] == "2022/23"]['Anzahl'].sum()