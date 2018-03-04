
import Triggerable
import sys

if __name__ == "__main__":
    if length(sys.argv) != 3:
        print 'Expected 3 paramters'
        sys.exit(1)
    else:
        trigger = new Triggerable(sys.argv[1])
        if sys.argv[2] == '1':
            trigger.on()
        elif sys.argv[2] == '0':
            trigger.off()
