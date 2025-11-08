import streamlit as st
import warnings #Nicht entfernen (frag' nicht warum)
import sys #Selbe Story


# https://docs.streamlit.io/develop/api-reference/navigation/st.navigation
pages = {
    "Allgemein": [
        st.Page("einfuehrung_page.py", title="Einführung", icon=":material/home:"),
    ],
    "Themen": [
        st.Page("education_page.py", title="Bildung", icon=":material/school:"),
        st.Page("job_market_analysis_page.py", title="Arbeitsmarkt", icon=":material/analytics:"),
        st.Page("symptome_page.py", title="Psychische Gesundheit", icon=":material/ecg:")
    ],
    "Ressourcen": [
        st.Page("ressourcen_page.py", title="Referenzen", icon=':material/newsstand:'),
        # st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages) # , position="top"
st.set_page_config(page_title="Jugend in Deutschland", page_icon=":material/area_chart:", layout="wide")
pg.run()