import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="My App",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "Welcome to DV4S",
                "Get Help": "https://www.polimi.it",
                "Report a bug": "https://www.polimi.it"}
)
st.title("My new :red[Streamlit] app")
st.header("Welcome to :green[DV4S]!")
st.subheader("Smile")
st.write("Welcome to my new **great** app!")

st.markdown("__")
st.markdown("> Ciao!")
st.markdown('<p style="color:yellow; font-size:20px;">Slider between 0 and 100</p>', unsafe_allow_html=True)

data = st.slider("Select a value", 0, 100, 50)

st.write("You selected:", data)

# Write function
# Allows to write in the app the arguments that are passed to it:
# st.write(*args, unsafe_allow_html=False, **kwargs)

# Displaying a number
st.write("Here is a number:", 42)

# Displaying a list
my_list = ["apple", "banana", "cherry"]
st.write("My list:", my_list)

# Displaying a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
st.write("Dictionary example:", my_dict)

# Displaying a DataFrame
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.write("Here is a DataFrame:", df)


# Define a list containing all the sports I know
sports_list = ['soccer', 'basketball', 'tennis', 'ski', 'football']

# Check if the button is pressed, show the list
if st.button("Sports", type="primary"):
    st.write(sports_list)

# st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary",disabled=False, use_container_width=False)

# Introduce a checkbox
if st.checkbox("I like DV4S!"):
    st.write("You like it, indeed!")
else:
    st.write("Please, like DV4S...")

    # Define a list of sports with icons
sports_dict = {
    '⚽ Soccer': 'soccer',
    '🏀 Basketball': 'basketball',
    '🎾 Tennis': 'tennis',
    '⛷ Ski': 'ski',
    '🏈 Football': 'football'
}

# Introduce a radio button
chosen_label = st.radio("Which sport do you prefer?", list(sports_dict.keys()))

# Get the corresponding sport name (without icon)
chosen_sport = sports_dict[chosen_label]

# Display result with icon
st.write(f'You like {chosen_label}, indeed!')

# Define a list of sports with icons
sports_dict = {
    '⚽ Soccer': 'soccer',
    '🏀 Basketball': 'basketball',
    '🎾 Tennis': 'tennis',
    '⛷ Ski': 'ski',
    '🏈 Football': 'football'
}

# Introduce a select box
chosen_label = st.selectbox("Which sport do you prefer?", list(sports_dict.keys()))

# Get the sport name without the icon if needed
chosen_sport = sports_dict[chosen_label]

# Display result
st.write(f'You like {chosen_label}, indeed!')


# Define a dictionary with players and goals in a season
players = {"Zoff": "10", "Ronaldo": "23", "Messi": "34"}

# Multiselect box
selection = st.multiselect("Select the player to analyse:", ["Zoff", "Ronaldo", "Messi"])

# Show results
for player in selection:
    st.markdown(f'**:red[{player}]**: {players[player]} goals!')


# Age
age = st.slider('How old are you?', 18, 100, 25)
st.write("You are", age, "years old!")

# Age ranges
age_range = st.slider('Select a range of valid ages', 18, 67, (25, 50))
st.write('You selected:', age_range)

# Datetime range
date_range = st.slider('Select a range of valid dates',
    value=(datetime(2020, 3, 15), datetime(2025, 3, 20)),
    min_value=datetime(2000, 1, 1),
    max_value=datetime(2025, 3, 31),
    format="DD/MM/YYYY"
)

# Unpack tuple
start_date, end_date = date_range

# Format dates correctly
st.write("Date range:", start_date.strftime("%d/%m/%Y")
, "to", end_date.strftime("%d/%m/%Y"))


# Text Input
name = st.text_input("Enter your name:", placeholder="Type here...")

# Number Input
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25, step=1)

# Display user input
if name:
    st.write(f"Hello, **{name}**! 👋")

if age:
    st.write(f"Your age is **{age}** years old.")

# Combining Inputs
if name and age:
    st.success(f"Welcome, {name}! You are {age} years old. 🎉")

    # Date range with widgets
date = st.date_input(
    "Select a date range",
    value=(datetime(2025, 3, 15), datetime(2025, 3, 20))
)

# Unpack and display the selected dates
start_date, end_date = date
st.write(f"You selected from **{start_date.strftime('%d/%m/%Y')}** to **{end_date.strftime('%d/%m/%Y')}**.")

# Creating a form
with st.form("user_form"):
    # Text input (name)
    name = st.text_input("Full Name:", placeholder="Enter your name...")

    # Number input (age)
    age = st.number_input("Age:", min_value=1, max_value=120, value=25, step=1)

    # Select box (dropdown) for gender
    gender = st.selectbox("Gender:", ["Select an option", "Male", "Female", "Other"])

    # Submit button
    submitted = st.form_submit_button("Submit")

# Display output after submission
if submitted:
    if name and gender != "Select an option":
        st.success(f"✅ Form submitted!\n\n**Name:** {name}\n**Age:** {age}\n**Gender:** {gender}")
    else:
        st.warning("⚠️ Please fill out all fields correctly.")