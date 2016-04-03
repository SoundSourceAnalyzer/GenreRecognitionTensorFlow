# W zwiazku z tym, ze narazie nie mamy wlasnego wyciagania feature'ow uzywamy do tego YAAFE
# Moze moglibysmy uzyc tego rowniez potem zamiast pisac cos swojego...

# TODO: owinac calosc w docker razem z TensorFlowem
# TODO: wciagnac skrypt dataSetPreparation tak, zeby rowniec pobieral dane
from __future__ import print_function
import os

from yaafelib import *


def get_features(audio_file):
    print('Getting features from ' + audio_file)
    fp = FeaturePlan(sample_rate=22050, normalize=1)  # sample rate of the .wav files TODO:check if only this
    # Features that seems to be most often used, so they are good to start with.
    fp.addFeature('mfcc: MFCC')
    fp.addFeature('zcr: ZCR')
    fp.addFeature('spectral_shape: SpectralShapeStatistics')
    fp.addFeature('lsf: LSF')
    fp.addFeature('magnitudeSpectrum: MagnitudeSpectrum')
    df = fp.getDataFlow()
    engine = Engine()
    engine.load(df)
    afp = AudioFileProcessor()
    afp.setOutputFormat('csv', 'output', {'Precision': '8', 'Metadata': 'False'})
    afp.processFile(engine, audio_file)
    engine.flush()


# get_features('/data/team-project/genres/rock/rock.00050.wav')

dataset = '/data/team-project/genres/'
for genre in os.listdir(dataset):
    for sample in os.listdir(dataset + genre):
        if sample.endswith('.wav'):
            absPath = dataset + genre + '/' + sample
            get_features(absPath)
