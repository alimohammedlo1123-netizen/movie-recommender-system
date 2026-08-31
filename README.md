# 🎬 Movie Recommendation System

A movie recommendation system built with **Python, Machine Learning, and Streamlit** that recommends movies based on their similarity to a selected movie.

## 🚀 Live Demo

👉 **[Try the Movie Recommendation System](https://movie-recommender-system-d8uj3wrjaqfzoekzjkcrmh.streamlit.app/)**

## 📌 Project Overview

This project provides a simple movie recommendation system that helps users discover movies similar to a movie they like.

The system uses **TF-IDF Vectorization** and **Cosine Similarity** to calculate the similarity between movies and generate recommendations.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* SciPy
* Streamlit
* Requests
* Git & Git LFS

## ⚙️ How It Works

1. The movie dataset is loaded and processed.
2. Relevant movie features are combined into a text representation.
3. **TF-IDF** converts the text data into numerical vectors.
4. **Cosine Similarity** calculates the similarity between movies.
5. When the user selects a movie, the system returns the most similar movies.
6. Movie posters and information are displayed through the Streamlit application.

## 📂 Project Structure

```text
movie-recommender-system/
│
├── app.py
├── final_project.ipynb
├── data_model.pkl
├── vec_title.pkl
├── vec_text.pkl
├── vec_genre.pkl
├── movies_metadata.csv
├── ratings_small.csv
├── links_small.csv
├── requirements.txt
└── .gitattributes
```

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/alimohammedlo1123-netizen/movie-recommender-system.git
```

Move into the project directory:

```bash
cd movie-recommender-system
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Recommendation Method

The system uses:

### TF-IDF

TF-IDF is used to convert movie text features into numerical vectors while reducing the importance of very common words.

### Cosine Similarity

Cosine similarity measures how similar two movie vectors are.

The movies with the highest similarity scores are returned as recommendations.

## 🎯 Features

* 🔎 Search/select a movie
* 🎬 Get similar movie recommendations
* 🖼️ Display movie posters
* 🌐 Web-based interface using Streamlit
* ⚡ Fast recommendations using precomputed vectors and similarity

## 📈 Future Improvements

* Improve recommendation accuracy.
* Add user-based and collaborative filtering.
* Add movie ratings and genres filters.
* Improve the user interface.
* Add personalized recommendations based on user history.

## 👨‍💻 Author

**Ali Mohamed Hassan Mohamed Badr**

Computer Science Student | Data Science & Machine Learning

---

⭐ If you find this project useful, feel free to star the repository!
