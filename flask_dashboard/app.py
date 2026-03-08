from flask import Flask
from gpio_control import relay

app = Flask(__name__)


@app.route("/")
def home():
    return "Smart Home Running"


@app.route("/light/on")
def light_on():
    relay.light_on()
    return "Light ON"


@app.route("/light/off")
def light_off():
    relay.light_off()
    return "Light OFF"


app.run(host="0.0.0.0", port=5000)
