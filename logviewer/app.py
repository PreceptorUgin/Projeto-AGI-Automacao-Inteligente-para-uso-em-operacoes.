from flask import Flask, render_template, jsonify
import threading
import time

LOG_FILE = "/var/log/asterisk/full"

class Server:
    def __init__(self):
        self.ip = "0.0.0.0"
        self.port = 8080

        self.app = Flask(
            __name__,
            static_folder="static",
            template_folder="templates"
        )

        self.logs = []
        self.setup_routes()
        self.start_log_reader()

    def start_log_reader(self):
        def tail_log():
            try:
                with open(LOG_FILE, "r") as f:
                    f.seek(0, 2)
                    while True:
                        line = f.readline()
                        if not line:
                            time.sleep(0.3)
                            continue
                        self.logs.append(line.rstrip())
                        self.logs = self.logs[-500:]
            except Exception as e:
                self.logs.append(f"[ERROR] {e}")

        threading.Thread(target=tail_log, daemon=True).start()

    def setup_routes(self):

        @self.app.route("/")
        @self.app.route("/logs")
        def logs():
            return render_template("logs.html")

        @self.app.route("/settings")
        def settings():
            return render_template("settings.html")

        @self.app.route("/api/logs")
        def api_logs():
            return jsonify(self.logs)

if __name__ == "__main__":
    server = Server()
    server.app.run(host=server.ip, port=server.port, debug=True)
