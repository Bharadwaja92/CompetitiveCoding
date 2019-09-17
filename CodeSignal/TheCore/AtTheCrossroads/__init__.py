days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# pm = [i for i in range(12) if days[i] == 30]
# print(pm)
# print([days[i] for i in pm])

pm = [i for i in range(12) if days[i] == 31]
print(pm)
print([days[i] for i in pm])
