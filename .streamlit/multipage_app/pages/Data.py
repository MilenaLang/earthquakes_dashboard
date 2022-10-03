import streamlit as st
import pandas as pd
import sys

st.set_page_config(
    page_title="Multipage App",
    layout = "wide"
)

#caching -> more efficiency
@st.cache

def get_data():
    """
    This function opens the data set for further use
    :return: dataset as pandas dataframe
    """
    try:
        data = pd.read_csv(
            "/Users/milenalang/Documents/Studium/Master/advanced_geoscripting/earthquakes_dashboard/.streamlit/multipage_app/earthquakes1800_2021.csv")
    except Exception:
        print(
            "Could not find earthquake file."
        )
        sys.exit()

    #rename the columns for streamlit and delete the ones missing coordinates
    data.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'}, inplace=True)
    data = data[data['longitude'].notna()]
    data = data[data['latitude'].notna()]
    return data


def main():
    """
    This function shows the raw dataset behind the dashboard
    :return: Table with data
    """

    # set title
    st.title("Data")

    # call get_data function
    data = get_data()

    # map data
    st.subheader("Earthquakes from 1800-2021")
    st.map(data)

    # give information
    st.write("Have a look at the raw dataset...")

    # give the user the opportunity to have a look at the data
    if st.checkbox("Show data..."):
        st.subheader("Raw data")
        # show data
        st.write(data)

    st.write("Data retrieved from: https://www.kaggle.com/datasets/ramjasmaurya/historical-data-of-earthquakes18002021")


if __name__ == "__main__":
    main()