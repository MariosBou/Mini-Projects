import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

movies = pd.read_pickle("model/movies.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")
movie_vectors = joblib.load("model/movie_vectors.pkl")

my_favorites = [
    "Bad Boys for Life",
    "Spider Man Far from Home",
    "John Wick Chapter 3 Parabellum"
]

#indices of favorite movies
favorite_indices = movies[movies["title"].isin(my_favorites)].index

#user profile
favorite_vectors = movie_vectors[favorite_indices]
user_profile = np.mean(favorite_vectors.toarray(), axis=0)

#calculate similarity scores
scores = cosine_similarity([user_profile], movie_vectors)[0]
movies["score"] = scores

recommendation = (
    movies[~movies["title"].isin(my_favorites)]
    .sort_values(by="score", ascending=False)
    .head(10)
)

print("Top 10 movie recommendations for you:")
print(recommendation[["title", "genre", "year", "score"]])