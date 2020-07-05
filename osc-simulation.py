'''
Generates random values for attention and meditation - values of 1 to 100
'''
import random
import time
import OSC

oscClient = OSC.OSCClient()
oscClient.connect(('127.0.0.1', 57120))

while True:
  attention = random.randint(1, 101)
  meditation = random.randint(1, 101)

  print "attention: " + str(attention) + " - " + "meditation: " + str(meditation)

  oscMsg = OSC.OSCMessage()
  oscMsg.setAddress("/neuro")
  oscMsg.append([attention, meditation])

  oscClient.send(oscMsg)

  time.sleep(0.1)
