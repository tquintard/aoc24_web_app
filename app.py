import streamlit as st
from PIL import Image  # Required for handling images

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
    img = Image.open("resources/pictures/aoc2024.png")
    st.image(img, use_column_width=True)
    st.write("This web app aims to share my Python code used to solve AoC puzzles.")
    st.write(
        "You can drop your inputs and run my code to check whether your solution is correct.")
    st.write("Select a puzzle from the menu to begin.")

# Puzzle Section
else:
    st.header(option)
    day = option.split(":")[0]
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
        uploaded_file = st.file_uploader("", type=["txt"])
        if uploaded_file is not None:
            # Read the uploaded file content
            input_data = uploaded_file.read().decode("utf-8")

    elif input_method == "Paste your input in the text box":
        # Text area for pasting input data
        input_data = st.text_area("", placeholder="Enter your input data...")

    # Button to run the puzzle solution
    if input_data and st.button(f"Run {day} code"):
        with st.spinner("Running your puzzle solution..."):
            try:
                # Example solution: Replace this with your actual Day 1 logic
                # Example: count the number of lines
                solution = len(input_data.splitlines())
                st.success(f"Your solution for {day} are: {solution}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
