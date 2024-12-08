import streamlit as st
from PIL import Image
from time import time
from modules import Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7, Day_8

DAY_MODULES = {"1": Day_1, "2": Day_2, "3": Day_3,
               "4": Day_4, "5": Day_5, "6": Day_6,
               "7": Day_7, "8": Day_8}

# Internet Browser tab name
st.set_page_config(page_title="Advent of Code 2024 Solver",
                   page_icon="🎄", layout="wide")


# Sidebar customization with a width of 400 pixels
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            max-width: 300px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main title of the app
st.title("🎄Advent of Code 2024 Solver🎄")

# Sidebar menu
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
    "Choose a puzzle",
    ["Homepage 🏠",
     "Day 1: Historian Hysteria 📍",
     "Day 2: Red-Nosed Reports ☢️",
     "Day 3: Mull It Over 👨‍💻",
     "Day 4: Ceres Search 🕵🏻",
     "Day 5: Print Queue 🖨️",
     "Day 6: Guard Gallivant 💂‍♂️",
     "Day 7: Bridge Repair 🚧",
     "Day 8: Resonant Collinearity 📡",]
)

# Homepage section
if option == "Homepage 🏠":
    # Display an image on the homepage
    img = Image.open("resources/pictures/aoc24.png")
    st.image(img, use_container_width=False, width=800)
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
    tab1, tab2 = st.tabs(["🧩 Solver", "📜 Code Viewer"])

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
