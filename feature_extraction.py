# W zwiazku z tym, ze narazie nie mamy wlasnego wyciagania feature'ow uzywamy do tego YAAFE
# Moze moglibysmy uzyc tego rowniez potem
# TODO: owinac calosc w docker razem z TensorFlowem
from __future__ import print_function
import numpy as np
import os
import sys

from yaafelib import *
def getFeatures(audiofile):
    fp = FeaturePlan(sample_rate=22050)
    fp.addFeature('mfcc: MFCC blockSize=512 stepSize=256')
    fp.addFeature('mfcc_d1: MFCC blockSize=512 stepSize=256 > Derivate DOrder=1')
    fp.addFeature('mfcc_d2: MFCC blockSize=512 stepSize=256 > Derivate DOrder=2')
    df = fp.getDataFlow()
    engine = Engine()
    engine.load(df)
    afp = AudioFileProcessor()
    afp.processFile(engine,audiofile)
    feats = engine.readAllOutputs()
    print(feats)
    afp.setOutputFormat('csv','output',{'Precision':'8'})
    afp.processFile(engine,audiofile)

getFeatures('/data/team-project/genres/rock/rock.00050.wav')

# dataset = '/data/team-project/genres/'
# for genre in os.listdir(dataset):
#     for sample in os.listdir(dataset + genre):
#         if sample.endswith('.wav'):
#             absPath = dataset + genre + '/' + sample
#             print('Working on ' + absPath)
#             getFeatures(absPath)
