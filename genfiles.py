import os, errno

ROLLS = [20171158, 20171160, 20171038]
# ROLLS = [20171158]

for roll in ROLLS:
    try:
        os.makedirs(str(roll))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    os.system(f"cp -r src/* {roll}/")                # 1
    os.system(f"mv {roll}/main.py {roll}/{roll}.py") # 2

    with open(f"{roll}/config.py", "w+") as config:  # 3 order is important
        config.write(f"ROLL = {roll}")
