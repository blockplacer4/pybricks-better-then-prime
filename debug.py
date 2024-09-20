from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
 
hub = PrimeHub()
 
class debug:
    def __init__(motorA, motorB, motorC, motorD):
        '''
        motorA: port for the first Motor
        motorB: port for the second Motor
        motorC: port for the third Motor
        motorD: port for the fourth Motor
        forceSensor: port for the force sensor
        '''
        self.motorA = Motor(port=motorA)
        self.motorB = Motor(port=motorB)
        self.motorC = Motor(port=motorC)
        self.motorD = Motor(port=motorD)
   
    def turnA(direction):
        '''
        direction: turn direction. 1 is clockwise, 2 is counterclockwise
        '''
        if direction == 1:
            angle = 100
        else:
            angle = -100
        await self.motorA.run_angle(angle)
   
    def turnB(direction):
        '''
        direction: turn direction. 1 is clockwise, 2 is counterclockwise
        '''
        if direction == 1:
            angle = 100
        else:
            angle = -100
        await self.motorB.run_angle(angle)
   
    def turnC(direction):
        '''
        direction: turn direction. 1 is clockwise, 2 is counterclockwise
        '''
        if direction == 1:
            angle = 100
        else:
            angle = -100
        await self.motorC.run_angle(angle)
   
    def turnD(direction):
        '''
        direction: turn direction. 1 is clockwise, 2 is counterclockwise
        '''
        if direction == 1:
            angle = 100
        else:
            angle = -100
        await self.motorD.run_angle(angle)
