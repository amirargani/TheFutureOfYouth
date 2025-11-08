import warnings #Nicht entfernen (frag' nicht warum)
import sys #Selbe Story
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


@st.cache_data
def plot_arbeitslos_total(path, title, filtered_df, key):
    arbeitslos = pd.read_csv(rf"amir_graphs\{path}", delimiter=",")
    arbeitslos = arbeitslos[arbeitslos["Jahr"].isin(filtered_df['Jahr'])]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=arbeitslos["Jahr"], y=arbeitslos["Insgesamt"],
        mode="lines+markers", name="Insgesamt",
        showlegend=True,
        line=dict(color="#E66C37", width=3),
        marker=dict(size=6),
        hovertemplate="<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
))

    fig.update_layout(
        # title=f"📊 {title}",
        xaxis=dict(title="Jahr", showgrid=True, tickmode="linear", dtick=2, range=[2010, 2024], gridcolor="lightgray", griddash="dot",tickangle=0),
        yaxis=dict(title="Anzahl", showgrid=True, gridcolor="lightgray", griddash="dot", tickformat=",d", range=[0, 3300000]),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        # legend=dict(title="Altersgruppen")
        legend_itemclick=False,
        legend_itemdoubleclick=False
    )

    st.plotly_chart(fig, use_container_width=True, key=key)

@st.cache_data
def plot_arbeitslos_group(path, title, filtered_df, key, show_fill, selected_arbeitslos):
    arbeitslos = pd.read_csv(rf"amir_graphs\{path}", delimiter=",")
    arbeitslos = arbeitslos[arbeitslos["Jahr"].isin(filtered_df['Jahr'])]

    fig = go.Figure()
    
    # Sichtbarkeit vorab definieren
    trace1_visible = True
    trace2_visible = True
    trace3_visible = True

    # if "Insgesamt" in selected_arbeitslos and "Junge Erwachsene 20-24" not in selected_arbeitslos and "Jugendliche unter 20 Jahre" not in selected_arbeitslos:
    #     trace1_visible = "legendonly"
    #     trace2_visible = "legendonly"
    # elif "Junge Erwachsene 20-24" in selected_arbeitslos and "Insgesamt" not in selected_arbeitslos and "Jugendliche unter 20 Jahre" not in selected_arbeitslos:
    #     trace2_visible = "legendonly"
    #     trace3_visible = "legendonly"
    # elif "Jugendliche unter 20 Jahre" in selected_arbeitslos and "Insgesamt" not in selected_arbeitslos and "Junge Erwachsene 20-24" not in selected_arbeitslos:
    #     trace1_visible = "legendonly"
    #     trace3_visible = "legendonly"
    # elif "Beide Gruppen anzeigen" in selected_arbeitslos and "Insgesamt" not in selected_arbeitslos:
    #     trace3_visible = "legendonly"

    # Trace 1: Junge Erwachsene 20–24
    trace1_args = {
        "x": arbeitslos["Jahr"],
        "y": arbeitslos["Junge Erwachsene 20-24"],
        "mode": "lines+markers",
        "name": "Junge Erwachsene 20-24",
        "visible": trace1_visible,
        "line": dict(color="#118DFF", width=2),
        "marker": dict(size=6),
        "hovertemplate": "<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
    }
    if show_fill:
        trace1_args["fill"] = "tozeroy"
        trace1_args["fillcolor"] = "rgba(105, 105, 105, 0.4)"
    fig.add_trace(go.Scatter(**trace1_args))

    # Trace 2: Jugendliche unter 20 Jahre
    trace2_args = {
        "x": arbeitslos["Jahr"],
        "y": arbeitslos["Jugendliche unter 20 Jahre"],
        "mode": "lines+markers",
        "name": "Jugendliche unter 20 Jahre",
        "visible": trace2_visible,
        "line": dict(color="#030F51", width=2),
        "marker": dict(size=6),
        "hovertemplate": "<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
    }
    if show_fill:
        trace2_args["fill"] = "tozeroy"
        trace2_args["fillcolor"] = "rgba(211, 211, 211, 0.2)"
    fig.add_trace(go.Scatter(**trace2_args))

    # Trace 3: Insgesamt
    trace3_args = {
        "x": arbeitslos["Jahr"],
        "y": arbeitslos["Insgesamt"],
        "mode": "lines+markers",
        "name": "Insgesamt",
        "visible": trace3_visible,
        "line": dict(color="#E66C37", width=3),
        "marker": dict(size=8),
        "hovertemplate": "<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
    }
    if show_fill:
        trace3_args["fill"] = "tozeroy"
        trace3_args["fillcolor"] = "rgba(128, 128, 128, 0.1)"
    fig.add_trace(go.Scatter(**trace3_args))

    fig.update_layout(
        xaxis=dict(title="Jahr", showgrid=True, tickmode="linear", dtick=2, range=[2010, 2024], gridcolor="lightgray", griddash="dot",tickangle=0),
        yaxis=dict(title="Anzahl", showgrid=True, gridcolor="lightgray", griddash="dot", tickformat=",d"),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        # legend=dict(title="Altersgruppen")
    )

    st.plotly_chart(fig, use_container_width=True, key=key)


