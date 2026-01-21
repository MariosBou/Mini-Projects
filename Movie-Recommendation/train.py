import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

os.makedirs("model", exist_ok=True)

conn = sqlite3.connect("data/combined.db")
movies = pd.read_sql("SELECT * FROM movies", conn)

movies["title"] = movies["title"].fillna("")
movies["genre"] = movies["genre"].fillna("")
movies["description"] = movies["description"].fillna("")

movies["text"] = movies["title"] + " " + movies["genre"] + " " + movies["description"]

#remove duplicates
movies_unique = movies.groupby("title").agg({
    "genre": lambda x: " ".join(set(x)),
    "year": "first",
    "text": "first"
}).reset_index()

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
movie_vectors = vectorizer.fit_transform(movies_unique["text"])

joblib.dump(vectorizer, "model/vectorizer.pkl")
joblib.dump(movie_vectors, "model/movie_vectors.pkl")
movies_unique.to_pickle("model/movies.pkl")

print("Training complete. ")
print("Movies learned:", len(movies))



