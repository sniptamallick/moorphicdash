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

# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Statistics", statistics.app)
app.add_page("Settings", settings.app)

# The main app
app.run()

#run sidebar 
