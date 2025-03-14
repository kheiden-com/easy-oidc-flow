from flask import Flask, request
from easy_oidc_flow import EasyOIDCFlow


app = EasyOIDCFlow(Flask(__name__))

@app.route("/")
def main():
  return f"hello {request.user_data["email"]}!"

if __name__ in "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)