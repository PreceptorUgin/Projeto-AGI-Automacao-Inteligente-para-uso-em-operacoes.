from flask import Flask, render_template, jsonify
from asterisk_client import AsteriskAMI
import threading

class Server:
    def __init__(self):
        self.ip = '0.0.0.0'
        self.port = 8080
        self.app = Flask(
            __name__,
            static_folder='static',
            template_folder='templates'
        )

        self.logs = []
        self.ami = AsteriskAMI()
        self.setup_routes()
        self.start_asterisk_listener()

    def start_asterisk_listener(self):
        def listen():
            self.ami.connect()
            while True:
                event = self.ami.read_event()
                if event:
                    self.logs.append(event)
                    self.logs = self.logs[-100:]  # mantém últimos 100

        thread = threading.Thread(target=listen, daemon=True)
        thread.start()

    def setup_routes(self):

        @self.app.route('/')
        def logs(): 
            return render_template('logs.html', active='logs')

        @self.app.route('/voicemail')
        def voicemail():
            return render_template('voicemail.html', active='voicemail')
        
        @self.app.route('/settings')
        def settings():
            return render_template('settings.html', active='settings')

        @self.app.route('/api/logs')
        def api_logs():
            return jsonify(self.logs)

if __name__ == '__main__':
    server = Server()
    server.app.run(host=server.ip, port=server.port, debug=True)
