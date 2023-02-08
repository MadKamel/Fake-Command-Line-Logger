unames = ['root', 'guest']
pwords = ['toor', '']
privs = [True, False]
username = None

def check_user_credentials(username, password):
    if username in unames:
        if pwords[unames.index(username)] == password:
            return True
    return False

def loghandle(message):
    logfile = open('00.log', 'at')
    logfile.write(message)
    logfile.close()

def log(message, urgency = 0):

    if urgency == 1:
        loghandle('\n[!!!] ' + message)
    elif urgency == 2:
        loghandle('\n[***] ' + message)
    else:
        loghandle('\n[---] ' + message)

log('===SYSTEM START!===')
while True:
    uIn = input('\n>')
    if username == None:
        log('logged-out user: >' + uIn, 2)
    else:
        log(username + ': >' + uIn, 2)

    #login command
    if uIn[0:5] == 'login':
        if uIn[6:] == '':
            zz_username = input('username: ')
        else:
            zz_username = uIn[6:]
        zz_password = input('password: ')
        log('login attempt:')
        log('\tusername: ' + zz_username)
        log('\tpassword: ' + zz_password)
        if check_user_credentials(zz_username, zz_password):
            username = zz_username
            log('user ' + username + ' has logged in.')
            print('logged in as ' + username)
        else:
            log('user login failed', 1)
            print('login failed')

    #logout command
    elif uIn[0:6] == 'logout':
        if username == None:
            log('logout attempt with logged-out user')
            print('already logged out')
        else:
            log('user ' + username + ' has logged out')
            username = None
            print('logged out')

    #whoami command
    elif uIn[0:6] == 'whoami':
        if username == None:
            print('not logged in')
        else:
            print('logged in as ' + username)

    #exit command
    elif uIn[0:4] == 'exit':
        log('===SYSTEM STOP!===')
        exit()
