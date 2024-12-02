import streamlit as st
from PIL import Image
from time import time
from modules import Day_1

DAY_MODULES = {'1': Day_1}

# Main title of the app
st.title("🎄Advent of Code 2024 Solver🎄")

# Sidebar menu
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
    "Choose a puzzle",
    ["🏠", "Day 1: Historian Hysteria🗺️"]
)

# Homepage section
if option == "🏠":
    # Display an image on the homepage
    img = Image.open("resources/pictures/aoc24.png")
    st.image(img, use_column_width=True)
    st.write("This web app aims to share my Python code I used to solve AoC puzzles.")
    st.write(
        "You can drop your inputs and run my code to check whether your solution is correct.")
    st.write("Select a puzzle from the menu to begin.")

# Puzzle Section
else:
    st.header(option)

    # Recover the day number
    day = option.split(":")[0].split()[1]

    # Create tabs for "Solver" and "Code"
    tab1, tab2 = st.tabs(["🧩Solver", "📜Code Viewer"])

    # Solver Tab
    with tab1:
        st.subheader("Provide your input data")
        input_method = st.radio(
            "Select a method for provding your data:",
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
            input_data = st.text_area(
                "", placeholder="Enter your input data...")

        # Button to run the puzzle solution
        if input_data and st.button(f"Run code"):
            with st.spinner("Running your puzzle solution..."):
                try:
                    start = time()
                    sol = DAY_MODULES[day].main(input_data)
                    elapsed_time = int((time() - start) * 1000)
                    st.success(f"""
                                Your solutions for Day {day} are:
                                - Part 1: {sol[0]}
                                - Part 2: {sol[1]}
                                - Execution time: {elapsed_time} ms
                                """)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    # View Code Tab
    with tab2:
        try:
            # Display the content of the corresponding Python module
            with open(f"modules/Day_{day}.py", "r") as f:
                code = f.read()
            st.code(code, language="python")
        except FileNotFoundError:
            st.error(f"Code for Day {day} is not available.")
