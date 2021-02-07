import pyaudio
import wave
from numpy import sin, cos, pi, linspace
from numpy.random import randn
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
# from matplotlib.pyplot import plot, legend, show, hold, grid, figure, savefig
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

def phaseSpace(samples):
    for k in xrange(1, 10, 1):
        ph = []

        for i in xrange(2 * k, len(samples), 1):
            ph += [(samples[i], samples[i - k], samples[i - 2 * k])]

        # plt.plot([t[0] for t in ph], [t[1] for t in ph], 'o')

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # ax.scatter([t[0] for t in ph], [t[1] for t in ph], [t[2] for t in ph])
        # plt.title("K = {0}".format(k))
        # plt.show()

        for i in xrange(len(ph)):
            curPoint = ph[i]

            for j in xrange(i + 1, len(ph), 1):
                perLen = j - i
                assert perLen > 0

                if curPoint == ph[j]:
                    print "PERIOD DETECTED, P = {0}, k = {1}, PL = {2}".format(curPoint, k, perLen)
                    raw_input()
                    pass

def combFilter(fftSamples):
    d = 3
    a, b, c = 0.2, 0.1, 0.7

    comb = []

    for i in xrange(d, len(fftSamples), 1):
        curVal = a * fftSamples[i] + b * fftSamples[i - d]
        # print i, d, len(comb)

        if i > d:
            curVal += c * comb[i - d - 1]

        comb += [curVal]

    # plt.plot([i for i in xrange(len(fftSamples))], fftSamples, '-')
    plt.plot([i for i in xrange(len(comb))], comb, '-')
    plt.show()

    pass

wf = wave.open('DWK_violin.wav', 'rb')
frame =  wf.getnframes()
print frame

sampFreq = wf.getframerate()
print sampFreq

chunk = 2048

sampFile = wf.getsampwidth()
print sampFile

# sampFrame = np.blackman(chunk)
# print len(sampFrame)
# print sampFrame

p = pyaudio.PyAudio()
streamWave = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = sampFreq,
                output = True)

dataFile = wf.readframes(chunk)

while len(dataFile) == chunk * sampFile: # until the end of file
    streamWave.write(dataFile) # Play sounds

    inData = np.array(wave.struct.unpack("%dh"%(len(dataFile)/sampFile), dataFile))
    # phaseSpace(inData)

    fftData = (abs(np.fft.rfft(inData)) ** 2)
    combFilter(fftData)

    maxFreq = fftData.argmax()

    if maxFreq < len(fftData) - 1:
        y0,y1,y2 = np.sin(fftData[maxFreq : maxFreq + 3])
        # print y0, y1, y2

        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        theFreq = ((maxFreq + x1) * sampFreq / chunk)
        print ("The freq is %f Hz." % (theFreq))
   
    dataFile = wf.readframes(chunk)

if dataFile:
    streamWave.write(dataFile)
streamWave.close()

p.terminate()
