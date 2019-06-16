#!/usr/bin/python

import websocket
import json

try:
    import thread
except ImportError:
    import _thread as thread
import time


def empty(dictionry, key):
    if key in dictionry:
        if dictionry[key]:
            return False
    return True


def on_message(ws, message):
    original = json.loads(message)
    if empty(original['message'], 'data'):
        print(original)
    else:
        print(original['message']['data'].replace('\\n', '\n'))


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        ws.send('{"action":"register","message":{"api":1,"type":"rdms","password":"lixisverygay"}}')
        time.sleep(10000)
        ws.close()
        print("thread terminating...")

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    print("Amadues远程调试监控系统启动中...")
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://45.40.204.211:2333/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
