import streamlit as st
import pandas as pd
from buesra_module import overview, allgemeinbild_abschluesse_geschlecht, allgemeinbild_ohne_abschluss, berufsbild_abschluesse_geschlecht, studium

# Lädt Daten in session state und dann in Variable
@st.cache_data
def load_data(path):
    df = pd.read_csv(f"{path}", delimiter=",")
    return df
    #return df.sort_values(by="Zeit")

col1, col2 = st.columns([1, 3])

with col1:
    st.image(r"buesra_images\bildung.png", width=300)

with col2:
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
    <div class="custom-title">Betrachtung der Bildungssituation von Jugendlichen</div>
    """,
    unsafe_allow_html=True
)

# with st.container():
# # 🎚️ Multiselect dropdown outside functions
#     selected_groups = st.multiselect(
#     "Wähle Altersgruppen aus:",
#     options=altersgruppe,
#     default=altersgruppe
# )strea
# Unterseiten-Auswahl

subpage = st.radio("", ["Übersicht", "Allgemeinbildende Schulen - Abschlüsse nach Geschlecht", "Allgemeinbildende Schulen - G8/G9 Ohne Abschluss","Allgemeinbildende Schulen - Ohne Abschluss","Berufsbildende Schulen - Schulabschlüsse nach Geschlecht" ,"Studium"])

if subpage == "Übersicht":
    st.subheader("Übersicht")
    
    with st.container():
        col1, col2 = st.columns([2,2])

        with col1:

            st.markdown(
        """
        <h3 style='text-align: center; color: #000; margin-bottom: 20px;'>
            Berufsbildende Schulen 
        </h3>
        <h5 style='text-align: center; color: #000; margin-bottom: 20px;'>
            Schuljahr 2022/23
        </h5>
        <div style='font-size: 16px; color: #000; text-align: center;'>
            <div style='display: flex; justify-content: space-between; width: 400px; margin: 0 auto 10px auto;'>
                <span><strong>Absolventen insgesamt:</strong></span>
                <span>{}</span>
            </div>
            <div style='display: flex; justify-content: space-between; width: 400px; margin: 0 auto 10px auto;'>
                <span><strong>Fachhochschulreife (weiblich):</strong></span>
                <span>{}</span>
            </div>
            <div style='display: flex; justify-content: space-between; width: 400px; margin: 0 auto 10px auto;'>
                <span><strong>Fachhochschulreife (männlich):</strong></span>
                <span>{}</span>
            </div>
            <div style='display: flex; justify-content: space-between; width: 400px; margin: 0 auto 10px auto;'>
                <span><strong>Andere Abschlüsse:</strong></span>
                <span>150394</span>
            </div>
        </div>
        """.format(
            overview.abgaenger_beruflich_gesamt(),
            overview.berufsb_absolventin_fachhochschulreife(),
            overview.berufsb_absolvent_fachhochschulreife()
        ),
        unsafe_allow_html=True
    )

            
        with col2:
                        st.markdown(
        """
        <h3 style='text-align: center; color: #000; margin-bottom: 20px;'>
            Allgemeinbildende Schulen
        </h3>
        <h5 style='text-align: center; color: #000; margin-bottom: 20px;'>
            Schuljahr 2022/23
        </h5>
        <div style='font-size: 16px; color: #000; text-align: center;'>
            <div style='display: flex; justify-content: space-between; width: 400px; margin: 0 auto 10px auto;'>
                <span><strong>AbgängerInnen insgesamt:</strong></span>
                <span>{}</span>
            </div>
            <div style='display: flex; justify-content: space-between; width: 400px; margin: 0 auto 10px auto;'>
                <span><strong>Allgemeine Hochschulreife (weiblich):</strong></span>
                <span>{}</span>
            </div>
            <div style='display: flex; justify-content: space-between; width: 400px; margin: 0 auto 10px auto;'>
                <span><strong>Allgemeine Hochschulreife (männlich):</strong></span>
                <span>{}</span>
            </div>
            <div style='display: flex; justify-content: space-between; width: 400px; margin: 0 auto 10px auto;'>
                <span><strong>Ohne Abschluss insgesamt:</strong></span>
                <span>{}</span>
            </div>
            <div style='display: flex; justify-content: space-between; width: 400px; margin: 0 auto 10px auto;'>
                <span><strong>Andere Abschlüsse:</strong></span>
                <span>467485</span>
            </div>
        </div>
        """.format(
            overview.allgemein_insgesamt(),
            overview.allg_hochschulreife_weiblich(),
            overview.allg_hochschulreife_man(),
            overview.abgaenger_ohne_abschluss()
        ),
        unsafe_allow_html=True
    )
            

#             st.markdown(
#     """
#     <h3 style='text-align: center; color: #000; margin-bottom: 20px;'>
#         Allgemeinbildende Schulen 
#     </h3>
#     <h5 style='text-align: center; color: #000; margin-bottom: 20px;'>
#         Schuljahr 2022/23
#     </h5>
#     """,
#     unsafe_allow_html=True
# )

