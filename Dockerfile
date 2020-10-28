FROM tensorflow/tensorflow:latest-gpu-py3-jupyter

RUN apt install wget

RUN pip install scikit-learn && \
    pip install pandas && \
    pip install seaborn && \
    pip install sklearn && \
    pip install xlrd && \
    pip install kaggle && \
    pip install tensorflow-hub && \
    pip install tensorflow-datasets && \
    pip install nltk && \
    pip install scikit-surprise

CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/tf --ip 0.0.0.0 --no-browser --allow-root"]
