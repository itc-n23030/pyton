import time, sys
def indent():
    indent = 0
    try:
        while True:
            if indent == 20:
                for i in reversed(range(20)):
                    time.sleep(0.1)
                    print(f"{' '*i}********")
                    indent -= 1
            else:
                time.sleep(0.1)
                indent+=1
                print(f"{' '*indent}********")

    except KeyboardInterrupt:
        sys.exit()

indent()

            

