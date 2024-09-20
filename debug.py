from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
 
class debug:
    def __init__(self, motorA, motorB, motorC, motorD, speed, angle):
        '''
        motorA: port for the first Motor
        motorB: port for the second Motor
        motorC: port for the third Motor
        motorD: port for the fourth Motor
        forceSensor: port for the force sensor
        '''
        self.speed = speed
        self.angle = angle
        self.motorA = Motor(port=motorA)
        self.motorB = Motor(port=motorB)
        self.motorC = Motor(port=motorC)
        self.motorD = Motor(port=motorD)
   
    def turnA(self, direction):
        '''
        direction: turn direction. 1 is clockwise, 2 is counterclockwise
        '''
        print("Motor A")
        if direction == 1:
            angle = self.angle
        else:
            angle = self.angle - 2*self.angle
        self.motorA.run_angle(self.speed, angle)
   
    def turnB(self, direction):
        '''
        direction: turn direction. 1 is clockwise, 2 is counterclockwise
        '''
        print("Motor B")
        if direction == 1:
            angle = self.angle
        else:
            angle = self.angle - 2*self.angle
        self.motorB.run_angle(self.speed, angle)
   
    def turnC(self, direction):
        '''
        direction: turn direction. 1 is clockwise, 2 is counterclockwise
        '''
        print("Motor C")
        if direction == 1:
            angle = self.angle
        else:
            angle = self.angle - 2*self.angle
        self.motorC.run_angle(self.speed, angle)
   
    def turnD(self, direction):
        '''
        direction: turn direction. 1 is clockwise, 2 is counterclockwise
        '''
        print("Motor D")
        if direction == 1:
            angle = self.angle
        else:
            angle = self.angle - 2*self.angle
        self.motorD.run_angle(self.speed, angle)

    def temp(self):
        pass
