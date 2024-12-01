import streamlit as st

st.title("Welcome to my Advent of Code 2024 web app")
# Description
st.write('-----------------------------------------------')
st.write("This web app aims to share my python code I used for each AoC day's puzzle")
st.write("Ultimately, you can drop your inputs and run my code on it to check wether your code is correct or not ;)")
st.write('-----------------------------------------------')


# Entrée utilisateur
script_name = st.text_input(
    "Nom du script à exécuter (e.g., script.py)", "example.py")

# Contenu personnalisé
if st.button("Exécuter le script"):
    with st.spinner("Exécution en cours..."):
        try:
            # Exemple : contenu d'un script à exécuter (remplacez cette partie selon vos besoins)
            exec(open(script_name).read())
            st.success("Le script a été exécuté avec succès !")
        except Exception as e:
            st.error(f"Erreur lors de l'exécution : {e}")
