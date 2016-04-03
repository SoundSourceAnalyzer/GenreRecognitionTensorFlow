FROM b.gcr.io/tensorflow/tensorflow:latest
MAINTAINER Pawel Cejrowski <pcejrowski@gmail.com>
RUN pip install scikit-learn
RUN rm -rf /notebooks/*
#todo: trzeba dorobic instalacje yaafe...
ADD *.ipynb /notebooks/
WORKDIR /notebooks
CMD ["/run_jupyter.sh"]
