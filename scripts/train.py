import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn

mlflow.set_experiment('uci_creditcard')
mlflow.start_run()
mlflow.sklearn.autolog()

pd_df = pd.read_csv('/home/cdsw/data/UCI_Credit_Card.csv.zip', compression='zip')

cat_cols = ['SEX', 'EDUCATION', 'MARRIAGE', 'AGE_GROUP']
numeric_cols = list(set(pd_df.columns) - set(cat_cols) - set(['ID', 'default.payment.next.month', 'AGE']))
pay_late_cols = ['PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5' , 'PAY_6']


def get_bill_ratio(df):
    blr_cols = []
    bins= [20, 30, 40, 50, 60, 100]
    labels = [1, 2, 3, 4, 5]
    
    for mth in range(1, 7, 1):
        blr_cols.append(['BLR'+str(mth), 'BILL_AMT'+str(mth)])
    
    for col_blr in blr_cols:
        df[col_blr[0]] = df[col_blr[1]] / df_clean['LIMIT_BAL']

    return df

def get_age_group(df):
    bins= [20, 30, 40, 50, 60, 100]
    labels = [1, 2, 3, 4, 5]
    df['AGE_GROUP'] = pd.cut(df['AGE'], bins=bins, labels=labels, right=False)
    df = df.drop('AGE', axis=1)
    
    return df



# Data Cleansing
pd_df = pd_df.drop(['ID'], axis=1)

df_clean = pd_df.replace({'EDUCATION': {0 : 5, 6: 5}})
df_clean = df_clean.replace({'MARRIAGE' : {0: 3}})

for col in pay_late_cols:
    df_clean.loc[df_clean[col] < 0, col] = 0

# Feature Engineering
df_ftr_1 = get_bill_ratio(df_clean)
df_ftr = get_age_group(df_ftr_1)

#Train Test split
X = df_ftr.drop('default.payment.next.month', axis=1).copy()
y = df_ftr['default.payment.next.month'].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=4)


# Model Training
scaler = Pipeline(
    steps=[("scaler", StandardScaler())]
)

one_hot_encoder = Pipeline(
    steps=[('encoder', OneHotEncoder())]
)

rf_clf = RandomForestClassifier(class_weight = "balanced")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", scaler, numeric_cols),
        ("cat", one_hot_encoder, cat_cols),
    ]
)

clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", rf_clf)]
)

parameters = {'classifier__n_estimators': [100, 200]}

optimizer = GridSearchCV(clf, parameters)

model = optimizer.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

mlflow.log_metric('train_score', train_score)
mlflow.log_metric('test_score', test_score)

mlflow.end_run()