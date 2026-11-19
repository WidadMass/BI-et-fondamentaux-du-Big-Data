FROM apache/spark:4.3.0-python3

USER root
RUN python3 -m pip install --no-cache-dir jupyterlab nbformat nbclient nbconvert ipykernel pandas matplotlib \
    && python3 -m ipykernel install --sys-prefix --name pyspark --display-name PySpark \
    && mkdir -p /home/spark /tmp/jupyter-runtime \
    && chown -R spark:spark /home/spark /tmp/jupyter-runtime

ENV HOME=/home/spark
ENV JUPYTER_RUNTIME_DIR=/tmp/jupyter-runtime
ENV SPARK_HOME=/opt/spark
ENV PYTHONPATH=/opt/spark/python:/opt/spark/python/lib/pyspark.zip:/opt/spark/python/lib/py4j-0.10.9.9-src.zip

USER spark
EXPOSE 8888
