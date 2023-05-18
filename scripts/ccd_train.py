import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer

# Read data from source
pd_df = pd.read_csv('/home/cdsw/data/UCI_Credit_Card.csv.zip', compression='zip')

# Data Cleaning
df_clean = pd_df.replace({'EDUCATION': {0 : 5, 6: 5}})
df_clean = df_clean.replace({'MARRIAGE' : {0: 3}})

# Feature Engineering
