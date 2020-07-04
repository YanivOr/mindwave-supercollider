'''
attention, meditation, rawValue, delta, theta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal, blinkStrength 

$ pip install pyserial
$ pip install NeuroPy
$ pip install pyosc
'''

from NeuroPy import NeuroPy
import OSC
import time

neuroPy = NeuroPy("/dev/rfcomm0", 57600)
neuroPy.start()

oscClient = OSC.OSCClient()
oscClient.connect(('127.0.0.1', 57120))

while True:
  attention = neuroPy.attention
  meditation = neuroPy.meditation

  oscMsg = OSC.OSCMessage()
  oscMsg.setAddress("/neuro")
  oscMsg.append([attention, meditation])

  oscClient.send(oscMsg)

  print "attention: " + str(attention) + " - " + "meditation: " + str(meditation)

  time.sleep(0.1)
