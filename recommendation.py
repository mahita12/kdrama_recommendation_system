from web_scrapping import df
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Genre'])

# Compute the cosine similarity between each kdrama using genres
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['Title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim, num_recommend = 10):
    idx = indices[title]
# Get the pairwsie similarity scores of kdramas
    sim_scores = list(enumerate(cosine_sim[idx]))
# Sort the kdrama based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
# Scores of the 10 most similar kdramas
    top_similar = sim_scores[1:num_recommend+1]
# kdrama indices
    movie_indices = [i[0] for i in top_similar]
# Return the top 10 most similar kdramas
    return df['Title'].iloc[movie_indices]

print(get_recommendations('Move to Heaven (2021)'))
