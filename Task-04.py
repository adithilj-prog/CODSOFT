import pandas as pd

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
tags = pd.read_csv('tags.csv')

print(movies.head())
print(ratings.head())
print(tags.head())

# Merge movies and tags on movieId
movie_tags = pd.merge(movies, tags, on='movieId', how='left')

# Fill missing tags with empty string
movie_tags['tag'] = movie_tags['tag'].fillna('')

# Create combined features column
movie_tags['combined_features'] = movie_tags['genres'] + ' ' + movie_tags['tag']

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Use only first 500 movies for testing
sample_df = movie_tags.head(500)

# Convert text to vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(sample_df['combined_features'])

# Compute similarity
similarity_matrix = cosine_similarity(tfidf_matrix)

def recommend(title, df, similarity_matrix):
    # Find index of the movie
    index = df[df['title'] == title].index[0]
    scores = list(enumerate(similarity_matrix[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommended = [df['title'][i[0]] for i in sorted_scores[1:6]]
    return recommended

print(recommend("Toy Story (1995)", sample_df, similarity_matrix))
print(recommend("Jumanji (1995)", sample_df, similarity_matrix))
print(recommend("Grumpier Old Men (1995)", sample_df, similarity_matrix))

