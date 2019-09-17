""""""
"""
Harry dropped out of school to pursue his dreams and work in Pipes Corporations. He is now in charge of a lot of pipes, 
and his task is to check the gauges twice a day. By analyzing the morning and evening pressures of each pipe, 
Harry should write a report about the minimum and the maximum pressure during the day.

Given the pressures Harry wrote down for each pipe, return two lists: the first one containing the minimum, 
and the second one containing the maximum pressure of each pipe during the day.

Example

For morning = [3, 5, 2, 6] and evening = [1, 6, 6, 6],
the output should be
pressureGauges(morning, evening) = [[1, 5, 2, 6], [3, 6, 6, 6]].
"""


def pressureGauges(morning, evening):
    x = [[min(m, e) for m, e in zip(morning, evening)], [max(m, e) for m, e in zip(morning, evening)]]
    y = zip(*map(sorted, zip(morning, evening)))
    z = [list(map(min, zip(morning, evening))), list(map(max, zip(morning, evening)))]
    z1 = list(zip(*[(min( t), max( t)) for t in zip(morning, evening)]))
    return x


morning = [3, 5, 2, 6]
evening = [1, 6, 6, 6]
print(pressureGauges(morning, evening))