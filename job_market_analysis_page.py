import warnings #Nicht entfernen (frag' nicht warum)
import sys #Selbe Story
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from amir_ml import arbeitslos_ml
from amir_module import arbeitslos, ausbildung

jahre = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 ]

import streamlit as st

col1, col2 = st.columns([1, 3])

with col1:
    st.image(r"amir_images/arbeit.jpg", width=200)

with col2:
    # st.title("Arbeitsmarktanalyse in Deutschland")
    st.markdown(
    """
    <style>
    .custom-title {
        font-size: 38px;
        font-weight: bold;
        color: #000;
        margin-top: 2em;
    }
    </style>
    <div class="custom-title">Arbeitsmarktanalyse in Deutschland</div>
    """,
    unsafe_allow_html=True
)

# Lädt Daten in session state und dann in Variable
@st.cache_data
def load_data(path):
    df = pd.read_csv(rf"amir_graphs\{path}", delimiter=",")
    return df.sort_values(by="Jahr")

with st.container():
    jahr_min = min(jahre)
    jahr_max = max(jahre)

    selected_range = st.slider(
        "Wähle Zeitraum:",
        min_value=jahr_min,
        max_value=jahr_max,
        value=(jahr_min, jahr_max),  # Standard: kompletter Bereich
        step=1
    )

# Filter für DataFrame
df = pd.DataFrame({"Jahr": jahre})
filtered_df = df[(df["Jahr"] >= selected_range[0]) & (df["Jahr"] <= selected_range[1])]

st.divider()
st.write("📊 Verlauf der Arbeitslosigkeit in Deutschland")

isfill_arbeitslos = st.toggle("Füllung", value=True, key="arbeitslos_fill")

# Selectbox
# col1_graph, col2_graph, col3_graph = st.columns([3,3,3])

# with col2_graph:

#     selected_arbeitslos_25 = st.selectbox(
#         "Wähle Legende aus:",
#         ("Insgesamt", "Jüngere unter 25 Jahre", "Alle anzeigen"),
#         index=1,  # ← „Insgesamt“ ist die Standardauswahl
#         key="selected_arbeitslos_25",
#     )

# with col3_graph:

#     selected_arbeitslos = st.selectbox(
#         "Wähle Legende aus:",
#         ("Insgesamt", "Junge Erwachsene 20-24", "Jugendliche unter 20 Jahre", "Beide Gruppen anzeigen", "Alle anzeigen"),
#         index=3,  # ← „Insgesamt“ ist die Standardauswahl
#         key="selected_arbeitslos"
#     )

# Selectbox

selected_arbeitslos = ["Beide Gruppen anzeigen"]
selected_arbeitslos_25 = ["Jüngere unter 25 Jahre"]

# Erste Zeile
with st.container():
    col1_graph, col2_graph = st.columns([2,2])

    with col1_graph:
        arbeitslos.plot_arbeitslos_total(r"arbeitslos\arbeitslos_insgesamt.csv", "Insgesamt", filtered_df, "arbeitslos_total")

        if st.toggle("Werte anzeigen", key ="toggle_arbeitslos_total"):
            st.dataframe(load_data(r"arbeitslos\arbeitslos_insgesamt.csv"))

    with col2_graph:

        if not isfill_arbeitslos:
            arbeitslos.plot_arbeitslos_group(r"arbeitslos\arbeitslos_nach altersgruppen.csv", "Nach Altersgruppen", filtered_df, "arbeitslos_agegroups", False, selected_arbeitslos)
        else:
            arbeitslos.plot_arbeitslos_group(r"arbeitslos\arbeitslos_nach altersgruppen.csv", "Nach Altersgruppen", filtered_df, "arbeitslos_agegroups", True, selected_arbeitslos)

        if st.toggle("Werte anzeigen", key ="toggle_arbeitslos_agegroups"):
            st.dataframe(load_data(r"arbeitslos\arbeitslos_nach altersgruppen.csv"))

# Zweite Zeile
with st.container():
    col1_graph, col2_graph, col3_graph = st.columns([1,2,1])


    # with col1_graph:

    #     if not isfill_arbeitslos:
    #         arbeitslos.plot_arbeitslos_group_25(r"arbeitslos\arbeitslos_nach_altersgruppen_unter_25.csv", "Nach Altersgruppen unter 25", filtered_df, "arbeitslos_agegroupsunder25", False, selected_arbeitslos_25)
    #     else:
    #         arbeitslos.plot_arbeitslos_group_25(r"arbeitslos\arbeitslos_nach_altersgruppen_unter_25.csv", "Nach Altersgruppen unter 25", filtered_df, "arbeitslos_agegroupsunder25", True, selected_arbeitslos_25)

    #     if st.toggle("Werte anzeigen", key ="toggle_arbeitslos_agegroupsunder25"):
    #         st.dataframe(load_data(r"arbeitslos\arbeitslos_nach_altersgruppen_unter_25.csv"))

 

st.divider()
st.write("📊 Verlauf des deutschen Ausbildungsmarkts")

isfill_ausbildung = st.toggle("Füllung", value=False, key="isfill_ausbildung")

col1_graph, col2_graph, col3_graph = st.columns([3,3,3])

