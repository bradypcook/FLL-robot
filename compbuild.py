# This code will only truly run in the LEGO Education SPIKE PRIME Environment, since it utilizes MicroPython
#As a result, the import statements will appear missing if ran in VScode.

from spike import PrimeHub, MotorPair, Motor
from spike.control import wait_for_seconds

# Initializes the hub and motors
hub = PrimeHub()
wheels = MotorPair('C', 'D')
wheels.set_default_speed(40)

#Mission #4 Movements
wheels.move_for_seconds(3.5, 'forward')
wheels.move(265, 'degrees', steering=-70)
wheels.move_for_seconds(2.65, 'forward')
wheels.move(65, 'degrees', steering=100)
wheels.move_for_seconds(1, 'forward')
wheels.move(65, 'degrees', steering=100)
wheels.move(0.2, 'rotations')

# Initializes E motor used for Mission #4
hub.port.E.motor.set_default_speed(10)
hub.port.E.motor.run_to_position(310, 'shortest path')
hub.port.E.motor.run_to_position(310, 'shortest path')

# Returning back to Right Base (a safe area)
wheels.move_for_seconds(1, 'forward')
wheels.move(265, 'degrees', steering=-65)
wheels.move_for_seconds(3, 'forward')
wheels.set_default_speed(50)
wheels.move(0.52, 'rotations')

# Mission #6
hub.port.E.motor.set_default_speed(10)
hub.port.E.motor.run_to_position(30, 'shortest path')
wheels.set_default_speed(25)
wheels.set_default_speed(50)
hub.port.E.motor.run_to_position(0, 'shortest path')

# Turns on light briefly to confirm successful code run
hub.light_matrix.show_image('HAPPY')
wait_for_seconds(0.1)
hub.light_matrix.off()


wheels.move_for_seconds(1, 'forward')
wheels.move(270, 'degrees', steering=50)
wheels.move_for_seconds(2.5, 'forward')

# Allows for physical repositioning for last mission
wait_for_seconds(2)

#Final Mission
wheels.move(-0.25, 'rotations')  
wheels.move(0.5, 'rotations', steering=65)  
wheels.move_for_seconds(1.5, 'forward')