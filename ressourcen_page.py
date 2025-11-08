import warnings #Nicht entfernen (frag' nicht warum)
import sys #Selbe Story
import streamlit as st

st.markdown(
    """
    <style>
    .custom-title {
        font-size: 58px;
        font-weight: bold;
        color: #000;
        text-align: center;
    }
    </style>
    <div class="custom-title">Quellen</div>
    """,
    unsafe_allow_html=True
)

st.divider()


st.markdown("## Amtliche Statistikinstitute")
st.markdown("""
- [Bildungsmonitoring – bildungsmonitoring.de](https://www.bildungsmonitoring.de/bildung/online/)
- [Datenportal des BMBF – datenportal.bmbf.de](http://www.datenportal.bmbf.de/)
- [BIBB Datenreport – bibb.de](http://www.bibb.de/datenreport/de/aktuell.php)
- [Regionalstatistik – regionalstatistik.de](https://www.regionalstatistik.de/genesis/online/)
- [Zensus 2022 Ergebnisse – zensus2022.de](https://ergebnisse.zensus2022.de/datenbank/online/)
- [GENESIS Online – destatis.de](https://www-genesis.destatis.de/datenbank/online/statistics) 
- [RKI Mental Health Surveillance – rki.de](https://www.rki.de/EN/Topics/Noncommunicable-diseases/Health-surveys/Studies/mental-health-surveillance.html)         
""")

st.markdown("## Bildnachweise")
st.markdown("""
- [The Importance of Mental Health
 – miamihighnews.com](https://miamihighnews.com/2022/12/16/the-importance-of-mental-health/)
- [Bildung für Zuwanderer aus Drittstaaten – bamf.de](https://www.bamf.de/DE/Themen/MigrationAufenthalt/ZuwandererDrittstaaten/Bildung/bildung-node.html)
- [Workspace Icon – vecteezy.com](https://www.vecteezy.com/vector-art/356782-workspace-vector-icon)
""")

st.markdown("## Gitlab & GitHub")
st.markdown("""
- [GitLab: Hochfrequente Mental Health Surveillance – opencode.de](https://gitlab.opencode.de/robert-koch-institut/Hochfrequente_Mental_Health_Surveillance)
- [GitHub: Hochfrequente Mental Health Surveillance – github.com](https://github.com/robert-koch-institut/Hochfrequente_Mental_Health_Surveillance)

""")