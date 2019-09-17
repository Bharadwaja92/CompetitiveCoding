""""""
"""
While migrating to a new operation system, you faced an unexpected problem: now you need to create a new build command 
for your favorite text editor plugin. The build command is stored as a JSON file that you should now update. In order 
to make the transition simpler, you decided to write a program that will create a template of the build command by 
replacing everything but dictionaries in given jsonFile with their default values: 
numbers with 0, strings with "" and lists with [].

It is guaranteed that there are only aforementioned types in the given JSON file.
"""

from json import dumps, loads

def buildCommand(jsonFile):
    ret = {}
    ls = eval(str(jsonFile))
    for n in ls:
        if type(ls[n]) == dict:
            ret[n] = buildCommand(ls[n])
        elif type(ls[n]) == list:
            ret[n] = []
        elif type(ls[n]) == str:
            ret[n] = ''
        else:
            ret[n] = 0

    return str(ret)


jsonFile = \
    "{" \
    "\"version\": \"0.1.0\"," \
    "\"command\": \"c:python\"," \
    "\"args\": [\"app.py\"]," \
    "\"problemMatcher\": {" \
        "\"fileLocation\": [\"relative\", \"${workspaceRoot}\"]," \
        "\"pattern\": {" \
            "\"regexp\": \"^(.*)+s$\", " \
            "\"message\": 1}" \
        "}" \
    "}"

jsonFile = "{\"version\": \"0.1.0\",\"command\": \"c:python\",\"args\": [\"app.py\"],\"problemMatcher\": {\"fileLocation\": [\"relative\", \"${workspaceRoot}\"],\"pattern\": {\"regexp\": \"^(.*)+s$\", \"message\": 1}}}"

print(buildCommand(jsonFile))

# "{\"version\": \"\", \"command\": \"\", \"args\": [], \"problemMatcher\": {\"fileLocation\": [], \"pattern\": {\"regexp\": \"\", \"message\": 0}}}"
