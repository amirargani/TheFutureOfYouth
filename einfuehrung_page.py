import warnings #Nicht entfernen (frag' nicht warum)
import sys #Selbe Story
import streamlit as st

st.markdown(
    """
    <style>
    .custom-title {
        font-size: 28px;
        font-weight: bold;
        color: #000;
        text-align: center;
    }
    </style>
    <div class="custom-title">Die Zukunft der Jugend: Trends in Bildung, Beschäftigung und mentaler Gesundheit</div>
    """,
    unsafe_allow_html=True
)

st.divider()

auswahl = st.radio("", ["These", "Analyse", "Anmerkung"], key='select_key')

if auswahl == "These":
    st.markdown("""
        ##### **Die mentale Gesundheit der jungen Generation gilt als besonders anfällig und wandelbar, zugleich entscheidet ihr Bildungsniveau maßgeblich über ihre beruflichen Zukunftschancen.**  
        """)

elif auswahl == "Analyse":
    methodik_tab, kriterien_tab = st.tabs(["Methodik", "Kriterien"])
    with methodik_tab:
        st.markdown("""
    #### **Datengrundlage:**  
    ##### – Amtliche Statistikinstitute (s. Referenzen)
                    
    #### **Zeitraum:**  
    ##### – Ab 2009
    """)
        
    with kriterien_tab:
        st.markdown("""
    ## Kriterien

    ##### - **Altersgruppe:** Jugendliche und junge Erwachsene im Alter von 15 bis 25 Jahren  
    ##### - **Schulart, Abschlussart, Geschlecht**


    """)

elif auswahl == "Anmerkung":
        st.markdown("""
    #### **Bildung:**  
    ##### – Fachhochschule mit nur schulischem Anteil = Mittlerer Schulabschluss
    ##### – Abgänger: Schülerinnen und Schüler, die die Schule verlassen – unabhängig davon, ob sie einen Abschluss erworben haben.
    ##### – Absolventen: Abgängerinnen und Abgänger, die einen Abschluss erfolgreich erreicht haben.
    """)