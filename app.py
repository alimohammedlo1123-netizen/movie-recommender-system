import streamlit as st
import pickle
import requests
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path 
import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
st.set_page_config(layout="wide")

BASE_DIR = Path(__file__).parent
data_model = pickle.load(open(BASE_DIR / "data_model.pkl", "rb"))
vector = pickle.load(open(BASE_DIR / "vector.pkl", "rb"))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US"
    response=requests.get(url)
    data=response.json()
    poster_path=data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None
def recommend(movie,k):
    index=data_model[data_model['title']==movie].index[0]
    similarity=cosine_similarity(vector[index],vector).flatten()
    distance=sorted(list(enumerate(similarity)),reverse=True,key=lambda x:x[1])
    recommend_movies=[]
    recommend_posters=[]
    for i in distance[0:k]:
        movie_title=data_model.iloc[i[0]]['title']
        moive_id=data_model.iloc[i[0]]['id']   
        recommend_movies.append(movie_title)
        recommend_posters.append(fetch_poster(moive_id))
    return recommend_movies,recommend_posters
st.title('🎬 Team4.Netflix')

select=st.selectbox('Choose The Movie You Like',[None]+list(data_model['title'].unique()))
cols=st.columns(5)
if select is not None:

    title, posters = recommend(select, 5)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:

            movie_id = data_model[
                data_model['title'] == title[i]
            ]['id'].iloc[0]

            movie_url = f"https://www.themoviedb.org/movie/{movie_id}"

            st.markdown(
                f"""
                <a href="{movie_url}" target="_blank">
                    <img src="{posters[i]}" width="200">
                </a>
                """,
                unsafe_allow_html=True
            )

            st.write(title[i]) 
else:    
    random_movie=data_model.sample(25)
    for row in range(5):
        cols=st.columns(5)
        for col in range(5):
            index=row*5+col
            with cols[col]:
                movie=random_movie.iloc[row*5+col]
                poster=fetch_poster(movie['id'])
                if poster is not None:
                    movie_id=movie['id']
                    movie_url = f"https://www.themoviedb.org/movie/{movie_id}"
                    st.write(movie['title'])
                    st.markdown(
                                                    f"""
                                                    <a href="{movie_url}" target="_blank">
                                                        <img src="{poster}" width="200">
                                                    </a>
                                                    """,
                                                    unsafe_allow_html=True
                                                )
                                    
                else:
                    st.write('No poster available')
