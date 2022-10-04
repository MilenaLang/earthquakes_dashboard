import plotly.express as px
import streamlit as st
import pandas as pd
import sys
sys.path.append("/Users/milenalang/Documents/Studium/Master/advanced_geoscripting/earthquakes_dashboard/.streamlit/multipage_app/pages")
from Data import get_data
import plotly.graph_objs as go

# set page layout
st.set_page_config(
    page_title="Multipage App",
    layout = "wide"
)

#get data
data = get_data()



# map damage over the years
fig = px.scatter(data, x="Year", y="Damage ($Mil)", color = 'Injuries')

st.plotly_chart(fig)

# map deaths over the years
fig = px.line(data, x="Year", y="Deaths", title='Deaths per year')
st.plotly_chart(fig)

# map deaths and injured over the years
fig = go.Figure([

    go.Scatter(
        name='Injured',
        x=data['Year'],
        y=data['Injuries'],
        mode='markers',
        marker=dict(color='red', size=3.5),
        showlegend=True
    ),

    go.Scatter(
        name='Deaths',
        x=data['Year'],
        y=data['Deaths'],
        mode='markers',
        marker=dict(color='blue', size=3.5),
        showlegend=True
    )
])

fig.update_layout(
    yaxis_title='Year',
    title='Deaths and Injured by Event',
    hovermode="y"
)
st.plotly_chart(fig)



