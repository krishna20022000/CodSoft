from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to compute recommendations based on a user's liked movie
def recommend_movies(movie_title, movie_features, movie_titles, top_n=3):
    """
    Recommends movies similar to the provided movie title based on content-based filtering.

    Parameters:
    - movie_title (str): The title of the movie the user likes.
    - movie_features (list of str): Descriptive features of all movies in the dataset.
    - movie_titles (list of str): Titles of all movies in the dataset.
    - top_n (int): The number of recommendations to return.

    Returns:
    - list of str: Titles of recommended movies.
    """
    # Step 1: Convert text features into a numerical matrix using TF-IDF Vectorizer
    print("Converting movie features into numerical representations using TF-IDF...")
    vectorizer = TfidfVectorizer()
    feature_matrix = vectorizer.fit_transform(movie_features)
    
    # Step 2: Compute the similarity matrix using cosine similarity
    print("Calculating cosine similarity between all movies...")
    similarity_matrix = cosine_similarity(feature_matrix, feature_matrix)
    
    # Step 3: Find the index of the given movie in the movie list
    try:
        movie_index = movie_titles.index(movie_title)
    except ValueError:
        return f"Error: Movie '{movie_title}' not found in the list. Please check the titlxe and try again."
    
    # Step 4: Get similarity scores for the selected movie
    print(f"Finding movies similar to '{movie_title}'...")
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    
    # Step 5: Sort the movies based on similarity scores (excluding the selected movie)
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:]  # Exclude the first movie (self-comparison)

    # Step 6: Extract the top N recommendations
    print(f"Selecting the top {top_n} similar movies...")
    top_recommendations = sorted_scores[:top_n]
    
    # Get the movie titles for the top recommendations
    recommended_movies = [movie_titles[i[0]] for i in top_recommendations]
    return recommended_movies


# Step 7: Input movie data
print("Setting up movie data...")
movie_titles = [
    "Inception", 
    "Titanic", 
    "Interstellar", 
    "The Dark Knight", 
    "Avatar"
]

movie_features = [
    "Sci-Fi Thriller Christopher Nolan Leonardo DiCaprio",
    "Romance Drama James Cameron Leonardo DiCaprio",
    "Sci-Fi Drama Christopher Nolan Matthew McConaughey",
    "Action Thriller Christopher Nolan Christian Bale",
    "Sci-Fi Action James Cameron Sam Worthington"
]

# Step 8: User Interaction
liked_movie = "Inception"  # Change this to try with different movies
print(f"User liked movie: {liked_movie}")

# Step 9: Get recommendations
recommendations = recommend_movies(liked_movie, movie_features, movie_titles)

# Step 10: Display recommendations
if isinstance(recommendations, str):  # If there's an error message
    print(recommendations)
else:
    print(f"\nRecommendations for '{liked_movie}':")
    for idx, movie in enumerate(recommendations, start=1):
        print(f"{idx}. {movie}")