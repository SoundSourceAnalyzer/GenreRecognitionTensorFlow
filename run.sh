#!/usr/bin/env bash

sudo docker run -p 8888:8888 -v /data/team-project/GenreRecognitionTensorFlow:/notebooks -it --rm pcej/tensor-with-yaafe:latest           