#             st.markdown(
#     f"""
#     <div style='font-size: 16px; color: #000;'>
#         <div style='display: flex; justify-content: space-between; width: 400px; margin-bottom: 10px;'>
#             <span><strong>AbgängerInnen insgesamt:</strong></span>
#             <span>{overview.allgemein_insgesamt()}</span>
#         </div>
#         <div style='display: flex; justify-content: space-between; width: 400px; margin-bottom: 10px;'>
#             <span><strong>Allgemeine Hochschulreife (weiblich):</strong></span>
#             <span>{overview.allg_hochschulreife_weiblich()}</span>
#         </div>
#         <div style='display: flex; justify-content: space-between; width: 400px; margin-bottom: 10px;'>
#             <span><strong>Allgemeine Hochschulreife (männlich):</strong></span>
#             <span>{overview.allg_hochschulreife_man()}</span>
#         </div>
#         <div style='display: flex; justify-content: space-between; width: 400px; margin-bottom: 10px;'>
#             <span><strong>Ohne Abschluss insgesamt:</strong></span>
#             <span>{overview.abgaenger_ohne_abschluss()}</span>
#         </div>
#         <div style='display: flex; justify-content: space-between; width: 400px; margin-bottom: 10px;'>
#             <span><strong>Andere Abschlüsse:</strong></span>
#             <span>467485</span>
#         </div>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

    with st.container():
        col1_graph, col2_graph = st.columns([2,2])
        with col1_graph:
            overview.overview("Abgänger und Absolventen an BerusbildendenSchulen.csv","Berufsbildende Schulen","#B43B07","berufliche overview")
            if st.toggle("Werte anzeigen", key = "Toggle Overview 1"):
                st.dataframe(load_data(r"buesra_graphs\1_Uebersicht\Abgänger und Absolventen an BerusbildendenSchulen.csv"))

        with col2_graph:
            overview.overview("Abgänger und Absolventen an Allgemeinbildende Schulen.csv", "Allgemeinbildende Schulen", "#1ABC9C","allgemeinbildende overview")
            if st.toggle("Werte anzeigen", key = "Toggle Overview 2"):
                st.dataframe(load_data(r"buesra_graphs\1_Uebersicht\Abgänger und Absolventen an Allgemeinbildende Schulen.csv"))

