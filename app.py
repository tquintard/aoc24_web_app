import streamlit as st
from PIL import Image  # Required for handling images
from functools import partial
import timeit
from time import time
from modules import Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7, Day_8, Day_9, Day_10, Day_11, Day_12, Day_13, Day_14, Day_15, Day_16, Day_17, Day_18, Day_19, Day_20, Day_21, Day_22, Day_23, Day_24, Day_25

DAY_MODULES = {'1': Day_1}

# Main title of the app
st.title("Welcome to my Advent of Code 2024 web app")

# Sidebar menu
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
    "Choose a puzzle",
    ["Homepage", "Day 1: Historian Hysteria"]
)

# Homepage section
if option == "Homepage":
    # Display an image on the homepage
    img = Image.open("resources/pictures/aoc24.png")
    st.image(img, use_column_width=True)
    st.write("This web app aims to share my Python code used to solve AoC puzzles.")
    st.write(
        "You can drop your inputs and run my code to check whether your solution is correct.")
    st.write("Select a puzzle from the menu to begin.")

# Puzzle Section
else:
    st.header(option)
    # Recover the day number
    day = option.split(":")[0].split()[1]
    # Options for input: file upload or text box
    st.subheader("Provide your input data")
    input_method = st.radio(
        "How would you like to provide your input?",
        ("Upload a text file", "Paste your input in the text box")
    )

    # Initialize input_data variable
    input_data = None

    if input_method == "Upload a text file":
        # File uploader for input data
        uploaded_file = st.file_uploader("", type=["txt", "csv"])
        if uploaded_file is not None:
            # Read the uploaded file content
            input_data = uploaded_file.read().decode("utf-8")

    elif input_method == "Paste your input in the text box":
        # Text area for pasting input data
        input_data = st.text_area("", placeholder="Enter your input data...")

    # Button to run the puzzle solution
    if input_data and st.button(f"Run Day {day} code"):
        with st.spinner("Running your puzzle solution..."):
            try:
                start = time()
                # Fetch input data
                fct = DAY_MODULES[day].main
                sol = fct(input_data)
                elapsed_time = (time() - start)*1000
                # partial_function = partial(solvepuzzle, day=day)
                # if 0 < elapsed_time < 100:
                #     nb_rep = int(min((200 // elapsed_time) - 1, 100))
                #     elapsed_time = f'{int(timeit.timeit(stmt=partial_function, number=nb_rep)*1000/nb_rep) + 1} ms'
                # else:
                #     elapsed_time = f"{int(elapsed_time) + 1} ms"
                #     solution = len(input_data.splitlines())
                st.success(f"Your solution for Day {day} are: {sol}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
