import streamlit as st
import plotly.graph_objects as go


def app():
    st.write("Home Page")

    config = {'displayModeBar': False}

    #create donut plots 
    col1, col2 = st.columns(2)

    labels = ['Distance','Goal']
    values = [2500, 4500]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
    fig.update_layout(width = 400, showlegend = False, title_text='Goal One', title_x=0.5)

    with col1: 
            st.plotly_chart(fig, config=config)


    labels = ['Other Goal','Goal']
    values = [1000, 4500]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
    fig.update_layout(width = 400, showlegend = False, title_text=' Goal Two', title_x=0.5)

    with col2: 
        st.plotly_chart(fig, config=config)
        







