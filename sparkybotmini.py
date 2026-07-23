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
        
        robot.set_motor(0, 0, 0, 0)
        
        def movement(key, msleep):
                if key == "w":
                        robot.set_motor(50, 50, 50, 50) # forward
                elif key == "a":
                        robot.set_motor(-50, 50, 50, -50) # left
                elif key == "x":
                        robot.set_motor(-50, -50, -50, -50) # backward
                elif key == "d":
                        robot.set_motor(50, -50, -50, 50) # right
                elif key == "q":
                        robot.set_motor(0, 50, 50, 0) # front left
                elif key == "c":
                        robot.set_motor(0, -50, -50, 0) # back right
                elif key == "z":
                        robot.set_motor(-50, 0, 0, -50) # back left
                elif key == "e":
                        robot.set_motor(50, 0, 0, 50) # front right
                elif key == "r":
                        robot.set_motor(-50, -50, 50, 50) # turn left
                elif key == "t":
                        robot.set_motor(50, 50, -50,  -50) # turn right
                elif key == "b":
                        robot.beep(200) # honk the horn
                time.sleep(msleep)
                robot.set_motor(0, 0, 0, 0)
        
        key_input = ""
        
        roll, pitch, yaw = robot.get_attitude(degrees=True)
        print(f"? Attitude: Roll={roll:.1f}° Pitch={pitch:.1f}° Yaw={yaw:.1f}°")
        
        # Move forward: all motors positive
        while key_input != " ":
                key_input = input("")
                
                movement(key_input, 0.3)
                
                # rotation correction
                
                """roll, pitch, yaw = robot.get_attitude(degrees=True)
                print(f"? Attitude: Roll={roll:.1f}° Pitch={pitch:.1f}° Yaw={yaw:.1f}°")
                
                robot.set_motor(0, 0, 0, 0)
                
                goal_yaw = round(yaw / 90) * 90
                if goal_yaw < yaw:
                        while goal_yaw < (round(yaw)):
                                robot.set_motor(20, 20, -20, -20)
                                roll, pitch, yaw = robot.get_attitude(degrees=True)
                                print(f"Yaw: {yaw}, Goal: {goal_yaw}")
                else:
                        while goal_yaw > (round(yaw)):
                                robot.set_motor(-20, -20, 20, 20)
                                roll, pitch, yaw = robot.get_attitude(degrees=True)
                                print(f"Yaw: {yaw}, Goal: {goal_yaw}")"""
                
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
