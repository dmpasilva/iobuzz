import socketio

from iobuzz.config import SERVER_URL, SERVER_SECRET


class WebSocketConnection:
    sio = None
    connection_handler = None
    message_handler = None

    def connect(self, room):
        headers = {
            "x-secret": SERVER_SECRET,
            "x-room": room
        }
        try:
            self.sio.connect(SERVER_URL, headers)
        except:
            self.connect_error()

    def connect_error(self):
        self.connection_handler.on_connection_failed()

    def send_buttons(self, controller, buttons):
        data = {
            'controller': controller,
            'buttons': [int(b) for b in buttons]
        }
        print('Sending inputs')
        print(data)
        self.sio.emit('button', data, '/game')

    def __init__(self, connection_handler, message_handler):
        sio = socketio.Client(reconnection = False)
        self.sio = sio
        self.connection_handler = connection_handler
        self.message_handler = message_handler

        @sio.event
        def connect():
            self.connection_handler.on_connection()

        @sio.event
        def connect_error():
            self.connection_handler.on_connection_failed()

        @sio.on('message', namespace='/game')
        def on_message(ns, data):
            print('Received a message!')
            print(ns)
            print(data)

        @sio.on('join', namespace='/game')
        def on_join(data):
            print('Joined a game room')

        @sio.on('read', namespace='/game')
        def on_event_read(data):
            if data is not None:
                self.message_handler.on_read(data, self)

        @sio.on('stop_read', namespace='/game')
        def on_event_read(data):
            self.message_handler.on_stop_read()

        @sio.on('write', namespace='/game')
        def on_event_write(data):
            if data is not None:
                self.message_handler.on_write(data)

        @sio.event
        def disconnect():
            self.connection_handler.on_connection_failed()


