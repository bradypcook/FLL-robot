#These pieces of code are blocks to set up both the Force and Color sensors that come with the robot.

from spike import PrimeHub, MotorPair, Motor, ColorSensor, DistanceSensor
from spike.control import wait_for_seconds

#Color Sensor (can sense colors using the camera attachment)
#Initializing necessary sensors/components
hub = PrimeHub()
wheels = MotorPair('C', 'D')
motor_e = Motor('E')
color_sensor = ColorSensor('B')
distance_sensor = DistanceSensor('F')

# Color condition for sensor to recognize (if color is AAA, then BBB)
if color_sensor.get_color() == 'white':  # Replace w/color of choice
    wheels.start(steering=100, speed=50)  # Turns right
else:
    wheels.start(steering=-100, speed=50)  # Turns left
    wheels.move(20, 'rotations', speed=-50)

#Distance condition for sensor to recognize (if color is detected with XYZ distance)
if distance_sensor.get_distance_cm() < 10:
    wheels.stop()
    motor_e.run_for_degrees(-75)  
    hub.speaker.beep(60, 0.2)

#Force Sensor (how hard the robot is pushing against something)
#Initializing necessary sensors/components (similar to above)
hub = PrimeHub()
wheels = MotorPair('C', 'D')
motor_e = Motor('E')
button_a = ForceSensor('A')

# Start moving forward
wheels.start(0, 50)  

# Check if button is pressed
if button_a.is_pressed():
    wheels.stop()
    
    motor_e.set_default_speed(100)
    motor_e.run_for_degrees(100)
    motor_e.run_for_degrees(-120)
    
    wheels.move_for_seconds(2, 'backward')
    
    wheels.move(0.5, 'rotations', steering=-65)
    
    wheels.move_for_seconds(2, 'forward')