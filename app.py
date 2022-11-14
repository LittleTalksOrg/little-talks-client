import requests, signal

#https://stackoverflow.com/questions/1335507/keyboard-input-with-timeout
TIMEOUT = 5


def get_server():
    global server
    server=input("Type your server! (blank for http://127.0.0.1:5000) \n")
    if server=='':
        server='http://127.0.0.1:5000'
    
def get_nickname():
    global nickname
    nickname=input("Type a nickname! \n")

def get_location():
    global lat
    global lng
    lat=input("Type your location (latitude, longitude)! (you can check on google maps) \n")
    if len(lat.split(',')) == 2:
        lng=lat.split(',')[1]
        lat=lat.split(',')[0]
    else:
        lng=input("Type your longitude location! (you can check on google maps) \n")

def cmon():
    global nickname
    global lat
    global lng
    
    signal.alarm(TIMEOUT)
    mytext = input("type:\n")
    signal.alarm(0)

    if mytext == '/exit':
        exit()
    
    elif mytext == '/nickname':
        get_nickname()
        cmon()
        return True
    
    elif mytext == '/location':
        get_location()
        cmon()
        return True
    
    else:
        send_msg(mytext)
        cmon()

def send_msg(mytext):
    data = {
                'msg':mytext,
                'nickname':nickname,
                'lat':lat,
                'lng':lng,
            }
    r = requests.post(server+'/', data = data)
    print(r.text)

def get_msgs(signum, frame):
    print(' refreshing...\n')
    send_msg(mytext='')
    print('type:')
    signal.alarm(TIMEOUT)
signal.signal(signal.SIGALRM, get_msgs)

get_server()
get_nickname()
get_location()
cmon()
