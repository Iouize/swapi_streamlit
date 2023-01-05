import streamlit as st
import pandas as pd
import numpy as np
import requests

def print_results(result, attribute):
    if attribute != "films":
        for res in result:
            st.markdown("- " + res["name"])
    else:
        for res in result:
            st.markdown("- " + res["title"])

st.title('Star Wars')

req = requests.get("https://swapi.dev/api/")
attributes = req.json()

col1, col2 = st.columns(2)

with col1:
    select_attribute = st.selectbox(
        'choose a category :',
        attributes
    )

with col2:
    searched = st.text_input("Search")


new_url = f"{attributes[select_attribute]}?search={searched}"
new_req = requests.get(new_url)

if searched != "":
    result = new_req.json()["results"]
    st.write("Résultats")
    print_results(result, select_attribute)

else:
    stantard_req = requests.get(attributes[select_attribute])
    stantard_res = stantard_req.json()["results"]
    print_results(stantard_res, select_attribute)


st.snow()
st.balloons()
