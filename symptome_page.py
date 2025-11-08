import warnings #Nicht entfernen (frag' nicht warum)
import sys #Selbe Story
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from mila_module import symptome

altersgruppe =["18-29", "30-44", "45-64", "65+"]
# jahre = [2019, 2020, 2021, 2022, 2023, 2024]


col1, col2 = st.columns([1, 3])

with col1:
    st.image(r"mila_images\mh.png", width=200)

with col2:
    # st.title("Beobachtung der psychischen Gesundheit in Deutschland")
    st.markdown(
    """
    <style>
    .custom-title-home {
        font-size: 38px;
        font-weight: bold;
        color: #000;
        margin-top: 2em;
    }
    </style>
    <div class="custom-title-home">Beobachtung der psychischen Gesundheit in Deutschland</div>
    """,
    unsafe_allow_html=True
)


# Lädt Daten in session state und dann in Variable
@st.cache_data
def load_data(path):
    df = pd.read_csv(rf"mila_graphs\{path}", delimiter=",")
    return df.sort_values(by="Jahr")

@st.cache_data
def load_data2():
    # Try utf-8-sig first, fallback to latin1 if needed
    try:
        return pd.read_csv(r"mila_graphs\RKI_Data_2024.csv", delimiter=";", encoding="utf-8-sig")
    except UnicodeDecodeError:
        return pd.read_csv(r"mila_graphs\RKI_Data_2024.csv", delimiter=";", encoding="latin1")

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .custom-title {
        font-size: 28px;
        font-weight: bold;
        color: #000;
    }
    </style>
    <div class="custom-title">Indikatoren nach Altersgruppen</div>
    """,
    unsafe_allow_html=True
)

with st.container():
    # Session State initialisieren
    if "selected_groups" not in st.session_state:
        st.session_state.selected_groups = altersgruppe

    if "toggle_was_on" not in st.session_state:
        st.session_state.toggle_was_on = False

    # Toggle-Schalter
    alle_anzeigen = st.toggle("Alle Gruppen anzeigen", key="alle_anzeige", value=True)

    if alle_anzeigen:
        selected = altersgruppe
        if not st.session_state.toggle_was_on:
            st.session_state.manual_selection = st.session_state.selected_groups.copy()
            st.session_state.toggle_was_on = True
        st.session_state.selected_groups = altersgruppe

    # Wenn Toggle deaktiviert → manuelle Auswahl wiederherstellen
    else:
        if st.session_state.toggle_was_on:
            st.session_state.selected_groups = st.session_state.manual_selection.copy()
            st.session_state.toggle_was_on = False

        # Multiselect mit gespeicherter Auswahl
        selected = st.multiselect(
            "Wähle Altersgruppen aus:",
            options=altersgruppe,
            default=st.session_state.selected_groups,
            key="gruppe_select"
        )
        st.session_state.selected_groups = selected

        # Wenn nichts ausgewählt
        if selected == []:
            st.session_state.selected_groups = altersgruppe




# 📈 Choose which symptom chart(s) to show
    # chart_option = st.radio(
    # "Welche Grafik möchtest du anzeigen?",
    # ["Angstsymptome", "Depressionssymptome", "Selbsteinschätzung"]
#)

# Erste Zeile
with st.container():
    col1_graph, col2_graph, col3_graph = st.columns([3,3,3])

with col1_graph:
    # 🔄 Dynamically show the selected chart
    # if chart_option == "Angstsymptome":
    #     symptome.angst_symptome (selected_groups)
    symptome.plot_symptome("Angstsymptome nach Altersgruppen.csv", "Angst", 25, selected, "angst")

    if st.toggle("Werte anzeigen", key = "Toggle Angst"):
        st.dataframe(load_data ("Angstsymptome nach Altersgruppen.csv"))

with col2_graph:
    symptome.plot_symptome("Depressionssymptome nach Altersgruppen.csv", "Depression", 25,selected, "depression")

    if st.toggle("Werte anzeigen", key = "Toggle Depression"):
        st.dataframe (load_data("Depressionssymptome nach Altersgruppen.csv"))

with col3_graph:
    symptome.plot_symptome("Selbsteinschätzung nach Altersgruppen.csv", "Selbsteinschätzung", 55, selected, "self_rated")

    if st.toggle("Werte anzeigen", key = "Toggle Selbsteinschätung"):
        st.dataframe (load_data("Selbsteinschätzung nach Altersgruppen.csv"))

st.divider()

with st.container():
    symptome.plot_symptome_18_29()

st.divider()

with st.container():
    st.markdown("""
### Psychische Gesundheitskategorien

| **Kategorie**       | **Frage**                                                                 | **Antwortoptionen & Punktzahlen**                                  |
|---------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------|
| **Selbsteinschätzung** | Wie würden Sie Ihren psychischen Gesundheitszustand im Allgemeinen beschreiben? | ausgezeichnet = 5, sehr gut = 4, gut = 3, weniger gut = 2, schlecht = 1 |
| **Depression**      | Wie oft fühlten Sie sich im Verlauf der letzten 2 Wochen durch die folgenden Beschwerden beeinträchtigt: |                                                                     |
|                     | - Wenig Interesse oder Freude an Ihren Tätigkeiten                        | überhaupt nicht = 0, an einzelnen Tagen = 1, an mehr als der Hälfte der Tage = 2, beinahe jeden Tag = 3 |
|                     | - Niedergeschlagenheit, Schwermut oder Hoffnungslosigkeit                 | überhaupt nicht = 0, an einzelnen Tagen = 1, an mehr als der Hälfte der Tage = 2, beinahe jeden Tag = 3 |
| **Angst**           | Wie oft fühlten Sie sich im Verlauf der letzten 2 Wochen durch die folgenden Beschwerden beeinträchtigt: |                                                                     |
|                     | - Nervosität, Ängstlichkeit oder Anspannung                               | überhaupt nicht = 0, an einzelnen Tagen = 1, an mehr als der Hälfte der Tage = 2, beinahe jeden Tag = 3 |
|                     | - Nicht in der Lage sein, Sorgen zu stoppen oder zu kontrollieren         | überhaupt nicht = 0, an einzelnen Tagen = 1, an mehr als der Hälfte der Tage = 2, beinahe jeden Tag = 3 |
""")