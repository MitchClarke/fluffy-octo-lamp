from Thermostat import Thermostat
from Thermometer import Thermometer
from Timer import Timer
from time import sleep
from Triggerable import Triggerable

Triggerable(25).off()
Triggerable(8).off()

gpio_config = [
    {
        "name": 'top_timer_pin',
        "trigger": Triggerable(23),
        "type": Timer
    },
    {
        "name": 'bottom_timer_pin',
        "trigger": Triggerable(12),
        "type": Timer

    },
    {
        "name": 'top_radiant_pin',
        "trigger": Triggerable(16),
        "type": Thermostat,
        "thermometer": Thermometer(21)
    },
    {
        "name": 'top_radiant_pin',
        "trigger": Triggerable(20),
        "type": Thermostat,
        "thermometer": Thermometer(24)
    }
]


def create_object(config_item):
    if config_item['type'] == Thermostat:
        new_obj = Thermostat(config_item["thermometer"], config_item["trigger"])
    else:
        new_obj = Timer(config_item["trigger"])
    new_obj.name = config_item.name
    return new_obj


BOTTOM_THERMOMETER_PIN = 17
TOP_THERMOMETER_PIN = 27

if __name__ == "__main__":

    envControls = map(gpio_config, create_object)

    try:
        while True:
            for component in envControls:
                if isinstance(component, Timer):
                    component.run()
            sleep(30)
    except KeyboardInterrupt:
        print 'You killed me :( '
