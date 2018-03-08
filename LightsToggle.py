
from Triggerable import Triggerable
import sys
import time 
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'Expected 3 paramters'
        sys.exit(1)
    else:
        trigger = Triggerable(int(sys.argv[1]))
        if sys.argv[2] == '1':
            trigger.on()
        elif sys.argv[2] == '0':
            trigger.off()
        time.sleep(60)
