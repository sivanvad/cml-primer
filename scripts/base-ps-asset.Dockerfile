FROM docker.repository.cloudera.com/cloudera/cdsw/ml-runtime-jupyterlab-python3.10-standard:2023.12.1-b8

# Copy required files
COPY ./requirements.txt /tmp/requirements.txt
 
# Upgrade packages in the base image
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y build-essential && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install standard packages required
RUN pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

# Override Runtime label and environment variables metadata
ENV ML_RUNTIME_EDITION="PS Project base runtime" \
    ML_RUNTIME_SHORT_VERSION="2024.1" \
    ML_RUNTIME_MAINTENANCE_VERSION="1" \
    ML_RUNTIME_FULL_VERSION="2024.1.1" \
    ML_RUNTIME_DESCRIPTION="This is the base runtime for PS asset project"


LABEL com.cloudera.ml.runtime.edition=$ML_RUNTIME_EDITION \
      com.cloudera.ml.runtime.full-version=$ML_RUNTIME_FULL_VERSION \
      com.cloudera.ml.runtime.short-version=$ML_RUNTIME_SHORT_VERSION \
      com.cloudera.ml.runtime.maintenance-version=$ML_RUNTIME_MAINTENANCE_VERSION \
      com.cloudera.ml.runtime.description=$ML_RUNTIME_DESCRIPTION