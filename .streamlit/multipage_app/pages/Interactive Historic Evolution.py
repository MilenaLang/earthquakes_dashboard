import plotly.express as px
import streamlit as st
import pandas as pd
import sys
sys.path.append("/Users/milenalang/Documents/Studium/Master/advanced_geoscripting/earthquakes_dashboard/.streamlit/multipage_app/pages")
from Data import get_data
import statsmodels.api as sm
import plotly.graph_objs as go

# set page layout
st.set_page_config(
    page_title="Multipage App",
    layout = "wide"
)

#get data
data = get_data()


def main():
    """
    This functions plots an interactive chart, showing the evolution over time
    :return:interactive chart
    """
    st.title("Interactive Historic Evolution")

    # selection of y-value
    y_axis_val = st.selectbox('Select y-axis value:', options = data.columns, index = 11)

    # colourpicker
    col = st.color_picker('Select a colour:')

    # plot
    plot = px.scatter(data, x = "Year", y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    plot.update_layout( plot_bgcolor = "rgba(0, 0, 0, 0)")
    st.plotly_chart(plot)

if __name__ == "__main__":
    main()