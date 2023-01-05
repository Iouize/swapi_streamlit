import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title('Star Wars')

req = requests.get("https://swapi.dev/api/")

attributes = req.json()

select_attribute = st.selectbox(
    'choose a category :',
    attributes
)

searched = st.text_input("Search")

new_url = f"{attributes[select_attribute]}?search={searched}"

if searched != "":
    new_req = requests.get(new_url)

    result = new_req.json()["results"]
    st.write("Résultats")

    for res in result:
        st.markdown("- " + res["name"])

st.snow()
st.balloons()