@st.cache_data
def plot_arbeitslos_group_25(path, title, filtered_df, key, show_fill, selected_arbeitslos_25):
    arbeitslos = pd.read_csv(rf"amir_graphs\{path}", delimiter=",")
    arbeitslos = arbeitslos[arbeitslos["Jahr"].isin(filtered_df['Jahr'])]

    fig = go.Figure()
    
    # Sichtbarkeit vorab definieren
    trace1_visible = True
    trace2_visible = True

    if "Insgesamt" in selected_arbeitslos_25 and "Jüngere unter 25 Jahre" not in selected_arbeitslos_25:
        trace1_visible = "legendonly"
    elif "Jüngere unter 25 Jahre" in selected_arbeitslos_25 and "Insgesamt" not in selected_arbeitslos_25:
        trace2_visible = "legendonly"

    # Trace 1: Jüngere unter 25 Jahre
    trace1_args = {
        "x": arbeitslos["Jahr"],
        "y": arbeitslos["Jüngere unter 25 Jahre"],
        "mode": "lines+markers",
        "name": "Jüngere unter 25 Jahre",
        "visible": trace1_visible,
        "line": dict(color="#249532", width=2),
        "marker": dict(size=6),
        "hovertemplate": "<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
    }
    if show_fill:
        trace1_args["fill"] = "tozeroy"
        trace1_args["fillcolor"] = "rgba(128, 128, 128, 0.4)"
    fig.add_trace(go.Scatter(**trace1_args))

    # Trace 2: Insgesamt
    trace2_args = {
        "x": arbeitslos["Jahr"],
        "y": arbeitslos["Insgesamt"],
        "mode": "lines+markers",
        "name": "Insgesamt",
        "visible": trace2_visible,
        "line": dict(color="#E66C37", width=3),
        "marker": dict(size=8),
        "hovertemplate": "<b>Jahr:</b> %{x}<br><b>Wert:</b> %{y:,}<extra></extra>"
    }
    if show_fill:
        trace2_args["fill"] = "tozeroy"
        trace2_args["fillcolor"] = "rgba(128, 128, 128, 0.1)"
    fig.add_trace(go.Scatter(**trace2_args))

    fig.update_layout(
        xaxis=dict(title="Jahr", showgrid=True, tickmode="linear", dtick=2, range=[2010, 2024], gridcolor="lightgray", griddash="dot",tickangle=0),
        yaxis=dict(title="Anzahl", showgrid=True, gridcolor="lightgray", griddash="dot", tickformat=",d"),
        hoverlabel=dict(bgcolor="black", font_size=13, font_color="white"),
        # legend=dict(title="Altersgruppen")
    )

    st.plotly_chart(fig, use_container_width=True, key=key)