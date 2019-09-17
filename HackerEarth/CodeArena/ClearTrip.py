"""
cleartrip decided that they wanted to verify the username and password of its users while they were authenticating for
a process. One of the code service forms a GET URL which contains the username and password as its parameters.
"""

# s = input('Enter URL: ')

s = 'http://www.cleartrip.com/signin/service?username=test&pwd=test&profile=developer&role=ELITE&key=manager'
s ='http://www.cleartrip.com/signin/service?username=test@123&pwd=test&123&profile=deve&loper&role=ELITE&key=manager'

un = s.find('username')
amp = s.find('&pwd')
uname = s[un+len('username')+1:amp]
print('username:',uname)

s = s[amp+1:]
pw = s.find('pwd')
amp = s.find('&profile')
pword = s[pw+len('pwd')+1:amp]
print('pwd:',pword)

s = s[amp+1:]
pf = s.find('profile')
amp = s.find('&role')
profile = s[pf+len('profile')+1:amp]
print('profile:',profile)

s = s[amp+1:]
rl = s.find('role')
amp = s.find('&key')
role = s[rl+len('role')+1:amp]
print('role:',role)

s = s[amp+1:]
ky = s.find('key')
amp = s.find('&')
key = s[rl+len('key')+1:]
print('key:',key)


print('Done')