elif subpage == "Allgemeinbildende Schulen - Abschlüsse nach Geschlecht":
    st.subheader("Allgemeinbildende Schulen - Abschlüsse nach Geschlecht")
    # Inhalte für Bildungsniveau

    st.markdown(
    "<span style='color: #000; margin-right: 15px; font-size: 16px;'>Legende: </span> "
    "<span style='color: #96B3A1; margin-right: 15px; font-size: 16px;'>Männlich</span> "
    "<span style='color: #DE6A73; margin-right: 15px; font-size: 16px;'>Weiblich</span>",
    unsafe_allow_html=True
)
    with st.container():
        col1_graph, col2_graph = st.columns([2,2])
        with col1_graph:
           allgemeinbild_abschluesse_geschlecht.allgemeinbild_abschluss("Allgemeine Hochschulreife.csv","Allgemeine Hochschulreife","allgemeine_hochschulreife")
           if st.toggle("Werte anzeigen", key = "Toggle Allgemeinbildende Allgemeine Hochschulreife"):
                st.dataframe(load_data(r"buesra_graphs\2_Allgemeinbildende Schulen _Abschlüsse Geschlecht\Allgemeine Hochschulreife.csv"))

        with col2_graph:
            allgemeinbild_abschluesse_geschlecht.allgemeinbild_abschluss("Mittlerer Schulabschluss.csv", "Mittler Schulabschluss", "mittlerer_abschluss")
            if st.toggle("Werte anzeigen", key = "Toggle Allgemeinbildende Mitllerer Abschluss"):
                st.dataframe(load_data(r"buesra_graphs\2_Allgemeinbildende Schulen _Abschlüsse Geschlecht\Mittlerer Schulabschluss.csv"))

    with st.container():
        col3_graph, col4_graph = st.columns([2,2])
        with col3_graph:
            allgemeinbild_abschluesse_geschlecht.allgemeinbild_abschluss("Erster Abschluss.csv", "Erster Schulabschluss", "erster_abschluss")
            if st.toggle("Werte anzeigen", key = "Toggle Allgemeinbildende Erster Abschluss"):
                st.dataframe(load_data(r"buesra_graphs\2_Allgemeinbildende Schulen _Abschlüsse Geschlecht\Erster Abschluss.csv"))

        with col4_graph:
            allgemeinbild_abschluesse_geschlecht.allgemeinbild_abschluss("Ohne Abschluss.csv", "Ohne Schulabschluss", "ohne_abschluss")
            if st.toggle("Werte anzeigen", key = "Toggle Allgemeinbildende Ohne Abschluss"):
                st.dataframe(load_data(r"buesra_graphs\2_Allgemeinbildende Schulen _Abschlüsse Geschlecht\Ohne Abschluss.csv"))

elif subpage == "Allgemeinbildende Schulen - G8/G9 Ohne Abschluss":
    st.subheader("Allgemeinbildende Schulen - G8/G9 Ohne Abschluss")

    with st.container():
        col1_graph, col2_graph = st.columns([2,2])
        with col1_graph:
           allgemeinbild_ohne_abschluss.ohne_abschluss("Gymnasium (G9).csv", "Gymnasium (G9)","#70BBFF",  1800,  "gymnasium_g9")
           if st.toggle("Werte anzeigen", key = "Toggle Ohne Abschluss Gymnasoum (G9)"):
                st.dataframe(load_data(r"buesra_graphs\3_Allgemeinbildende Schulen - Ohne Abschluss\Gymnasium (G9).csv"))

        with col2_graph:
            allgemeinbild_ohne_abschluss.ohne_abschluss("Gymnasium (G8).csv", "Gymnasium (G8)", "#0E1A77", 1800,  "gymnasium_g8")
            if st.toggle("Werte anzeigen",key = "Toggle Ohne Abschluss Gymnasium (G8)"):
                st.dataframe(load_data(r"buesra_graphs\3_Allgemeinbildende Schulen - Ohne Abschluss\Gymnasium (G8).csv"))
        
elif subpage == "Allgemeinbildende Schulen - Ohne Abschluss":
    st.subheader("Allgemeinbildende Schulen - Ohne Abschluss")

    with st.container():
        col3_graph, col4_graph = st.columns([2,2])
        with col3_graph:
            allgemeinbild_ohne_abschluss.ohne_abschluss("Realschulen.csv","Realschule","#094780", 14000, "realschulen")
            if st.toggle("Werte anzeigen", key = "Toggle Ohne Abschluss Realschule"):
                st.dataframe(load_data(r"buesra_graphs\3_Allgemeinbildende Schulen - Ohne Abschluss\Realschulen.csv"))

        with col4_graph:
            allgemeinbild_ohne_abschluss.ohne_abschluss("Hauptschulen.csv", "Hauptschule", "#0D6ABF", 14000, "hauptschulen")
            if st.toggle("Werte anzeigen", key = "Toggle Ohne Abschluss Hauptschule"):
                st.dataframe(load_data(r"buesra_graphs\3_Allgemeinbildende Schulen - Ohne Abschluss\Hauptschulen.csv"))

    with st.container():
        col5_graph, col6_graph, col7_graph = st.columns([1,2,1])
        with col6_graph:
           allgemeinbild_ohne_abschluss.ohne_abschluss("Schularten mit drei Bildungsgängen.csv", "Schulart mit drei Bildungsgängen (z. B. Gesamtschulen, Oberschulen, Sekundarschulen, …)", "#41A4FF", 14000, "drei_bildungsgaengen")
           if st.toggle("Werte anzeigen", key = "Toggle Ohne Abschluss Drei Bilgungsgänge"):
                st.dataframe(load_data(r"buesra_graphs\3_Allgemeinbildende Schulen - Ohne Abschluss\Schularten mit drei Bildungsgängen.csv"))



    # Inhalte für Zugang zu Bildung

