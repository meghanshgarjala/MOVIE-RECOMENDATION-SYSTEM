import os
import pickle
import streamlit as st
import requests
import pandas as pd
from streamlit_lottie import st_lottie  # For Lottie animations
import zipfile

# Function to create the ZIP file if it doesn't already exist
def create_zip():
    if not os.path.exists('similarity.zip'):
        if os.path.exists('similarity.pkl'):
            with zipfile.ZipFile('similarity.zip', 'w') as zipf:
                zipf.write('similarity.pkl', arcname='similarity.pkl')
            st.success("The ZIP file 'similarity.zip' has been created.")
        else:
            st.error("The file 'similarity.pkl' does not exist in the project directory. Please add it.")

# Function to load similarity data from the ZIP file
def load_similarity_data():
    create_zip()  # Create the ZIP file if it doesn't exist
    try:
        with zipfile.ZipFile('similarity.zip', 'r') as zipf:
            with zipf.open('similarity.pkl') as f:
                similarity_data = pickle.load(f)
        return similarity_data
    except KeyError:
        st.error("The file 'similarity.pkl' is not found in the ZIP archive.")
        return None
    except FileNotFoundError:
        st.error("The ZIP file 'similarity.zip' could not be found.")
        return None

# Load the similarity data
similarity = load_similarity_data()
if similarity is None:
    st.stop()  # Stop execution if similarity data is not loaded

# Load movies data
if os.path.exists('movie_dict.pkl'):
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
else:
    st.error("The file 'movie_dict.pkl' is missing.")
    st.stop()

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', "")
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""

# Your existing Streamlit app code continues here...


# Function to get Lottie animation URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to recommend movies based on similarity
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# Load data and pre-trained model
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = similarity = load_similarity_data()
movies = pd.DataFrame(movies_dict)

# Streamlit layout settings
st.set_page_config(page_title="Movie Recommender", layout="wide", page_icon="🎬")
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f8b500, #fceabb);
        font-family: Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True
)

# Load Lottie animation
lottie_url = "https://assets7.lottiefiles.com/packages/lf20_w51pcehl.json"
lottie_animation = load_lottieurl(lottie_url)

# Header section
st.title("🎬 Movie Recommender System")
st_lottie(lottie_animation, height=200, key="header_animation")

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Display recommendations when button is clicked
if st.button('Show Recommendation'):
    with st.spinner("Fetching recommendations..."):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Displaying recommendations in a dynamic layout
    st.subheader("Top Recommendations")
    col1, col2, col3, col4, col5 = st.columns(5)

    # Function to display movie info in a column
    def display_movie(column, movie_name, movie_poster):
        with column:
            st.image(movie_poster, use_column_width=True, caption=movie_name)
            st.button("More Info", key=movie_name)

    # Display each recommendation in its respective column
    for idx, col in enumerate([col1, col2, col3, col4, col5]):
        display_movie(col, recommended_movie_names[idx], recommended_movie_posters[idx])

    # Adding animation and styling for a smooth experience
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: #f8f9fa;
        }
        .css-1kyxreq {
            animation: fadeIn 2s;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        </style>
        """, unsafe_allow_html=True
    )