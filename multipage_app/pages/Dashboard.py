import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import statsmodels.api as sm
import plotly.graph_objs as go

# set page layout
st.set_page_config(
    page_title="Multipage App",
    layout = "wide"
)

# import data ″
sys.path.append("/Users/milenalang/Documents/Studium/Master/advanced_geoscripting/earthquakes_dashboard/.streamlit/multipage_app/pages")
from Data import get_data


def main():
    """
    This function provide a dashboard for all earthquakes occurring from 1800 to 2021.
    :return: interactive dashboard
    """

    #add title
    st.title("Dashboard")

    # import data
    data = get_data()


    ### ROW 1 ####

    left_col, middle_col, right_col = st.columns(3)

    with left_col:
        #a average magnitude
        data["Mag"] = pd.to_numeric(data["Mag"])
        magnitude = data["Mag"]
        mean_mag = magnitude.mean()
        st.subheader("Ø Magnitude:")
        st.subheader(f"{mean_mag:.2f}")

    with middle_col:
        # average damage
        damage = data["Damage ($Mil)"]
        mean_damage = damage.mean()
        st.subheader("Ø Damage:")
        st.subheader(f"{mean_damage:.2f} Mil. $")

    with right_col:
        # deaths
        deaths = data['Deaths']
        mean_deaths = deaths.mean()
        st.subheader("Ø Deaths/Earthquake:")
        st.subheader(f"{mean_deaths:.2f}")


    st.markdown("---")


    ### ROW 2 ###

    st.subheader('Magnitude')

    left_col2, middle_col2 = st.columns(2)

    with left_col2:
        # display top 10 highest magnitudes
        top_mag = data.nlargest(10, 'Mag')

        fig = px.bar(
            top_mag,
            y='Location Name',
            x='Mag',
            orientation='h',
            color_discrete_sequence =['blue']*len(data),
            title="Locations of the strongest earthquakes"
        )
        fig.update_xaxes(range=(6, 10))
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

    with middle_col2:
        # plot all magnitudes
        fig = px.histogram(data,
                           x="Mag",
                           nbins=50,
                           title="Magnitude of all earthquakes"
        )
        st.plotly_chart(fig, use_container_width=True)


    st.markdown("---")


    ### ROW 3 ###

    st.subheader('Deaths')

    left_col3, right_col3 = st.columns(2)

    with left_col3:

        # plot (only) deathly earthquakes
        # selected data must not be zero
        Deaths_noNa = data[data['Deaths'].notna()]
        fig12 = px.scatter_mapbox(Deaths_noNa,
                                  lat="latitude",
                                  lon="longitude",
                                  color="Deaths",
                                  size="Deaths",
                                  color_continuous_scale=px.colors.sequential.Plotly3,
                                  size_max=15,
                                  zoom=0.2,
                                  title="Deadly earthquakes"
        )
        fig12.update_layout(mapbox_style="carto-positron")
        st.plotly_chart(fig12, use_container_width=True)

    with right_col3:
        # map deaths and injured over the years
        fig = go.Figure([

            go.Scatter(
                name='Injured',
                x=Deaths_noNa['Year'],
                y=Deaths_noNa['Injuries'],
                mode='markers',
                marker=dict(color='red', size=3.5),
                showlegend=True
            ),

            go.Scatter(
                name='Deaths',
                x=Deaths_noNa['Year'],
                y=Deaths_noNa['Deaths'],
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
        st.plotly_chart(fig, use_container_width=True)



    st.markdown("---")


    ### ROW 4 ###

    st.subheader('Damage')

    left_col4, right_col4 = st.columns(2)

    with left_col4:

        # plot (only) earthquakes with damages
        # selected data must not be zero
        damage_noNa = data[data['Damage ($Mil)'].notna()]
        fig12 = px.scatter_mapbox(damage_noNa,
                                  lat="latitude",
                                  lon="longitude",
                                  color="Damage ($Mil)",
                                  size="Damage ($Mil)",
                                  color_continuous_scale=px.colors.cyclical.IceFire,
                                  size_max=15,
                                  zoom=0.2,
                                  title="Earthquakes with damages"
                                  )
        fig12.update_layout(mapbox_style="carto-positron")
        st.plotly_chart(fig12, use_container_width=True)

    with right_col4:

        # plot a bar of the 10 earthquakes with the most damage
        fig = px.scatter(damage_noNa,
                         y='Damage ($Mil)',
                         x='Houses Destroyed',
                         trendline="ols",
                         title="Correlation of damage and destroyed houses",
                         color="Deaths",
                         color_continuous_scale=px.colors.cyclical.IceFire
        )

        st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()