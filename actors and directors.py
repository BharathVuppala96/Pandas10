import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df=actor_director.groupby(['actor_id','director_id']).count().reset_index()
    df=df[df['timestamp']>=3]
    return df[['actor_id','director_id']]