from flask import Flask
from easy_oidc_flow import EasyOIDCFlow


app = EasyOIDCFlow(Flask(__name__))
# app = Flask(__name__)

def start():
  app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ in "__main__":
  start()