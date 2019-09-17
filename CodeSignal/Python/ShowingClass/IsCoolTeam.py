""""""
"""
You are organizing a team of eSportsmen, and you are determined to make it cool. You are already thinking about winning 
the world championship: when it happens, the names of your teammates will be chanted one after another by a large 
audience. You believe that it will sound cool if and only if the first letter of one player's name will be the same as 
the last letter in the name of the player before them.

Now you are considering one particular team. Its members are definitely professional gamers, but you're not sure if all 
together they form a cool team. Implement a function that will check if the team is cool.

Example

For team = ["Mark", "Kelly", "Kurt", "Terk"], the output should be
isCoolTeam(team) = true.

The following team announcement will sound cool: "Mark", "Kurt", "Terk", "Kelly".

"""

class Team(object):
    def __init__(self, names):
        self.names = names

    def __nonzero__(self):
        first = [x[0].lower() for x in self.names]
        last = [x[-1].lower() for x in self.names]
        print('first is', first)
        print('last is', last)
        for f in first:
            try:
                last.remove(f)
            except:
                pass

        return len(last) == 1 or len(last) == 0


# def isCoolTeam(team):
#     return bool(Team(team))

# team = ["Mark", "Kelly", "Kurt", "Terk"]
# print(isCoolTeam(team))

def isCoolTeam(team):
    first = [x[0].lower() for x in team]
    last = [x[-1].lower() for x in team]
    print('first is', first)
    print('last is', last)

    for f in first:
        try:
            last.remove(f)
        except:
            pass

    print('last is', last)
    print(len(last))

    return False

team = ["Rob", "Bobby", "Billy"]
print(isCoolTeam(team))
