<h1 align="center">Movie Recommendation System</h1>

<p align="center">
    A content-based movie recommendation system that uses Natural Language Processing (NLP) techniques to suggest movies based on the content provided by the user. The project leverages machine learning algorithms and NLP to analyze movie metadata and provide personalized recommendations.
</p>

## Overview

The Movie Recommendation System is built using content-based filtering and NLP. It analyzes the movie's plot, genre, cast, and other metadata to find similarities with the content provided by the user. By applying text processing techniques and vectorization, it calculates the similarity scores between different movies and suggests a list of movies that closely match the user's input. The system is implemented using Flask for the web interface, NLTK for text processing, and Scikit-learn for machine learning algorithms.

## Key Features

- **Content-Based Filtering:** Recommends movies based on their content such as plot, genre, and actors.
- **Natural Language Processing (NLP):** Uses NLP techniques to process and analyze movie metadata.
- **Flask Web Application:** Provides a user-friendly interface for searching and viewing movie recommendations.
- **Similarity Calculation:** Utilizes techniques such as TF-IDF and cosine similarity for movie comparison.
- **Scalable Design:** Can be extended to include more complex recommendation techniques or additional data sources.

## Requirements

- **Flask:** For building the web application interface.
- **NLTK:** For natural language processing and text analysis.
- **Scikit-Learn:** For implementing machine learning algorithms such as TF-IDF vectorization and cosine similarity.
- **Python 3.6 or above**

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/movie-recommendation-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd movie-recommendation-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```bash
    python app.py
    ```
5. Open a web browser and visit:
    ```
    http://127.0.0.1:5000/
    ```

## Screenshots

<p align="center">
    <img src="PROJECT SCREENSHOTS\1.png" alt="Screenshot 1" width="600">
    <br>
    <em>Homepage of the Movie Recommendation System</em>
</p>

<p align="center">
    <img src="PROJECT SCREENSHOTS\2.png" alt="Screenshot 2" width="600">
    <br>
    <em>Recommendation List</em>
</p>

<p align="center">
    <img src="PROJECT SCREENSHOTS\3.png" alt="Screenshot 2" width="600">
    <br>
    <em>Recommendation results based on user input</em>
</p>

<p align="center">
    <img src="PROJECT SCREENSHOTS\4.png" alt="Screenshot 2" width="600">
    <br>
    <em>Recommendation results based on user input</em>
</p>

## How It Works

1. **Data Collection:** Movie metadata such as titles, genres, plots, and cast are collected and preprocessed.
2. **Text Processing:** NLP techniques are used to tokenize and vectorize the textual data using tools like NLTK.
3. **Feature Extraction:** Uses Scikit-learn's TF-IDF vectorizer to convert textual data into numerical features.
4. **Similarity Calculation:** Cosine similarity is used to find the closest matches between the user's input and the movie dataset.
5. **Recommendations Display:** The top recommendations are presented on the web interface for the user to explore.

## Technologies Used

- **Flask:** For the web framework.
- **NLTK:** For text processing.
- **Scikit-Learn:** For machine learning algorithms.
- **HTML/CSS:** For the front-end interface.

## Future Enhancements

- Integrating collaborative filtering for hybrid recommendations.
- Adding a user feedback mechanism to improve recommendation quality.
- Expanding the dataset to include more metadata such as reviews and ratings.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

<p align="center">
    <em>Feel free to contribute or reach out if you have any suggestions for improvements!</em>
</p>
