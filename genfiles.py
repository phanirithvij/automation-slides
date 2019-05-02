"""
This file generates three directories
"""
import os
import errno

ROLLS = [20171158, 20171160, 20171038]
# ROLLS = [20171158]

for roll in ROLLS:
    try:
        os.makedirs(str(roll))
    except OSError as e_snake:
        if e_snake.errno != errno.EEXIST:
            raise OSError

    os.system(f"rm -r src/__pycache__ src/2017*")    # 1
    os.system(f"cp -r src/* {roll}/")                # 2
    os.system(f"mv {roll}/main.py {roll}/{roll}.py") # 3

    with open(f"{roll}/config.py", "w+") as config:  # 4 order is important
        config.write(f"ROLL = {roll}")
