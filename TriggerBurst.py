
import Triggerable
import sys
from time import sleep

if __name__ == "__main__":
    if length(sys.argv) != 4:
        print 'Expected 4 paramters'
        sys.exit(1)
    else:
        trigger = new Triggerable(sys.argv[1])
        if sys.argv[2] == '1':
            trigger.on()
            sleep(sys.argv[3])
            trigger.off()
        elif sys.argv[2] == '0':
            trigger.off()
            sleep(sys.argv[3])
            trigger.on()
