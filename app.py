import streamlit as st

# Custom imports 
from multipage import MultiPage
from datetime import date
from pages import home, settings, statistics

# Create an instance of the app 
app = MultiPage()

# Title of the main page
today = date.today()
d2 = today.strftime("%B %d, %Y")
st.header(d2)

st.title("Moorphic Dashboard")

#load sidebar 

st.sidebar.image('./icons/user.png')
st.sidebar.title("John Doe")
st.sidebar.header("Gender, Age")

col1, col2 = st.sidebar.columns(2)
col1.metric("Height", "5' 2")
col2.metric("Weight", "125 lb")

st.sidebar.radio("Activity Summary", ["Daily", "Weekly", "Monthly", "Yearly"])


# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Statistics", statistics.app)
app.add_page("Settings", settings.app)

# The main app
app.run()

#run sidebar 
