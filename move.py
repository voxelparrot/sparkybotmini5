#!/usr/bin/env python3
# coding: utf-8
"""
SparkyBotMini5 Simple Forward Movement
"""

import time
from sparkybotmini import SparkyBotMini


if __name__ == "__main__":
    # Create robot instance
    robot = SparkyBotMini(port="/dev/ttyUSB0", debug=True)
    
    try:
        # Connect
        if not robot.connect():
            exit(1)
        
        print("\n? Moving forward...\n")
        
        key = ""
        
        # Move forward: all motors positive
        while key != " ":
                key = input("")
                if key == "w":
                        robot.set_motor(50, 50, 50, 50) # forward
                elif key == "a":
                        robot.set_motor(-50, 50, 50, -50) # left
                elif key == "s":
                        robot.set_motor(-50, -50, -50, -50) # backward
                elif key == "d":
                        robot.set_motor(50, -50, -50, 50) # right
                elif key == "q":
                        robot.set_motor(-50, -50, 50, 50) # turn left
                elif key == "e":
                        robot.set_motor(50, 50, -50,  -50) # turn right
                elif key == "b":
                        robot.beep(200) # honk the horn
                time.sleep(0.3)
                robot.set_motor(0, 0, 0, 0)
        
        # Stop
        robot.set_motor(0, 0, 0, 0)
        print("\n? Stopped!\n")
        
    except KeyboardInterrupt:
        print("\n\n? Interrupted by user")
    
    finally:
        robot.set_motor(0, 0, 0, 0)
        robot.disconnect()
        print("? Goodbye!")
