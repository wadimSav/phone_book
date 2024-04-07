import pandas as pd
import random
from sklearn.preprocessing import OneHotEncoder

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

encoder = OneHotEncoder(handle_unknown='ignore')

encoder_df = encoder.fit_transform(data[['whoAmI']]).toarray()

final_df = pd.DataFrame(encoder_df, columns = encoder.categories_[0])

final_df.head()