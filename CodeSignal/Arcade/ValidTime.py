"""
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.
"""

def validTime(time):
    return 0 <= int(time.split(':')[0]) <= 23 and 0 <= int(time.split(':')[1]) <= 59


time = "13:58"
time = "25:51"
time = "02:76"
print(validTime(time))