from websocket import create_connection, WebSocket


class MycroftAPI(object):
    def __init__(self, mycroft_ip):
        self.mycroft_ip = mycroft_ip
        self.url = "ws://" + self.mycroft_ip + ":8181/core"
        print(self.url)
        self._ws = create_connection(self.url)

    def speak_text(self, text):
        mycroft_speak = ('"{}"'.format(text))
        mycroft_type = '"speak"'
        mycroft_data = '{"expect_response": false, "utterance": %s}, "context": null' % mycroft_speak
        message = '{"type": ' + mycroft_type + ', "data": ' + mycroft_data + '}'
        self._ws.send(message)
        response = "Message Sent to Mycroft Instance: {}".format(self.mycroft_ip)
        return response