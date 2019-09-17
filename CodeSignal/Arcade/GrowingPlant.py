"""
Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due to the
lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when
the height of the plant will reach a certain level.

Example

For upSpeed = 100, downSpeed = 10, and desiredHeight = 910, the output should be
growingPlant(upSpeed, downSpeed, desiredHeight) = 10.
"""


def growingPlant(upSpeed, downSpeed, desiredHeight):
    days, ht = 1, upSpeed
    while ht < desiredHeight:
        days += 1
        ht -= downSpeed
        print('Ht is ', ht)
        ht += upSpeed
        print('Ht is ', ht)
        print('\tDay', days,' Height is', ht)
    return days


upSpeed = 100
downSpeed = 10
desiredHeight = 910

# upSpeed= 10
# downSpeed= 9
# desiredHeight= 4

print(growingPlant(upSpeed, downSpeed, desiredHeight))