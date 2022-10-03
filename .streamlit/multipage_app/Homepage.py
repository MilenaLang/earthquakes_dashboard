#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An earthquake streamlit dashboard"""

# Python code for an earthquake dashboard from 1800-2021.

import streamlit as st
from PIL import Image

# set page layout
st.set_page_config(
    page_title="Multipage App",
    layout = "wide"
)


def main():
    """
    This function creates the home section
    :return: Home section
    """

    # add information to the sideboard
    st.sidebar.success("Select a page above")
    st.sidebar.info(
        """
        This app is developed by Milena Lang (last updated 10.10.2022).
        """
    )
    # add title
    st.title("Earthquake-Dashboard (1800-2021)")
    # information about the project
    st.write("This earthquake dashboard is designed to analyze and visualize all earthquakes occurring worldwide since 1800.")
    st.markdown("* The dashboard provides information and maps on magnitudes, deaths, and damages.")
    st.markdown("* Raw data can be viewed in the data section.")
    st.markdown("* The historic evolution section allows to select the desired parameters for a chronological view.")

    # add image
    url = 'https://github.com/MilenaLang/earthquakes_dashboard/blob/master/.streamlit/multipage_app/erdbeben.jpg'
    image = Image.open(url)
    st.image(image, caption="Earthquake, derived from https://rp-online.de/panorama/ausland/taiwan-erdbeben-der-staerke-6-4-reisst-menschen-aus-dem-schlaf_bid-18908485")


    # information on data and ressources
    st.markdown("## Ressources")
    st.markdown("* Coding is fun(2022): How to create a Streamlit Multi-Page Web App, derived from https://www.youtube.com/watch?v=YClmpnpszq8 on 30.09.2022")
    st.markdown("* Dataprofessor(2022): Streamlit App Starter Kit, derived from https://github.com/streamlit/app-starter-kit on 30.09.2022")
    st.markdown("* Andy McDonald(2022): Adding Interactive Plotly Charts to a Streamlit App, derived from https://www.youtube.com/watch?v=3f-j-PZ5N8A on 30.09.2022")
    st.markdown("* Plotly(2022): Plotly Open Source Graphing Library for Python, derived from https://plotly.com/python/ on 30.09.2022")

if __name__ == "__main__":
        main()