import numpy as np

#Run 2
#parameters = {'classifier__n_estimators': list(range(250,350,25)), 'classifier__max_depth': list(range(13, 18, 1)), 
#              'classifier__min_samples_split': np.arange(0.2, 0.8, 0.2), 'classifier__min_samples_leaf': np.arange(0.1, 0.3, 0.1)}

# Run 3
#parameters = {'classifier__n_estimators': list(range(250,300,10)), 'classifier__max_depth': list(range(13, 18, 1)), 
#              'classifier__min_samples_split': np.arange(0.5, 0.9, 0.1), 'classifier__min_samples_leaf': np.arange(0.1, 0.2, 0.1)}

# Run 4
parameters = {'classifier__n_estimators': list(range(250,290,1)), 'classifier__max_depth': list(range(14, 19, 1)), 
              'classifier__min_samples_split': np.arange(0.6, 1.0, 0.1), 'classifier__min_samples_leaf': [0.1]}
