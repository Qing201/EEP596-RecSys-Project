import pandas as pd

def tSNE_recommend(title, sorted_movies_df, range=20, n=5):
    movie_index = sorted_movies_df.index[sorted_movies_df['primaryTitle'] == title].tolist()
    
    if movie_index:
        movie_index = movie_index[0]

        len = sorted_movies_df.shape[0]
        if range > len-2:
            return 'Range out of list'

        front = movie_index - range//2 
        back = movie_index + range//2 

        if front < 0:
            back += -front
            front = 0
        elif back > len-1:
            front -= back - (len-1)
            back = len-1
        
        similar_movie_df = sorted_movies_df[front:back].drop(index = movie_index)
        
        return similar_movie_df
    
    else:
        return 'Can\'t Find this Movie'


def user_recommend(user_id, similar_movie_df, rating_pred, n=5):
    sorted_id = list(rating_pred.loc[user_id].sort_values(ascending=False).index)
    i = 0
    range_movie_id = similar_movie_df['movieId'].to_list()
    rec_id_list = []
    for index in range(len(sorted_id)):
        if i >=  n:
            break
        else:
            if int(sorted_id[index]) in range_movie_id:
                rec_id_list.append(similar_movie_df[similar_movie_df['movieId'] == int(sorted_id[index])].index.to_list()[0])
                i += 1
    
    ## get movie name
    id_name = similar_movie_df['primaryTitle'].to_dict()

    name_list = []
    for id in rec_id_list:
        name_list.append(id_name[id])

    return name_list


def main(movie, user_id):
    pred = pd.read_csv('../Data/UserRec/Prediction/rating_hat_svd.csv')
    pred.set_index('userId', inplace=True)

    movies_sorted = pd.read_csv('../Data/UserRec/recommend/tSNE_sorted.csv')

    similar_movie_df = tSNE_recommend(movie, movies_sorted)

    name_list = user_recommend(user_id, similar_movie_df, pred)

    print(name_list)

if __name__ == "__main__":
    main(movie = 'The Avengers', user_id = 50)