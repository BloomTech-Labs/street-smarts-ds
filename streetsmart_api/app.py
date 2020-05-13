from flask import Flask, request

# Make app factory
def api():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Streetsmart dummy endpoint"

    @app.route("/dummy", methods=['POST'])
    def dummy():
        req_data = request.get_json()

        samp = req_data["dummy"]

        output = {"success":samp}

        return output
    
    return app