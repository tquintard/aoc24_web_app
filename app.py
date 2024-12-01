import streamlit as st

st.title("Welcome to my Advent of Code 2024 web app")
# Description
st.write('-----------------------------------------------')
st.write("This web app aims to share my python code I used for each AoC day's puzzle")
st.write("Ultimately, you can drop your inputs and run my code on it to check wether your code is correct or not ;)")
st.write('-----------------------------------------------')


st.sidebar.title("Options")
option = st.sidebar.selectbox("Choisissez une action", [
                              "Accueil", "Exécuter un script", "Analyser des données"])

if option == "Accueil":
    st.write("Bienvenue sur votre site Python interactif.")
    st.write("Utilisez le menu à gauche pour explorer les fonctionnalités.")
elif option == "Exécuter un script":
    script_name = st.text_input(
        "Entrez le nom du script à exécuter", "example.py")
    if st.button("Exécuter"):
        with st.spinner("Exécution en cours..."):
            try:
                exec(open(script_name).read())
                st.success("Script exécuté avec succès.")
            except Exception as e:
                st.error(f"Erreur : {e}")
elif option == "Analyser des données":
    uploaded_file = st.file_uploader("Chargez un fichier CSV")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data.head())
        st.write("Histogramme des colonnes numériques :")
        data.hist(bins=20)
        st.pyplot(plt)
