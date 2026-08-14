import streamlit as st
import pickle
import requests
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(layout="wide")

data_model=pickle.load(open(r"D:\ali\SIC\Project\Recoomend System\movies_metadata.csv\data_model.pkl",'rb'))
vector=pickle.load(open(r"D:\ali\SIC\Project\Recoomend System\movies_metadata.csv\vector.pkl","rb"))

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
    for i in distance[1:k+1]:
        movie_title=data_model.iloc[i[0]]['title']
        moive_id=data_model.iloc[i[0]]['id']   
        recommend_movies.append(movie_title)
        recommend_posters.append(fetch_poster(moive_id))
    return recommend_movies,recommend_posters        

st.title("🎬 Movie Recommender System")

select = st.selectbox(
    "Choose the movie you like",
    data_model["title"].unique()
)

button = st.button("Recommend other movies")


# Show recommendations
if button:

    movie_names, movie_posters = recommend(select, 5)

    st.subheader("Recommended Movies")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(movie_names[0])
        if movie_posters[0]:
            st.image(movie_posters[0])
    with col2:
        st.write(movie_names[1])
        if movie_posters[1]:
            st.image(movie_posters[1])

    with col3:
        st.write(movie_names[2])
        if movie_posters[2]:
            st.image(movie_posters[2])

    with col4:
        st.write(movie_names[3])
        if movie_posters[3]:
            st.image(movie_posters[3])

    with col5:
        st.write(movie_names[4])
        if movie_posters[4]:
            st.image(movie_posters[4])
