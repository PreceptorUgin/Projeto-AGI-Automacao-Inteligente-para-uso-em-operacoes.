import socket

class AsteriskAMI:
    def __init__(self, host='localhost', port=5038, user='admin', secret='admin123'):
        self.host = host
        self.port = port
        self.user = user
        self.secret = secret
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self._login()

    def _login(self):
        login_cmd = (
            f"Action: Login\r\n"
            f"Username: {self.user}\r\n"
            f"Secret: {self.secret}\r\n\r\n"
            "Events: on\r\n\r\n"
        )
        self.sock.send(login_cmd.encode())

    def read_event(self):
        data = self.sock.recv(4096).decode(errors='ignore')
        return data
