import pandas as pd
import numpy as np
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate

def recommend_movies(data, user_id, num_recommendations):
    reader = Reader()
    movie_data = Dataset.load_from_df(data[['userId', 'movieId', 'rating']], reader)
    algo = SVD()
    trainset = movie_data.build_full_trainset()
    algo.fit(trainset)

    # Prever a classificação de um filme para um usuário específico
    def predict_rating(user_id, movie_id):
        prediction = algo.predict(user_id, movie_id)
        return prediction.est

    user_ratings = data[data['userId'] == user_id][['movieId', 'rating']]
    movie_ids = [x for x in data['movieId'] if x not in user_ratings['movieId'].tolist()]
    predictions = [predict_rating(user_id, x) for x in movie_ids]
    recommendations = pd.DataFrame({'movieId': movie_ids, 'prediction': predictions})
    recommendations = recommendations.sort_values('prediction', ascending=False).reset_index(drop=True)
    return recommendations.head(num_recommendations)

def main():
    # Carregando dados do IMDB
    df = pd.read_csv('data.csv')

    # Validação cruzada do modelo
    cv_results = cross_validate(SVD(), df[['userId', 'movieId', 'rating']], measures=['RMSE'], cv=5)
    print("Cross Validation Results: ", cv_results)

    # Gerar recomendações de filmes para um usuário
    user_id = int(input("Enter user id: "))
    num_recommendations = int(input("Enter number of recommendations: "))
    recommendations = recommend_movies(df, user_id, num_recommendations)
    print("Movie Recommendations for User ", user_id)
    print(recommendations)

if __name__ == '__main__':
    main()
