import pigpio
import time
import asyncio
import math
pi1 = pigpio.pi()

#set range to allow for .5/1 second total times
pi1.set_PWM_range(13, 250)
pi1.set_PWM_range(19, 250)
pi1.set_PWM_range(26, 250)

#set PWM to default frequency (to allow for smooth brightness transition)
pi1.set_PWM_frequency(13, 800)
pi1.set_PWM_frequency(19, 800)
pi1.set_PWM_frequency(26, 800)

#function to slowly ramp up then down a single pin using PWM
async def breatheLED(pin):
	for duty in range(0,100):
		val = 0 - .5*math.cos(2*math.pi*duty/100)+.5
		pi1.set_PWM_dutycycle(pin, val*249)
		await asyncio.sleep(.01)
async def main():
	while True:
		#1. turn off all lights
		pi1.write(13, 0)
		pi1.write(19, 0)
		pi1.write(26, 0)
		#2. delay 1 second
		time.sleep(1)
		#3,4,5. breathe red, green, blue
		await breatheLED(19)
		await breatheLED(26)
		await breatheLED(13)

		#6. use async to run all 3 at same time, breathing white
		t1 = asyncio.create_task(breatheLED(19))
		t2 = asyncio.create_task(breatheLED(13))
		t3 = asyncio.create_task(breatheLED(26))
		await t1
		await t2
		await t3

asyncio.run(main())
