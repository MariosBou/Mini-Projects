# Movie Recommender System

This project is a simple **content-based movie recommendation system**. It uses **TF-IDF** on movie titles, genres, and descriptions to recommend movies similar to the ones you like. The project includes scripts to **train the model** and **generate recommendations automatically**.

---

## Project Structure

```

project/
│
├─ main.py # Main script to run training and recommendations
├─ train.py # Trains the TF-IDF model on your movie dataset
├─ recommend.py # Generates movie recommendations based on favorites
├─ requirements.txt # Python dependencies
├─ model/ # Folder where trained model and data are saved
├─ data/
  └─ combined.db # SQLite database with movie dataset

```

---

## Setup

1. Clone this repository or download the project files.
2. Make sure your `data/combined.db` file exists.
3. Install required Python packages:

```bash
pip install -r requirements.txt

```

This will:

Train the TF-IDF model on the deduplicated movies from the database (train.py).

Generate recommendations based on your favorite movies (recommend.py).

## Dataset

This project uses a movie dataset collected from **FZMovies**  which includes movies across different genres, along with metadata such as:
```
https://github.com/Simatwa/movies-dataset.git
```
- **Title**  
- **Genre**  
- **Year of release**  
- **Description / synopsis**  
- **URLs for streaming and cover images**

The database `combined.db` consolidates CSVs from multiple genres (e.g., Adventure, Action, etc.) into a single SQLite database for easier processing.  






## Usage

Add your favorite movies in recommend.py under the my_favorites list.
The system will calculate similarity scores and print the top 10 recommended movies, excluding your favorites.

Example in recommend.py:
```
my_favorites = [
    "Avengers - Endgame",
    "Black Panther",
    "Avatar The Way of Water"
]
```
