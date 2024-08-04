import streamlit as st
import plotly.express as px
from backend import get_date

# add title, text input, slider, select_box and subheader
st.title("WEATHER FORECAST - (next 5 days)")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="select the number of days")
option = st.selectbox("select type of data",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


if place:

    # get temperature/sky data
    filtered_data = get_date(place, days)

    # plot the temperature data
    if option == "Temperature":
        temperature = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # create a temperature plot.
        figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (c)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(image_paths, width=130, )
