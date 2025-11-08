import warnings #Nicht entfernen (frag' nicht warum)
import sys #Selbe Story
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


@st.cache_data
def plot_ausbildung_total(path, title, selected_groups, key):
    ausbildung = pd.read_csv(rf"amir_graphs\{path}", delimiter=",")

    ausbildung = ausbildung[ausbildung["Jahr"].isin(selected_groups['Jahr'])]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=ausbildung["Jahr"], y=ausbildung["Auszubildende"],
        mode="lines+markers", name="Auszubildende",
        showlegend=True,
        line=dict(color="#E66C37", width=3),
        marker=dict(size=8),
        hovertemplate="<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
))

    fig.update_layout(
        title=f"{title}",
        xaxis=dict(title="Jahr", showgrid=True, tickmode="linear", dtick=2, range=[2010, 2022], gridcolor="lightgray", griddash="dot", tickangle=0),
        yaxis=dict(title="Anzahl", showgrid=True, gridcolor="lightgray", griddash="dot", tickformat=",d", range=[0, 1700000], dtick=250000),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        legend_itemclick=False,
        legend_itemdoubleclick=False
    )

    st.plotly_chart(fig, use_container_width=True, key=key)

@st.cache_data
def plot_ausbildung_group_contracts(path, title, selected_groups, key, show_fill=True):
    ausbildung = pd.read_csv(rf"amir_graphs\{path}", delimiter=",")
    ausbildung = ausbildung[ausbildung["Jahr"].isin(selected_groups['Jahr'])]

    fig = go.Figure()

    # Trace 1: Nachfrage
    trace1_args = {
        "x": ausbildung["Jahr"],
        "y": ausbildung["Ausbildungsplatznachfrage"],
        "mode": "lines+markers",
        "name": "Ausbildungsplatznachfrage",
        "line": dict(color="#0988FF", width=2),
        "marker": dict(size=6),
        "hovertemplate": "<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
    }
    if show_fill:
        trace1_args["fill"] = "tozeroy"
        trace1_args["fillcolor"] = "rgba(128, 128, 128, 0.1)"
    fig.add_trace(go.Scatter(**trace1_args))

    # Trace 2: Angebot
    trace2_args = {
        "x": ausbildung["Jahr"],
        "y": ausbildung["Ausbildungsplatzangebot"],
        "mode": "lines+markers",
        "name": "Ausbildungsplatzangebot",
        "line": dict(color="#D64550", width=3),
        "marker": dict(size=8),
        "hovertemplate": "<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
    }
    if show_fill:
        trace2_args["fill"] = "tozeroy"
        trace2_args["fillcolor"] = "rgba(211, 211, 211, 0.2)"
    fig.add_trace(go.Scatter(**trace2_args))

    fig.update_layout(
        title=f"{title}",
        xaxis=dict(title="Jahr", showgrid=True, tickmode="linear", dtick=2, range=[2010, 2022], gridcolor="lightgray", griddash="dot", tickangle=0),
        yaxis=dict(title="Anzahl", showgrid=True, gridcolor="lightgray", griddash="dot", tickformat=",d", range=[0, 7000000], dtick=1000000),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        legend_itemclick=False,
        legend_itemdoubleclick=False
    )

    st.plotly_chart(fig, use_container_width=True, key=key)


@st.cache_data
def plot_ausbildung_group_contracts_positions(path, title, selected_groups, key, show_fill, selected_ausbildung):
    ausbildung = pd.read_csv(rf"amir_graphs\{path}", delimiter=",")
    ausbildung = ausbildung[ausbildung["Jahr"].isin(selected_groups['Jahr'])]

    fig = go.Figure()

    # Sichtbarkeit vorab definieren
    trace1_visible = True
    trace2_visible = True

    if "Neu abgeschlossene Ausbildungsverträge (Insgesamt)" in selected_ausbildung and "Unbesetzte Ausbildungsplätze" not in selected_ausbildung:
        trace1_visible = "legendonly"
    elif "Unbesetzte Ausbildungsplätze" in selected_ausbildung and "Neu abgeschlossene Ausbildungsverträge (Insgesamt)" not in selected_ausbildung:
        trace2_visible = "legendonly"

    # Trace 1: Unbesetzte Ausbildungsplätze
    trace1 = {
        "x": ausbildung["Jahr"],
        "y": ausbildung["Unbesetzte Ausbildungsplätze"],
        "mode": "lines+markers",
        "name": "Unbesetzte Ausbildungsplätze",
        "visible": trace1_visible,
        "line": dict(color="#23B15A", width=2),
        "marker": dict(size=6),
        "hovertemplate": "<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
    }
    if show_fill:
        trace1["fill"] = "tozeroy"
        trace1["fillcolor"] = "rgba(128, 128, 128, 0.4)"

    fig.add_trace(go.Scatter(**trace1))

    # Trace 2: Insgesamt
    trace2 = {
        "x": ausbildung["Jahr"],
        "y": ausbildung["Insgesamt"],
        "mode": "lines+markers",
        "name": "Insgesamt",
        "visible": trace2_visible,
        "line": dict(color="#DE6A73", width=3),
        "marker": dict(size=8),
        "hovertemplate": "<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
    }
    if show_fill:
        trace2["fill"] = "tozeroy"
        trace2["fillcolor"] = "rgba(128, 128, 128, 0.1)"

    fig.add_trace(go.Scatter(**trace2))

    fig.update_layout(
        title=f"{title}",
        xaxis=dict(title="Jahr", showgrid=True, tickmode="linear", dtick=2, range=[2010, 2022], gridcolor="lightgray", griddash="dot", tickangle=0),
        yaxis=dict(title="Anzahl", showgrid=True, gridcolor="lightgray", griddash="dot", tickformat=",d", range=[0, 6500000], dtick=1000000),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        # legend_itemclick=False,
        # legend_itemdoubleclick=False
    )

    st.plotly_chart(fig, use_container_width=True, key=key)