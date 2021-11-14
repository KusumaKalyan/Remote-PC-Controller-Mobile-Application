from datetime import datetime
import pytz
import requests

from cryptography.fernet import Fernet
key = b'DAvY1K4-Mhvqb3iNS9qJhYni99Olz8Ksty3ZFKGrir4='
f = Fernet(key)

def onMachine():
    raw_time = str(datetime.now(pytz.timezone('Asia/Kolkata'))).split(' ')[1].split(':')
    t = raw_time[0]+raw_time[1]
    code = f.encrypt(bytes(t, 'utf-8')).decode('utf-8')
    response = requests.post('http://kusumakalyan.pythonanywhere.com/setonvalue?code='+code)
    print(response.content.decode('utf-8'))
    return response.content.decode('utf-8')

def offMachine():
    raw_time = str(datetime.now(pytz.timezone('Asia/Kolkata'))).split(' ')[1].split(':')
    t = raw_time[0]+raw_time[1]
    code = f.encrypt(bytes(t, 'utf-8')).decode('utf-8')
    response = requests.post('http://kusumakalyan.pythonanywhere.com/setoffvalue?code='+code)
    print(response.content.decode('utf-8'))
    return response.content.decode('utf-8')

def getPCStatus():
    response = requests.get('http://kusumakalyan.pythonanywhere.com/getonoffvalue')
    return response.content.decode('utf-8')