elif subpage == "Berufsbildende Schulen - Schulabschlüsse nach Geschlecht":
    st.subheader("Berufsbildende Schulen - Schulabschlüsse nach Geschlecht")
    # Inhalte für Zugang zu Bildung
    abschlussart = ["Fachhochschulreife", "Hauptschulabschluss", "Hochschulreife", "Mittlerer Schulabschluss"]

    # 🎚️ Multiselect dropdown outside functions
    selected_groups = st.multiselect(
    "Wähle Abschlussart aus:",
    options=abschlussart,
    default=abschlussart, 
    key = "abschlussart"
)

    st.markdown(
    "<span style='color: #000; margin-right: 15px; font-size: 16px;'>Legende: </span> "
    "<span style='color: #E30620; margin-right: 15px; font-size: 16px;'>Fachhochschulreife</span> "
    "<span style='color: #A38600; margin-right: 15px; font-size: 16px;'>Hauptschulabschluss</span>"
    "<span style='color: #249532; margin-right: 15px; font-size: 16px;'>Hochschulreife</span>"
    "<span style='color: #118DFF; margin-right: 15px; font-size: 16px;'>Mittlerer Schulabschluss</span>",
    unsafe_allow_html=True
)

    with st.container():
        col1_graph, col2_graph = st.columns([2,2])

        # Männlich
        with col1_graph:
            berufsbild_abschluesse_geschlecht.beruliche_absolventen("Absolventen an beruflichen Schulen.csv", "Absolventen", selected_groups, "absolvent_männlich")
            if st.toggle("Werte anzeigen", key = "Toggle Berufsbildende Absolvent"):
                st.dataframe(load_data(r"buesra_graphs\4_Berufsbildende Schulen - Schulabschlüsse (Geschlecht)\Absolventen an beruflichen Schulen.csv"))

        with col2_graph:
            berufsbild_abschluesse_geschlecht.beruliche_absolventen("Absolventinnen an beruflichen Schulen.csv", "Absolventinnen", selected_groups, "absolvent_weiblich")
            if st.toggle("Werte anzeigen", key = "Toggle Berufsbildende Absolventin"):
                st.dataframe(load_data(r"buesra_graphs\4_Berufsbildende Schulen - Schulabschlüsse (Geschlecht)\Absolventinnen an beruflichen Schulen.csv"))

elif subpage == "Studium":
    st.subheader("Studium")
    # Inhalte für Zugang zu Bildung
    with st.container():
        col1_graph, col2_graph = st.columns([2,2])
        with col1_graph:
            studium.allgemeinbild_hochschulreife()
            if st.toggle("Werte anzeigen", key = "Toggle Studium 1"):
                st.dataframe(load_data(r"buesra_graphs\5_Studium\Allgemeinbildende Schulen.csv"))

        with col2_graph:
            studium.berufsbild_hoehere_abschluesse()
            if st.toggle("Werte anzeigen", key = "Toggle Studium 2"):
                st.dataframe(load_data(r"buesra_graphs\5_Studium\Berufsbilden Schulen.csv"))

    
    with st.container():
        isfill_studium = True

        if not st.toggle("Füllung", key="studium"):
            isfill_studium = False

        col3_graph, col4_graph = st.columns([2,2])
        with col3_graph:
            if not isfill_studium:
                studium.studium("Studierende.csv","Studierende", 3000000, "studierende", False)
            else: 
                studium.studium("Studierende.csv","Studierende", 3000000, "studierende")
            
            if st.toggle("Werte anzeigen", key = "Toggle Studium 3"):
                st.dataframe(load_data(r"buesra_graphs\5_Studium\Studierende.csv"))

        with col4_graph:
            if not isfill_studium:
                studium.studium("Studienanfänger.csv","Studienanfänger", 500000, "studienanfaenger", False)
            else: 
                studium.studium("Studienanfänger.csv","Studienanfänger", 500000, "studienanfaenger")
            
            if st.toggle("Werte anzeigen", key = "Toggle Studium 4"):
                st.dataframe(load_data(r"buesra_graphs\5_Studium\Studienanfänger.csv"))

