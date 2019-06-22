import websocket
import json
import time

try:
    import thread
except ImportError:
    import _thread as thread


def empty(dictionary, key):
    if key in dictionary:
        if dictionary[key]:
            return False
    return True


class RdmsClient:
    ip = '127.0.0.1'
    port = 2333
    password = 'lixisverygay'
    apiversion = 1

    def __init__(self, ip='127.0.0.1', port=2333, password='lixisverygay', apiversion=1):
        RdmsClient.ip = ip
        RdmsClient.port = port
        RdmsClient.password = password
        RdmsClient.apiversion = apiversion
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://" + str(self.ip) + ":" + str(self.port) + "/",
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close,
                                         on_open=self.on_open)

    def connect(self):
        self.ws.run_forever()

    @staticmethod
    def on_open(ws):
        ws.send(
            '{"action":"register","message":{"api":' + str(RdmsClient.apiversion) + ',"type":"rdms","password":"' + str(
                RdmsClient.password) + '"}}')

    @staticmethod
    def on_message(ws, message):
        original = json.loads(message)
        if empty(original['message'], 'data'):
            print(original)
        else:
            print(original['message']['data'].replace('\\n', '\n'))

    @staticmethod
    def on_error(ws, error):
        print('344')

    @staticmethod
    def on_close(ws):
        print('344')
