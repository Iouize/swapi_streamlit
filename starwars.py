import streamlit as st
import pandas as pd
import numpy as np
import requests

def generate_url(url, category, searched):
    return f"{url}{category}?search={searched}"

def make_request(url):
    return requests.get(url)

def choose_category(url):
    categories = make_request(url).json()
    category = st.selectbox(
        'Choose a category :',
        categories
    )
    return category

def generate_url_pages_results(req, url):
    nb_pages = req.json()['count'] // 10
    if req.json()['count'] > nb_pages * 10 :
        nb_pages += 1
    link_pages = []
    for i in range(nb_pages):
        link_pages.append(f"{url}&page={i+1}")
    return link_pages

def print_results(list_url, category):
    results = []
    for url in list_url:
        req = requests.get(url)
        for res in req.json()["results"]:
            if category != "films":
                results.append(res["name"])
            else:
                results.append(res["title"])
    return results

def display_site():
    url = "https://swapi.dev/api/"

    st.title('Star Wars')

    col1, col2 = st.columns(2)

    with col1:
        category = choose_category(url)

    with col2:
        searched = st.text_input("Search")

    new_url = generate_url(url, category, searched)
    req = make_request(new_url)

    list_pages = generate_url_pages_results(req, new_url)
    list_results = print_results(list_pages, category)

    st.write(f"We found {len(list_results)} result(s) :")

    for result in list_results:
        st.markdown("- " + result)

display_site()
