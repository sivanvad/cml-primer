# Download dataset from Kaggle
# kaggle competitions download -c amex-default-prediction

# Unzip data to local
# unzip amex-default-prediction.zip -d amex-default-prediction/

# Set STORAGE environment
python setup.py

# Copy data to s3
# hdfs dfs -cp amex-default-prediction/* ${STORAGE}/ps-ml/american-express-kaggle/data/