with col2_graph:

    selected_ausbildung = st.radio(
        "Wähle Legende aus:",
        ("Neu abgeschlossene Ausbildungsverträge (Insgesamt)", "Unbesetzte Ausbildungsplätze", "Alle anzeigen"),
        index=2  # ← „Insgesamt“ ist die Standardauswahl
    )

# Dritte Zeile
with st.container():
    col1_graph, col2_graph, col3_graph = st.columns([3,3,3])

with col1_graph:
    ausbildung.plot_ausbildung_total(r"ausbildung\Auszubildende.csv", "Auszubildende am Jahresende", filtered_df, "ausbildung_total")

    if st.toggle("Werte anzeigen", key ="toggle_ausbildung_total"):
        st.dataframe(load_data(r"ausbildung\Auszubildende.csv"))
        
        wert_2010 = 1508328
        wert_2011 = 1460658
        veraenderung_abs = wert_2011 - wert_2010
        veraenderung_rel = round((veraenderung_abs / wert_2010) * 100, 1)

        st.markdown(f"""
        Wie viel hat sich verändert?  
        Veränderung abs.: 2011 [<span style='font-size:14px; color:white; background-color:#082308; padding:2px 6px; border-radius:3px; font-weight:bold;'>{wert_2011}</span>] − 2010 [<span style='font-size:14px; color:white; background-color:#082308; padding:2px 6px; border-radius:3px; font-weight:bold;'>{wert_2010}</span>] = <span style='font-size:14px; color:white; background-color:#082308; padding:2px 6px; border-radius:3px; font-weight:bold;'>{veraenderung_abs}</span>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        Wie hoch war die Veränderung in Prozent?  
        Veränderung rel. (%): (2011 [<span style='font-size:14px; color:white; background-color:#082308; padding:2px 6px; border-radius:3px; font-weight:bold;'>{wert_2011}</span>] − 2010 [<span style='font-size:14px; color:white; background-color:#082308; padding:2px 6px; border-radius:3px; font-weight:bold;'>{wert_2010}</span>]) / 2010 [<span style='font-size:14px; color:white; background-color:#082308; padding:2px 6px; border-radius:3px; font-weight:bold;'>{wert_2010}</span>] × 100 = <span style='font-size:14px; color:white; background-color:#082308; padding:2px 6px; border-radius:3px; font-weight:bold;'>{veraenderung_rel}%</span>
        """, unsafe_allow_html=True)

with col2_graph:

    if not isfill_ausbildung:
        ausbildung.plot_ausbildung_group_contracts_positions(r"ausbildung\Insgesamt_und_Ausbildungsstellenangebot.csv", "Vergleich unbesetzter Ausbildungsplätze", filtered_df, "ausbildung_contracts_positions", False, selected_ausbildung)
    else:
        ausbildung.plot_ausbildung_group_contracts_positions(r"ausbildung\Insgesamt_und_Ausbildungsstellenangebot.csv", "Vergleich unbesetzter Ausbildungsplätze", filtered_df, "ausbildung_contracts_positions", True, selected_ausbildung)

    if st.toggle("Werte anzeigen", key ="toggle_ausbildung_contracts_positions"):
        st.dataframe(load_data(r"ausbildung\Insgesamt_und_Ausbildungsstellenangebot.csv"))

with col3_graph:

    if not isfill_ausbildung:
        ausbildung.plot_ausbildung_group_contracts(r"ausbildung\Ausbildungsnachfrage_und_Ausbildungsstellenangebot.csv", "Zusammenspiel von Ausbildungsangebot und -nachfrage", filtered_df, "ausbildung_contracts", False)
    else:
        ausbildung.plot_ausbildung_group_contracts(r"ausbildung\Ausbildungsnachfrage_und_Ausbildungsstellenangebot.csv", "Zusammenspiel von Ausbildungsangebot und -nachfrage", filtered_df, "ausbildung_contracts", True)

    if st.toggle("Werte anzeigen", key ="toggle_ausbildung_contracts"):
        st.dataframe(load_data(r"ausbildung\Ausbildungsnachfrage_und_Ausbildungsstellenangebot.csv"))


st.divider()
st.write("📊 Prognose der Arbeitslosigkeit 2025 in Deutschland mit Machine Learning [2010 - 2025]")

with st.container():
    col1, col2 = st.columns([2,2])

    with col1:
        # st.subheader("Originalewerte Januar-September 2025")
        st.markdown("<span style='font-size:15px'>Originalewerte Januar–September 2025</span>", unsafe_allow_html=True)
        # st.markdown("<br>", unsafe_allow_html=True)
        df_arbeitslos_ml = arbeitslos_ml.load_data()
        df_filtered = df_arbeitslos_ml[df_arbeitslos_ml["Jahr"] >= 2025]
        st.dataframe(df_filtered)

    with col2:
        ml_modelle = arbeitslos_ml.ml_modelle()
        st.dataframe(ml_modelle[0])

st.divider()

with st.container():
    col1_graph, col2_graph = st.columns([2,2])  

    with col1_graph:
        arbeitslos_ml.plot_arbeitslos_total(arbeitslos_ml.load_data())

    with col2_graph:
        arbeitslos_ml.plot_prognose(ml_modelle[1])