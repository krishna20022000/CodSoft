from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Define the book recommendation function
def recommend_books(book_title, book_features, book_titles, top_n=3):
    """
    Recommends books similar to the provided book title based on content-based filtering.

    Parameters:
    - book_title (str): The title of the book the user likes.
    - book_features (list of str): Descriptive features for all books in the dataset.
    - book_titles (list of str): Titles of all books in the dataset.
    - top_n (int): The number of recommendations to return.

    Returns:
    - list of str: Titles of recommended books.
    """
    # Step 1: Convert the book features into numerical vectors using TF-IDF
    print("Step 1: Converting book features into numerical representations using TF-IDF...")
    vectorizer = TfidfVectorizer(stop_words="english")
    feature_matrix = vectorizer.fit_transform(book_features)
    print("TF-IDF transformation complete.")
    
    # Step 2: Calculate the cosine similarity between all books
    print("Step 2: Calculating cosine similarity between all books...")
    similarity_matrix = cosine_similarity(feature_matrix, feature_matrix)
    print("Cosine similarity calculation complete.")
    
    # Step 3: Find the index of the book the user likes
    print(f"Step 3: Searching for the book '{book_title}' in the dataset...")
    try:
        book_index = book_titles.index(book_title)
        print(f"Book '{book_title}' found at index {book_index}.")
    except ValueError:
        return f"Error: The book '{book_title}' was not found in the dataset. Please check the title and try again."
    
    # Step 4: Retrieve similarity scores for the user's liked book
    print(f"Step 4: Retrieving similarity scores for the book '{book_title}'...")
    similarity_scores = list(enumerate(similarity_matrix[book_index]))
    
    # Step 5: Sort the books by similarity score (excluding the liked book itself)
    print("Step 5: Sorting books by similarity score...")
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:]  # Exclude the first item (self-comparison)
    
    # Step 6: Select the top N recommendations
    print(f"Step 6: Selecting the top {top_n} most similar books...")
    top_recommendations = sorted_scores[:top_n]
    recommended_books = [book_titles[i[0]] for i in top_recommendations]
    print("Top recommendations selected.")
    
    # Return the recommended book titles
    return recommended_books


# Step 2: Input data for the books
print("\nSetting up book data...")
book_titles = [
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "Brave New World",
]

book_features = [
    "Classic Fiction Racism Coming-of-age Harper Lee",
    "Dystopian Fiction Totalitarian George Orwell",
    "Romance Classic Elizabeth Bennet Jane Austen",
    "Classic American Dream Tragedy F. Scott Fitzgerald",
    "Dystopian Science Fiction Aldous Huxley",
]
print("Book data setup complete.\n")

# Step 3: Simulate user interaction
print("Simulating user interaction...\n")
liked_book = "1984"  # The book the user likes
print(f"User's liked book: {liked_book}")

# Step 4: Generate recommendations
print("\nGenerating recommendations...\n")
recommendations = recommend_books(liked_book, book_features, book_titles, top_n=3)

# Step 5: Display recommendations
print("\nDisplaying recommendations:")
if isinstance(recommendations, str):  # If there's an error message
    print(recommendations)
else:
    print(f"Because you liked '{liked_book}', you might enjoy:")
    for idx, book in enumerate(recommendations, start=1):
        print(f"{idx}. {book}")

print("\nRecommendation process complete.")