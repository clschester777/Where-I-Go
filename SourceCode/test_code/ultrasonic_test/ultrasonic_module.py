import RPi.GPIO as gpio
import time

info = {}

def distance_level(trig, echo) :
	gpio.output(trig, False)
	time.sleep(0.2)

	gpio.output(trig, True)
	time.sleep(0.00001)
	gpio.output(trig, False)

	while gpio.input(echo) == 0 :
		pulse_start = time.time()

	while gpio.input(echo) == 1 :
		pulse_end = time.time()			

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17000
	distance = round(distance, 2)

	# specify figure is modified after test

	if 0 <= distance and distance < 100 :
		level = 0
	elif 100 <= distance and distance < 200 :
		level = 1
	elif 200 <= distance and distance < 300 :
		level = 2
	else :
		level = False

	return level

def speaker_out() :
	if info["LH"] == 0 :
		print "Sound Size : 100, Left Speaker sounds out highly"
	elif info["LH"] == 1 :
		print "Sound Size : 50, Left Speaker sounds out highly"
	elif info["LH"] == 2 :
		print "Sound Size : 10, Left Speaker sounds out highly"

	if info["LL"] == 0 :
		print "Sound Size : 100, Left Speaker sounds out lowly"
	elif info["LL"] == 1 :
		print "Sound Size : 50, Left Speaker sounds out lowly"
	elif info["LL"] == 2 :
		print "Sound Size : 10, Left Speaker sounds out lowly"

	if info["RH"] == 0 :
		print "Sound Size : 100, Right Speaker sounds out highly"
	elif info["RH"] == 1 :
		print "Sound Size : 50, Right Speaker sounds out highly"
	elif info["RH"] == 2 :
		print "Sound Size : 10, Right Speaker sounds out highly"

	if info["RL"] == 0 :
		print "Sound Size : 100, Right Speaker sounds out lowly"
	elif info["RL"] == 1 :
		print "Sound Size : 50, Right Speaker sounds out lowly"
	elif info["RL"] == 2 :
		print "Sound Size : 10, Right Speaker sounds out lowly"

def motor_out() :
	print "motor_out"

gpio.setmode(gpio.BCM)

RH_trig = 2
RH_echo = 3

RL_trig = 23
RL_echo = 22

FH_trig = 27
FH_echo = 18

FL_trig = 25
FL_echo = 9

LH_trig = 17
LH_echo = 4

LL_trig = 24
LL_echo = 10

print "start"

gpio.setup(RH_trig, gpio.OUT)
gpio.setup(RH_echo, gpio.IN)

gpio.setup(RL_trig, gpio.OUT)
gpio.setup(RL_echo, gpio.IN)

gpio.setup(FH_trig, gpio.OUT)
gpio.setup(FH_echo, gpio.IN)

gpio.setup(FL_trig, gpio.OUT)
gpio.setup(FL_echo, gpio.IN)

gpio.setup(LH_trig, gpio.OUT)
gpio.setup(LH_echo, gpio.IN)

gpio.setup(LL_trig, gpio.OUT)
gpio.setup(LL_echo, gpio.IN)

try :
	while True :

		info["RH"] = distance_level(RH_trig, RH_echo)
		info["RL"] = distance_level(RL_trig, RL_echo)
		info["FH"] = distance_level(FH_trig, FH_echo)
		info["FL"] = distance_level(FL_trig, FL_echo)
		info["LH"] = distance_level(LH_trig, LH_echo)
		info["LL"] = distance_level(LL_trig, LL_echo)

		print info

except :
	print "except"
	gpio.cleanup()
