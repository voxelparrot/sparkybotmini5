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
        
        # Move forward: all motors positive
        robot.set_motor(50, 50, 50, 50)
        time.sleep(3)
        
        # Stop
        robot.set_motor(0, 0, 0, 0)
        print("\n? Stopped!\n")
        
    except KeyboardInterrupt:
        print("\n\n? Interrupted by user")
    
    finally:
        robot.set_motor(0, 0, 0, 0)
        robot.disconnect()
        print("? Goodbye!")
