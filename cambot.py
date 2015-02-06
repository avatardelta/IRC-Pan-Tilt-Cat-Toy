import willie		
import serial
import time
from time import sleep
global ser
ser = serial.Serial('/dev/ttyACM0', 115200)
import laser as laser
@willie.module.commands('bl')
def blacks(bot, trigger):
	bot.say('ack: bl engaged')
	laser.blacklighttoggle()
@willie.module.commands('led')
def led(bot, trigger):
	bot.say('ack: laser')
	laser.ledtoggle()
@willie.module.commands('left')
def goleft(bot, trigger):
#	bot.say('ack: l')
	print('left')
	laser.left()
@willie.module.commands('right')
def goright(bot, trigger):
	print('right')
#	bot.say('ack: r')
	laser.right()
@willie.module.commands('up')
def goup(bot, trigger):
#	bot.say('ack: u')
	print('up')
	laser.up()
@willie.module.commands('down')
def godown(bot, trigger):
#	bot.say('ack: d')
	print('down')
	laser.down()
@willie.module.commands('cup')
def cup(bot, trigger):
#	bot.say('ack:c up')
	print('camera up')
	ser.write('{3 ; -1 ; 75}')
	sleep(1)
#	print("derp")
	ser.write("{3 ; 0 ; 100}")
@willie.module.commands('cdown')
def cdown(bot, trigger):
#	bot.say('ack:c down')
	print('camera down')
	ser.write('{ 3 ; 1 ; 75 }')
	sleep(1)
	ser.write('{ 3 ; 0 ; 1 }')
@willie.module.commands('cright')
def cright(bot, trigger):
#	bot.say('ack:c r')
	print('camera right')
	ser.write("{ 4 ; -1 ; 75 }")
	sleep(1)
	ser.write("{ 4 ; 0 ; 1 }")
	
@willie.module.commands('cleft')
def cleft(bot, trigger):
#	bot.say('ack:c l')
	print('camera left')
	ser.write('{ 4 ; 1 ; 75 }')
	sleep(1)
	ser.write("{ 4 ; 0 ; 1 }")

@willie.module.commands('coff')
def coff(bot, trigger):
#	bot.say('ack: cams off')
	print('Both Cam Motors Off')
	sleep(.5)
	ser.write('{ 3 ; 0 ; 0 }')
	sleep(.5)
	ser.write('{ 4 ; 0 ; 0 }')
#	sleep(.5)
#	ser.write('setzero')
@willie.module.commands('reset')
def reset(bot, trigger):
#	bot.say('Dave.')
#	bot.say("I can't let you do that Dave")
	laser.idle()
	bot.say("Critical Failure, Rebooting Universe")
#	ser.write("setzero")
#	ser.write("reset")

@willie.module.commands('setzero')
def reset_1(bot, trigger):
	ser.write('setzero')
	bot.say('no  stahp!?')
	sleep(1)
