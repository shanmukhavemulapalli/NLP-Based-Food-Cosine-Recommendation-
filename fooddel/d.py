import pandas as pd
import pickle
cosine_similarities=pickle.load(open('m.pkl','rb'))
import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

def recommend1(name):
    
    # Create a list to put top restaurants
    recommend_restaurant = []
    indices=pd.read_csv("./file1.csv")
    df_percent=pd.read_csv("./file2.csv")
    # Find the index of the hotel entered
    idx = indices[indices['name'] == name].index[0]
    # Find the restaurants with a similar cosine-sim value and order them from bigges number
    score_series = pd.Series(cosine_similarities[idx]).sort_values(ascending=False)
    
    # Extract top 30 restaurant indexes with a similar cosine-sim value
    top30_indexes = list(score_series.iloc[0:31].index)
    
    # Names of the top 30 restaurants
    for each in top30_indexes:
        recommend_restaurant.append(list(df_percent.index)[each])
    
    # Creating the new data set to show similar restaurants
    df_new = pd.DataFrame(columns=['cuisines', 'Mean Rating', 'cost','name'])
    
    # Create the top 30 similar restaurants with some of their columns
    for each in recommend_restaurant:
        df_new = df_new.append(pd.DataFrame(df_percent[['cuisines','Mean Rating', 'cost','name']][df_percent.index == each].sample()))
 
    # Drop the same named restaurants and sort only the top 10 by the highest rating
    df_new = df_new.drop_duplicates(subset=['cuisines','Mean Rating', 'cost','name'], keep=False)
    df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(10)
    l=df_new["name"].values.tolist()
    
    print('TOP %s RESTAURANTS LIKE %s WITH SIMILAR REVIEWS: ' % (str(len(df_new)), name))

    return (l)   
  
