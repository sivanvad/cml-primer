import sys
import pandas as pd
#import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

import mlflow
import mlflow.sklearn

# import hyperparams
from hyperparams import parameters

exp = sys.argv[1]

mlflow.set_experiment(exp)

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


if __name__ == "__main__":
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

    #parameters = {'classifier__n_estimators': [100, 150, 200, 250, 300], 'classifier__max_depth': list(range(1, 20, 5)), 
    #              'classifier__min_samples_split': np.arange(0.1, 1.0, 0.5), 'classifier__min_samples_leaf': np.arange(0.1, 0.5, 0.2)}
    
    with mlflow.start_run():
        optimizer = GridSearchCV(clf, parameters)
        model = optimizer.fit(X_train, y_train)

        best_score = model.best_score_
        best_estimator = model.best_estimator_

        rf_clf_params = best_estimator.steps[1][1].get_params()

        params_in = ['n_estimators', 'max_depth', 'min_samples_leaf', 'min_samples_split']

        for p in params_in:
            mlflow.log_param(p, rf_clf_params[p])

        mlflow.log_metric('best_score', best_score)
        mlflow.sklearn.log_model(best_estimator, "model", registered_model_name="testmodel")